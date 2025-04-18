from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Начало  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# /start

start_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Предыстория', callback_data = 'background')],
    
    [InlineKeyboardButton(text = 'Конфиги', callback_data = 'configs'), 
     InlineKeyboardButton(text = 'Консоль', callback_data = 'console')],

    # [InlineKeyboardButton(text = '⚙ Квесты', callback_data = 'quests'), 
    #  InlineKeyboardButton(text = '⚙ Достижения', callback_data = 'achievements'),
    #  InlineKeyboardButton(text = '⚙ Концовки', callback_data = 'endings')],

    [InlineKeyboardButton(text = 'Тайники', callback_data = 'hidden'), 
     InlineKeyboardButton(text = 'Аномалии', callback_data = 'anomalies'),
     InlineKeyboardButton(text = 'Артефакты', callback_data = 'artifacts')],
    
    # [InlineKeyboardButton(text = '⚙ Персонажи', callback_data = 'characters'), 
    #  InlineKeyboardButton(text = '⚙ Группировки', callback_data = 'groups'),
    #  InlineKeyboardButton(text = '⚙ Мутанты', callback_data = 'mutants')],
    
    # [InlineKeyboardButton(text = '⚙ Предметы', callback_data = 'items'),
    #  InlineKeyboardButton(text = '⚙ Оружия', callback_data = 'weapon'), 
    #  InlineKeyboardButton(text = '⚙ Броня', callback_data = 'armor')],

    [InlineKeyboardButton(text = 'Ошибки', url = 'https://stalked.ru/kak-ispravit-oshibka-xray-engine-v-stalkere'), 
     InlineKeyboardButton(text = 'Баги', url = 'https://steamcommunity.com/sharedfiles/filedetails/?l=russian&id=3043465186')],
    
    [InlineKeyboardButton(text = 'Случайный совет', callback_data = 'advice')]])




# « Начало

back_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])



"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Предыстория - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# Предыстория: Слайд 1-2

background_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Остальные слайды (11) »»', callback_data = 'background_slides')],
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 3 »', callback_data = 'background_slide3')]])




# Предыстория: Слайд 3

background_inline3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 4 »', callback_data = 'background_slide4')]])




# Предыстория: Слайд 4

background_inline4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 5 »', callback_data = 'background_slide5')]])




# Предыстория: Слайд 5

background_inline5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 6 »', callback_data = 'background_slide6')]])




# Предыстория: Слайд 6

background_inline6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 7 »', callback_data = 'background_slide7')]])




# Предыстория: Слайд 7

background_inline7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 8 »', callback_data = 'background_slide8')]])




# Предыстория: Слайд 8

background_inline8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 9 »', callback_data = 'background_slide9')]])




# Предыстория: Слайд 9

background_inline9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 10 »', callback_data = 'background_slide10')]])




# Предыстория: Слайд 10

background_inline10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 11 »', callback_data = 'background_slide11')]])




# Предыстория: Слайд 11

background_inline11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 12 »', callback_data = 'background_slide12')]])




# Предыстория: Слайд 12

background_inline12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Слайд 13 »', callback_data = 'background_slide13')]])




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Конфиги - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# Конфиги

configs_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Повелитель Зоны', callback_data = 'lordofthezone')],

    [InlineKeyboardButton(text = 'Количество денег в начале игры', callback_data = 'moneyinstart')],
    
    [InlineKeyboardButton(text = 'Поле зрения', callback_data = 'fov'), 
     InlineKeyboardButton(text = 'Течение времени', callback_data = 'passoftime')],

    [InlineKeyboardButton(text = 'Радиус прорисовки', callback_data = 'drawradius'), 
     InlineKeyboardButton(text = 'Период сохранений', callback_data = 'asperiod')],
    
    [InlineKeyboardButton(text = 'Общий вес', callback_data = 'totalweight'), 
     InlineKeyboardButton(text = 'Сложность', callback_data = 'difficult'),
     InlineKeyboardButton(text = 'Персонаж', callback_data = 'actor')],

    [InlineKeyboardButton(text = 'Броня', callback_data = 'inprocessconf'), 
     InlineKeyboardButton(text = 'Оружия', callback_data = 'inprocessconf2'),
     InlineKeyboardButton(text = 'Гранаты', callback_data = 'configs_grenades')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Конфиги: «« Начало | « Конфиги

backconfigs_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),]])




# Конфиги: Повелитель Зоны

lordofthezone_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Установка', callback_data = 'lordofthezoneinstall')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),]])


lordofthezoneinstall_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Все шаги (6) »»', callback_data = 'lordofthezoneinstallall')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 2 »', callback_data = 'lordofthezoneinstall2')]])


lordofthezoneinstall2_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 3 »', callback_data = 'lordofthezoneinstall3')]])


lordofthezoneinstall3_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 4 »', callback_data = 'lordofthezoneinstall4')]])


lordofthezoneinstall4_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 5 »', callback_data = 'lordofthezoneinstall5')]])


lordofthezoneinstall5_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 6 »', callback_data = 'lordofthezoneinstall6')]])


lordofthezoneinstall6_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 7 »', callback_data = 'lordofthezoneinstall7')]])


lordofthezoneinstall7_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])




# Конфиги: Поле зрения

