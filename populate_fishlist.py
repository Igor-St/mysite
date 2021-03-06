# -*- coding: utf8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from fishlist.models import Fish


def populate():
    #python_cat = add_cat("Python", views=128, likes=64)

    add_fish(fish_name="Жерех",
             fish_text="Жерех (лат. Aspius aspius) — самый распространённый вид рыб рода Жерехи семейства карповых отряда карпообразных. Жерех отличается от других рыб тёмной синевато-серой спиной, серебристо-сероватыми боками и белым брюхом. Спинной и хвостовой плавники его серые, с тёмными концами; нижняя часть хвоста несколько длиннее верхней; остальные плавники красноватые у основания и сероватые к концу, голова несколько удлинённая, с выдающейся кверху нижней челюстью. Эта рыба вырастает до 120 см в длину и веса в 12 кг. Но обычно размер не превышает 80 см, а в среднем составляет 40 - 50 см при весе 1,5 - 2 кг. Может жить до 15 лет. Нерестятся большей частью во второй половине апреля, когда уже останется прибылой воды около 70 см, по-видимому днем, но не ночью, подобно язям, так как это вполне дневная рыба. Выметавшие икру шересперы, изнуренные длинным зимним постом и нерестом, чрезвычайно слабеют и вряд ли вначале умеют Ловить какую-либо Бодрую рыбу; но они очень жадно сейчас же затевают питаться червями, почему нередко попадаются на донную, причем не выказывают почти никакого противостояния. Жерех - рыба вполне дневная. Она обожает свет, простор и удерживается на дне и на глубине только по ночам. Впрочем, в майские и июньские, воробьиные, ночи он питается и всю ночь напролет. В бездонной жидкости жерех большей частью плавает в полводы или в нижнем слое, в мелочной же - почти на поверхности, так что видно случается его внушительное спинное перо. Маленькие жерехи передвигаются всегда более или менее скоро и своим корпусом образуют крупную волну; внушительные жерехи, напротив, плывут всегда неторопливо и несколько бездоннее в жидкости, так что вал, волна, которую они гонят своим спинным плавником, не так верховен, но зато шире и надежнее.")

    add_fish(fish_name="Карась",
             fish_text="Карась (лат. Carassius) — род лучепёрых рыб")

    add_fish(fish_name="Красноперка", fish_text="Красноперка")

    add_fish(fish_name="Лещ", fish_text="Лещ")

    add_fish(fish_name="Окунь",
        fish_text="Речной окунь, или обыкновенный окунь (лат. Perca fluviatilis) — рыба рода пресноводных окуней семейства окунёвых (Percidae) отряда окунеобразных (Perciformes). Речной окунь относится к хищным рыбам: в рационе взрослого окуня значительную долю занимают другие пресноводные рыбы. Речной окунь предпочитает придерживаться равнинных водоёмов, его можно встретить в реках, озёрах, прудах, водохранилищах и даже в менее солоноватых участках морей. Нерест у речного окуня происходит ранней весной, самка окуня откладывает икринки в форме длинной (до 1 м) студенистой ленты. В центральной России речной окунь мечет икру обыкновенно, когда жидкость пойдет на убыль, прежде всего в маленьких речках. В полупроточных прудах, то есть обладающих движение только весной и после мощных ливней, нерест возникает на несколько часов позднее, чем в реках, а в непроточных озерах он замедляется еще более. Таким ликом, в одной и той же местности разница во времени нереста может быть более недели, иногда десятидневная. Явление это объясняется тем, что всякая порода рыбы не мечет икру прежде, чем жидкость достигнет общеизвестной влажности, при которой делается достижимым развитие икры той или иной породы. Окунь, по-видимому, нерестится, когда жидкость добивается +7 или +8 градусов тепла. Вообще у нас, под Москвой, начало нереста окуня в речках и реках совпадает с происхождением распускания березы, а самый поздний нерест случается в происхождении мая, когда лист уже вполне развернулся.")

    add_fish(fish_name="Плотва",
        fish_text="Плотва обыкновенная - вид лучепёрых рыб из семейства карповых (Cyprinidae). Имеет много подвидов, из которых некоторые имеют собственные названия: тарань, вобла. От ближайших к ней видов плотва отличается незазубренными и расположенными с каждой стороны в один ряд глоточными зубами (по 5—6 с каждой стороны), относительно крупной чешуей (40—45 чешуй в боковой линии), пастью на конце морды и положением начала спинного плавника над основаниями брюшных. Спина черноватая, с голубым или зелёным отливом, бока и брюхо серебристые, спинной и хвостовой плавники зеленовато-серые с красноватым оттенком, грудные желтоватые, брюшные и заднепроходный красные, радужная оболочка жёлтая с красным пятном. Попадаются также экземпляры с глазами и плавниками жёлтого цвета, с золотистой чешуей, с красноватым оттенком на боках и спине. Наиболее простой способ отличия от краснопёрки — цвет глаз: у краснопёрки — глаза оранжевые, с красным пятном вверху[2], тогда как у плотвы — кроваво-красный. Ещё одно отличие — количество мягких перьев на спинном плавнике: у краснопёрки их 8—9, тогда как у плотвы 10—12. Иногда встречаются гибридные формы этих рыб, обладающие признаками обоих видов. Держится обычно стаями в местах со слабым течением под защитой коряг, свисающих деревьев или водной растительности. При этом в стае средних и мелких рыб могут быть и единичные крупные экз. Мелкая и средняя рыба не пуглива. Максимальная длина тела свыше 50 см, и масса до 3-х кг, максимальная продолжительность жизни — 21 год. Мировым рекордом считается национальный рекорд бывшей ГДР - там была поймана и зафиксирована плотва весом 2.58 кг. Близкий к рекордному и иногда ошибочно полагаемая за мировой рекорд признается пойманная в Финляндии в 1939 году плотва весом 2.550 кг.")

    add_fish(fish_name="Уклейка",
        fish_text="Уклейка (лат. Alburnus alburnus) — распространённый вид рыб из семейства карповых. Имеет пелагическую окраску — спинка тёмная, серовато-голубая с зеленоватым отливом, а брюшко и бока серебристые, со светлым отблеском. Спинной и хвостовой плавники тёмные, а остальные желтоватые или красноватые. Чешуя нестойкая, от прикосновения остается на пальцах. Достигает длины до 20 см (средне 12—15, наибольшее — 25) и массы до 60 граммов, встречаются экземпляры весом 80—100 граммов. Любимая наживка — личинки мясной мухи (рощеник, опарыш). Обитает в реках, озёрах и водохранилищах, также может жить в солоноватой воде устьев рек. Является стайной рыбой, предпочитает верхние слои воды. Питается планктоном, также подбирает с поверхности воды упавших мелких насекомых и пыльцу. Нерест порционный, начинается в конце мая, заканчивается в начале июля.")

    add_fish(fish_name="Щука",
        fish_text="Щука (лат. Esox lucius) - рыба семейства щуковых. Распространена в пресных водах Евразии и Северной Америки. Живёт обычно в прибрежной зоне, в водных зарослях, в непроточных или слабопроточных водах. По своей хищности, повсеместному распространению и величине, которой уступает только далеко не столь многочисленному сому, щука, несомненно, составляет одну из наиболее замечательных и наиболее известных пресноводных пород рыб. Хищность, прожорливость и проворство ее вошли в пословицу; она не водится только в небольших стоячих водах и то с многочисленными исключениями; во многих местностях, наконец, она достигает 32, даже 48 и более килограммов веса и 2-метровой длины. В средней России нерест ее имеет место в марте, редко в начале или средине апреля.")

    # Print out what we have added to the user.
    #for c in Category.objects.all():
    #    for p in Page.objects.filter(category=c):
    #       print ("- {0} - {1}".format(str(c), str(p)))

def add_fish(fish_name, fish_text):
    p = Fish.objects.get_or_create(fish_name=fish_name, fish_text=fish_text)[0]
    p.fish_name=fish_name
    p.fish_text=fish_text
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print ("Starting Fishlist population script...")
    populate()
