from PIL import Image
import photoshop_back


def use_filter(obj):
    print()
    use_choice = input("Применить фильтр к картинке? (Да/Нет): ")
    if use_choice.lower() == "да":
        new_img = obj.filter(img)
        save_path = input("Куда сохранить: ")
        new_img.save(save_path)
    elif use_choice.lower() != "нет":
        print()
        print("Некорректный ввод, попробуйте ещё раз")
        print()
        use_filter(obj)

    again_choice = input("Ещё раз? (Да/Нет): ")
    if again_choice.lower() == "да":
        print()
        print("-------------------------------")
        print()
        choice()
    elif again_choice.lower() == "нет":
        print()
        print("Спасибо, что воспользовались нашей программой!")
        return
    else:
        print()
        print("Некорректный ввод, завершаем работу программы...")


def choice():
    print("Меню фильтров:")
    print("1: Красно-синий фильтр")
    print("2: Фильтр 'По квадратам'")
    print("3: Инверсия")
    print("4: Чёрно-белый пуантилизм")
    print("0: Выход")
    print()
    start_choice = input("Выберите фильтр (или 0 для выхода): ")
    obj = ""
    if start_choice == "0":
        print()
        print("Спасибо, что воспользовались нашей программой!")
        return
    elif start_choice == "1":
        obj = photoshop_back.Red_and_blue()
    elif start_choice == "2":
        obj = photoshop_back.Squares()
    elif start_choice == "3":
        obj = photoshop_back.Inversion()
    elif start_choice == "4":
        obj = photoshop_back.Black_and_White()
    else:
        print()
        print("Некорректный ввод")
        print()
        print("-------------------------------")
        print()
        start_choice()

    print(f"{obj.name}: ")
    print(obj.text)
    use_filter(obj)


def main():
    global img
    print("Добро пожаловать в российский фотошоп!!!")
    flag = False
    while not flag:
        try:
            path = input("Введите путь к файлу: ")
            img = Image.open(path)
            flag = True
        except Exception:
            print("Некорректный путь. Попробуйте снова.")
    print()
    choice()


if __name__ == "__main__":
    main()