fov_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Установка', callback_data = 'fovinstall')],

    [InlineKeyboardButton(text = '55°', callback_data = 'fov55'),
     InlineKeyboardButton(text = '67,5°', callback_data = 'fov675')],

    [InlineKeyboardButton(text = '75°', callback_data = 'fov75'),
     InlineKeyboardButton(text = '83°', callback_data = 'fov83')],

    [InlineKeyboardButton(text = '85°', callback_data = 'fov85'),
     InlineKeyboardButton(text = '90°', callback_data = 'fov90')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


fov55_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Установка', callback_data = 'fovinstall')],

    [InlineKeyboardButton(text = '67,5°', callback_data = 'fov675')],

    [InlineKeyboardButton(text = '75°', callback_data = 'fov75'),
     InlineKeyboardButton(text = '83°', callback_data = 'fov83')],

    [InlineKeyboardButton(text = '85°', callback_data = 'fov85'),
     InlineKeyboardButton(text = '90°', callback_data = 'fov90')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


fov675_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Установка', callback_data = 'fovinstall')],

    [InlineKeyboardButton(text = '55°', callback_data = 'fov55')],

    [InlineKeyboardButton(text = '75°', callback_data = 'fov75'),
     InlineKeyboardButton(text = '83°', callback_data = 'fov83')],

    [InlineKeyboardButton(text = '85°', callback_data = 'fov85'),
     InlineKeyboardButton(text = '90°', callback_data = 'fov90')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


fov75_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Установка', callback_data = 'fovinstall')],

    [InlineKeyboardButton(text = '55°', callback_data = 'fov55'),
     InlineKeyboardButton(text = '67,5°', callback_data = 'fov675')],

    [InlineKeyboardButton(text = '83°', callback_data = 'fov83')],

    [InlineKeyboardButton(text = '85°', callback_data = 'fov85'),
     InlineKeyboardButton(text = '90°', callback_data = 'fov90')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


fov83_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Установка', callback_data = 'fovinstall')],

    [InlineKeyboardButton(text = '55°', callback_data = 'fov55'),
     InlineKeyboardButton(text = '67,5°', callback_data = 'fov675')],

    [InlineKeyboardButton(text = '75°', callback_data = 'fov75')],

    [InlineKeyboardButton(text = '85°', callback_data = 'fov85'),
     InlineKeyboardButton(text = '90°', callback_data = 'fov90')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


fov85_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Установка', callback_data = 'fovinstall')],

    [InlineKeyboardButton(text = '55°', callback_data = 'fov55'),
     InlineKeyboardButton(text = '67,5°', callback_data = 'fov675')],

    [InlineKeyboardButton(text = '75°', callback_data = 'fov75'),
     InlineKeyboardButton(text = '83°', callback_data = 'fov83')],

    [InlineKeyboardButton(text = '90°', callback_data = 'fov90')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


fov90_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Установка', callback_data = 'fovinstall')],

    [InlineKeyboardButton(text = '55°', callback_data = 'fov55'),
     InlineKeyboardButton(text = '67,5°', callback_data = 'fov675')],

    [InlineKeyboardButton(text = '75°', callback_data = 'fov75'),
     InlineKeyboardButton(text = '83°', callback_data = 'fov83')],

    [InlineKeyboardButton(text = '85°', callback_data = 'fov85')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


fovinstall_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Все шаги (3) »»', callback_data = 'fovinstallall')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 2 »', callback_data = 'fovinstall2')]])


fovinstall2_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 3 »', callback_data = 'fovinstall3')]])


fovinstall3_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start')],
     
    [InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs'),
     InlineKeyboardButton(text = 'Шаг 4 »', callback_data = 'fovinstall4')]])


fovinstall4_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])




# Конфиги: Общий вес

totalweight_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Второй файл »', callback_data = 'totalweight2')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


totalweight2_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Первый файл »', callback_data = 'totalweight1')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])




# Конфиги: Сложность

difficult_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Новичок', callback_data = 'difficultnovice')],

    [InlineKeyboardButton(text = 'Сталкер', callback_data = 'difficultstalker')],

    [InlineKeyboardButton(text = 'Ветеран', callback_data = 'difficultveteran')],

    [InlineKeyboardButton(text = 'Мастер', callback_data = 'difficultmaster')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


difficultnovice_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Сталкер', callback_data = 'difficultstalker')],

    [InlineKeyboardButton(text = 'Ветеран', callback_data = 'difficultveteran')],

    [InlineKeyboardButton(text = 'Мастер', callback_data = 'difficultmaster')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]]) 


difficultstalker_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Новичок', callback_data = 'difficultnovice')],

    [InlineKeyboardButton(text = 'Ветеран', callback_data = 'difficultveteran')],

    [InlineKeyboardButton(text = 'Мастер', callback_data = 'difficultmaster')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


difficultveteran_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Новичок', callback_data = 'difficultnovice')],

    [InlineKeyboardButton(text = 'Сталкер', callback_data = 'difficultstalker')],

    [InlineKeyboardButton(text = 'Мастер', callback_data = 'difficultmaster')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


difficultmaster_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Новичок', callback_data = 'difficultnovice')],

    [InlineKeyboardButton(text = 'Сталкер', callback_data = 'difficultstalker')],

    [InlineKeyboardButton(text = 'Ветеран', callback_data = 'difficultveteran')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])




# Конфиги: Броня

configs_armor_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Бронежилет ЧН-3а', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Бронекостюм «Берилл-5М»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Бронекостюм «Булат»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Кожаный плащ', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Комбинезон «Ветер свободы»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Комбинезон «Заря»', callback_data = 'inprocess'),
     InlineKeyboardButton(text = 'Баржи', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Список 2 »', callback_data = 'configs_armor_2')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


configs_armor_1_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Бронежилет ЧН-3а', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Бронекостюм «Берилл-5М»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Бронекостюм «Булат»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Кожаный плащ', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Комбинезон «Ветер свободы»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Комбинезон «Заря»', callback_data = 'inprocess'),
     InlineKeyboardButton(text = 'Баржи', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Список 2 »', callback_data = 'configs_armor_2')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


configs_armor_2_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Комбинезон «СЕВА»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Комбинезон «Страж свободы»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Комбинезон ССП-99М', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'ПС5-М «Универсальная защита»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'ПСЗ-9д «Броня Долга»»', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Противогаз', callback_data = 'inprocess'),
     InlineKeyboardButton(text = 'Шутника', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = '« Список 1', callback_data = 'configs_armor_1'),
     InlineKeyboardButton(text = 'Список 3 »', callback_data = 'configs_armor_3')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


configs_armor_3_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Стальной шлем', callback_data = 'inprocess'),
     InlineKeyboardButton(text = 'Коряги', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Тактический шлем', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Шлем Сфера М12', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Шлем заслон', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = 'Экзоскелет', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = '« Список 2', callback_data = 'configs_armor_2')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])




# Конфиги: Гранаты

configs_grenades_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Ф1', callback_data = 'configs_f1'),
     InlineKeyboardButton(text = 'РГД-5', callback_data = 'configs_rgd5')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


configs_f1_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'РГД-5', callback_data = 'configs_rgd5')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])


configs_rgd5_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Ф1', callback_data = 'configs_f1')],

    [InlineKeyboardButton(text = '«« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Конфиги', callback_data = 'configs')]])




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Консоль - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# Консоль: « Начало | Команды (45) »

