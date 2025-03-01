# 3. В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

example_str = ' PyCharm — кроссплатформенная интегрированная среда разработки для языка программирования Python, \
 разработанная компанией JetBrains[4] на основе IntelliJ IDEA. Предоставляет пользователю комплекс средств для написания \
 кода и визуальный отладчик.\
  Продукт доступен в двух версиях: PyCharm Community Edition — бесплатная версия, находится под лицензией Apache License, и\
PyCharm Professional Edition — расширенная версия продукта, обладающая дополнительной функциональностью,\
 является проприетарным ПО[5].\
Возможности:\
Отладка кода при помощи PyDev;\
    Рефакторинг кода;\
    Поддержка Git, SVN, Mercurial и других систем контроля версиями;\
    Автодополнение кода.\
Плагины\
Пользователи могут сами писать свои плагины, тем самым расширять возможности PyCharm. \
Некоторые плагины из других JetBrains IDE могут работать с PyCharm. \
Существует более тысячи плагинов, совместимых с PyCharm.\
Лицензирование:\
PyCharm Professional Edition имеет несколько вариантов лицензий, которые отличаются функциональностью, стоимостью и \
 условиями использования, а также является бесплатным для образовательных учреждений и проектов с открытым исходным кодом.\
Существует также бесплатная версия Community Edition, обладающая усеченным набором возможностей[6]. \
Распространяется под лицензией Apache 2. При этом PyCharm Community Edition можно использовать для создания проприетарного ПО, в частности коммерческого[7]'

TOP_LIST = 10

example_str = example_str.lower().replace('.', '').replace(',', '').replace('[', ' [')
list_word = example_str.split()
dict_word = {}

for item in list_word:
    if item not in dict_word:
        dict_word[item] = list_word.count(item)
count = 0
print('ТОП 10 слов:  ')
while len(dict_word) != 0 and TOP_LIST > count:
    for item in dict_word:
        if dict_word[item] == max(dict_word.values()):
            print(f'"{item}":{dict_word[item]}', end='')
            if len(dict_word) != 1 and TOP_LIST > count+1:
                print(', ', end='')
            dict_word.pop(item)
            count += 1
            break