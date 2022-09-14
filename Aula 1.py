Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print hello mundo
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(hello mundo)?
>>> print ('Hello mundo!')
Hello mundo!
>>> a=2
>>> b=1
>>> c=(a+b)
>>> d=(c*3)
>>> e=(a+b+c+d)
>>> 
>>> print (a)
2
>>> print (b)
1
>>> print (c)
3
>>> print (d)
9
>>> print (e)
15
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> print ('7')+('4')
7
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print ('7')+('4')
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
>>> PRINT '7'+'4'
SyntaxError: invalid syntax
>>> print ('7'+'4')
74
>>> nome='charles'
>>> idade=35
>>> peso=80
>>> print (nome, idade, peso)
charles 35 80
>>> nome'charles'
SyntaxError: invalid syntax
>>> 
>>> nome='charles'
>>> idade=35
>>> peso=80.5
>>> print ('meu nome é' nome, 'e tenho' idade 'anos', 'Meu peso' peso)
SyntaxError: invalid syntax
>>> print ('meu nome é', nome, 'e tenho', idade, 'anos', 'Meu peso', peso)
meu nome é charles e tenho 35 anos Meu peso 80.5
>>> nome=input ('Qual seu nome?')
Qual seu nome?João
>>> idade-input ('Qual sua idade?')
Qual sua idade?28
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    idade-input ('Qual sua idade?')
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> 
>>> idade=input ('Qual sua idade?')
Qual sua idade?28
>>> peso=input ('Qual seu peso')
Qual seu peso82
>>> print ('meu nome é', nome, 'e tenho', idade, 'anos', 'Meu peso', peso)
meu nome é João e tenho 28 anos Meu peso 82
>>> file
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    file
NameError: name 'file' is not defined
>>> 
============ RESTART: C:/Users/Aluno SENAI/Desktop/python charles.py ============
Qual seu nome?Jose
Qua asua idade?34
Qual seu peso?75
Seu nome é Jose . Sua idadade é 34 . Seu peso é 75
>>> 