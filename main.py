
from PIL import Image
import filters as f
import text as t
import random

print()
print("Добро пожаловать в консольный фоторедактор.")

while 1:
    print()
    print("Меню фильтров:")

    for i in range(len(t.filters_menu)):  # Вывод меню
        print(str(i + 1) + ":", end=" ")
        print(t.filters_menu[i + 1]["name"])

    print()
    Filter = input("Выберите фильтр (или 0 для выхода): ")

    arrCorrect = []     # Массив правильных ответов
    for i in range(len(t.filters_menu) + 1):
        arrCorrect.append(str(i))       # Сохраняем правильные ответы

    while Filter not in arrCorrect:     # Проверяем правильный ответ
        Filter = input("Вы можете вводить только цифры от 0 до 6: ")

    if Filter == '0':       # Выход
        break

    print()
    print(t.filters_menu[int(Filter)]["name"])             # Вывод имени фильтра
    print(t.filters_menu[int(Filter)]["description"])      # Вывод описания фильтра

    In = input("Применить фильтр к картинке? (Да/Нет): ")
    while In.lower() not in ['да', 'нет']:
        In = input("Вы можете ввести только Да или Нет: ")

    if In.lower() == 'да':
        path = str(input("Введите путь к файлу (изображение): "))

        WrongPath = True
        while WrongPath:  # Проверка правильности пути
            try:
                img = Image.open(str(path)).convert('RGB')  # Открываем изображение
                WrongPath = False
            except:
                random_number = random.randint(1, 3)
                path = str(input(t.ErrorText[random_number]))  # Выводим сообщение об ошибке
                WrongPath = True

        img = Image.open(str(path)).convert('RGB')  # Дублируем чтобы img стал глобальной

        print("Загрузка...")

        global img_new

        if Filter == '1':
            img_new = f.RedFilter().apply_to_image(img)
        elif Filter == '2':
            img_new = f.GreenFilter().apply_to_image(img)
        elif Filter == '3':
            img_new = f.BlueFilter().apply_to_image(img)
        elif Filter == '4':
            img_new = f.InverseFilter().apply_to_image(img)
        elif Filter == '5':
            img_new = f.BrightFilter().apply_to_image(img)
        else:
            img_new = f.DarkFilter().apply_to_image(img)

        # current_file = os.path.realpath(path)
        # file = os.path.basename(path)
        # print(current_file)
        # print(file)

        save_path = str(input("Куда сохранить: "))  # Строка для сохранения пути

        WrongPath = True
        while WrongPath:  # Проверка правильности пути
            try:
                img_new.save(save_path)  # Сохраняем изображение
                WrongPath = False
            except:
                random_number = random.randint(1, 3)
                save_path = str(input(t.ErrorText[random_number]))  # Выводим сообщение об ошибке
                WrongPath = True

        print("Сохранено в " + str(save_path))

        In = input("Ещё раз? (Да/Нет): ")
        while In.lower() not in ['да', 'нет']:
            In = input("Вы можете ввести только Да или Нет: ")

        if In.lower() == 'нет':  # Выход
            break

print("До свиданья")
