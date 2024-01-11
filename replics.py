import random

cart = '''Оля - дочка могущественной феи, но жили они достаточно бедно.
Оля научилась от неё колдавать, хотя в подростковом возрасте почти перестала это делать. После смерти матери она сначали жила у команды пиратов (это были не здоровенне мужики, а такие же подростки, как она), потом её отправили в Невердип. Там она долгое время была скованна, но постепенно раскрылась и вписалась в местное общество.'''
cartoon = {'Характер':'Оля достаточно сообразительна, весела, но не выпендрёжница и не театральщица, как многие в Невердипе. При этом она достаточно молчалива и улыбчива, она может выслушать и помочь. Врагов в Невердипе у неё нет. Она твёрдая, иногда упрямая и эмоциональная, но в целом спокойная.',
           'Биография':f'Девочка имеет очень трагичную историю. Она сирота, её мать умерла. У неё осталась тёплые воспоминания о маме, её память она защищает так же рьяно, как собственную жизнь.\nДевочка разочаровалась в жителях Диснея после того, как чуть не замёрзла насмерть на улице под Рождество. Ей никто не помог, нашли её под самый праздник подростки, обчищающие дома. Это были пираты. Оставить её умирать они не могли и отнесли к себе в пещеру, где она и очнулась. Сперва Оля была обескуражена, но постепенно прониклась к своим спасителям. Летом пираты отправили девочку на остров, так как она не могла приспособиться к жизни пиратов. На острове её приняли, и Оля постепенно раскрыла свой достаточно бойкий характер. С пиратами по прежнему общалась и даже дружила. С четырнадцати пошла на работу, где её высоко ценили (отдельная история). Когда ей было восемнадцать, гитарист группы "Хеллоуин" Михаил написал про неё песню "Девочка со спичками". Ещё чего-то с ней пока не произошло.',
           'Сила':'Оля отдаёт предпочтения огненным чарам, которые она давно довела до совершенства. Для неё стало привычным наколдовывать спичку и зажигать её, это своего рода релаксация. Она неплохо знает заклятия, но редко ими пользуется, как и магией в целом. Способности в магии у неё в основном связаны с трансформацией чего-либо, перемещения, внушение и контроль окружающей среды – это не её. Исключение представляет собой огонь.',
           'Возраст':'Ей 18. Родилась в феврале 24.'}

h = '''Привет! Я - бот-визитка, который может присылать тебе фотографии и отвечать на некоторые сообщения. Вот мои команды:
    /help - подскажу, как я работаю. Это я и делаю сейчас.
    /start - я начну общаться с тобой заново.
    /about - я расскажу о человеке, визиткой которого я являюсь.
    /about_personality - я расскажу про характер персонажа.
    /about_biography - я расскажу биографию персонажа.
    /about_power - я расскажу про способности персонажа.
    /about_age - я открою тебе возраст персонажа (как известно, возраст дамы спрашивать невежливо).
    /weather - если ты живёшь в Самаре, то можешь узнать погоду за окном. Жители других городов, не обижайтесь на меня, пожалуйста.
    /questionnaire - пришлю тебе код такого же, как я, бота.'''

hi = ['Привет. Как у тебя дела?', 'Приветики. Чем занимаешься?', 'Приветствую тебя, пользователь Telegram.']
def _hi_(hi):
    x = random.randint(0, 2)
    return hi[x]

by = ['Пока', 'Возвращайся скорее', 'До встречи']
def _by_(by):
    x = random.randint(0, 2)
    return by[x]

good = ['Рад за тебя.', 'У меня тоже всё чудесно.', 'Дальше будет ещё лучше.']
def _good_(good):
    x = random.randint(0, 2)
    return good[x]

bad = ['Не отчаивайся.', 'У меня тоже не очень. Ничего, вместе справимся.', 'Дальше - лучше.']
def _bad_(bad):
    x = random.randint(0, 2)
    return bad[x]

know = ['Рутина всё.', 'У меня всё чудесно. А у тебя?', 'Живу - не жалуюсь.']
def _know_(know):
    x = random.randint(0, 2)
    return know[x]

thanks = ['Пожалуйста', 'Рад помочь.', 'Обращайся']
def _thanks_(thank):
    x = random.randint(0, 2)
    return thank[x]

photo = ['5.jpg','1111.jpg', 'холл.jpg','закат.jpg',"киги.jpg"]
def _photo_(photo):
    x = random.randint(0, 4)
    return photo[x]
coments = ['Вот такая фоточка есть у меня', 'У меня тоже есть галлерея))', 'А такая фоточка красивая?']
def _coment_(thank):
    x = random.randint(0, 2)
    return thank[x]