console_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Команды (45) »', callback_data = 'commands')]])




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Тайники - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# Тайники: Затон
#          Окрестности «Юпитера»
#          Путепровод «Припять-1»
#          г. Припять
#          Лаборатория X8"


hidden_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Затон', callback_data = 'zaton')],
    
    [InlineKeyboardButton(text = 'Окрестности «Юпитера»', callback_data = 'upiter')], 
    
    [InlineKeyboardButton(text = 'Путепровод «Припять-1»', callback_data = 'overpass')],
    
    [InlineKeyboardButton(text = 'г. Припять', callback_data = 'pripyat')],

    [InlineKeyboardButton(text = 'Лаборатория X8', callback_data = 'x8')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Тайники: Окрестности «Юпитера»
#          Путепровод «Припять-1»
#          г. Припять
#          Лаборатория X8

zaton_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Окрестности «Юпитера»', callback_data = 'upiter')], 
    
    [InlineKeyboardButton(text = 'Путепровод «Припять-1»', callback_data = 'overpass')],
    
    [InlineKeyboardButton(text = 'г. Припять', callback_data = 'pripyat')], 
     
    [InlineKeyboardButton(text = 'Лаборатория X8', callback_data = 'x8')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Тайники: Затон
#          Путепровод «Припять-1»
#          г. Припять
#          Лаборатория X8

upiter_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Затон', callback_data = 'zaton')],
    
    [InlineKeyboardButton(text = 'Путепровод «Припять-1»', callback_data = 'overpass')],
    
    [InlineKeyboardButton(text = 'г. Припять', callback_data = 'pripyat')], 
    
    [InlineKeyboardButton(text = 'Лаборатория X8', callback_data = 'x8')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Тайники: Затон
#          Окрестности «Юпитера»
#          г. Припять
#          Лаборатория X8

overpass_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Затон', callback_data = 'zaton')],
    
    [InlineKeyboardButton(text = 'Окрестности «Юпитера»', callback_data = 'upiter')],
    
    [InlineKeyboardButton(text = 'г. Припять', callback_data = 'pripyat')],

    [InlineKeyboardButton(text = 'Лаборатория X8', callback_data = 'x8')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Тайники: Затон
#          Окрестности «Юпитера»
#          Путепровод «Припять-1»
#          Лаборатория X8

pripyat_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Затон', callback_data = 'zaton')],
    
    [InlineKeyboardButton(text = 'Окрестности «Юпитера»', callback_data = 'upiter')], 
    
    [InlineKeyboardButton(text = 'Путепровод «Припять-1»', callback_data = 'overpass')],
    
    [InlineKeyboardButton(text = 'Лаборатория X8', callback_data = 'x8')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Тайники: Затон
#          Окрестности «Юпитера»
#          Путепровод «Припять-1»
#          г. Припять

x8_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Затон', callback_data = 'zaton')],
    
    [InlineKeyboardButton(text = 'Окрестности «Юпитера»', callback_data = 'upiter')], 
    
    [InlineKeyboardButton(text = 'Путепровод «Припять-1»', callback_data = 'overpass')],
    
    [InlineKeyboardButton(text = 'г. Припять', callback_data = 'pripyat')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Аномалии  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# Аномалии: Список 1
# - - - - - - - - -
#           Аномальная роща
#           «Бетонная ванна»
#           «Битум»
#           «Вулкан»
#           «Железный лес»
#           Земснаряд 
# 
#           Список 2 »
#           « Начало

anomalies_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Аномальная роща', callback_data = 'anomalous_grove')],

    [InlineKeyboardButton(text = '«Бетонная ванна»', callback_data = 'concrete_bath')],  

    [InlineKeyboardButton(text = '«Битум»', callback_data = 'bitumen')],

    [InlineKeyboardButton(text = '«Вулкан»', callback_data = 'volcano')],

    [InlineKeyboardButton(text = '«Железный лес»', callback_data = 'iron_forest')],

    [InlineKeyboardButton(text = 'Земснаряд', callback_data = 'dredger')],

    [InlineKeyboardButton(text = 'Список 2 »', callback_data = 'anomalies_2_scroll')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




anomalous_grove_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Душа»', callback_data = 'soul')],

    [InlineKeyboardButton(text = '«Колобок»', callback_data = 'kolobok')],

    [InlineKeyboardButton(text = '«Кровь камня»', callback_data = 'blood_of_stone')],

    [InlineKeyboardButton(text = '«Ломоть мяса»', callback_data = 'hunk_of_meat')],

    [InlineKeyboardButton(text = '«Пузырь»', callback_data = 'bubble')],

    [InlineKeyboardButton(text = '«Светляк»', callback_data = 'firefly')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 1', callback_data = 'anomalies_1')]])


bitumen_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Золотая рыбка»', callback_data = 'goldfish')],

    [InlineKeyboardButton(text = '«Каменный цветок»', callback_data = 'stone_flower')],

    [InlineKeyboardButton(text = '«Мамины бусы»', callback_data = 'mothers_beads')],

    [InlineKeyboardButton(text = '«Ночная звезда»', callback_data = 'night_star')],

    [InlineKeyboardButton(text = '«Огненный шар»', callback_data = 'fireball')],
    
    [InlineKeyboardButton(text = '«Выверт»', callback_data = 'twist'),
     InlineKeyboardButton(text = '«Глаз»', callback_data = 'eye')],

    [InlineKeyboardButton(text = '«Грави»', callback_data = 'gravi'),
     InlineKeyboardButton(text = '«Кристалл»', callback_data = 'crystal')],  

    [InlineKeyboardButton(text = '«Медуза»', callback_data = 'jellyfish'),
     InlineKeyboardButton(text = '«Пламя»', callback_data = 'flame')],  

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 1', callback_data = 'anomalies_1')]])


volcano_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Глаз»', callback_data = 'eye')],

    [InlineKeyboardButton(text = '«Кристалл»', callback_data = 'crystal')],

    [InlineKeyboardButton(text = '«Мамины бусы»', callback_data = 'mothers_beads')],

    [InlineKeyboardButton(text = '«Огненный шар»', callback_data = 'fireball')],

    [InlineKeyboardButton(text = '«Пламя»', callback_data = 'flame')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 1', callback_data = 'anomalies_1')]])


iron_forest_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Батарейка»', callback_data = 'battery')],

    [InlineKeyboardButton(text = '«Бенгальский огонь»', callback_data = 'sparkler')],

    [InlineKeyboardButton(text = '«Вспышка»', callback_data = 'flash')],

    [InlineKeyboardButton(text = '«Лунный свет»', callback_data = 'moonlight')],

    [InlineKeyboardButton(text = '«Пустышка»', callback_data = 'dummy')],

    [InlineKeyboardButton(text = '«Снежинка»', callback_data = 'snowflake')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 1', callback_data = 'anomalies_1')]])


dredger_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Выверт»', callback_data = 'twist')],

    [InlineKeyboardButton(text = '«Грави»', callback_data = 'gravi')],

    [InlineKeyboardButton(text = '«Золотая рыбка»', callback_data = 'goldfish')],

    [InlineKeyboardButton(text = 'Изменённый изолятор', callback_data = 'altered_isolator')], 
    
    [InlineKeyboardButton(text = '«Каменный цветок»', callback_data = 'stone_flower')],

    [InlineKeyboardButton(text = '«Медуза»', callback_data = 'jellyfish')],

    [InlineKeyboardButton(text = '«Ночная звезда»', callback_data = 'night_star')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 1', callback_data = 'anomalies_1')]])




# Аномалии: Список 2
# - - - - - - - - -
#           Карьер
#           КБО «Юбилейный»
#           «Коготь»
#           «Котёл»
#           «Лоза»
#           Мост им. Преображенского
# 
#           « Список 1 | Список 3 »
#           « Начало

anomalies_2_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Карьер', callback_data = 'career')],

    [InlineKeyboardButton(text = 'КБО «Юбилейный»', callback_data = 'kbo_anniversary')],  

    [InlineKeyboardButton(text = '«Коготь»', callback_data = 'claw')],

    [InlineKeyboardButton(text = '«Котёл»', callback_data = 'boiler')],

    [InlineKeyboardButton(text = '«Лоза»', callback_data = 'vine')],

    [InlineKeyboardButton(text = 'Мост им. Преображенского', callback_data = 'bridge')],
    
    [InlineKeyboardButton(text = '« Список 1', callback_data = 'anomalies_1_scroll'),
     InlineKeyboardButton(text = 'Список 3 »', callback_data = 'anomalies_3_scroll')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




career_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Душа»', callback_data = 'soul')],

    [InlineKeyboardButton(text = '«Колобок»', callback_data = 'kolobok')],

    [InlineKeyboardButton(text = '«Кровь камня»', callback_data = 'blood_of_stone')],

    [InlineKeyboardButton(text = '«Ломоть мяса»', callback_data = 'hunk_of_meat')],

    [InlineKeyboardButton(text = '«Пузырь»', callback_data = 'bubble')],

    [InlineKeyboardButton(text = '«Светляк»', callback_data = 'firefly')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'anomalies_2')]])


kbo_anniversary_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Батарейка»', callback_data = 'battery')],

    [InlineKeyboardButton(text = '«Бенгальский огонь»', callback_data = 'sparkler')],

    [InlineKeyboardButton(text = '«Вспышка»', callback_data = 'flash')],

    [InlineKeyboardButton(text = '«Лунный свет»', callback_data = 'moonlight')],

    [InlineKeyboardButton(text = '«Пустышка»', callback_data = 'dummy')],

    [InlineKeyboardButton(text = '«Снежинка»', callback_data = 'snowflake')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'anomalies_2')]])


claw_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Выверт»', callback_data = 'twist')],

    [InlineKeyboardButton(text = '«Грави»', callback_data = 'gravi')],

    [InlineKeyboardButton(text = '«Золотая рыбка»', callback_data = 'goldfish')],
    
    [InlineKeyboardButton(text = '«Каменный цветок»', callback_data = 'stone_flower')],

    [InlineKeyboardButton(text = '«Медуза»', callback_data = 'jellyfish')],

    [InlineKeyboardButton(text = '«Ночная звезда»', callback_data = 'night_star')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'anomalies_2')]])


boiler_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Глаз»', callback_data = 'eye')],

    [InlineKeyboardButton(text = '«Кристалл»', callback_data = 'crystal')],

    [InlineKeyboardButton(text = '«Мамины бусы»', callback_data = 'mothers_beads')],

    [InlineKeyboardButton(text = '«Огненный шар»', callback_data = 'fireball')],

    [InlineKeyboardButton(text = '«Пламя»', callback_data = 'flame')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'anomalies_2')]])




