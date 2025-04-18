from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import app.keyboards as kb
import random




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Начало  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




photo_start = 'AgACAgIAAxkBAAIlV2ftRIfGgOizpPDc8yJTQ6noL1PPAALO7TEbMhJwS9YFnUxmMm8FAQADAgADdwADNgQ'




# dp.include_router(router)

router = Router()




# # получение ID изображения

# @router.message(F.photo)
# async def get_file_id(message: Message) -> None:
# 	photo_id = message.photo[-1].file_id
# 	await message.reply(f'<code>\'{photo_id}\'</code>', parse_mode=ParseMode.HTML)




# # получение ID файла

# @router.message(F.document)
# async def get_file_id(message: Message) -> None:
#     document_id = message.document.file_id
#     await message.reply(f'<code>\'{document_id}\'</code>', parse_mode=ParseMode.HTML)




# /start

@router.message(CommandStart())
async def start(message: Message):
    if message.from_user.last_name:
        full_name = f'{message.from_user.first_name} {message.from_user.last_name}'
        await message.answer_photo(photo = photo_start,
                                   caption = f'Игра сохранена: {message.from_user.first_name}_{message.from_user.last_name} - начало игры', 
                                   reply_markup=kb.start_inline)
    else:
        full_name = message.from_user.first_name
        await message.answer_photo(photo = photo_start, 
                                   caption = f'Игра сохранена: {message.from_user.full_name} - начало игры', 
                                   reply_markup=kb.start_inline)




# « Начало

@router.callback_query(F.data == 'start')
async def start(callback: CallbackQuery):
    await callback.answer()
    if callback.from_user.last_name:
        full_name = f'{callback.from_user.first_name} {callback.from_user.last_name}'
        await callback.message.answer_photo(photo = photo_start, 
                                            caption = f'Игра сохранена: {callback.from_user.first_name}_{callback.from_user.last_name} - начало игры', 
                                            reply_markup=kb.start_inline)
    else:
        full_name = callback.from_user.first_name
        await callback.message.answer_photo(photo = photo_start, 
                                            caption = f'Игра сохранена: {callback.from_user.full_name} - начало игры', 
                                            reply_markup=kb.start_inline)




# ответ на сообщение пользователя

@router.message()
async def user_message(message: Message):
    await message.reply('Бот не умеет отвечать на сообщения от пользователя.')
    await message.answer('Используйте /start и кнопки под сообщениями бота.',
                         reply_markup=kb.start_inline)




# ответ на неготовые элементы: ⚙ В разработке...

@router.callback_query(F.data == 'inprocess')
async def inprocess(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('⚙ В разработке...',
                                  reply_markup=kb.back_inline)




# ответ на неготовые элементы «Конфиги»: ⚙ В разработке...

@router.callback_query(F.data == 'inprocessconf')
async def inprocessconf(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('⚙ В разработке...',
                                  reply_markup=kb.backconfigs_inline)
    

@router.callback_query(F.data == 'inprocessconf2')
async def inprocessconf(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('⚙ В разработке...',
                                  reply_markup=kb.backconfigs_inline)




# # шаблон ответа на нажатие callback

# @router.callback_query(F.data == 'name')
# async def name(callback: CallbackQuery):
#     await callback.answer() # для завершения анимации нажатия
#     # await callback.message.answer_ можно комбинировать
#     await callback.message.answer_document(document = '') # для отправки файла
#     await callback.message.answer_photo(photo = '', # отправка изображения
#                                         caption = '', # подпись к изображению
#                                         parse_mode=ParseMode.HTML, # форматирование текста
#                                         show_caption_above_media = True, # подпись выше изображения
#                                         reply_markup=kb.name_inline) # inline-клавиатура
#     await callback.message.answer_animation(animation = '', # отправка гифки
#                                             caption = '', # подпись к гифке
#                                             parse_mode=ParseMode.HTML, # форматирование текста
#                                             show_caption_above_media = True, # подпись выше гифки
#                                             reply_markup=kb.name_inline) # inline-клавиатура




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Предыстория - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




@router.callback_query(F.data == 'background_slides')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICQGfBtZTd44SYfW_-E3VRRsl4oAW5AALT6zEbUbkRSp61URPhfllNAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Остальные слайды (11)</b>\n\nПоследствия аварии оказались настолько серьёзными, что правительство Советского Союза было вынуждено провести срочную эвакуацию близлежащих населённых пунктов.',
                                        parse_mode=ParseMode.HTML)
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICQmfBtclFVvgqULz_7GIyMWcrOIgcAALU6zEbUbkRSlWDrD5Og_y6AQADAgADeQADNgQ',
                                        caption = 'Заражённые территории в радиусе тридцати километров от станции превратились в строго охраняемую Зону полного отчуждения.')
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICc2fBujuC4y1qmsAPc8vD8_tcLNvvAALV6zEbUbkRSp3v4vJ7yfdmAQADAgADeQADNgQ',
                                        caption = 'После возведения железобетонного саркофага над разрушенным энергоблоком эксплуатация ЧАЭС возобновилась. Доступность мощного источника энергии и отсутствие населения позволили создать на закрытой территории комплекс секретных лабораторий.')
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICRGfBtwXsCvNQrXm8KYcT4aBWYuleAALX6zEbUbkRSuHVfpJTr_-oAQADAgADeQADNgQ',
                                        caption = '10 июня 2006 года Зона внезапно осветилась нестерпимым светом. На несколько мгновений наступила полная тишина, и было видно, как в небе испаряются облака. Потом пришёл страшный грохот, содрогнулась земля. Большинство военнослужащих, охранявших периметр, мгновенно погибли.')
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICRmfBtyCD4G5Y6aLiRkHKoAPl6gMMAALa6zEbUbkRSr4KwO6_McDGAQADAgADeQADNgQ',
                                        caption = '2007 год. Учёные до сих пор не могут дать внятных объяснений случившемуся. Экспедиции неизменно заканчиваются трагедией, а редкие уцелевшие рассказывают о животных-мутантах, обладающих поразительными способностями.')
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICSGfBtz8afoFnVvSbzEZANOnWbYtLAALe6zEbUbkRSnxcFA9sV43eAQADAgADeQADNgQ',
                                        caption = '2009 год. На территории Зоны отчуждения по разным оценкам присутствуют от одной до трёх сотен неучтённых лиц. Эти люди называют себя сталкерами и занимаются в основном поиском так называемых артефактов - аномальных образований, за которые можно выручить солидные деньги.')
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICSmfBuAVi74fw15AcFf2ycb1M3XAiAALf6zEbUbkRSgIGBFLCuQLyAQADAgADeQADNgQ',
                                        caption = '2010 год. Несмотря на расположенные по периметру кордоны, сталкерство приобретает всё больший размах. Но исследованы только окраины Зоны: попытки проникнуть к её центру заканчиваются неудачей.')
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICTGfBuDMakkA5tXHNgq2Vnb8TvLjXAALg6zEbUbkRSg_6QSJyDXsYAQADAgADeQADNgQ',
                                        caption = 'В 2012 году сталкер по прозвищу Стрелок разгадал загадку Выжигателя Мозгов - мощного излучателя, способного разрушить разум человека, - и отключил его. После этого сталкеры массово ринулись к центру Зоны: одни искали легендарный Клондайк артефактов, другие - не менее легендарный Исполнитель Желаний.')
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICTmfBuEzjB-Lp6Y2XnvupCEOMQdTgAALi6zEbUbkRShcLVGN-QvrnAQADAgADeQADNgQ',
                                        caption = 'В изменившихся условиях Совет национальной безопасности и обороны Украины принял решение о немедленном проведении спецоперации «Фарватер». Ориентируясь по заранее составленным картам аномальных полей, десятки военных вертолётов с десантом на борту взяли курс на ЧАЭС. Несмотря на тщательную подготовку, операция завершилась провалом: ни одна из машин на базу не вернулась.')
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICUGfBuGz_-Rv9w4z2xf5yTxQHG4UKAALj6zEbUbkRSl16z7zBlQJCAQADAgADeQADNgQ',
                                        caption = 'Для выяснения причин провала операции в Зону направлен сотрудник СБУ, майор Дегтярёв, в прошлом - опытный сталкер.')    
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICUmfBuINYHjapzZCPCROR0uyzHoNYAALk6zEbUbkRStPbyJHWGyYBAQADAgADeQADNgQ',
                                        caption = 'С двухнедельным запасом провизии, автоматом и рацией для связи с Центром он начинает свой путь вглубь Зоны.',
                                        reply_markup=kb.back_inline)


@router.callback_query(F.data == 'background')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICLGfBri0niToDl4IoYd0lYGKzbFaCAALQ6zEbUbkRSpdTstbAsf-vAQADAgADeQADNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICLmfBrmM4ok3Kh_KFOEflwMDzMsR7AAKE5zEbAdUQSl39h4vrzCpJAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория</b>\n\nВ ночь на 26 апреля 1986 года реактор четвёртого энергоблока Чернобыльской АЭС разрушился в результате мощного теплового взрыва. Подхваченная ветром радиоактивная пыль частично выпала на территории СССР, оставила очаги излучения в Европе и даже достигла берегов Америки.', 
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline)


@router.callback_query(F.data == 'background_slide3')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICQGfBtZTd44SYfW_-E3VRRsl4oAW5AALT6zEbUbkRSp61URPhfllNAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 3</b>\n\nПоследствия аварии оказались настолько серьёзными, что правительство Советского Союза было вынуждено провести срочную эвакуацию близлежащих населённых пунктов.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline3)


@router.callback_query(F.data == 'background_slide4')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICQmfBtclFVvgqULz_7GIyMWcrOIgcAALU6zEbUbkRSlWDrD5Og_y6AQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 4</b>\n\nЗаражённые территории в радиусе тридцати километров от станции превратились в строго охраняемую Зону полного отчуждения.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline4)

    
@router.callback_query(F.data == 'background_slide5')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICc2fBujuC4y1qmsAPc8vD8_tcLNvvAALV6zEbUbkRSp3v4vJ7yfdmAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 5</b>\n\nПосле возведения железобетонного саркофага над разрушенным энергоблоком эксплуатация ЧАЭС возобновилась. Доступность мощного источника энергии и отсутствие населения позволили создать на закрытой территории комплекс секретных лабораторий.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline5)


@router.callback_query(F.data == 'background_slide6')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICRGfBtwXsCvNQrXm8KYcT4aBWYuleAALX6zEbUbkRSuHVfpJTr_-oAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 6</b>\n\n10 июня 2006 года Зона внезапно осветилась нестерпимым светом. На несколько мгновений наступила полная тишина, и было видно, как в небе испаряются облака. Потом пришёл страшный грохот, содрогнулась земля. Большинство военнослужащих, охранявших периметр, мгновенно погибли.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline6)


@router.callback_query(F.data == 'background_slide7')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICRmfBtyCD4G5Y6aLiRkHKoAPl6gMMAALa6zEbUbkRSr4KwO6_McDGAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 7</b>\n\n2007 год. Учёные до сих пор не могут дать внятных объяснений случившемуся. Экспедиции неизменно заканчиваются трагедией, а редкие уцелевшие рассказывают о животных-мутантах, обладающих поразительными способностями.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline7)


@router.callback_query(F.data == 'background_slide8')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICSGfBtz8afoFnVvSbzEZANOnWbYtLAALe6zEbUbkRSnxcFA9sV43eAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 8</b>\n\n2009 год. На территории Зоны отчуждения по разным оценкам присутствуют от одной до трёх сотен неучтённых лиц. Эти люди называют себя сталкерами и занимаются в основном поиском так называемых артефактов - аномальных образований, за которые можно выручить солидные деньги.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline8)


@router.callback_query(F.data == 'background_slide9')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICSmfBuAVi74fw15AcFf2ycb1M3XAiAALf6zEbUbkRSgIGBFLCuQLyAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 9</b>\n\n2010 год. Несмотря на расположенные по периметру кордоны, сталкерство приобретает всё больший размах. Но исследованы только окраины Зоны: попытки проникнуть к её центру заканчиваются неудачей.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline9)


@router.callback_query(F.data == 'background_slide10')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICTGfBuDMakkA5tXHNgq2Vnb8TvLjXAALg6zEbUbkRSg_6QSJyDXsYAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 10</b>\n\nВ 2012 году сталкер по прозвищу Стрелок разгадал загадку Выжигателя Мозгов - мощного излучателя, способного разрушить разум человека, - и отключил его. После этого сталкеры массово ринулись к центру Зоны: одни искали легендарный Клондайк артефактов, другие - не менее легендарный Исполнитель Желаний.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline10)


@router.callback_query(F.data == 'background_slide11')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICTmfBuEzjB-Lp6Y2XnvupCEOMQdTgAALi6zEbUbkRShcLVGN-QvrnAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 11</b>\n\nВ изменившихся условиях Совет национальной безопасности и обороны Украины принял решение о немедленном проведении спецоперации «Фарватер». Ориентируясь по заранее составленным картам аномальных полей, десятки военных вертолётов с десантом на борту взяли курс на ЧАЭС. Несмотря на тщательную подготовку, операция завершилась провалом: ни одна из машин на базу не вернулась.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline11)


@router.callback_query(F.data == 'background_slide12')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICUGfBuGz_-Rv9w4z2xf5yTxQHG4UKAALj6zEbUbkRSl16z7zBlQJCAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 12</b>\n\nДля выяснения причин провала операции в Зону направлен сотрудник СБУ, майор Дегтярёв, в прошлом - опытный сталкер.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.background_inline12)


