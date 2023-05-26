def readfile():
    data = [i.split() for i in open("test.txt", "r", encoding = 'utf-8')]
    return data

def printinfo(data):
    for i in data:
        print(i)
        
def search (data):
    start = -1
    famil = input('искомая Фамилия: ')
    for i in data:
        if famil in i:
            start = 0
            print(i)
    if start: print('Такой фамилии не найдено')

def add_new (data):
    a = input("Введите фамилию (только на англ, русский язык не работает): ")
    b = input("Введите номер: ")
    with open('test.txt', 'a') as f:
        f.write(a +"    "+ b +'\n')
    return data
    
def export():
    pass

def delete():
    pass

def main():
    my_choice = -1
    data = readfile()
    while my_choice != 0:
        print("выберите одно из действий:")
        print("1 - вывести инфо на экран")
        print("2 - поиск по фамилии")
        print("3 - добавить контакт")
        print("4 - удалить контакт")
        print("5 - экспорт данных")
        print("0 - выйти из программы")
        my_choice = int(input())
        if my_choice == 1:
            printinfo(data)
        elif my_choice == 2:
            search (data)
        elif my_choice == 3:
            add_new (data)
        elif my_choice == 4:
            delete (data)
        elif my_choice == 5:
            export (data)

    print("До свидания")

if __name__ == "__main__":
    main()