# Аномалии: Список 3
# - - - - - - - - -
#           Оазис
#           «Пепелище»
#           Пещеры сгоревшего хутора
#           Плавни
#            «Пространственный пузырь»
#           «Рубец» 
# 
#           « Список 2 | Список 4 »
#           « Начало

anomalies_3_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Оазис»', callback_data = 'oasis')],

    [InlineKeyboardButton(text = '«Пепелище»', callback_data = 'ashes')],  

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')],

    [InlineKeyboardButton(text = '«Плавни»', callback_data = 'floodplains')],

    [InlineKeyboardButton(text = 'Пространственный пузырь', callback_data = 'spatial_bubble')],

    [InlineKeyboardButton(text = '«Рубец»', callback_data = 'scar')],

    [InlineKeyboardButton(text = '« Список 2', callback_data = 'anomalies_2_scroll'),
     InlineKeyboardButton(text = 'Список 4 »', callback_data = 'anomalies_4_scroll')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




oasis_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Сердце Оазиса»', callback_data = 'heart_of_the_oasis')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'anomalies_3')]])


ash_heap_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Глаз»', callback_data = 'eye')],

    [InlineKeyboardButton(text = '«Кристалл»', callback_data = 'crystal')],

    [InlineKeyboardButton(text = '«Мамины бусы»', callback_data = 'mothers_beads')],

    [InlineKeyboardButton(text = '«Огненный шар»', callback_data = 'fireball')],

    [InlineKeyboardButton(text = '«Пламя»', callback_data = 'flame')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'anomalies_3')]])


