meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            'РОФЛ':'шутка'
            }
            
word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('у нас пока нет такого слова, но мы над этим работаем...')           