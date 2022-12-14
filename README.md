<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
  <div id="badges">
  <a href="your-linkedin-URL">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="your-youtube-URL">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  <a href="your-twitter-URL">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
</div>
<h1>
  hey there
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>
</div>

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/RedMooner/RedLan-Language)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/RedMooner/RedLan-Language?label=Last%20update%20tag)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/RedMooner/RedLan-Language)
![GitHub followers](https://img.shields.io/github/followers/RedMooner?style=social)
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


 # Функция use

> Данная функция подключает встроенные библиотеки в интерпретатор, данные библиотеки находятся с папке с интерпретатором. Их исходный код является открытым. Каждая библиотека дает возможность использовать содержащиеся в ней модули
<details><summary>Показать пример</summary>
<p>

##### Пример
```ruby
    use os;
    createFile("filename.txt",some value);
```   
   Данный код, подключает библиотеку os и использует ее функцию createFile для создания файлов
   
</p>
</details>

   # Базовый функционал
# Переменные
> Как и в любом другом языке, здесь есть **переменные** - поименованная, либо адресуемая иным способом область памяти

<details><summary>Показать пример</summary>
<p>

##### Пример
```ruby
    $variable = Hello World;
```
   Данный код, создает переменную с именем variable и значением Hello World
   
</p>
</details>

# Массивы
> **Массив** — структура данных, хранящая набор значений

# Объявление массива
<details><summary>Показать пример</summary>
<p>

##### Пример
```ruby
    $array[] = {1,2,3,4,5};
```
Данный код объявляет массив с названием array с пятью элементами 1,2,3,4,5
</p>
</details>

# Функции для работы с массивами

# Функция **length()** - возвращает кол-во элементов в массиве
```ruby
    $array[] = {1,2,3,4,5};
    $array[].length();
```
   >Вывод: 5
   
# Функция **add(param)** - добавляет указанный как параметр *param* элемент в массив
```ruby
    $array[] = {1,2,3,4,5};
    $array[].add(1);
```
   > Вывод: будет добавлен элемент со значением 1
   
# Функция Python
> Данная функция подключает кастомный модуль в RedLan

Пример на готовой структуре проекта RedLan
**RedLan Код: /code.redlan** 
```ruby
	$a = 1;
	$b = 1;
	python(test.py > $a,$b);
```
**Python модуль: /Modules/test.py**
```python
    class Module:
       def main(self, args):
          return str(float(args[0]) + float(args[1]
```
> Вывод: результат выполнения: 2.0