caves_of_the_burnt_farm_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Глаз»', callback_data = 'eye'),
     InlineKeyboardButton(text = '«Душа»', callback_data = 'soul')],

    [InlineKeyboardButton(text = '«Кристалл»', callback_data = 'crystal'),
     InlineKeyboardButton(text = '«Колобок»', callback_data = 'kolobok')],

    [InlineKeyboardButton(text = '«Мамины бусы»', callback_data = 'mothers_beads'),
     InlineKeyboardButton(text = '«Кровь камня»', callback_data = 'blood_of_stone')],

    [InlineKeyboardButton(text = '«Огненный шар»', callback_data = 'fireball'),
     InlineKeyboardButton(text = '«Ломоть мяса»', callback_data = 'hunk_of_meat')],

    [InlineKeyboardButton(text = '«Пламя»', callback_data = 'flame'),
     InlineKeyboardButton(text = '«Пузырь»', callback_data = 'bubble')],

    [InlineKeyboardButton(text = '«Светляк»', callback_data = 'firefly')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'anomalies_3')]])


floodplains_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Душа»', callback_data = 'soul')],

    [InlineKeyboardButton(text = '«Колобок»', callback_data = 'kolobok')],

    [InlineKeyboardButton(text = '«Кровь камня»', callback_data = 'blood_of_stone')],

    [InlineKeyboardButton(text = '«Ломоть мяса»', callback_data = 'hunk_of_meat')],

    [InlineKeyboardButton(text = '«Пузырь»', callback_data = 'bubble')],

    [InlineKeyboardButton(text = '«Светляк»', callback_data = 'firefly')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'anomalies_3')]])


spatial_bubble_inline = InlineKeyboardMarkup(inline_keyboard=[
    # [InlineKeyboardButton(text = 'Детектор «Велес»', callback_data = 'items_detector_veles')],

    # [InlineKeyboardButton(text = 'Аномальная активность: ...', callback_data = 'quests_scientists_anomaly-activity')],

    # [InlineKeyboardButton(text = 'История «Долга»: ...', callback_data = 'quests_kpk_duty-history')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'anomalies_3')]])


scar_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Батарейка»', callback_data = 'battery')],

    [InlineKeyboardButton(text = '«Бенгальский огонь»', callback_data = 'sparkler')],

    [InlineKeyboardButton(text = '«Вспышка»', callback_data = 'flash')],

    [InlineKeyboardButton(text = '«Лунный свет»', callback_data = 'moonlight')],

    [InlineKeyboardButton(text = '«Пустышка»', callback_data = 'dummy')],

    [InlineKeyboardButton(text = '«Снежинка»', callback_data = 'snowflake')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'anomalies_3')]])






# Аномалии: Список 4
# - - - - - - - - -
#           Сгоревший хутор
#           «Соснодуб»
#           Старый КБО
#           Стоянка
#           Телепорт на сгоревшем хуторе
#           «Тесла»
# 
#           « Список 3 | Список 5 »
#           « Начало

anomalies_4_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Сгоревший хутор', callback_data = 'burnt_farm')],

    [InlineKeyboardButton(text = '«Соснодуб»', callback_data = 'pine_oak')],  

    [InlineKeyboardButton(text = 'Старый КБО', callback_data = 'old_kbo')],

    [InlineKeyboardButton(text = 'Стоянка', callback_data = 'parking')],

    [InlineKeyboardButton(text = 'Телепорт на сгоревшем хуторе', callback_data = 'burnt_farm_teleport')],

    [InlineKeyboardButton(text = '«Тесла»', callback_data = 'tesla')],

    [InlineKeyboardButton(text = '« Список 3', callback_data = 'anomalies_3_scroll'),
     InlineKeyboardButton(text = 'Список 5 »', callback_data = 'anomalies_5_scroll')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




burnt_farm_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Глаз»', callback_data = 'eye')],

    [InlineKeyboardButton(text = '«Кристалл»', callback_data = 'crystal')],

    [InlineKeyboardButton(text = '«Мамины бусы»', callback_data = 'mothers_beads')],

    [InlineKeyboardButton(text = '«Огненный шар»', callback_data = 'fireball')],

    [InlineKeyboardButton(text = '«Пламя»', callback_data = 'flame')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'anomalies_4')]])


pine_oak_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Душа»', callback_data = 'soul')],

    [InlineKeyboardButton(text = '«Колобок»', callback_data = 'kolobok')],

    [InlineKeyboardButton(text = '«Кровь камня»', callback_data = 'blood_of_stone')],

    [InlineKeyboardButton(text = '«Ломоть мяса»', callback_data = 'hunk_of_meat')],

    [InlineKeyboardButton(text = '«Пузырь»', callback_data = 'bubble')],

    [InlineKeyboardButton(text = '«Светляк»', callback_data = 'firefly')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'anomalies_4')]])


old_kbo_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Батарейка»', callback_data = 'battery')],

    [InlineKeyboardButton(text = '«Бенгальский огонь»', callback_data = 'sparkler')],

    [InlineKeyboardButton(text = '«Вспышка»', callback_data = 'flash')],

    [InlineKeyboardButton(text = '«Лунный свет»', callback_data = 'moonlight')],

    [InlineKeyboardButton(text = '«Пустышка»', callback_data = 'dummy')],

    [InlineKeyboardButton(text = '«Снежинка»', callback_data = 'snowflake')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'anomalies_4')]])


burnt_farm_teleport_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'anomalies_4')]])


tesla_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'anomalies_4')]])




# Аномалии: Список 5
# - - - - - - - - -
#           Топь
#           Подвал универмага
#           «Цирк»
#           Школа
# 
#           « Список 5
#           « Начало