@router.callback_query(F.data == 'background_slide13')
async def background(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICUmfBuINYHjapzZCPCROR0uyzHoNYAALk6zEbUbkRStPbyJHWGyYBAQADAgADeQADNgQ',
                                        caption = '<b>» Предыстория: Слайд 13</b>\n\nС двухнедельным запасом провизии, автоматом и рацией для связи с Центром он начинает свой путь вглубь Зоны.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.back_inline)




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Конфиги - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




@router.callback_query(F.data == 'configs')
async def configs(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIGa2fDAAEXut4QCAqtsCnx_XI0MBKvhwACN-sxGxMHGUqmTq6lc5dVHwEAAwIAA3gAAzYE',
                                        caption = '<b>» Конфиги</b>\n\nКонфигурационные файлы открываются блокнотом.\n\nИзменения будут в файлах папок \\bin и \\gamedata, расположенных в корневой папке игры.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.configs_inline)




@router.callback_query(F.data == 'lordofthezone')
async def lordofthezone(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIJNGfDQlhUfchiCKnLx5XcDwMa8h30AALDcAACEwchSnuUDFXj8DjmNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAII_WfDN-_BoDTkuDE1d_x05dBCI63bAAJq6zEbEwchSjb1apYaXBzJAQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Повелитель Зоны</b>\n\n<blockquote><b>Что это вообще такое:</b>\nЭто тестово-читерский мод, предназначеный для тех, кому либо хочется поразвлекатся или сделать красивые скриншоты, или (как я например) для модостроителей, которые с помощью него могут протестировать мод.\n\n(c) Shoker, <u>автор мода</u></blockquote>',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.lordofthezone_inline)


@router.callback_query(F.data == 'lordofthezoneinstallall')
async def lordofthezoneinstall(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKP2fECHjhFtD35-3l6zUe7lxlIzSFAALQ7jEbEwchStKncJnVk6IYAQADAgADeAADNgQ',
                                        caption = '<b>» Все шаги (6)</b>\n\n2. Скопируйте папку \\gamedata в корневую папку игры с заменой файлов.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True)
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKQ2fECJwBKxx5Ezz1YRodVlTWYc2nAALS7jEbEwchSnQ4jiYVjYylAQADAgADeAADNgQ',
                                        caption = '3. Продолжите с заменой для всех текущих элементов.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True)
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKdWfEEsB9FQhC70qQ3Py59mWfGZeXAAL36jEbGvIgSj84NiBWqE6CAQADAgADeAADNgQ',
                                        caption = '4. Запустите игру.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True)
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKd2fEFDuy1oduLYvNOUll5yNm4gdZAAL96jEbGvIgSiFf9cSBGQAB3AEAAwIAA3cAAzYE',
                                        caption = '5. Загрузите любое сохранение.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True)
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKeWfEFEwPIlTSudAOFE9XY21h8_MAAwPrMRsa8iBKbeQhfyqrsX0BAAMCAAN3AAM2BA',
                                        caption = '6. Выйдите в меню игры.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True)
    
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKe2fEFF37OdAZUcSDMsIZOHYIaQnQAAIE6zEbGvIgSjFIRlue7yG7AQADAgADdwADNgQ',
                                        caption = '7. Нажмите F1 (или F1 + Fn).',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.lordofthezoneinstall7_inline)  


@router.callback_query(F.data == 'lordofthezoneinstall')
async def lordofthezoneinstall(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKH2fEBDPe2d3s2AjDM3BjoV18C4epAAIF6TEbVNghSsYqp7BZgT2vAQADAgADeAADNgQ',
                                        caption = '<b>» Конфиги: Установка мода</b>\n\nСкачайте и распакуйте архив.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.lordofthezoneinstall_inline)


@router.callback_query(F.data == 'lordofthezoneinstall2')
async def lordofthezoneinstall2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKP2fECHjhFtD35-3l6zUe7lxlIzSFAALQ7jEbEwchStKncJnVk6IYAQADAgADeAADNgQ',
                                        caption = '<b>» Шаг 2</b>\n\nСкопируйте папку \\gamedata в корневую папку игры с заменой файлов.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.lordofthezoneinstall2_inline)


@router.callback_query(F.data == 'lordofthezoneinstall3')
async def lordofthezoneinstall3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKQ2fECJwBKxx5Ezz1YRodVlTWYc2nAALS7jEbEwchSnQ4jiYVjYylAQADAgADeAADNgQ',
                                        caption = '<b>» Шаг 3</b>\n\nПродолжите с заменой для всех текущих элементов.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.lordofthezoneinstall3_inline)


@router.callback_query(F.data == 'lordofthezoneinstall4')
async def lordofthezoneinstall4(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKdWfEEsB9FQhC70qQ3Py59mWfGZeXAAL36jEbGvIgSj84NiBWqE6CAQADAgADeAADNgQ',
                                        caption = '<b>» Шаг 4</b>\n\nЗапустите игру.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.lordofthezoneinstall4_inline)


@router.callback_query(F.data == 'lordofthezoneinstall5')
async def lordofthezoneinstall5(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKd2fEFDuy1oduLYvNOUll5yNm4gdZAAL96jEbGvIgSiFf9cSBGQAB3AEAAwIAA3cAAzYE',
                                        caption = '<b>» Шаг 5</b>\n\nЗагрузите любое сохранение.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.lordofthezoneinstall5_inline)


@router.callback_query(F.data == 'lordofthezoneinstall6')
async def lordofthezoneinstall6(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKeWfEFEwPIlTSudAOFE9XY21h8_MAAwPrMRsa8iBKbeQhfyqrsX0BAAMCAAN3AAM2BA',
                                        caption = '<b>» Шаг 6</b>\n\nВыйдите в меню игры.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.lordofthezoneinstall6_inline)


@router.callback_query(F.data == 'lordofthezoneinstall7')
async def lordofthezoneinstall7(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIKe2fEFF37OdAZUcSDMsIZOHYIaQnQAAIE6zEbGvIgSjFIRlue7yG7AQADAgADdwADNgQ',
                                        caption = '<b>» Шаг 7</b>\n\nНажмите (F1) или (F1 + Fn).',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.lordofthezoneinstall7_inline) 




@router.callback_query(F.data == 'moneyinstart')
async def moneyinstart(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIZFmfNfvyORu63Hf6tan2hkImBtqn5AAKwaAACbPJoSkJlRJK9lt_XNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAINVmfFYsDzj7SG9JUhpiZmvSySZ5PgAAKM8DEbGvIoSnVI3M-u53qDAQADAgADeQADNgQ',   
                                        caption = '<b>» Конфиги: Количество денег в начале игры</b>\n\n1. Перейдите в папку\n<code>\\gamedata\\configs\\gameplay</code>\n\n2. Откройте файл\n<code>character_desc_general.xml</code>\nс помощью блокнота.\n\n3. Найдите параметры (Ctrl + F)\n<code>&lt;money min="2500"  max="2500"  infinitive="0"&gt;</code>\n\n4.1. Измените значения параметров\n<code>min="2500"</code>\n<code>max="2500"</code>\nзаменив "2500" на количество RU, которое вам нужно в начале игры.\n\n4.2. Измените значение параметра\n<code>infinitive="0"</code>\nзаменив "0" на "1", чтобы иметь бесконечные деньги в начале игры.\n\n5. Сохраните изменения (Ctrl + S).\n\n6. Начните новую игру.',
                                        parse_mode=ParseMode.HTML,
                                        # show_caption_above_media = True,
                                        reply_markup=kb.backconfigs_inline) 




@router.callback_query(F.data == 'fov')
async def fov(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAILEWfEHYz9T2Tz423QmKj2sb--lJXwAAIlZQACVNghSh7ZlocCVquhNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAILBGfEGZ-LWzK-24GajwajeHmztS5aAAId6zEbGvIgSq2kVKvoD6OLAQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Поле зрения</b>\n\nВ «Зове Припяти»: 55°\nВ «Чистом небе»: 67,5°',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.fov_inline)


@router.callback_query(F.data == 'fov55')
async def fov55(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAILJGfEH0uysvyCVzcIYFySSVeF9GCGAAJ9YQACGvIgSq3nmJWq1KQ2NgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAILBGfEGZ-LWzK-24GajwajeHmztS5aAAId6zEbGvIgSq2kVKvoD6OLAQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Поле зрения 55°</b>',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.fov55_inline)


@router.callback_query(F.data == 'fov675')
async def fov675(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAILJmfEH6eEWxIC65T_KSmpZmml-WCoAAKHYQACGvIgSscV_YuA6HipNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAILKGfEH-ZMqQZDV8TskbV5BOsUGi4lAAI56zEbGvIgSqqc4dc1Y5ERAQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Поле зрения 67,5°</b>',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.fov675_inline)


@router.callback_query(F.data == 'fov75')
async def fov75(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAILKmfEH_sJs4cUgskxeDliIoXQwAsGAAKPYQACGvIgSgu6Ikx4bc-iNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAILLGfEH_8g0mh_57hcY3ZV6a17NJbpAAI76zEbGvIgSoEF04EOX8soAQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Поле зрения 75°</b>',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.fov75_inline)


@router.callback_query(F.data == 'fov83')
async def fov83(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAILLmfEIBe4K_mZd5XFg_YqHZWbaUHsAAKWYQACGvIgSszNNHP2F36uNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAILMGfEIBp60H7KwtLThnIjvs7HNAO6AAI86zEbGvIgSmsGVM2wOgpeAQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Поле зрения 83°</b>',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.fov83_inline)


@router.callback_query(F.data == 'fov85')
async def fov85(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAILMmfEIDTD3AY8hJlLyVZhb9onpooTAAKaYQACGvIgSvxCr1gs8Y57NgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAILNGfEIDhgvBvaSooY2sJAg6clxuY6AAI96zEbGvIgSl44kOcRYxiXAQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Поле зрения 85°</b>',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.fov85_inline)


@router.callback_query(F.data == 'fov90')
async def fov90(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAILNmfEIFAYsGXkseuRSR9N6T-FZnJ8AAJMZQACVNghSjHR-TpZklvUNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAILOGfEIFPxDOBi0xVFXJAMuRcrqgd9AAJC6zEbGvIgSjVBUDzE7cC4AQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Поле зрения 90°</b>',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.fov90_inline)


@router.callback_query(F.data == 'fovinstallall')
async def fovinstallall(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIL6mfEMmlVJO93Z0r-sOhkLn4q6AE-AALe6zEbGvIgSge4OykCeRXvAQADAgADeAADNgQ',
                                        caption = '<b>» Все шаги (3)</b>\n\n2. Распакуйте архив.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True)
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIL7GfEMzi2I9LWuNtjIdfSCD2z6C6eAALZ8TEbme0pSoHpWCEXPiUYAQADAgADbQADNgQ',
                                        caption = '3. В распакованном архиве выберете папку, в названии которой будет указан нужный FOV.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True)
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIL5mfEMN_Eq2sttZJObZI9WbJApBJAAALC6zEbGvIgSo-GtWNTYqZ6AQADAgADeAADNgQ',
                                        caption = '4. Из выбранной папки скопируйте файл xrGame.dll в папку \\bin с заменой.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,                                        
                                        reply_markup=kb.backconfigs_inline)


@router.callback_query(F.data == 'fovinstall')
async def fovinstall(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIY7WfNe-yveKsL4u5JwvX5KOLEIh1ZAAKx7DEbbPJoSoOIgcIfXQRKAQADAgADeAADNgQ',
                                        caption = '<b>» Конфиги: Установка поле зрения</b>\n\nСкачайте файл или архив.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.fovinstall_inline)


@router.callback_query(F.data == 'fovinstall2')
async def fovinstall2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIL6mfEMmlVJO93Z0r-sOhkLn4q6AE-AALe6zEbGvIgSge4OykCeRXvAQADAgADeAADNgQ',
                                        caption = '<b>» Шаг 2</b>\n\nРаспакуйте архив.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,
                                        reply_markup=kb.fovinstall2_inline)


@router.callback_query(F.data == 'fovinstall3')
async def fovinstall3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIL7GfEMzi2I9LWuNtjIdfSCD2z6C6eAALZ8TEbme0pSoHpWCEXPiUYAQADAgADbQADNgQ',
                                        caption = '<b>» Шаг 3</b>\n\nВ распакованном архиве выберете папку, в названии которой будет указан нужный FOV.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,                                        
                                        reply_markup=kb.fovinstall3_inline)


@router.callback_query(F.data == 'fovinstall4')
async def fovinstall4(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIL5mfEMN_Eq2sttZJObZI9WbJApBJAAALC6zEbGvIgSo-GtWNTYqZ6AQADAgADeAADNgQ',
                                        caption = '<b>» Шаг 4</b>\n\nИз выбранной папки скопируйте файл xrGame.dll в папку \\bin с заменой.',
                                        parse_mode=ParseMode.HTML,
                                        show_caption_above_media = True,                                        
                                        reply_markup=kb.fovinstall4_inline)




@router.callback_query(F.data == 'passoftime')
async def passoftime(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIZHmfNgGoZjpV6j0TpoTKWAAFrPMMlGgACymgAAmzyaErakodJyyGvUzYE')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIOCmfFxUAhdcZ_AiG3dKYW4jSQixoGAAPsMRsa8jBK2wcqGwOApTABAAMCAAN5AAM2BA',
                                        caption = '<b>» Конфиги: Течение времени</b>\n\n1. Перейдите в папку\n<code>\\gamedata\\configs</code>\n\n2. Откройте файл\n<code>alife.ltx</code>\nс помощью блокнота.\n\n3. Найдите параметр (Ctrl + F)\n<code>time_factor</code>\nустановив флажок «Обтекание текстом».\n\n4. Измените значения параметра\n<code>10;</code> – умножение реального времени на 10;\n<code>1;</code>\n<code>;</code>\n<code>396.0</code>\n\n5. Сохраните изменения (Ctrl + S).',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.backconfigs_inline) 




@router.callback_query(F.data == 'drawradius')
async def drawradius(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIZHmfNgGoZjpV6j0TpoTKWAAFrPMMlGgACymgAAmzyaErakodJyyGvUzYE')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIOSWfFyPCZeKT1Di830M9NSGFmeQAB-AACIewxGxryMEqjOdcS2o1MxwEAAwIAA3kAAzYE',
                                        caption = '<b>» Конфиги: Радиус прорисовки</b>\n\n 1. Перейдите в папку\n<code>\\gamedata\\configs</code>\n\n2. Откройте файл <code>\nalife.ltx</code>\nс помощью блокнота.\n\n3. Найдите параметр (Ctrl + F)\n<code>switch_distance</code>\nустановив флажок «Обтекание текстом».\n\n4. Измените значения параметра \n<code>150;\n0;</code>\n<code>150;</code>\n<code>75.0</code>\n\n5. Сохраните изменения (Ctrl + S).',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.backconfigs_inline) 




@router.callback_query(F.data == 'asperiod')
async def asperiod(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIZHmfNgGoZjpV6j0TpoTKWAAFrPMMlGgACymgAAmzyaErakodJyyGvUzYE')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIOVGfFyjd0Nzi9zL75QXv1B0HXFlGwAAIu7DEbGvIwSo1ethhrUDM2AQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: Период сохранений</b>\n\n 1. Перейдите в папку\n<code>\\gamedata\\configs</code>\n\n2. Откройте файл\n<code>alife.ltx</code>\nс помощью блокнота.\n\n3. Найдите параметр (Ctrl + F)\n<code>autosave_interval</code>\nустановив флажок «Обтекание текстом».\n\n4. Измените значение параметра\n<code>01:05:00</code> – автосохранение каждый 1 час 5 минут.\n\n5. Сохраните изменения (Ctrl + S).',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.backconfigs_inline) 




@router.callback_query(F.data == 'totalweight')
async def totalweight(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIO3WfGj-ojROa7Uw1fk7oPVRi9y4otAAIJZgACo804SuwCGTZkgnncNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIOYGfFza2_oA42IBNi95YrngEB_hd4AAJS7DEbGvIwSmFf6gzaiJ33AQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: Общий вес</b>\n\n1.1. Перейдите в папку\n<code>\\gamedata\\configs\\creatures</code>\n\n1.2. Откройте файл\n<code>actor.ltx</code>\nс помощью блокнота.\n\n1.3. Найдите параметр (Ctrl + F)\n<code>max_walk_weight</code>\nустановив флажок «Обтекание текстом».\n\n1.4. Измените значение параметра\n<code>60</code> – вес, с которого персонаж не сможет двигаться.\n\n1.5. Сохраните изменения (Ctrl + S).\n\n1.6. Измените второй файл.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.totalweight_inline)


@router.callback_query(F.data == 'totalweight1')
async def totalweight1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIO3WfGj-ojROa7Uw1fk7oPVRi9y4otAAIJZgACo804SuwCGTZkgnncNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIOYGfFza2_oA42IBNi95YrngEB_hd4AAJS7DEbGvIwSmFf6gzaiJ33AQADAgADeQADNgQ',
                                        caption = '<b>» Первый файл</b>\n\n1.1. Перейдите в папку\n<code>\\gamedata\\configs\\creatures</code>\n\n1.2. Откройте файл\n<code>actor.ltx</code>\nс помощью блокнота.\n\n1.3. Найдите параметр (Ctrl + F)\n<code>max_walk_weight</code>\nустановив флажок «Обтекание текстом».\n\n1.4. Измените значение параметра\n<code>60</code> – вес, с которого персонаж не сможет двигаться.\n\n1.5. Сохраните изменения (Ctrl + S).\n\n1.6. Измените второй файл.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.totalweight_inline)


@router.callback_query(F.data == 'totalweight2')
async def totalweight2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIZmGfNhRkgbUtzHx3i6so-f0gWMpQpAAJKaQACbPJoSmPb9C9h1iMhNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIOYmfFz2OqHfyv7TZdMQABQiT4l4pYyQACZ-wxGxryMEoHGeNesYrWqwEAAwIAA3kAAzYE',
                                        caption = '<b>» Второй файл</b>\n\n2.1. Перейдите в папку\n<code>\\gamedata\\configs</code>\n\n2.2. Откройте файл\n<code>system.ltx</code>\nс помощью блокнота.\n\n2.3. Найдите параметр (Ctrl + F)\n<code>max_weight</code>\nустановив флажок «Обтекание текстом».\n\n2.4. Измените значение параметра\n<code>50</code> – вес, с которого начинается ускоренный расход сил.\n\n2.5. Сохраните изменения (Ctrl + S).\n\n2.6. Измените первый файл.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.totalweight2_inline) 




@router.callback_query(F.data == 'difficult')
async def difficult(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIO0mfGixVnATdqFLgfPQ36TfHlt6FbAALQ6zEbo804ShjceshjLDNaAQADAgADdwADNgQ',
                                        caption = '<b>» Конфиги: Сложность</b>\n\nВыберете изменяемую сложность:',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.difficult_inline) 


@router.callback_query(F.data == 'difficultnovice')
async def difficultnovice(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIO3WfGj-ojROa7Uw1fk7oPVRi9y4otAAIJZgACo804SuwCGTZkgnncNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIO7GfGllFskblb92r_dkz2owTZ_IY7AAL16zEbo804Skw02sdu2YZLAQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: Сложность «Новичок»</b>\n\n1. Перейдите в папку\n<code>\\gamedata\\configs\\creatures</code>\n\n2. Откройте файл\n<code>actor.ltx</code>\nс помощью блокнота.\n\n3. Найдите секцию (Ctrl + F)\n<code>[actor_immunities_gd_novice]</code>\nустановив флажок «Обтекание текстом».\n\n4. Найдите параметры секции\n<code>burn_immunity</code> – <i>огонь (костры, огненные аномалии);</i>\n<code>strike_immunity</code> – <i>удар (падение с большой высоты, столкновение, аномалии типа «Трамплин»);</i>\n<code>shock_immunity</code> – <i>электрошок;</i>\n<code>wound_immunity</code> – <i>разрыв (порезы, атаки животных);</i>\n<code>radiation_immunity</code> – <i>радиация;</i>\n<code>telepatic_immunity</code> – <i>псивоздействие;</i>\n<code>chemical_burn_immunity</code> – <i>химические вещества;</i>\n<code>explosion_immunity</code> – <i>стойкость к взрывам;</i>\n<code>fire_wound_immunity</code> – <i>пулестойкость.</i>\n\n5. Измените первые (после "=") значения параметров секции \n<code>0.0</code> – <i>абсолютная стойкость к воздействию;</i>\n<code>1.0</code> – <i>без иммунитета к воздействию</i>.\n\n6. Сохраните изменения (Ctrl + S).',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.difficultnovice_inline) 


@router.callback_query(F.data == 'difficultstalker')
async def difficultstalker(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIO3WfGj-ojROa7Uw1fk7oPVRi9y4otAAIJZgACo804SuwCGTZkgnncNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIPDGfGm01CTnK4hdmq-F8ztVLaCybmAAIK7DEbo804SsT8w_FlCNxZAQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: «Сталкер»</b>\n\n1. Перейдите в папку\n<code>\\gamedata\\configs\\creatures</code>\n\n2. Откройте файл\n<code>actor.ltx</code>\nс помощью блокнота.\n\n3. Найдите секцию (Ctrl + F)\n<code>[actor_immunities_gd_stalker]</code>\nустановив флажок «Обтекание текстом».\n\n4. Найдите параметры секции\n<code>burn_immunity</code> – <i>огонь (костры, огненные аномалии);</i>\n<code>strike_immunity</code> – <i>удар (падение с большой высоты, столкновение, аномалии типа «Трамплин»);</i>\n<code>shock_immunity</code> – <i>электрошок;</i>\n<code>wound_immunity</code> – <i>разрыв (порезы, атаки животных);</i>\n<code>radiation_immunity</code> – <i>радиация;</i>\n<code>telepatic_immunity</code> – <i>псивоздействие;</i>\n<code>chemical_burn_immunity</code> – <i>химические вещества;</i>\n<code>explosion_immunity</code> – <i>стойкость к взрывам;</i>\n<code>fire_wound_immunity</code> – <i>пулестойкость.</i>\n\n5. Измените первые (после "=") значения параметров секции \n<code>0.0</code> – <i>абсолютная стойкость к воздействию;</i>\n<code>1.0</code> – <i>без иммунитета к воздействию</i>.\n\n6. Сохраните изменения (Ctrl + S).',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.difficultstalker_inline)


@router.callback_query(F.data == 'difficultveteran')
async def difficultveteran(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIO3WfGj-ojROa7Uw1fk7oPVRi9y4otAAIJZgACo804SuwCGTZkgnncNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIPDmfGm1Q1NnCffbg2DuhzWNHpgUoUAAIL7DEbo804ShlNwU0c1WHuAQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: «Ветеран»</b>\n\n1. Перейдите в папку\n<code>\\gamedata\\configs\\creatures</code>\n\n2. Откройте файл\n<code>actor.ltx</code>\nс помощью блокнота.\n\n3. Найдите секцию (Ctrl + F)\n<code>[actor_immunities_gd_veteran]</code>\nустановив флажок «Обтекание текстом».\n\n4. Найдите параметры секции\n<code>burn_immunity</code> – <i>огонь (костры, огненные аномалии);</i>\n<code>strike_immunity</code> – <i>удар (падение с большой высоты, столкновение, аномалии типа «Трамплин»);</i>\n<code>shock_immunity</code> – <i>электрошок;</i>\n<code>wound_immunity</code> – <i>разрыв (порезы, атаки животных);</i>\n<code>radiation_immunity</code> – <i>радиация;</i>\n<code>telepatic_immunity</code> – <i>псивоздействие;</i>\n<code>chemical_burn_immunity</code> – <i>химические вещества;</i>\n<code>explosion_immunity</code> – <i>стойкость к взрывам;</i>\n<code>fire_wound_immunity</code> – <i>пулестойкость.</i>\n\n5. Измените первые (после "=") значения параметров секции \n<code>0.0</code> – <i>абсолютная стойкость к воздействию;</i>\n<code>1.0</code> – <i>без иммунитета к воздействию</i>.\n\n6. Сохраните изменения (Ctrl + S).',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.difficultveteran_inline)


@router.callback_query(F.data == 'difficultmaster')
async def difficultmaster(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIO3WfGj-ojROa7Uw1fk7oPVRi9y4otAAIJZgACo804SuwCGTZkgnncNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIPEGfGm1uzLBZik2q0By8J2J9eY-iSAAIM7DEbo804Sj24svS3LbKAAQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: «Мастер»</b>\n\n1. Перейдите в папку\n<code>\\gamedata\\configs\\creatures</code>\n\n2. Откройте файл\n<code>actor.ltx</code>\nс помощью блокнота.\n\n3. Найдите секцию (Ctrl + F)\n<code>[actor_immunities_gd_master]</code>\nустановив флажок «Обтекание текстом».\n\n4. Найдите параметры секции\n<code>burn_immunity</code> – <i>огонь (костры, огненные аномалии);</i>\n<code>strike_immunity</code> – <i>удар (падение с большой высоты, столкновение, аномалии типа «Трамплин»);</i>\n<code>shock_immunity</code> – <i>электрошок;</i>\n<code>wound_immunity</code> – <i>разрыв (порезы, атаки животных);</i>\n<code>radiation_immunity</code> – <i>радиация;</i>\n<code>telepatic_immunity</code> – <i>псивоздействие;</i>\n<code>chemical_burn_immunity</code> – <i>химические вещества;</i>\n<code>explosion_immunity</code> – <i>стойкость к взрывам;</i>\n<code>fire_wound_immunity</code> – <i>пулестойкость.</i>\n\n5. Измените первые (после "=") значения параметров секции \n<code>0.0</code> – <i>абсолютная стойкость к воздействию;</i>\n<code>1.0</code> – <i>без иммунитета к воздействию</i>.\n\n6. Сохраните изменения (Ctrl + S).',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.difficultmaster_inline)




@router.callback_query(F.data == 'actor')
async def actor(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIO3WfGj-ojROa7Uw1fk7oPVRi9y4otAAIJZgACo804SuwCGTZkgnncNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIPg2fGvvMf8xumslkGf53UtlOWuwj8AAIE7TEbo804SsKiSz1jfIjEAQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: Персонаж</b>\n\n 1. Перейдите в папку\n<code>\\gamedata\\configs\\creatures</code>\n\n2. Откройте файл\n<code>actor.ltx</code>\nс помощью блокнота.\n\n3. Найдите секцию (Ctrl + F)\n<code>[actor_condition]</code>\nустановив флажок «Обтекание текстом».\n\n4. Найдите параметры секции и измените значения этих параметров',
                                        parse_mode=ParseMode.HTML)
    await callback.message.answer('<code>jump_speed</code> = \n<code>6</code> – <i>высота прыжка</i>\n\n<code>satiety_v</code> =\n<code>0.0000162</code> – <i>скорость уменьшения сытости со временем</i>\n\n<code>radiation_v</code> = \n<code>0.0</code> – <i>скорость уменьшения радиации</i>\n\n<code>satiety_power_v</code> =\n<code>0.005</code> – <i>увеличение силы при уменьшении сытости</i>\n\n<code>satiety_health_v</code> =\n<code>0.0001</code> – <i>увеличение здоровья при уменьшении сытости</i>\n\n<code>satiety_critical</code> =\n<code>0.3</code> – <i>критическое значения сытости</i>\n\n<code>radiation_health_v</code> = \n<code>0.002</code> – <i>уменьшение здоровья при воздействии радиации</i>\n\n<code>psy_health_v</code> = \n<code>0.001</code> – <i>скорость восстановления psy–здоровья</i>\n\n<code>alcohol_v</code> = \n<code>0.0003</code> – <i>уменьшение радиации при использовании водки</i>\n\n<code>health_hit_part</code> =\n<code>1.0</code> – <i>процент хита, уходящий на отнимание здоровья</i>\n\n<code>power_hit_part</code> =\n<code>0.1</code> – <i>процент хита, уходящий на отнимание силы</i>\n\n<code>bleeding_v</code> =\n<code>0.002;</code> <code>0.0005</code> – <i>потеря крови при номинальной ране в секунду</i>\n\n<code>wound_incarnation_v</code> =\n<code>0.0003;</code> <code>0.003</code> – <i>скорость заживления раны</i>\n\n<code>min_wound_size</code> =\n<code>0.0256</code> – <i>минимальный размер раны, после которого она считается зажившей</i>\n\n<code>walk_power</code> = \n<code>0.00002;</code> <code>0.000012</code> – <i>уменьшение силы за секунду во время ходьбы без учета веса ноши</i>\n\n<code>walk_weight_power</code> = \n<code>0.0002;</code> <code>0.0001</code> – <i>умешьшение силы за секунду во время ходьбы с учетом веса ноши для максимального допустимого веса</i>.\n\n',
                                  parse_mode=ParseMode.HTML) 
    await callback.message.answer('5. Сохраните изменения (Ctrl + S).',
                                  reply_markup=kb.backconfigs_inline)




@router.callback_query(F.data == 'configs_armor')
async def configs_armor(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIeA2fpY16luDIKZh-ruVNnAVGtWSWQAAI2cwACcYxIS6itPeU5fDguNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIbzWfNvaRQWHeihWZLBVG1Ss70iFJKAAJJ7zEbbPJoSsNVYST-0xnZAQADAgADdwADNgQ',
                                        caption = 

"""<b>» Конфиги: Броня</b>

1. Перейдите в папку
<code>\\gamedata\\configs\\misc</code>

2. Откройте файл
<code>outfit.ltx</code>
с помощью блокнота.

3. Выберете изменяемую броню:""", 

                                        parse_mode=ParseMode.HTML, 
                                        reply_markup=kb.configs_armor_inline) 


@router.callback_query(F.data == 'configs_armor_1')
async def configs_armor_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 
                                        
"""<b>» Броня: Список 1</b>
    
1. Перейдите в папку
<code>\\gamedata\\configs\\misc</code>

2. Откройте файл
<code>outfit.ltx</code>
с помощью блокнота.

3. Выберете изменяемую броню:""", parse_mode=ParseMode.HTML) 
    await callback.message.edit_reply_markup(reply_markup=kb.configs_armor_1_inline)


@router.callback_query(F.data == 'configs_armor_2')
async def configs_armor_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Броня: Список 2</b>    
                                                  
1. Перейдите в папку
<code>\\gamedata\\configs\\misc</code>

2. Откройте файл
<code>outfit.ltx</code>
с помощью блокнота.

3. Выберете изменяемую броню:""", parse_mode=ParseMode.HTML) 
    await callback.message.edit_reply_markup(reply_markup=kb.configs_armor_2_inline)


@router.callback_query(F.data == 'configs_armor_3')
async def configs_armor_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 
                                        
"""<b>» Броня: Список 3</b>
    
1. Перейдите в папку
<code>\\gamedata\\configs\\misc</code>

2. Откройте файл
<code>outfit.ltx</code>
с помощью блокнота.

3. Выберете изменяемую броню:""", parse_mode=ParseMode.HTML) 
    await callback.message.edit_reply_markup(reply_markup=kb.configs_armor_3_inline)




@router.callback_query(F.data == 'configs_grenades')
async def configs_grenades(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIay2fNmoJOBNjP2RsixNWt9uKWM635AALK7TEbbPJoShBlAAG-y2IznQEAAwIAA3cAAzYE',
                                        caption = '<b>» Конфиги: Гранаты</b>\n\nВыберете изменяемую гранату:',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.configs_grenades_inline) 


@router.callback_query(F.data == 'configs_f1')
async def configs_f1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIa4mfNqJgzWklI9aXFvnIH5d9KIYkhAAI_bAACbPJoSm1uYKePgL-MNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIcHWfNxbtc5fcFJYj6yHGNj8WuZGk3AAKZ7zEbbPJoSqYem6o2M3XxAQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: Граната Ф1</b>\n\n1. Перейдите в папку\n<code>\\gamedata\\configs\\weapons</code>\n\n2. Откройте файл\n<code>w_f1.ltx</code>\nс помощью блокнота.\n\n3. Найдите параметры гранаты (Ctrl + F) и измените значения этих параметров',
                                        parse_mode=ParseMode.HTML) 
    
    await callback.message.answer('<code>destroy_time</code> = \n<code>2500;3500</code> – <i>время детонации</i>\n\n<code>blast</code> = \n<code>3.0</code> – <i>урон, наносимый фугасным воздействием</i>\n\n<code>blast_r</code> = \n<code>5</code> – <i>радиус фугасного воздействия</i>\n\n<code>blast_impulse</code> = \n<code>150</code> – <i>сила удара от фугаса</i>\n\n<code>frags</code> = \n<code>12</code> – <i>количество осколков</i>\n\n<code>frags_r</code> = \n<code>20</code> – <i>радиус разлета осколков</i>\n\n<code>frag_hit</code> =\n<code>0.3</code> – <i>урон от осколка</i>\n\n<code>frag_hit_impulse</code> =\n<code>50</code> – <i>сила удара от осколков</i>\n\n<code>fragment_speed</code> = \n<code>50</code> – <i>скорость осколков</i>',
                                  parse_mode=ParseMode.HTML)
    
    await callback.message.answer('4. Сохраните изменения (Ctrl + S).',
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=kb.configs_f1_inline) 


@router.callback_query(F.data == 'configs_rgd5')
async def configs_rgd5(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIa5GfNqLuvccGJDSy2BHuvlr9uAZtjAAJBbAACbPJoSnm84BmGtd_-NgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIcH2fNxdspHbPTFDCPfmoNGIjV_jjuAAKc7zEbbPJoSrYzLC1MC7aLAQADAgADeQADNgQ',
                                        caption = '<b>» Конфиги: Граната РГД-5</b>\n\n1. Перейдите в папку\n<code>\\gamedata\\configs\\weapons</code>\n\n2. Откройте файл\n<code>w_rgd5.ltx</code>\nс помощью блокнота.\n\n3. Найдите параметры гранаты (Ctrl + F) и измените значения этих параметров',
                                        parse_mode=ParseMode.HTML) 
    
    await callback.message.answer('<code>destroy_time</code> = \n<code>2500;3500</code> – <i>время детонации</i>\n\n<code>blast</code> = \n<code>1.5</code> – <i>урон, наносимый фугасным воздействием</i>\n\n<code>blast_r</code> = \n<code>5</code> – <i>радиус фугасного воздействия</i>\n\n<code>blast_impulse</code> = \n<code>100</code> – <i>сила удара от фугаса</i>\n\n<code>frags</code> = \n<code>10</code> – <i>количество осколков</i>\n\n<code>frags_r</code> =\n<code>10</code> – <i>радиус разлета осколков</i>\n\n<code>frag_hit</code> =\n<code>0.3</code> – <i>урон от осколка</i>\n\n<code>frag_hit_impulse</code> =\n<code>100</code> – <i>сила удара от осколков</i>\n\n<code>fragment_speed</code> = \n<code>200</code> – <i>скорость осколков</i>',
                                  parse_mode=ParseMode.HTML)
    
    await callback.message.answer('4. Сохраните изменения (Ctrl + S).',
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=kb.configs_rgd5_inline) 




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Консоль - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




@router.callback_query(F.data == 'console')
async def console(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIF92fC4rwX9yCbE4H5PKz7n8sowKPVAAJ-6jEbEwcZSg1uyf-sSqU4AQADAgADdwADNgQ',
                                        caption = '<b>» Консоль</b>\n\nКонсоль открывается нажатием клавиши «~». \n\nВведение консольных команд возможно в игровом меню и во время игрового процесса.',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.console_inline)


@router.callback_query(F.data == 'commands')
async def commands(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('<b>» Консоль: Команды (45)</b>\n\n<code>_preset (Minimum, Low, Default, High, Extreme)</code>\n – команда отвечает за графические настройки и качество изображения в игре. В зависимости от значения в скобках будет изменяться качество картинки во время игрового процесса.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>ai_use_torch_dynamic_lights (1/0)</code>\n – значение 1 позволяет ботам использовать источники динамического света (фонарики). После выставлении значения 0 боты перестанут пользоваться фонариками.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>bind &lt;клавиша&gt;</code>\n – позволяет запрограммировать клавишу под определённое действие, выполняемое игровым персонажем.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>cam_inert [0.000, 1.000]</code>\n – параметр, регулирующий резкость движения камеры. Если увеличивать значение, резкие движения мышкой будут слабее видны на экране.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>cl_cod_pickup_mode (1/0)</code>\n – изменяет характер подбора предметов во время игры. Если выключить параметр, придётся наводить мышкой на предмет на земле, чтобы появилась возможность его подбора.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>cl_dynamiccrosshair (1/0)</code>\n – включает и отключает динамический прицел во время игры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>cl_mpdemosave (1/0)</code>\n – позволяет включить и отключить запись демонстрационного видеоролика.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>default_controls</code>\n – поможет, если игрок запутался в установленных настройках управления. Команда вернёт всё в изначальный вид и установит каждой клавише стандартное действие.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>disconnect</code>\n – команда завершает текущую игровую сессию и возвращает пользователя в главное меню игры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_always_run (1/0)</code>\n – изменяет настройки бега по умолчанию. После активации команды персонаж будет передвигаться бегом без нажатия дополнительных клавиш.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_autopickup (1/0)</code>\n – после активации команды предметы во время игры будут автоматически подбираться в инвентарь персонажа.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_backrun (1/0)</code>\n – интересная команда, позволяющая активировать бег спиной вперёд.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_crouch_toggle (1/0)</code>\n – отвечает за включение и отключение режима перехода персонажа в положение приседа и выхода из него.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_dynamic_music (1/0)</code>\n – позволяет отключить (значение 0) динамическую музыку в игре. Является альтернативным способом, так как это можно сделать и в настройках игры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_game_difficulty (gd_novice gd_stalker gd_veteran gd_master)</code>\n – полезная команда, позволяющая изменять сложность, не покидая игрового процесса. Значения в скобках соответствуют значениям сложности, предлагаемых игрой после первого запуска.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_important_save (1/0)</code>\n – включение и отключение автоматического сохранения, не требующего действий от игрока. При активации игра сама сохранится после важных внутриигровых событий.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_kill</code>\n – после введения команды произойдёт самоубийство персонажа. Пригодится в различных ситуациях: например, баги во время игрового процесса или в момент провала персонажа под текстуры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_restart</code>\n – перезапускает текущую игровую сессию.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>g_sleep_time [1, 24]</code>\n – значение от 1 до 24 отвечает за количество часов сна в однопользовательской игре.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>help</code>\n – универсальная команда, позволяющая ознакомиться со всем списком доступных консольных команд.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>hide</code>\n – позволяет скрыть консоль. Также это можно сделать повторным нажатием клавиши ~(Ё).', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>hud_crosshair (1/0)</code>\n – отвечает за отображение прицела во время игры. Значение 0 отключает видимость прицела для игрока. Команда позволяет добавить реалистичности в игровой процесс, однако увеличивает сложность стрельбы.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>hud_crosshair_dist (1/0)</code>\n –включает и отключает отображение расстояния до цели. Также поможет в увеличении реалистичности игрового процесса.', 
                                  parse_mode=ParseMode.HTML)  

    await callback.message.answer('<code>hud_draw (1/0)</code>\n – отвечает за вывод элементов интерфейса на монитор игрока.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>hud_info (1/0)</code>\n – включение опции позволяет игре узнавать различных игровых персонажей и предоставлять пользователю информацию о них.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>hud_weapon (1/0)</code>\n – отвечает за отображение выбранного оружия.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>input_exclusive_mode</code>\n – позволяет вводить консольные команды ещё проще. Если ввести команду в консоль, не нужно будет постоянно нажимать Enter, чтобы активировать команды.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>load_last_save</code>\n – поможет быстро загрузить последнее сохранение и продолжить игру.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>main_menu (1/0)</code>\n – отвечает за показ на мониторе пользователя элементов графического интерфейса.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>mouse_invert (1/0)</code>\n – аналог стандартной опции в настройках. Активирует и выключает инвертирование мыши.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>mouse_sens [0.001, 0.600]</code>\n – поможет изменить чувствительность мыши прямо из консоли. Регулирование происходит изменением значений в скобках.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>ph_iterations [15, 50]</code>\n – команда поможет при возникновении проблем с производительностью. Отвечает за регулирование физики в игре. Если выставить минимальное значение, нагрузка на процессор уменьшится. И, наоборот, если выставить значение 50,процессор будет загружен, но увеличится качество физики во время игры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>r1_detail_textures (1/0)</code>\n – отвечает за детализированные структуры в игре. Отключение повысит производительность, но ухудшит качество изображения. ', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>r1_dlights (1/0)</code>\n – позволяет выключить использование фонариков (они являются динамическими источниками света в игре).', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>r1_fog_luminance [0.200, 5.000]</code>\n – изменяет яркость окружающего тумана. При выставлении минимального значения тумана практически не будет видно.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>r2_slight_fade [0.200, 1.000]</code>\n – команда является аналогом опции из настроек. Позволяет изменить дальность освещения.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>r2_sun_lumscale [-1.000, 3.000]</code>\n – отвечает за интенсивность освещения от внутриигрового солнца.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>r__tf_aniso [1, 16]</code>\n – команда изменяет интенсивность фильтрации текстур. Минимальное значение увеличит количество кадров в секунду, но ухудшит графическую составляющую игры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>rs_c_brightness [0.500, 1.500]</code>\n – изменение общей яркости в игре. Идентичная опция присутствует в настройках в меню игры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>rs_stats (1/0)</code>\n – позволяет отобразить статистику использования ресурсов компьютера или ноутбука на экране. Также показывает количество FPS прямо во время игры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>screenshot</code>\n – после введения команды в папке screenshots, находящейся в основной папке с игрой, появится новый снимок экрана.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>snd_acceleration (1/0)</code>\n – отвечает за ускорение звука посредством физических ресурсов компьютера или ноутбука.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>snd_targets [4, 32]</code>\n – позволяет уменьшить или увеличить количество источников звука, воспроизводимых вместе.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>sv_anomalies_enabled (1/0)</code>\n – значение 0 позволяет отключить всевозможные аномалии во время игры.', 
                                  parse_mode=ParseMode.HTML)

    await callback.message.answer('<code>unbindall</code>\n – удаляет действия, привязанные игроком к определённым клавишам.', 
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=kb.back_inline)




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Тайники - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




@router.callback_query(F.data == 'hidden')
async def hidden(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIG12fDE9kjLwOFUWzWdVAMioXKGNaQAAKx6TEbEwchSqJiJdKHL_YaAQADAgADeQADNgQ',
                                        caption = '<b>» Тайники</b>\n\nВыберете карту тайников интересующей локации:',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.hidden_inline)


@router.callback_query(F.data == 'zaton')
async def zaton(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIHJGfDHrseVu5hdUmKO9AmYRAQ8d5cAAL7bQACEwchSmUfdUCPe-aJNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIG3GfDFSoosS_SAgxE7AINvJy2i0SDAAK06TEbEwchSnVReHqy0cQlAQADAgADdwADNgQ',
                                        caption = '<b>» Тайники: Затон</b>\n\n',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.zaton_inline)


@router.callback_query(F.data == 'upiter')
async def upiter(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIHJmfDHtN2MUwgdmfnIqEKuIttn3XOAAL9bQACEwchSp5aTMzScbHiNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIG3mfDFjpkNo4vCOV_y00TH70iVD_0AAK96TEbEwchSk1xHu3edE48AQADAgADdwADNgQ',
                                        caption = '<b>» Тайники: Окрестности «Юпитера»</b>\n\n',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.upiter_inline)


@router.callback_query(F.data == 'overpass')
async def overpass(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIHKGfDHuOH-D0ZF_IJwQuXihyjoG4bAANuAAITByFKU2gBjuKxXDk2BA')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIG4GfDFklP5WuuMmQbBAHdhEq9Y4Y_AAK_6TEbEwchSnbKCIQv1aMHAQADAgADeQADNgQ',
                                        caption = '<b>» Тайники: Путепровод «Припять-1»</b>\n\n',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.overpass_inline)


@router.callback_query(F.data == 'pripyat')
async def pripyat(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIHKmfDHvZ9pIhNh4A2uzy4-M5q94GdAAIGbgACEwchSm0qHsh9T7ZENgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIG4mfDFnEMULUwRcbrkhxN8UP7JYvLAALA6TEbEwchSgJ8mJYWGkEzAQADAgADdwADNgQ',
                                        caption = '<b>» Тайники: г. Припять</b>\n\n',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.pripyat_inline)


@router.callback_query(F.data == 'x8')
async def x8(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_document(document = 'BQACAgIAAxkBAAIIFGfDI1C5uVGIcjPcjORpw7NxhiWdAAJ7bgACVNgZSvAfVZaBmcJSNgQ')
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAIG5GfDFoHhnbuGtYHFyN1M9k6lm3cKAALB6TEbEwchSsSMPr3HYIklAQADAgADdwADNgQ',
                                        caption = '<b>» Тайники: Лаборатория X8</b>\n\n',
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.x8_inline)




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Аномалии  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# Аномалии 1 списка

photo_anomalies = 'AgACAgIAAxkBAAIhWWfqdt0jZO5Mjg-SiRlztrOfGv3CAALE6DEb3v1RSyDQORElynL7AQADAgADeQADNgQ'

gif_anomalous_grove = 'CgACAgIAAxkBAAIhNWfqctEIBAMqMGUTt-G9xlOf01TtAAJVbgAC3v1RS9401mfsr5v9NgQ'

gif_concrete_bath = 'CgACAgIAAxkBAAIhN2fqc3ggVSVggUpt2TA1kbDQcHpnAAJYbgAC3v1RS6FhbbCnsZWRNgQ'

gif_bitumen = 'CgACAgIAAxkBAAIhOWfqc4fEKEX8iUd8BRHezLHIRVSoAAJZbgAC3v1RS4DC-uafu97GNgQ'

gif_volcano = 'CgACAgIAAxkBAAIhO2fqc5bRNV1vSfBNuf-Xcwn4NTbxAAJcbgAC3v1RS2OjkRgB3t-HNgQ'

gif_iron_forest = 'CgACAgIAAxkBAAIhPWfqc6aROp8K29g3-7rr_SCWUC3LAAJdbgAC3v1RS2s-RCOwx8OgNgQ'

photo_dredger = 'AgACAgIAAxkBAAIhHWfqbvzX91tUgccOZCgqlU4vnfWeAAJ-6DEb3v1RS6G-3MuyrUKTAQADAgADeQADNgQ'

# Аномалии 2 списка

photo_career = 'AgACAgIAAxkBAAIjyWfr9xORKN_B3kud7Z8UhMToT1kkAALk6jEbMhJgS7Ru8GbmuM62AQADAgADeQADNgQ'

photo_kbo_anniversary = 'AgACAgIAAxkBAAIjy2fr9x8Z1ehu_ukdj9YXUnNqkNVcAALn6jEbMhJgS-WtauU4NxRIAQADAgADeQADNgQ'

photo_claw = 'AgACAgIAAxkBAAIjzWfr9yMtJEmbxRk6dQeUsVGIiDkkAALo6jEbMhJgSwOu10s_4hD1AQADAgADeQADNgQ'

gif_boiler = 'CgACAgIAAxkBAAIjz2fr9ypa_dre1FceqjORyutIChn-AAJqbQACMhJgS03xoDs2DGvDNgQ'

gif_vine = 'CgACAgIAAxkBAAIj0Wfr9zG131Qk0Tqp-771kBIR3XhkAAJrbQACMhJgSyaqY5lQbTNmNgQ'

photo_bridge = 'AgACAgIAAxkBAAIj02fr9zYyrKLa6GWry8t50H2IPs0MAALp6jEbMhJgSz0YZjyFpyh8AQADAgADeQADNgQ'

# Аномалии 3 списка

gif_oasis = 'CgACAgIAAxkBAAIkW2fsKF7hzLdisXL01D50mChHQ4QZAAKncAACMhJgS39meiE-DqlANgQ'

photo_oasis_place = 'AgACAgIAAxkBAAIkZ2fsKMF_EKepRrrDwqKl2Gp1ySGYAAK_7DEbMhJgS4RyQGURiQKDAQADAgADeQADNgQ'

gif_ash_heap = 'CgACAgIAAxkBAAIkXWfsKGhX5xLXG9lklTtuuBy0XFmUAAKpcAACMhJgSwbZZe0Zf1VJNgQ'

photo_caves_of_the_burnt_farm = 'AgACAgIAAxkBAAIkX2fsKGtd0Fz319aYplkolFMi-N2YAAK87DEbMhJgS7F9IXq4E6xmAQADAgADeQADNgQ'

photo_floodplains = 'AgACAgIAAxkBAAIkYWfsKHQxy6OnolaVVfuNOaue1ZI4AAK97DEbMhJgS87h429D4an_AQADAgADeQADNgQ'

gif_spatial_bubble = 'CgACAgIAAxkBAAIkY2fsKITsoHVfdfsLAYWpEBYDWjUtAAKucAACMhJgSxw-zNaI6hIrNgQ'

photo_spatial_bubble_place = 'AgACAgIAAxkBAAIkaWfsKMaGZ7yfh_KY6mOQ4npMZpQSAALA7DEbMhJgS67hHp86vkX0AQADAgADeQADNgQ'

gif_scar = 'CgACAgIAAxkBAAIkZWfsKJLOahSeAS8JE-zmbHoAAdxfsgACr3AAAjISYEuDB5LGSr8cGzYE'

# Аномалии 4 списка

photo_burnt_farm = 'AgACAgIAAxkBAAIkyGftNO00i9QBnmr4mzYgHbXNJ2ydAAJN8jEbMhJoS5DUtvAJVQFVAQADAgADeQADNgQ'

photo_pine_oak = 'AgACAgIAAxkBAAIkymftNPN4Ar9aD3nAIIK5AjFTMMBnAAJO8jEbMhJoSyw1IPWbh6g6AQADAgADeAADNgQ'

photo_old_kbo = 'AgACAgIAAxkBAAIkzmftNQAB_dgDj9ctLCOoVSgYhfjBygACUPIxGzISaEuSacfD95UyDwEAAwIAA3kAAzYE'

photo_parking = 'AgACAgIAAxkBAAIk0GftNQfoW9QiVHgFmu9Pl1knTrd2AAJR8jEbMhJoS2kSnDbwHRnDAQADAgADeQADNgQ'

photo_burnt_farm_teleport = 'AgACAgIAAxkBAAIk0mftNRUetkPhF02VCwG_gbMLMvBYAAJS8jEbMhJoSwIzH_eMYzRqAQADAgADeQADNgQ'

gif_tesla = 'CgACAgIAAxkBAAIk1GftNR5o0doXReOEXMplQs8T7D3nAAKwcQACMhJoS_PzXVQjaA76NgQ'

# Аномалии 5 списка

gif_swamp = 'CgACAgIAAxkBAAIk1mftNSrK5DWFx4T2JOP1LNJsh9QYAAKxcQACMhJoS9mofyiydeKiNgQ'

photo_department_store = 'AgACAgIAAxkBAAIk2GftNS4Xozgqt4g0pX7cLKhoDdYdAAJV8jEbMhJoS92sNgq-QIrGAQADAgADeQADNgQ'

gif_circus = 'CgACAgIAAxkBAAIk2mftNTatgVXDjOgIJUXHBrtm6_3FAAKzcQACMhJoS4hG1NJO9RnwNgQ'

photo_school = 'AgACAgIAAxkBAAInjmfuCV3D1ZcwaC1A-JpFVEG8ZuEIAAKD7TEbvfhwS6I2odLut0Y1AQADAgADeQADNgQ'




# Аномалии: Список 1
# - - - - - - - - -
#           Аномальная роща
#           «Бетонная ванна»
#           «Битум»
#           «Вулкан»
#           «Железный лес»
#           Земснаряд

@router.callback_query(F.data == 'anomalies')
async def anomalies(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_anomalies,
                                        caption = 

"""<b>» Аномалии</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.anomalies_inline)


@router.callback_query(F.data == 'anomalies_1')
async def anomalies_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_anomalies,
                                        caption = 

"""<b>» Аномалии: Список 1</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.anomalies_inline)


@router.callback_query(F.data == 'anomalies_1_scroll')
async def anomalies_1_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Аномалии: Список 1</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.anomalies_inline)




@router.callback_query(F.data == 'anomalous_grove')
async def anomalous_grove(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_anomalous_grove,
                                            caption = 

"""<b>» Аномалия: Аномальная роща</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.anomalous_grove_inline)


@router.callback_query(F.data == 'concrete_bath')
async def concrete_bath(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_concrete_bath,
                                            caption = 

"""<b>» Аномалия: «Бетонная ванна»</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.anomalous_grove_inline)


@router.callback_query(F.data == 'bitumen')
async def bitumen(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_bitumen,
                                            caption = 

"""<b>» Аномалия: «Битум»</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.bitumen_inline)


@router.callback_query(F.data == 'volcano')
async def volcano(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_volcano,
                                            caption = 

"""<b>» Аномалия: «Вулкан»</b>

<b>Располагается на локации:</b>
г. Припять

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.volcano_inline)


@router.callback_query(F.data == 'iron_forest')
async def iron_forest(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_iron_forest,
                                            caption = 

"""<b>» Аномалия: «Железный лес»</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.iron_forest_inline)


@router.callback_query(F.data == 'dredger')
async def dredger(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_dredger,
                                        caption = 

"""<b>» ~Аномалия: Земснаряд</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.dredger_inline)




# Аномалии: Список 2
# - - - - - - - - -
#           Карьер
#           КБО «Юбилейный»
#           «Коготь»
#           «Котёл»
#           «Лоза»
#           Мост им. Преображенского

@router.callback_query(F.data == 'anomalies_2')
async def anomalies_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_anomalies,
                                        caption = 

"""<b>» Аномалии: Список 2</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.anomalies_2_inline)


@router.callback_query(F.data == 'anomalies_2_scroll')
async def anomalies_2_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Аномалии: Список 2</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.anomalies_2_inline)




@router.callback_query(F.data == 'career')
async def career(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_career,
                                        caption = 

"""<b>» ~Аномалия: Карьер</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.career_inline)


@router.callback_query(F.data == 'kbo_anniversary')
async def kbo_anniversary(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_kbo_anniversary,
                                        caption = 

"""<b>» ~Аномалия: КБО «Юбилейный»</b>

<b>Располагается на локации:</b>
г. Припять

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.kbo_anniversary_inline)


@router.callback_query(F.data == 'claw')
async def claw(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_claw,
                                        caption = 

"""<b>» Аномалия: «Коготь»</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.claw_inline)


@router.callback_query(F.data == 'boiler')
async def boiler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_boiler,
                                            caption = 

"""<b>» Аномалия: «Котёл»</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.boiler_inline)


@router.callback_query(F.data == 'vine')
async def vine(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_vine,
                                            caption = 

"""<b>» Аномалия: «Лоза»</b>

<b>Располагается на локации:</b>
г. Припять

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.career_inline)


@router.callback_query(F.data == 'bridge')
async def bridge(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_bridge,
                                        caption = 

"""<b>» ~Аномалия: Мост им. Преображенского</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.claw_inline)




# Аномалии: Список 3
# - - - - - - - - -
#           Оазис
#           «Пепелище»
#           Пещеры сгоревшего хутора
#           Плавни
#            «Пространственный пузырь»
#           «Рубец» 

@router.callback_query(F.data == 'anomalies_3')
async def anomalies_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_anomalies,
                                        caption = 

"""<b>» Аномалии: Список 3</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.anomalies_3_inline)


@router.callback_query(F.data == 'anomalies_3_scroll')
async def anomalies_3_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Аномалии: Список 3</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.anomalies_3_inline)




@router.callback_query(F.data == 'oasis')
async def oasis(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_oasis_place)
    await callback.message.answer_animation(animation = gif_oasis,
                                            caption = 

"""<b>» Аномалия: «Оазис»</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемый артефакт:</b>""", # <b>Связанное:</b>

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.oasis_inline)


@router.callback_query(F.data == 'ash_heap')
async def ash_heap(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_ash_heap,
                                            caption = 

"""<b>» Аномалия: «Пепелище»</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.ash_heap_inline)


@router.callback_query(F.data == 'caves_of_the_burnt_farm')
async def caves_of_the_burnt_farm(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_caves_of_the_burnt_farm,
                                        caption = 

"""<b>» ~Аномалия: Пещеры сгоревшего хутора</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.caves_of_the_burnt_farm_inline)


@router.callback_query(F.data == 'floodplains')
async def floodplains(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_floodplains,
                                        caption = 

"""<b>» Аномалия: «Плавни»</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.floodplains_inline)


@router.callback_query(F.data == 'spatial_bubble')
async def spatial_bubble(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_spatial_bubble_place)
    await callback.message.answer_animation(animation = gif_spatial_bubble,
                                            caption = 

"""<b>» Аномалия: «Пространственный пузырь»</b>

<b>Располагается на локации:</b>
Градирня, окрестности «Юпитера»""", # <b>Связанное:</b>

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.spatial_bubble_inline)


@router.callback_query(F.data == 'scar')
async def scar(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_scar,
                                            caption = 

"""<b>» Аномалия: «Рубец»</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.scar_inline)




# Аномалии: Список 4
# - - - - - - - - -
#           Сгоревший хутор
#           «Соснодуб»
#           Старый КБО
#           Стоянка
#           Телепорт на сгоревшем хуторе
#           «Тесла»

@router.callback_query(F.data == 'anomalies_4')
async def anomalies_4(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_anomalies,
                                        caption = 

"""<b>» Аномалии: Список 4</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.anomalies_4_inline)


@router.callback_query(F.data == 'anomalies_4_scroll')
async def anomalies_4_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Аномалии: Список 4</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.anomalies_4_inline)




@router.callback_query(F.data == 'burnt_farm')
async def burnt_farm(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_burnt_farm,
                                        caption = 

"""<b>» ~Аномалия: Сгоревший хутор</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.burnt_farm_inline)


@router.callback_query(F.data == 'pine_oak')
async def pine_oak(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_pine_oak,
                                        caption = 

"""<b>» Аномалия: «Соснодуб»</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.pine_oak_inline)


@router.callback_query(F.data == 'old_kbo')
async def old_kbo(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_old_kbo,
                                        caption = 

"""<b>» ~Аномалия: Старый КБО</b>

<b>Располагается на локации:</b>
г. Припять

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.old_kbo_inline)


@router.callback_query(F.data == 'parking')
async def parking(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_parking,
                                        caption = 

"""<b>» ~Аномалия: Стоянка</b>

<b>Располагается на локации:</b>
Окрестности «Юпитера»

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.old_kbo_inline)


@router.callback_query(F.data == 'burnt_farm_teleport')
async def burnt_farm_teleport(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_burnt_farm_teleport,
                                        caption = 

"""<b>» ~Аномалия: Телепорт на сгоревшем хуторе</b>

<b>Располагается на локации:</b>
Сгоревший хутор, Затон""", # <b>Связанное:</b>

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.burnt_farm_teleport_inline)


@router.callback_query(F.data == 'tesla')
async def tesla(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_tesla,
                                            caption = 

"""<b>» Аномалия: «Тесла»</b>

<b>Располагается на локации:</b>
Поезд, окрестности «Юпитера»""", # <b>Связанное:</b>

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.tesla_inline)




# Аномалии: Список 5
# - - - - - - - - -
#           Топь
#           Подвал универмага
#           «Цирк»
# 
#           « Список 5
#           « Начало

@router.callback_query(F.data == 'anomalies_5')
async def anomalies_5(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_anomalies,
                                        caption = 

"""<b>» Аномалии: Список 5</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.anomalies_5_inline)


@router.callback_query(F.data == 'anomalies_5_scroll')
async def anomalies_5_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Аномалии: Список 5</b>

Выберете интересующую аномалию:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.anomalies_5_inline)




@router.callback_query(F.data == 'swamp')
async def swamp(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_swamp,
                                            caption = 

"""<b>» Аномалия: Топь</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.swamp_inline)


@router.callback_query(F.data == 'department_store')
async def department_store(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_department_store,
                                        caption = 

"""<b>» ~Аномалия: Подвал универмага</b>

<b>Располагается на локации:</b>
г. Припять

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.swamp_inline)


@router.callback_query(F.data == 'circus')
async def circus(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_circus,
                                            caption = 

"""<b>» Аномалия: «Цирк»</b>

<b>Располагается на локации:</b>
Затон

<b>Порождаемые артефакты:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.circus_inline)


@router.callback_query(F.data == 'school')
async def school(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_school,
                                        caption = 

"""<b>» ~Аномалия: Школа</b>

<b>Располагается на локации:</b>
г. Припять

<b>Порождаемые артефакты:</b>""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.school_inline)




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Артефакты - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




# Артефакты: Список 1

photo_artifacts = 'AgACAgIAAxkBAAIhW2fqd00SgyfjsDqb5Yu51pCLl33eAALM6DEb3v1RSzXVNXGTfCoRAQADAgADeQADNgQ'

gif_battery = 'CgACAgIAAxkBAAIe1mfphGWhDYBnJnXvcAOMUyZp3_WOAAK_dgACcYxIS7IW1oAavBTGNgQ'

gif_sparkler = 'CgACAgIAAxkBAAIe2GfphGz_CVHQAoQthDKrqyKTcOzwAALCdgACcYxIS_Td91ncR4g0NgQ'

gif_flash = 'CgACAgIAAxkBAAIe2mfphHJbG2JL5y8lqpufCsABmlzvAALEdgACcYxIS9_ke-mP3IRGNgQ'

gif_twist = 'CgACAgIAAxkBAAIe3GfphHq_R4HH1BRx0Q9SXsr2LVZXAALGdgACcYxIS5Aak3s1oj1oNgQ'

gif_eye = 'CgACAgIAAxkBAAIe3mfphH5T7StOg_l0J56CyLxdnHcsAALHdgACcYxIS71aRXrAri3ENgQ'

gif_gravi = 'CgACAgIAAxkBAAIe4GfphJTmz7RQ4dXqLTfTg1QQ5DScAALIdgACcYxIS1ZMJgrubJUONgQ'

# Артефакты: Список 2

gif_soul = 'CgACAgIAAxkBAAIe4mfphKFzzauUJ9y3NdOqQdg3LCpuAALJdgACcYxIS_tFLkfvs3soNgQ'

gif_goldfish = 'CgACAgIAAxkBAAIe5GfphK2VR-HCGRJnSqlyGq6EbIWiAALMdgACcYxISyLjyocKiNTlNgQ'

gif_altered_isolator = 'CgACAgIAAxkBAAIe5mfphLl61l8eHTWcIrt0dkTcZZllAALOdgACcYxIS61djYPezdVxNgQ'

gif_altered_steering_wheel = 'CgACAgIAAxkBAAIe6GfphMOe7g3z_7Dz48bPypcZNmCkAALPdgACcYxIS7Q-7XP4iyRsNgQ'

gif_stone_flower = 'CgACAgIAAxkBAAIe6mfphZFbmQu6vs7AfcVzLrDnR850AALjdgACcYxISy44QSmzDlzbNgQ'

gif_kolobok = 'CgACAgIAAxkBAAIe62fphZF80iEPfYPKUn53j-3Bt4gtAALkdgACcYxIS6As8L5Xu8YdNgQ'

gif_compass = 'CgACAgIAAxkBAAIe7mfphbHcI2Y6OBf7Majk__hRiFRbAALodgACcYxISyAPGb2LnAaTNgQ'

# Артефакты: Список 3

gif_crystal = 'CgACAgIAAxkBAAIe8GfphcgOowJxeJ_hQjRfzqcZIuxaAALsdgACcYxIS1vSm4Gkbd7XNgQ'

gif_blood_of_stone = 'CgACAgIAAxkBAAIe8mfphfMizLZ6RmAGA1vY41Wy2GIKAALudgACcYxISx5rcB6WtSAmNgQ'

gif_hunk_of_meat = 'CgACAgIAAxkBAAIe9GfphfhxC_0YnEqfd8gvNIYnXa48AALvdgACcYxIS4wzDe2RS3mcNgQ'

gif_moonlight = 'CgACAgIAAxkBAAIe9mfphf0heTlu6Nm0wdQ2ONEm84h8AALxdgACcYxIS6g9t-8PkayuNgQ'

gif_mothers_beads = 'CgACAgIAAxkBAAIe-Gfphf8doKBZK4JD3cfYYtmOAVEsAALydgACcYxIS3zQC8FWAnb3NgQ'

gif_jellyfish = 'CgACAgIAAxkBAAIe-mfphgGGxV1Nc3t2RXM1sfITT-ZrAALzdgACcYxIS6trtaGaN9RONgQ'

gif_night_star = 'CgACAgIAAxkBAAIe_Gfphij1kp145yZz83BETUOqqfVYAAL5dgACcYxIS1m_X1qDSRCKNgQ'

# Артефакты: Список 4

gif_fireball = 'CgACAgIAAxkBAAIfAAFn6hejhSTCpcqdZH5n4EFxHGH8tQAC-mkAAt79UUt665DlOdCV7DYE'

gif_flame = 'CgACAgIAAxkBAAIfAmfqF6qjVVP5nwR30PdseAyvwHrQAAL7aQAC3v1RS4mkL2MpOJ1GNgQ'

gif_bubble = 'CgACAgIAAxkBAAIfBGfqF7COwMlMVIuyguodaIKdwGjTAAL9aQAC3v1RS60gwd4p_n2INgQ'

gif_dummy = 'CgACAgIAAxkBAAIfBmfqF7jT3gFlcNAJoZFhFwHhrzxnAAL_aQAC3v1RS1HHFk-P2P1SNgQ'

gif_firefly = 'CgACAgIAAxkBAAIfCGfqF7xQVcnLYDevDp39_3_No6oPAANqAALe_VFLUjkE53YFCvs2BA'

gif_heart_of_the_oasis = 'CgACAgIAAxkBAAIfCmfqF8Sr_41IoewElWmoTXZ9ClDcAAICagAC3v1RS-ltAAGRHXx_YDYE'

gif_snowflake = 'CgACAgIAAxkBAAIfDGfqF_C6UYlw2dBFgkBu2mO4cMb0AAIFagAC3v1RSwU8K4IhmcBpNgQ'




# Артефакты: Список 1
# - - - - - - - - - - -
#            «Батарейка»
#            «Бенгальский огонь»
#            «Вспышка»
#            «Выверт»
#            «Глаз»
#            «Грави»

@router.callback_query(F.data == 'artifacts')
async def artifacts(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_artifacts,
                                        caption = 

"""<b>» Артефакты</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.artifacts_inline)


@router.callback_query(F.data == 'artifacts_1')
async def artifacts_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_artifacts,
                                        caption = 

"""<b>» Артефакты</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.artifacts_inline)


@router.callback_query(F.data == 'artifacts_1_scroll')
async def artifacts_1_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Артефакты: Список 1</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.artifacts_inline)




@router.callback_query(F.data == 'battery')
async def battery(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_battery,
                                            caption = 

"""<b>» Артефакт: «Батарейка»</b>

<b>Характеристики:</b>
Восст. сил +2
Радиация +1

<b>Стоимость:</b>
6000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (1/6)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_battery_inline)


@router.callback_query(F.data == 'sparkler')
async def sparkler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_sparkler,
                                            caption = 

"""<b>» Артефакт: «Бенгальский огонь»</b>

<b>Характеристики:</b>
Электрозащита +3
Радиация +1

<b>Стоимость:</b>
2000 RU

<b>Обнаружение:</b>
Детектор «Отклик»

<b>Местонахождение:</b> (1/4)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_battery_inline)


@router.callback_query(F.data == 'flash')
async def flash(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_flash,
                                            caption = 

"""<b>» Артефакт: «Вспышка»</b>

<b>Характеристики:</b>
Электрозащита +6
Радиация +2

<b>Стоимость:</b>
4000 RU

<b>Обнаружение:</b>
Детектор «Отклик»

<b>Местонахождение:</b> (1/4)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_battery_inline)


@router.callback_query(F.data == 'twist')
async def twist(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_twist,
                                            caption = 

"""<b>» Артефакт: «Выверт»</b>

<b>Характеристики:</b>
Радиация -3

<b>Стоимость:</b>
8000 RU

<b>Обнаружение:</b>
Детектор «Медведь»

<b>Местонахождение:</b> (1/6)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_twist_inline)


@router.callback_query(F.data == 'eye')
async def eye(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_eye,
                                            caption = 

"""<b>» Артефакт: «Глаз»</b>

<b>Характеристики:</b>
Заживление ран +4
Радиация +2

<b>Стоимость:</b>
12000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (2/11)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_eye_inline)


@router.callback_query(F.data == 'gravi')
async def gravi(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_gravi,
                                            caption = 

"""<b>» Артефакт: «Грави»</b>

<b>Характеристики:</b>
Макс. вес +8
Радиация +2

<b>Стоимость:</b>
12000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (1/12)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_twist_inline)




# Артефакты: Список 2
# - - - - - - - - -
#            «Душа»
#            «Золотая рыбка»
#            Изменённый изолятор
#            Изменённый штурвал
#            «Каменный цветок»
#            «Колобок»
#            «Компас»

@router.callback_query(F.data == 'artifacts_2')
async def artifacts_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_artifacts,
                                        caption = 

"""<b>» Артефакты: Список 2</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.artifacts_2_inline)


@router.callback_query(F.data == 'artifacts_2_scroll')
async def artifacts_2_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Артефакты: Список 2</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.artifacts_2_inline)




@router.callback_query(F.data == 'soul')
async def soul(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_soul,
                                            caption = 

"""<b>» Артефакт: «Душа»</b>

<b>Характеристики:</b>
Восст. здоровья +2
Радиация +2

<b>Стоимость:</b>
6000 RU

<b>Обнаружение:</b>
Детектор «Медведь»

<b>Местонахождение:</b> (1/6)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_soul_inline)


@router.callback_query(F.data == 'goldfish')
async def goldfish(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_goldfish,
                                            caption = 

"""<b>» Артефакт: «Золотая рыбка»</b>

<b>Характеристики:</b>
Макс. вес +12
Радиация +3

<b>Стоимость:</b>
18000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (1/12)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_goldfish_inline)


@router.callback_query(F.data == 'altered_isolator')
async def altered_isolator(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_altered_isolator,
                                            caption = 

"""<b>» Артефакт: Изменённый изолятор</b>

<b>Характеристики:</b>
Радиация +6

<b>Стоимость:</b>
1000 RU

<b>Обнаружение:</b>
Без детектора

<b>Местонахождение:</b>
Ж/д тоннель «Юпитера»""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_altered_isolator_inline)


@router.callback_query(F.data == 'altered_steering_wheel')
async def altered_steering_wheel(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_altered_steering_wheel,
                                            caption = 

"""<b>» Артефакт: Изменённый изолятор</b>

<b>Характеристики:</b>
Радиация +6

<b>Стоимость:</b>
1000 RU

<b>Обнаружение:</b>
Без детектора

<b>Местонахождение:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_altered_steering_wheel_inline)


@router.callback_query(F.data == 'stone_flower')
async def stone_flower(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_stone_flower,
                                            caption = 

"""<b>» Артефакт: «Каменный цветок»</b>

<b>Характеристики:</b>
Пси-защита +3
Радиация +1

<b>Стоимость:</b>
3000 RU

<b>Обнаружение:</b>
Детектор «Отклик»

<b>Местонахождение:</b> (1/4)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_goldfish_inline)


@router.callback_query(F.data == 'kolobok')
async def kolobok(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_kolobok,
                                            caption = 

"""<b>» Артефакт: «Колобок»</b>

<b>Характеристики:</b>
Пси-защита +3
Радиация +1

<b>Стоимость:</b>
3000 RU

<b>Обнаружение:</b>
Детектор «Отклик»

<b>Местонахождение:</b> (1/6)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_kolobok_inline)


@router.callback_query(F.data == 'compass')
async def compass(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_compass,
                                            caption = 

"""<b>» Артефакт: «Компас»</b>

<b>Характеристики:</b>
Термозащита +3
Химзащита +3
Пси-защита +3
Электрозащита +3
Восст. сил +2
Радиация +4

<b>Стоимость:</b>
50000 RU

<b>Местонахождение:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_compass_inline)




# Артефакты: Список 3
# - - - - - - - - - - -
#            «Кристалл»
#            «Кровь камня»
#            «Ломоть мяса»
#            «Лунный свет»
#            «Мамины бусы»
#            «Медуза»
#            «Ночная звезда»

@router.callback_query(F.data == 'artifacts_3')
async def artifacts_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_artifacts,
                                        caption = 

"""<b>» Артефакты: Список 3</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.artifacts_3_inline)


@router.callback_query(F.data == 'artifacts_3_scroll')
async def artifacts_3_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Артефакты: Список 3</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.artifacts_3_inline)




@router.callback_query(F.data == 'crystal')
async def crystal(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_crystal,
                                            caption = 

"""<b>» Артефакт: «Кристалл»</b>

<b>Характеристики:</b>
Термозащита +3
Радиация +1

<b>Стоимость:</b>
2000 RU

<b>Обнаружение:</b>
Детектор «Отклик»

<b>Местонахождение:</b> (3/11)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_crystal_inline)


@router.callback_query(F.data == 'blood_of_stone')
async def blood_of_stone(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_blood_of_stone,
                                            caption = 

"""<b>» Артефакт: «Кровь камня»</b>

<b>Характеристики:</b>
Химзащита +3
Радиация +1

<b>Стоимость:</b>
2000 RU

<b>Обнаружение:</b>
Детектор «Отклик»

<b>Местонахождение:</b> (1/4)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_blood_of_stone_inline)


@router.callback_query(F.data == 'hunk_of_meat')
async def hunk_of_meat(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_hunk_of_meat,
                                            caption = 

"""<b>» Артефакт: «Ломоть мяса»</b>

<b>Характеристики:</b>
Химзащита +6
Радиация +2

<b>Стоимость:</b>
4000 RU

<b>Обнаружение:</b>
Детектор «Отклик»

<b>Местонахождение:</b> (1/4)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_blood_of_stone_inline)


@router.callback_query(F.data == 'moonlight')
async def moonlight(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_moonlight,
                                            caption = 

"""<b>» Артефакт: «Лунный свет»</b>

<b>Характеристики:</b>
Пси-защита +6
Радиация +2

<b>Стоимость:</b>
6000 RU

<b>Обнаружение:</b>
Детектор «Медведь»

<b>Местонахождение:</b> (1/6)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_moonlight_inline)


@router.callback_query(F.data == 'mothers_beads')
async def mothers_beads(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_mothers_beads,
                                            caption = 

"""<b>» Артефакт: «Мамины бусы»</b>

<b>Характеристики:</b>
Заживление ран +2
Радиация +1

<b>Стоимость:</b>
6000 RU

<b>Обнаружение:</b>
Детектор «Медведь»

<b>Местонахождение:</b> (2/11)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_crystal_inline)


@router.callback_query(F.data == 'jellyfish')
async def jellyfish(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_jellyfish,
                                            caption = 

"""<b>» Артефакт: «Медуза»</b>

<b>Характеристики:</b>
Радиация -2

<b>Стоимость:</b>
4000 RU

<b>Обнаружение:</b>
Детектор «Отклик»

<b>Местонахождение:</b> (1/4)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_jellyfish_inline)


@router.callback_query(F.data == 'night_star')
async def night_star(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_night_star,
                                            caption = 

"""<b>» Артефакт: «Ночная звезда»</b>

<b>Характеристики:</b>
Макс. вес +4
Радиация +1

<b>Стоимость:</b>
6000 RU

<b>Обнаружение:</b>
Детектор «Медведь»

<b>Местонахождение:</b> (1/4)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_jellyfish_inline)




# Артефакты: Список 4
# - - - - - - - - - - -
#            «Огненный шар»
#            «Пламя»
#            «Пузырь»
#            «Пустышка»
#            «Светляк»
#            «Сердце Оазиса»
#            «Снежинка»

@router.callback_query(F.data == 'artifacts_4')
async def artifacts_4(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo = photo_artifacts,
                                        caption = 

"""<b>» Артефакты: Список 4</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.artifacts_4_inline)


@router.callback_query(F.data == 'artifacts_4_scroll')
async def artifacts_4_scroll(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_caption(caption = 

"""<b>» Артефакты: Список 4</b>

Выберете интересующий артефакт:""",

                                        parse_mode=ParseMode.HTML)
    await callback.message.edit_reply_markup(reply_markup=kb.artifacts_4_inline)


@router.callback_query(F.data == 'fireball')
async def fireball(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_fireball,
                                            caption = 

"""<b>» Артефакт: «Огненный шар»</b>

<b>Характеристики:</b>
Термозащита +6
Радиация +2

<b>Стоимость:</b>
4000 RU

<b>Обнаружение:</b>
Детектор «Медведь»

<b>Местонахождение:</b> (3/11)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_fireball_inline)


@router.callback_query(F.data == 'flame')
async def flame(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_flame,
                                            caption = 

"""<b>» Артефакт: «Пламя»</b>

<b>Характеристики:</b>
Заживление ран +6
Радиация +3

<b>Стоимость:</b>
18000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (1/11)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_fireball_inline)


@router.callback_query(F.data == 'bubble')
async def bubble(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_bubble,
                                            caption = 

"""<b>» Артефакт: «Пузырь»</b>

<b>Характеристики:</b>
Радиация -4

<b>Стоимость:</b>
12000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (1/12)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_bubble_inline)


@router.callback_query(F.data == 'dummy')
async def dummy(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_dummy,
                                            caption = 

"""<b>» Артефакт: «Пустышка»</b>

<b>Характеристики:</b>
Восст. сил +4
Радиация +2

<b>Стоимость:</b>
12000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (1/12)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_dummy_inline)


@router.callback_query(F.data == 'firefly')
async def firefly(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_firefly,
                                            caption = 

"""<b>» Артефакт: «Светляк»</b>

<b>Характеристики:</b>
Восст. здоровья +6
Радиация +3

<b>Стоимость:</b>
18000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (1/12)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_bubble_inline)


@router.callback_query(F.data == 'heart_of_the_oasis')
async def heart_of_the_oasis(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_heart_of_the_oasis,
                                            caption = 

"""<b>» Артефакт: «Сердце Оазиса»</b>

<b>Характеристики:</b>
Восст. здоровья +2
Насыщение +1
Восст. сил +2
Заживление ран +2
Радиация +4

<b>Стоимость:</b>
50000 RU

<b>Обнаружение:</b>
Без детектора

<b>Местонахождение:</b>""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_heart_of_the_oasis_inline)


@router.callback_query(F.data == 'snowflake')
async def snowflake(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_animation(animation = gif_snowflake,
                                            caption = 

"""<b>» Артефакт: «Снежинка»</b>

<b>Характеристики:</b>
Восст. сил +6
Радиация +3

<b>Стоимость:</b>
18000 RU

<b>Обнаружение:</b>
Детектор «Велес»

<b>Местонахождение:</b> (1/12)""",

                                            parse_mode=ParseMode.HTML,
                                            reply_markup=kb.artifacts_dummy_inline)




"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Случайный совет - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""




ADVICES = [# «100 СОВЕТОВ ПО ВЫЖИВАНИЮ В ЗОНЕ»

    # 1-10

    "Совет №1:\n\nВодка — дешёвая альтернатива противорадиационным препаратам и самый доступный способ снизить воздействие радиации на организм.",

    "Совет №2:\n\nСвойства оружия, защитного костюма или шлема можно улучшить у техников в сталкерских лагерях.",

    "Совет №3:\n\nКоличество переносимого груза напрямую влияет на снижение выносливости. Большой вес ограничит мобильность, а перегрузка не позволит передвигаться вообще.",

    "Совет №4:\n\nПри помощи фильтров в КПК можно скрывать и отображать различные типы отметок на карте. Кнопки управления фильтрами расположены между изображением карты и строкой активного задания.",

    "Совет №5:\n\nНекоторые костюмы комплектуются интегрированными шлемами. Ношение других шлемов с такими костюмами невозможно.",

    "Совет №6:\n\nБезопасно переждать выброс можно в надёжном строении либо под землёй. При приближении выброса расположение ближайшего укрытия будет отображено в КПК.",

    "Совет №7:\n\nДальность — параметр оружия, влияющий на траекторию полёта пули, а удобность — на скорость возврата прицела в исходное положение.",

    "Совет №8:\n\nДля остановки кровотечения можно воспользоваться бинтом, армейской аптечкой или препаратом «Барвинок». Не остановленное вовремя кровотечение может нанести значительный урон организму и закончиться гибелью.",

    "Совет №9:\n\nЭффект от приёма медикаментов не является мгновенным, а некоторые отличаются весьма продолжительный действием. Повторный приём препарата перекрывает уже действующие аналогичные эффекты.",

    "Совет №10:\n\nПодробности текущего задания можно узнать, удерживая «Tab».",

    # 11-20

    "Совет №11:\n\nЧтобы пополнить запасы патронов, разряжайте найденное оружие. Для этого необходимо щёлкнуть правой клавишей мыши на изображение оружия в рюкзаке, а затем выбрать соответствующую команду в контекстном меню.",

    "Совет №12:\n\nДля быстрого использования предмета нужно перетащить его из содержимого рюкзака в одну из четырех ячеек быстрого доступа.",

    "Совет №13:\n\nДетектор необходим для поиска артефактов. Более совершенные детекторы облегчают поиск и помогают обнаружить более ценные артефакты.",

    "Совет №14:\n\nСталкеры не пускают в лагерь людей с оружием наперевес. Чтобы спрятать оружие, нажмите соответствующую ему клавишу («1», «2», «3», «4»).",

    "Совет №15:\n\nГраницы аномалии можно определить, «прощупав» их болтами. Чтобы приготовить болт для броска, нажмите «6».",

    "Совет №16:\n\nОдна из самых распространённых опасностей в Зоне — радиация. Сильное облучение организма приводит к ухудшению состояния здоровья, а без должного лечения — и к смерти.",

    "Совет №17:\n\nПища не только утоляет голод, но и несколько улучшает состояние здоровья.",

    "Совет №18:\n\nЭнергетический напиток временно ускоряет восстановление выносливости, что увеличивает потенциальную мобильность.",

    "Совет №19:\n\nУходя в дальнюю вылазку, нужно взять с собой запас съестного. Сильный голод негативно сказывается на выносливости и здоровье.",

    "Совет №20:\n\nОтсутствие запаса выносливости может обернуться утратой мобильности в критический момент и сделает уязвимым для противника.",

    # 21-30

    "Совет №21:\n\nСтепень заметности для стороннего глаза можно контролировать при помощи индикаторов издаваемого шума и видимости. Оба индикатора расположены в левом верхнем углу экрана.",

    "Совет №22:\n\nДетектор в одной руке не мешает взять в другую нож, пистолет или болт.",

    "Совет №23:\n\nНекоторые медикаменты повышают уровень сопротивляемости организма вредным воздействиям и могут оказаться единственным спасением во время вылазок в аномальные районы.",

    "Совет №24:\n\nСимвол в виде капли крови в правом нижнем углу экрана предупреждает о не остановленном кровотечении. Цвет символа указывает на интенсивность кровотечения.",

    "Совет №25:\n\nСимвол радиационной опасности в правом нижнем углу экрана предупреждает о радиационном облучении организма. Цвет символа указывает на интенсивность облучения.",

    "Совет №26:\n\nВзаимоотношения с окружающими напрямую влияют на цену предлагаемых ими товаров и услуг. При плохих отношениях не стоит надеяться на скидки; хорошие отношения, наоборот, подтолкнут торговца предложить на продажу уникальный товар.",

    "Совет №27:\n\nДля предметов в рюкзаке можно вызвать дополнительное контекстное меню, наведя курсор на нужный предмет и нажав правую клавишу мыши.",

    "Совет №28:\n\nНесмотря на все полезные свойства, большинство артефактов радиоактивны. Данный эффект можно компенсировать артефактами, которые поглощают радиацию.",

    "Совет №29:\n\nНож малоэффективен против врагов, вооружённых огнестрельным оружием. Область его применения — рукопашный бой и бесшумное устранение противника.",

    "Совет №30:\n\nДетектор — единственный надёжный способ проверить наличие артефактов в аномальной зоне.",

    # 31-40

    "Совет №31:\n\nБольшинство артефактов мигрируют внутри аномалий и не видимы глазом, пока не будут выявлены при помощи детектора.",

    "Совет №32:\n\nНочь — время активности мутантов, поэтому сталкеры предпочитают совершать вылазки в светлое время суток.",

    "Совет №33:\n\nПри сильном радиоактивном облучении необходимо воспользоваться противорадиационными препаратами или обратиться к медику. Если такой возможности нет, можно воспользоваться аптечкой, чтобы срочно снизить негативное воздействие радиации на организм.",

    "Совет №34:\n\nБольшинство сталкеров могут провести по окрестностям, но лишь опытный проводник приведёт в отдалённые места быстро и безопасно. В любом случае, свои услуги проводники обычно оценивают в немалую сумму.",

    "Совет №35:\n\nПрибыль могут принести не только артефакты, но и продажа излишков снаряжения. При этом нужно учесть, что торговцы не заплатят полную стоимость снаряжения и не станут покупать повреждённые вещи.",

    "Совет №36:\n\nЧтобы починить оружие, костюм или шлем, необходимо найти техника и, выбрав нужный предмет в окне улучшений, нажать на кнопке ремонта.",

    "Совет №37:\n\nАС-96/2 обладает уникальным режимом стрельбы с отсечкой по два патрона. В этом режиме обе выпущенные пули попадают в одну и ту же точку.",

    "Совет №38:\n\nЧтобы отсоединить установленные на оружии глушитель, оптический прицел или подствольный гранатомёт, необходимо щёлкнуть правой кнопкой мыши на иконке оружия в рюкзаке и воспользоваться соответствующей командой в контекстном меню.",

    "Совет №39:\n\nДвуствольные дробовики могут произвести два выстрела практически одновременно.",

    "Совет №40:\n\nЧтобы не издавать лишнего шума, можно передвигаться шагом, нажав «Shift», или присев, нажав «Ctrl».",

    # 41-50

    "Совет №41:\n\nДробовик — оружие малых дистанций: чем дальше находится цель, тем менее эффективным будет его использование.",

    "Совет №42:\n\nВыбирая укрытие от пуль, необходимо учитывать материал преграды. Деревянная доска или тонкий листовой металл не обеспечат надёжной защиты — в отличие от железобетонной стены.",

    "Совет №43:\n\nНе стоит недооценивать пистолеты. Они обладают высоким убойным действием и очень эффективны против слабо бронированных противников.",

    "Совет №44:\n\nПрямое попадание пули в голову является смертельным для большинства противников.",

    "Совет №45:\n\nУ каждого вида мутантов Зоны своя манера защиты и нападения. Учитывая это, можно значительно повысить свои шансы на выживание.",

    "Совет №46:\n\nДальность броска гранаты можно регулировать, удерживая «MOUSE 2».",

    "Совет №47:\n\nПротивники могут — и будут — активно использовать гранаты. Заметив на экране символ гранаты, немедленно покиньте предполагаемую зону поражения.",

    "Совет №48:\n\nИспользуя прыжок с разбега, можно преодолевать большие ямы и трещины.",

    "Совет №49:\n\nКлючевые индикаторы — состояния здоровья и выносливости — находятся в правом нижнем углу экрана.",

    "Совет №50:\n\nСнайперские винтовки, благодаря высокой настильности и точности, идеально подходят для уничтожения противников на больших дистанциях. Однако в ближнем бою они не столь эффективны.",

    # 51-60

    "Совет №51:\n\nТочность ведения огня в движении значительно ниже, чем из более устойчивого положения — стоя или сидя.",

    "Совет №52:\n\nВ суровых условиях Зоны оружие и защитный комбинезон быстро изнашиваются. Изношенное оружие стреляет менее точно и начинает давать осечки, а изношенный комбинезон теряет защитные свойства.",

    "Совет №53:\n\nЗона живет своей жизнью. Это означает, что всегда остаётся шанс встретить мутанта или враждебно настроенного сталкера в уже зачищенном районе.",

    "Совет №54:\n\nВ Зоне нельзя утрачивать бдительность и полагаться на старую информацию. Оказавшись в некой аномальной зоне снова, можно обнаружить, что её нельзя преодолеть по прежнему маршруту.",

    "Совет №55:\n\nОбычно артефакты не статичны и постепенно передвигаются внутри аномальных зон. В результате бездумного следования за артефактом можно легко попасть в аномалию.",

    "Совет №56:\n\nНекоторые медикаменты обладают уникальными свойствами — как, например, препарат «Геркулес», позволяющий на время увеличить переносимый груз, или препарат пси-блокады, увеличивающий сопротивление воздействию на психику.",

    "Совет №57:\n\nНекоторые сталкеры могут предложить на продажу информацию, уникальный товар или предоставить заказ на конкретный артефакт.",

    "Совет №58:\n\nВ общении с обычными сталкерами можно узнать полезную информацию о новых местах или о событиях, произошедших в последнее время.",

    "Совет №59:\n\nПосле выброса в уже исследованных районах могут появиться новые артефакты.",

    "Совет №60:\n\nЯчейки для размещения оружия позволяют использовать любой его тип. Попробуйте подобрать наиболее удобную для себя комбинацию: автомат и дробовик, пистолет и снайперская винтовка, пулемёт и гранатомёт и т. д.",

    # 61-70

    "Совет №61:\n\nКаждый торговец в лагере сталкеров может предложить свой особенный ассортимент товаров. Скажем, самый лучший выбор медикаментов наверняка окажется у медика.",

    "Совет №62:\n\nПопав в лагерь сталкеров с облучением или раной, можно рассчитывать на бесплатную помощь со стороны здешнего медика.",

    "Совет №63:\n\nЧтобы не носить с собой лишний груз, можно оставить свои вещи в личном ящике на территории лагеря. Как правило, такие ящики находятся неподалёку от мест отдыха.",

    "Совет №64:\n\nПри необходимости скоротать время до определённого часа можно вздремнуть в лагере. Для этого найдите место для отдыха, нажмите «F»/«а» и выберите длительность сна.",

    "Совет №65:\n\nБазовый прибор ночного видения на шлеме можно заменить более совершенным устройством второго поколения, разрешающая способность которого значительно выше.",

    "Совет №66:\n\nОбращайте внимание на треск счётчика Гейгера — он сигнализирует о радиационном излучении. Реагируйте и на сигнал аномальной опасности, который начинает звучать вблизи от аномалии.",

    "Совет №67:\n\nВ Зоне всегда лучше иметь при себе пару запасных магазинов, поскольку они могут понадобиться в любой момент.",

    "Совет №68:\n\nПериодическое сохранение игры может существенно сэкономить время, поскольку в случае гибели не потребуется заново проходить те же места.",

    "Совет №69:\n\nДля рационального применения медикаментов необходимо знать их свойства. Внимательно изучите описание каждого из препаратов.",

    "Совет №70:\n\nЧтобы достать противника в укрытии, можно воспользоваться гранатой. При этом необходимо учесть радиус поражения взрывной волной и осколками, чтобы не навредить союзникам.",

    # 71-80

    "Совет №71:\n\nЧтобы выбросить предмет из рюкзака, необходимо щёлкнуть на нужном предмете правой клавишей мыши и воспользоваться соответствующей командой в контекстном меню. Также, можно просто перетащить предмет в левую часть экрана.",

    "Совет №72:\n\nОтдельный пункт в настройках игры позволяет задействовать автоматическое сохранение игры в ключевых точках.",

    "Совет №73:\n\nПосле возвращения в лагерь рекомендуется починить снаряжение, продать ненужные артефакты и пополнить запасы патронов и медикаментов.",

    "Совет №74:\n\nСтепень сложности игры можно в любой момент откорректировать в настройках.",

    "Совет №75:\n\nЧтобы уменьшить вредное воздействие на организм во время вылазки в аномальные зоны, можно усовершенствовать защитный костюм, использовать протекторные свойства артефактов или применить соответствующие медицинские препараты.",

    "Совет №76:\n\nКаждая единица оружия обладает своими уникальными характеристиками точности, удобности, повреждения и темпа стрельбы. Это даёт возможность каждому выбрать наиболее подходящий образец.",

    "Совет №77:\n\nПомимо боеприпасов и оружия на трупах противников можно обнаружить другие ценные предметы, например КПК с важной информацией.",

    "Совет №78:\n\nАртефакты — не просто ценный товар, зачастую они обладают полезными свойствами.",

    "Совет №79:\n\nВ условиях Зоны многие объекты имеют повышенный радиационный фон, приближаться к ним без соответствующей защиты опасно.",

    "Совет №80:\n\nНекоторые виды оружия могут оснащаться регулируемым дальномерным прицелом. Для регулировки прицельной дистанции используйте колёсико мыши.",

    # 81-90

    "Совет №81:\n\nАвтоматическое оружие позволяет вести огонь в нескольких режимах. Для переключения между режимами ведения огня используйте «9» или «0».",

    "Совет №82:\n\nНекоторые места не позволяют передвигаться даже в согнутом положении. Чтобы присесть как можно ниже, нажмите «Ctrl» и «Shift» одновременно.",

    "Совет №83:\n\nЧтобы сделать скриншот, нажмите клавишу «F12».",

    "Совет №84:\n\nЧтобы уменьшить вероятность поражения под огнём противника, можно вести стрельбу, выглядывая из-за угла. Для этого необходимо удерживать «Q»/«й» или «E»/«у».",

    "Совет №85:\n\nБлагодаря встроенному целеуказателю бинокль позволяет не только рассмотреть удалённые объекты, но и обнаружить среди них противника. Для извлечения бинокля нажмите «5».",

    "Совет №86:\n\nДля включения и выключения фонарика нажмите «L»/«д».",

    "Совет №87:\n\nЧтобы достать болт, нажмите «6».",

    "Совет №88:\n\nВключить и отключить встроенный в шлем прибор ночного видения можно, нажав «N»/«т».",

    "Совет №89:\n\nНажатие «F1», «F2», «F3» или «F4» позволяет использовать соответствующий предмет на панели быстрого доступа.",

    "Совет №90:\n\nВ КПК хранятся карта местности, информация о текущих заданиях, личная статистика и история сообщений. Для активации КПК нажмите «P»/«з».",

    # 91-100

    "Совет №91:\n\nДля поиска артефактов необходимо достать детектор. Чтобы сделать это, нажмите «O»/«щ».",

    "Совет №92:\n\nЧтобы приостановить игру, нажмите «Pause».",

    "Совет №93:\n\nБыстрое сохранение происходит при нажатии «F5». Загрузка последнего сохранения — при нажатии «F9».",

    "Совет №94:\n\nБег — самый быстрый вид перемещения, хотя и приводит к быстрой потере выносливости. Для перехода к этому виду передвижения нажмите «X»/«ч».",

    "Совет №95:\n\nВ режиме прицеливания пули ложатся в цель гораздо точнее, чем при стрельбе навскидку. Для использования прицела нажмите «MOUSE 2».",

    "Совет №96:\n\nПри наличии на оружии подствольного гранатомёта переключение между режимами стрельбы с гранатомёта и обычным, осуществляется нажатием «V»/«м».",

    "Совет №97:\n\nПри наличии нескольких видов патронов для текущего оружия нужный вид выбирается нажатием «Y»/«н».",

    "Совет №98:\n\nЧтобы перезарядить оружие, не дожидаясь полного израсходования патронов в магазине, нажмите «R»/«к».",

    "Совет №99:\n\nЧтобы выбросить текущее оружие, нажмите «G»/«п».",

    "Совет №100:\n\nЧтобы заглянуть в содержимое своего рюкзака, нажмите «I»/«ш»."]


def get_random_advice():
    return random.choice(ADVICES)


@router.callback_query(F.data == 'advice')
async def advice(callback: CallbackQuery):
    advice = get_random_advice()
    await callback.answer() 
    await callback.message.answer_photo(photo = 'AgACAgIAAxkBAAICGmfBqZtaQLW45kUDpu0ZuxR-CBfMAAIV5jEbqV4RShr1cvDtcXI-AQADAgADdwADNgQ', 
                                        caption = '<b>» Случайный совет</b>\n\n' + advice, 
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.advice_inline)


@router.callback_query(F.data == 'random_advice')
async def random_advice(callback: CallbackQuery):
    advice = get_random_advice()
    await callback.answer()
    await callback.message.edit_caption(caption = '<b>» Случайный совет</b>\n\n' + advice, 
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=kb.advice_inline)