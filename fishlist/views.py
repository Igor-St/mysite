from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from fishlist.models import Fish, Comment
from fishlist.forms import FishForm, CommentForm, UserForm, UserProfileForm
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    fish_list = Fish.objects.order_by('fish_name')
    paginator = Paginator(fish_list, 2)

    page = request.GET.get('page')
    try:
        fishs = paginator.page(page)
    except PageNotAnInteger:
        fishs = paginator.page(1)
    except EmptyPage:
        fishs = paginator.page(paginator.num_pages)
    context_dict = {'fishs': fishs}


    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')

    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 5:
            visits += 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits

    response = render(request, 'fishlist/index.html', context_dict)

    return response

def fish(request, id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['fish'] = get_object_or_404(Fish, id=id)
    args['comments'] = Comment.objects.filter(fish_id=id)
    args['form'] = comment_form
    return render(request, 'fishlist/fish.html', args)


def add_fish(request):
    if request.method == 'POST':
        form = FishForm(request.POST, request.FILES)

        if form.is_valid():
            fish = form.save(commit=False)
            fish.fish_date = timezone.now()
            fish.save()
            return redirect('fishlist.views.index')
        else:
            print(form.errors)
    else:
        form = FishForm()
    return render(request, 'fishlist/add_fish.html', {'form': form})

@login_required
def edit_fish(request, id):
    fish = get_object_or_404(Fish, id=id)
    if request.method == "POST":
        form = FishForm(request.POST, request.FILES, instance=fish)
        if form.is_valid():
            fish = form.save(commit=False)
            fish.fish_date = timezone.now()
            fish.save()
            return redirect('/fishlist/%s' % id)
    else:
        form = FishForm(instance=fish)
    return render(request, 'fishlist/add_fish.html', {'form': form})

@login_required
def addcomment(request, id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.fish_id = int(id)
            comment.comment_date = timezone.now()
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/fishlist/%s' % id)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'fishlist/register.html',
                  {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/fishlist/')
            else:
                return HttpResponse("Вход в систему закрыт")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Неверные данные")
    else:
        return render(request, 'fishlist/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Вы видите этот текст, потому что вошли в систему")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/fishlist/')
