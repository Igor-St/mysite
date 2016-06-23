from django.contrib import admin
from fishlist.models import Fish, Comment, UserProfile

#class FishAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug':('fish_name',)}


class CommentAdmin(admin.ModelAdmin):
    fields = ['comment_text', 'comment_date']
    list_filter = ['comment_date']

admin.site.register(Fish)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)