anomalies_5_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Топь', callback_data = 'swamp')],  

    [InlineKeyboardButton(text = 'Подвал универмага', callback_data = 'department_store')],

    [InlineKeyboardButton(text = '«Цирк»', callback_data = 'circus')],

    [InlineKeyboardButton(text = 'Школа', callback_data = 'school')],

    [InlineKeyboardButton(text = '« Список 4', callback_data = 'anomalies_4_scroll')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




swamp_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Душа»', callback_data = 'soul')],

    [InlineKeyboardButton(text = '«Колобок»', callback_data = 'kolobok')],

    [InlineKeyboardButton(text = '«Кровь камня»', callback_data = 'blood_of_stone')],

    [InlineKeyboardButton(text = '«Ломоть мяса»', callback_data = 'hunk_of_meat')],

    [InlineKeyboardButton(text = '«Пузырь»', callback_data = 'bubble')],

    [InlineKeyboardButton(text = '«Светляк»', callback_data = 'firefly')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 5', callback_data = 'anomalies_5')]])


circus_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Глаз»', callback_data = 'eye')],

    [InlineKeyboardButton(text = '«Кристалл»', callback_data = 'crystal')],

    [InlineKeyboardButton(text = '«Мамины бусы»', callback_data = 'mothers_beads')],

    [InlineKeyboardButton(text = '«Огненный шар»', callback_data = 'fireball')],

    [InlineKeyboardButton(text = '«Пламя»', callback_data = 'flame')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 5', callback_data = 'anomalies_5')]])


school_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Выверт»', callback_data = 'twist')],

    [InlineKeyboardButton(text = '«Грави»', callback_data = 'gravi')],

    [InlineKeyboardButton(text = '«Золотая рыбка»', callback_data = 'goldfish')],
    
    [InlineKeyboardButton(text = '«Каменный цветок»', callback_data = 'stone_flower')],

    [InlineKeyboardButton(text = '«Медуза»', callback_data = 'jellyfish')],

    [InlineKeyboardButton(text = '«Ночная звезда»', callback_data = 'night_star')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 5', callback_data = 'anomalies_5')]])



"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Артефакты - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# Артефакты: Список 1
# - - - - - - - - - - -
#            «Батарейка»
#            «Бенгальский огонь»
#            «Вспышка»
#            «Выверт»
#            «Глаз»
#            «Грави»

artifacts_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Батарейка»', callback_data = 'battery')],
    
    [InlineKeyboardButton(text = '«Бенгальский огонь»', callback_data = 'sparkler')], 
    
    [InlineKeyboardButton(text = '«Вспышка»', callback_data = 'flash')],
    
    [InlineKeyboardButton(text = '«Выверт»', callback_data = 'twist')],

    [InlineKeyboardButton(text = '«Глаз»', callback_data = 'eye')],

    [InlineKeyboardButton(text = '«Грави»', callback_data = 'gravi')],

    [InlineKeyboardButton(text = 'Список 2 »', callback_data = 'artifacts_2_scroll')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Артефакт: «Батарея»
# - - - - - - - - - - - - 
#           «Железный лес»
#           Завод «Юпитер»
#           Крыша КБО «Юбилейный»
#           «Рубец»
#           Старый КБО
#           Стоянка

artifacts_battery_inline = InlineKeyboardMarkup(inline_keyboard=[    
    [InlineKeyboardButton(text = '«Железный лес»', callback_data = 'iron_forest')], 
    
    [InlineKeyboardButton(text = 'Завод «Юпитер»', callback_data = 'upiter_plant')],

    [InlineKeyboardButton(text = 'Крыша КБО «Юбилейный»', callback_data = 'kbo_anniversary')],

    [InlineKeyboardButton(text = '«Рубец»', callback_data = 'scar')],

    [InlineKeyboardButton(text = 'Старый КБО', callback_data = 'old_kbo')],
    
    [InlineKeyboardButton(text = 'Стоянка', callback_data = 'parking')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 1', callback_data = 'artifacts_1')]])




# Артефакт: «Выверт»
# - - - - - - - - -
#           «Битум»
#           Земснаряд
#           «Коготь»
#           Мост им. Преображенского
#           Пещеры сгоревшего хутора
#           Школа

artifacts_twist_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Битум»', callback_data = 'bitumen')],

    [InlineKeyboardButton(text = 'Земснаряд', callback_data = 'dredger')], 
    
    [InlineKeyboardButton(text = '«Коготь»', callback_data = 'claw')],
    
    [InlineKeyboardButton(text = 'Мост им. Преображенского', callback_data = 'bridge')], 

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')],

    [InlineKeyboardButton(text = 'Школа', callback_data = 'school')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 1', callback_data = 'artifacts_1')]])




# Артефакт: «Глаз»
# - - - - - - - - -
#           «Битум»
#           «Вулкан»
#           «Котёл»
#           «Пепелище»
#           Сгоревший хутор
#           Цементный завод
#           «Цирк»

artifacts_eye_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Битум»', callback_data = 'bitumen'),
     InlineKeyboardButton(text = '«Вулкан»', callback_data = 'volcano')],
    
    [InlineKeyboardButton(text = '«Котёл»', callback_data = 'boiler'),
     InlineKeyboardButton(text = '«Пепелище»', callback_data = 'ash_heap')],

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')],

    [InlineKeyboardButton(text = 'Сгоревший хутор', callback_data = 'burnt_farm')],
    
    [InlineKeyboardButton(text = 'Цементный завод', callback_data = 'cement_plant')],

    [InlineKeyboardButton(text = '«Цирк»', callback_data = 'circus')], 

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 1', callback_data = 'artifacts_1')]])




# Артефакты: Список 2
# - - - - - - - - -
#            «Душа»
#            «Золотая рыбка»
#            Изменённый изолятор
#            Изменённый штурвал
#            «Каменный цветок»
#            «Колобок»
#            «Компас»

artifacts_2_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Душа»', callback_data = 'soul')],
    
    [InlineKeyboardButton(text = '«Золотая рыбка»', callback_data = 'goldfish')], 
    
    [InlineKeyboardButton(text = 'Изменённый изолятор', callback_data = 'altered_isolator')],
    
    [InlineKeyboardButton(text = 'Изменённый штурвал', callback_data = 'altered_steering_wheel')],

    [InlineKeyboardButton(text = '«Каменный цветок»', callback_data = 'stone_flower')],

    [InlineKeyboardButton(text = '«Колобок»', callback_data = 'kolobok')],

    [InlineKeyboardButton(text = '«Компас»', callback_data = 'compass')],

    [InlineKeyboardButton(text = '« Список 1', callback_data = 'artifacts_1_scroll'),
     InlineKeyboardButton(text = 'Список 3 »', callback_data = 'artifacts_3_scroll')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Артефакт: «Душа»
# - - - - - - - - - - - - - 
#           Аномальная роща
#           «Бетонная ванна»
#           Карьер | «Лоза»
#           Пещеры сгоревшего хутора
#           «Плавни»
#           «Соснодуб» | Топь
#           Подвал универмага

artifacts_soul_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Аномальная роща', callback_data = 'anomalous_grove')],

    [InlineKeyboardButton(text = '«Бетонная ванна»', callback_data = 'concrete_bath')],

    [InlineKeyboardButton(text = 'Карьер', callback_data = 'career'),
     InlineKeyboardButton(text = '«Лоза»', callback_data = 'vine')],

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')], 

    [InlineKeyboardButton(text = '«Плавни»', callback_data = 'floodplains')],

    [InlineKeyboardButton(text = '«Соснодуб»', callback_data = 'pine_oak'),
     InlineKeyboardButton(text = 'Топь', callback_data = 'swamp')],
    
    [InlineKeyboardButton(text = 'Подвал универмага', callback_data = 'department_store')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'artifacts_2')]])




# Артефакт: «Золотая рыбка»
# - - - - - - - - -
#           «Битум»
#           Земснаряд
#           «Коготь»
#           Мост им. Преображенского
#           Пещеры сгоревшего хутора
#           Школа

artifacts_goldfish_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Битум»', callback_data = 'bitumen')],

    [InlineKeyboardButton(text = 'Земснаряд', callback_data = 'dredger')], 
    
    [InlineKeyboardButton(text = '«Коготь»', callback_data = 'claw')],
    
    [InlineKeyboardButton(text = 'Мост им. Преображенского', callback_data = 'bridge')], 

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')],

    [InlineKeyboardButton(text = 'Школа', callback_data = 'school')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'artifacts_2')]])




# Артефакт: «Изменённый изолятор»
# - - - - - - - - - - - - - - - -
#           Ж/д тоннель «Юпитера»
#           Переменное пси-излучение: ...

artifacts_altered_isolator_inline = InlineKeyboardMarkup(inline_keyboard=[
    # [InlineKeyboardButton(text = 'Ж/д тоннель «Юпитера»', callback_data = 'inprocess')],

    # [InlineKeyboardButton(text = 'Переменное пси-излучение: ...', callback_data = 'inprocess')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'artifacts_2')]])




# Артефакт: «Изменённый штурвал»
# - - - - - - - - - -
#           Земснаряд

artifacts_altered_steering_wheel_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Земснаряд', callback_data = 'dredger')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'artifacts_2')]])




# Артефакт: «Колобок»
# - - - - - - - - - - - - - 
#           Аномальная роща
#           «Бетонная ванна»
#           Карьер | «Лоза»
#           Пещеры сгоревшего хутора
#           «Плавни»
#           «Соснодуб» | Топь
#           Подвал универмага

artifacts_kolobok_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Аномальная роща', callback_data = 'anomalous_grove')],

    [InlineKeyboardButton(text = '«Бетонная ванна»', callback_data = 'concrete_bath')],

    [InlineKeyboardButton(text = 'Карьер', callback_data = 'career'),
     InlineKeyboardButton(text = '«Лоза»', callback_data = 'vine')],

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')], 

    [InlineKeyboardButton(text = '«Плавни»', callback_data = 'floodplains')],

    [InlineKeyboardButton(text = '«Соснодуб»', callback_data = 'pine_oak'),
     InlineKeyboardButton(text = 'Топь', callback_data = 'swamp')],
    
    [InlineKeyboardButton(text = 'Подвал универмага', callback_data = 'department_store')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'artifacts_2')]])




# Артефакт: «Компас»
# - - - - - - - - - - - - - - -
#           Старая баржа, у Ноя
#           «Компас»: найти Ноя и узнать, ...

artifacts_compass_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Старая баржа, у Ноя', callback_data = 'old_barge')],
    
    [InlineKeyboardButton(text = '«Компас»: найти Ноя и узнать, ...', callback_data = 'quest_noi')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 2', callback_data = 'artifacts_2')]])




# Артефакты: Список 3
# - - - - - - - - - - -
#            «Кристалл»
#            «Кровь камня»
#            «Ломоть мяса»
#            «Лунный свет»
#            «Мамины бусы»
#            «Медуза»
#            «Ночная звезда»

artifacts_3_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Кристалл»', callback_data = 'crystal')],
    
    [InlineKeyboardButton(text = '«Кровь камня»', callback_data = 'blood_of_stone')], 
    
    [InlineKeyboardButton(text = '«Ломоть мяса»', callback_data = 'hunk_of_meat')],
    
    [InlineKeyboardButton(text = '«Лунный свет»', callback_data = 'moonlight')],

    [InlineKeyboardButton(text = '«Мамины бусы»', callback_data = 'mothers_beads')],

    [InlineKeyboardButton(text = '«Медуза»', callback_data = 'jellyfish')],

    [InlineKeyboardButton(text = '«Ночная звезда»', callback_data = 'night_star')],

    [InlineKeyboardButton(text = '« Список 2', callback_data = 'artifacts_2_scroll'),
     InlineKeyboardButton(text = 'Список 4 »', callback_data = 'artifacts_4_scroll')],
     
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Артефакт: «Кристалл»
# - - - - - - - - -
#           «Битум»
#           «Вулкан»
#           «Котёл»
#           «Пепелище»
#           Сгоревший хутор
#           Цементный завод
#           «Цирк»

artifacts_crystal_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Битум»', callback_data = 'bitumen'),
     InlineKeyboardButton(text = '«Вулкан»', callback_data = 'volcano')],
    
    [InlineKeyboardButton(text = '«Котёл»', callback_data = 'boiler'),
     InlineKeyboardButton(text = '«Пепелище»', callback_data = 'ash_heap')],

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')],

    [InlineKeyboardButton(text = 'Сгоревший хутор', callback_data = 'burnt_farm')],
    
    [InlineKeyboardButton(text = 'Цементный завод', callback_data = 'cement_plant')],

    [InlineKeyboardButton(text = '«Цирк»', callback_data = 'circus')], 

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'artifacts_3')]])




