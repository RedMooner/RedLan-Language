


# RedRackView Cable Magazine Project
 # Introduction
 
Учет в IT играет очень важную роль. Безусловно, знания как настроить Catalyst с нуля, собрать degraded RAID и настроить новый инстанс БД Oracle очень ценны и человек ими владеющий достоин уважения. Однако когда этих Catalyst-ов и прочих IBM Flex-ов несколько серверных стоек, и не в одной комнате, то вопрос: «Где находится тот самый сервак на котором RAID посыпался», может поставить в тупик не одного специалиста. Поиск определенного сервера, я уж не говорю про сетевые кабели, может превратиться в увлекательнейший квест. И не дай вам пинг напороться на такой квест в условиях случившейся аварии. Вот на такой случай мы начали разработку данной программы.


# RedLang scripting language

Встроенный скриптовый язык , для автоматизации работы системных администраторов. Каждый сможет написать автоматизированный алгоритм для заполнения журнала. Например, для добавления в блейд-шасси  модулей и серверов. Сделать такое в других программах будет затруднительно, но здесь это легко сделать как в самой программе, так и в своих целях усилия можно свести на нет с помощью скрипта. Например скрипт предложит ввести название модуля сервер и.т.п. и все сделает за вас.
Также стоит отметить, что язык вы можете использовать не только для автоматизаций процессов самой программы, но и для личных целей. Также каждый сможет расширить функционал данного языка , с помощью модулей написанных на Python. RedLang с легкостью сможет работать с ними.
 Язык на данный момент находится на этапе разработки, активно развивается и готовится для релиза. Пользоваться им вместе с программой можно будет примерно через 3-4 месяца. А для личных целей уже в ближайшее время. 

> Следите за развитием: https://github.com/RedMooner/RedLan-Language

# Синтаксис

## В данном разделе разберем уже добавленные функции языка


 ### Функция use
 

> Данная функция подключает встроенные библиотеки в интерпретатор, данные библиотеки находятся с папке с интерпретатором. Их исходный код является открытым. Каждая библиотека дает возможность использовать содержащиеся в ней модули
##### Пример

    use os;
    createFile("filename.txt",some value);
   
   Данный код, подключает библиотеку os и использует ее функцию createFile для создания файлов
   
   ### Базовый функционал
### Переменные
> Как и в любом другом языке, здесь есть **переменные** - поименованная, либо адресуемая иным способом область памяти
##### Пример

    $variable = Hello World;
   Данный код, создает переменную с именем variable и значением Hello World
   
### Массивы
> **Массив** — структура данных, хранящая набор значений

#### Объявление массива

    $array[] = {1,2,3,4,5};
Данный код объявляет массив с названием array с пятью элементами 1,2,3,4,5
### Функции для работы с массивами

#### Функция **length()** - возвращает кол-во элементов в массиве

    $array[] = {1,2,3,4,5};
    $array[].length();
   
   >Вывод: 5
   
#### Функция **add(param)** - добавляет указанный как параметр *param* элемент в массив

    $array[] = {1,2,3,4,5};
    $array[].add(1);
   > Вывод: будет добавлен элемент со значением 1
   





