# Язык описания конечных автоматов

## Описание языка

Для начала зададим алфавит, данном случае он будет состоять из слов:
```
alphabet { "северный", "попугай", "синий", "нутрия", "олень" }
```
 
Затем нужно перечислить состояния, которые есть у автомата:
```
states { q0, q1, q2, q3, q4, q5 }
```
 
Нужно указать терминальные вершины:
```
terminal { q1, q5 }
```
 
Иногда состояний может быть слишком много, настолько, что название не способно отразить суть. Будут полезны описания состояний, при необходимости их можно добавить так:
```c++
state q1 { "два синих попугая и один северный олень" } // state <name_state> { <description> }
```
 
Затем нужно добавить переходы между состояниями, они характеризуются состоянием, из которого переходим, в которое переходим, и элементами из алфавита:
```c++
q0 ---> q5 ["северный", "олень"] // <out_state> ---> <in_state> [<elements_of_alphabet>]
```
 
Если автомат создан неверно (нет состояния, которое могло бы быть начальным, или их наобот несколько, не по всем элементам алфавита можно выйти из вершины и тд), то такой автомат создан не будет. Если всё верно, то начальная вершина будет определена автоматически (это вершина, в которую не входит ни одно ребро, или все входящие ребра - петли)

Cимволом алфавита является произвольная последовательность символьного типа `char`, необходимо выделять её в кавычки - `""`. Чтобы использовать `"` в качестве одного из символов последовательности, нужно их экранировать - `\"`, аналогично для использования `\`, нужно экранировать - `\\`.

Также можно писать комментарии, как это показано выше.

Пример описания автомата:

Путешественникам, чтобы добраться до волшебного места, нужно обязательно два раза подряд пойти направо, остальные их передвижения не так важны.

```
alphabet { "←", "→", "↑", "↓" }
states { q0, q1, q2}
terminal { q2 }
state q1 { "одна → подряд" }
state q2 { "две → подряд, победа!" }
q0 ---> q1 [ "→" ]
q0 ---> q0 [ "←", "↑", "↓" ]
q1 ---> q2 [ "→" ]
q1 ---> q0 [ "←", "↑", "↓" ]
q2 ---> q2 [ "←", "→", "↑", "↓" ]
```

## Лексер

[Лексер](https://github.com/Fawentus/describing-finite-machine/Lex/myLex.py) написан на языке Python, использован ply.lex. Консольное приложение запускается командой: 
```
python3.8 myLex.py "<name_file>"
```

Например, так запускается [мой "нулевой" тест](https://github.com/Fawentus/describing-finite-machine/Lex/ex):
```
python3.8 myLex.py "ex"
```
Этот код не строит осмысленный автомат, я включила туда то, что могло бы продемонстрировать все возможности моего лексера. [Это](https://github.com/Fawentus/describing-finite-machine/Lex/ex.out) то, что будет в выходном файле после работы программы (значения токенов типа `STR` выводятся с отбрасыванием `""`).
  
Это примеры работы лексера на тестах из прошлого домашнего задания:
  
  [Тест 1](https://github.com/Fawentus/describing-finite-machine/Lex/ex1) - [результат работы лексера](https://github.com/Fawentus/describing-finite-machine/Lex/ex1.out)
  
  [Тест 2](https://github.com/Fawentus/describing-finite-machine/Lex/ex2) - [результат работы лексера](https://github.com/Fawentus/describing-finite-machine/Lex/ex2.out)
  
  [Тест 3](https://github.com/Fawentus/describing-finite-machine/Lex/ex3) - [результат работы лексера](https://github.com/Fawentus/describing-finite-machine/Lex/ex3.out)


## Парсер

[Мой синтаксический анализатор](https://github.com/Fawentus/describing-finite-machine/Parse/parse.py) реализован на языке Python, с помощью генератора синтаксических анализаторов семейства yacc.

Консольное приложение запускается командой: 
```
python3.8 parse.py "<name_file>"
```

Например, так запускается тест с названием `ex1`:
```
python3.8 parse.py "ex1"
```

В результате синтаксического анализа конечный автомат представляется в виде экземпляра класса `Automaton`. Из него можно узнать, к примеру, какие есть состояние, является ли состояние терминальным, какие ребра ведут в определенной состояние, какое состояние является начальны, по каким символам можно перейти из одного состояния в другое, есть ли одинаковые состояния, по всем ли символам можно перейти из некоторого состояния и многое другое.

В файле с результатом в случае успешного создания конечного автомата указываются символы алфавита, состояния (для каждого из них: имя, является ли оно терминальным и его описание), ребра (для каждого из них: куда и откуда они ведут, по каким символам можно совершить переход) и имя начального состояния. В случае ошибки при создании автомата будет выведено сообщение об этой ошибки, и пользователь будет уведомлен, что конечный автомат создан не будет.

Тесты:

1) [входные данные](https://github.com/Fawentus/describing-finite-machine/Parse/ex1) - [выходные данные](https://github.com/Fawentus/describing-finite-machine/Parse/ex1.out)
2) [входные данные](https://github.com/Fawentus/describing-finite-machine/Parse/ex2) - [выходные данные](https://github.com/Fawentus/describing-finite-machine/Parse/ex2.out)
3) [входные данные](https://github.com/Fawentus/describing-finite-machine/Parse/ex3) - [выходные данные](https://github.com/Fawentus/describing-finite-machine/Parse/ex3.out)

## Тесты:

1) Полные детерминированные автоматы, у которых есть начальное состояние, все состояния и символы уникальны приведены в задании 2
2) Автомат, не имеющий однозначно определенного начального состояния: [входные данные](https://github.com/Fawentus/describing-finite-machine/Parse/have_not_initial_state) - [выходные данные](https://github.com/Fawentus/describing-finite-machine/Parse/have_not_initial_state.out)
3) Автомат, символы которого не уникальны: [входные данные](https://github.com/Fawentus/describing-finite-machine/Parse/not_unique_symbols) - [выходные данные](https://github.com/Fawentus/describing-finite-machine/Parse/not_unique_symbols.out)
4) Неполный автомат: [входные данные](https://github.com/Fawentus/describing-finite-machine/Parse/not_complete) - [выходные данные](https://github.com/Fawentus/describing-finite-machine/Parse/not_complete.out)
5) Недетерминированный автомат: [входные данные](https://github.com/Fawentus/describing-finite-machine/Parse/not_deterministic) - [выходные данные](https://github.com/Fawentus/describing-finite-machine/Parse/not_deterministic.out)
6) Автомат, состояния которого не уникальны: [входные данные](https://github.com/Fawentus/describing-finite-machine/Parse/not_unique_states) - [выходные данные](https://github.com/Fawentus/describing-finite-machine/Parse/not_unique_states.out)