# Артефакт: «Кровь камня»
# - - - - - - - - - - - - - 
#           Аномальная роща
#           «Бетонная ванна»
#           Карьер | «Лоза»
#           Пещеры сгоревшего хутора
#           «Плавни»
#           «Соснодуб» | Топь
#           Подвал универмага

artifacts_blood_of_stone_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Аномальная роща', callback_data = 'anomalous_grove')],

    [InlineKeyboardButton(text = '«Бетонная ванна»', callback_data = 'concrete_bath')],

    [InlineKeyboardButton(text = 'Карьер', callback_data = 'career'),
     InlineKeyboardButton(text = '«Лоза»', callback_data = 'vine')],

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')], 

    [InlineKeyboardButton(text = '«Плавни»', callback_data = 'floodplains')],

    [InlineKeyboardButton(text = '«Соснодуб»', callback_data = 'pine_oak'),
     InlineKeyboardButton(text = 'Топь', callback_data = 'swamp')],
    
    [InlineKeyboardButton(text = 'Подвал универмага', callback_data = 'department_store')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'artifacts_3')]])




# Артефакт: «Лунный свет»
# - - - - - - - - - - - - 
#           «Железный лес»
#           Завод «Юпитер»
#           Крыша КБО «Юбилейный»
#           «Рубец»
#           Старый КБО
#           Стоянка

