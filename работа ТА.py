#1. Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
#Напишите функцию, которая создаёт из этих ключей и значений словарь.
#Если ключу не хватило значения, в словаре должно быть значение None.
#Значения, которым не хватило ключей, нужно игнорировать.
print('1 задание');
keys = ['Фрукты', 'Овощи', 'Бакалея'];
products = ['Бананы', 'Капуста', 'Сахар', 'Молоко'];
def shop(keys,products):
    if len(keys)>len(products):
        while len(keys)>len(products):
            products.append(None);
    else:
        products = products[0:len(keys)];
    return {key:value for key,value in zip(keys, products)};
print ('Отсуствие ключа к значению:');
print (shop(keys, products));
print ('Отсуствие значения к ключу:');
keys = ['Фрукты', 'Овощи', 'Бакалея','Кулинария'];
products = ['Бананы', 'Капуста', 'Сахар'];
print (shop(keys, products));
#2. Есть строка, содержащая текст и целые числа.
#Напишите функцию, которая создаёт список из целых чисел в строке.
print('2 задание');
stroka = 'Этот тескт 541 7ого числа был 65328 написан555';
print(stroka);
#print('Введите строку: ');
#stroka = input();
spisok=[];
def iz_stroki_v_spisok(stroka):
    i=0;
    l=len(stroka);
    while i<l:
        a = '';
        b = stroka[i];
        while '0' <= b <= '9':
            a += b;
            i += 1;
            if i < l:
                b = stroka[i];
            else:
                break;
        i += 1;
        if a != '':
            spisok.append(int(a));
iz_stroki_v_spisok(stroka);
print (spisok);
#3. Написать класс "Кошка". В качестве аргумента, класс принимает число - кол-во котят.
#В конструкторе класса случайным образом создаются котята мальчики (кол-во) и
#котята девочки (кол-во), общее кол-во которых равно аргументу класса - кол-во котят.
#У класса есть два метода: метод "девочки", возвращает кол-во котят девочек и метод "мальчики",
#который возвращает кол-во котят мальчиков.   
print ('3 задание');
import random;
class Cat():
    mankit=0;
    womankit=0;
    def __init__(self, kitten):
        self.kitten = kitten;
        self.mankit = random.randint(0, kitten);
        self.womankit = kitten - self.mankit;
    def info(self):
        print('Всего {0} котят;'.format(self.kitten));
    def womencat(self):
        print('Из них {0} девочек,'.format(self.womankit));
        return self.womankit;
    def mencat(self):
        print('и {0} мальчиков.'.format(self.mankit));
        return self.mankit;
print ('Введите количество котят: ');
m = int(input());
kut1 = Cat(m);
kut1.info();
kut1.womencat();
kut1.mencat();
import os
os.system("pause")