artifacts_moonlight_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Железный лес»', callback_data = 'iron_forest')], 
    
    [InlineKeyboardButton(text = 'Завод «Юпитер»', callback_data = 'upiter_plant')],

    [InlineKeyboardButton(text = 'Крыша КБО «Юбилейный»', callback_data = 'kbo_anniversary')],

    [InlineKeyboardButton(text = '«Рубец»', callback_data = 'scar')],

    [InlineKeyboardButton(text = 'Старый КБО', callback_data = 'old_kbo')],
    
    [InlineKeyboardButton(text = 'Стоянка', callback_data = 'parking')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'artifacts_3')]])




# Артефакт: «Медуза»
# - - - - - - - - -
#           «Битум»
#           Земснаряд
#           «Коготь»
#           Мост им. Преображенского
#           Пещеры сгоревшего хутора
#           Школа

artifacts_jellyfish_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Битум»', callback_data = 'bitumen')],

    [InlineKeyboardButton(text = 'Земснаряд', callback_data = 'dredger')], 
    
    [InlineKeyboardButton(text = '«Коготь»', callback_data = 'claw')],
    
    [InlineKeyboardButton(text = 'Мост им. Преображенского', callback_data = 'bridge')], 

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')],

    [InlineKeyboardButton(text = 'Школа', callback_data = 'school')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 3', callback_data = 'artifacts_3')]])




# Артефакты: Список 4
# - - - - - - - - - - -
#            «Огненный шар»
#            «Пламя»
#            «Пузырь»
#            «Пустышка»
#            «Светляк»
#            «Сердце Оазиса»
#            «Снежинка»

artifacts_4_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Огненный шар»', callback_data = 'fireball')],
    
    [InlineKeyboardButton(text = '«Пламя»', callback_data = 'flame')], 
    
    [InlineKeyboardButton(text = '«Пузырь»', callback_data = 'bubble')],
    
    [InlineKeyboardButton(text = '«Пустышка»', callback_data = 'dummy')],

    [InlineKeyboardButton(text = '«Светляк»', callback_data = 'firefly')],

    [InlineKeyboardButton(text = '«Сердце Оазиса»', callback_data = 'heart_of_the_oasis')],

    [InlineKeyboardButton(text = '«Снежинка»', callback_data = 'snowflake')],

    [InlineKeyboardButton(text = '« Список 3', callback_data = 'artifacts_3_scroll')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start')]])




# Артефакт: «Огненный шар»
# - - - - - - - - -
#           «Битум»
#           «Вулкан»
#           «Котёл»
#           «Пепелище»
#           Сгоревший хутор
#           Цементный завод
#           «Цирк»

artifacts_fireball_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Битум»', callback_data = 'bitumen'),
     InlineKeyboardButton(text = '«Вулкан»', callback_data = 'volcano')],
    
    [InlineKeyboardButton(text = '«Котёл»', callback_data = 'boiler'),
     InlineKeyboardButton(text = '«Пепелище»', callback_data = 'ash_heap')],

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')],

    [InlineKeyboardButton(text = 'Сгоревший хутор', callback_data = 'burnt_farm')],
    
    [InlineKeyboardButton(text = 'Цементный завод', callback_data = 'cement_plant')],

    [InlineKeyboardButton(text = '«Цирк»', callback_data = 'circus')], 

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'artifacts_4')]])




# Артефакт: «Пузырь»
# - - - - - - - - - - - - - 
#           Аномальная роща
#           «Бетонная ванна»
#           Карьер | «Лоза»
#           Пещеры сгоревшего хутора
#           «Плавни»
#           «Соснодуб» | Топь
#           Подвал универмага

artifacts_bubble_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Аномальная роща', callback_data = 'anomalous_grove')],

    [InlineKeyboardButton(text = '«Бетонная ванна»', callback_data = 'concrete_bath')],

    [InlineKeyboardButton(text = 'Карьер', callback_data = 'career'),
     InlineKeyboardButton(text = '«Лоза»', callback_data = 'vine')],

    [InlineKeyboardButton(text = 'Пещеры сгоревшего хутора', callback_data = 'caves_of_the_burnt_farm')], 

    [InlineKeyboardButton(text = '«Плавни»', callback_data = 'floodplains')],

    [InlineKeyboardButton(text = '«Соснодуб»', callback_data = 'pine_oak'),
     InlineKeyboardButton(text = 'Топь', callback_data = 'swamp')],
    
    [InlineKeyboardButton(text = 'Подвал универмага', callback_data = 'department_store')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'artifacts_4')]])




# Артефакт: «Пустышка»
# - - - - - - - - - - - - 
#           «Железный лес»
#           Завод «Юпитер»
#           Крыша КБО «Юбилейный»
#           «Рубец»
#           Старый КБО
#           Стоянка

artifacts_dummy_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '«Железный лес»', callback_data = 'iron_forest')], 
    
    [InlineKeyboardButton(text = 'Завод «Юпитер»', callback_data = 'upiter_plant')],

    [InlineKeyboardButton(text = 'Крыша КБО «Юбилейный»', callback_data = 'kbo_anniversary')],

    [InlineKeyboardButton(text = '«Рубец»', callback_data = 'scar')],

    [InlineKeyboardButton(text = 'Старый КБО', callback_data = 'old_kbo')],
    
    [InlineKeyboardButton(text = 'Стоянка', callback_data = 'parking')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'artifacts_4')]])




# Артефакт: «Сердце Оазиса»
# - - - - - - - - - - - - - - - - -
#           Под вентиляционным комплексом

artifacts_heart_of_the_oasis_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Под вентиляционным комплексом', callback_data = 'oasis')],

    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = '« Список 4', callback_data = 'artifacts_4')]])




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Советы  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




advice_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '« Начало', callback_data = 'start'),
     InlineKeyboardButton(text = 'Случайный... »', callback_data = 'random_advice')]])