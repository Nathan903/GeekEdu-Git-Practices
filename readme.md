\[ [Index](index.md) | []() | [Exercise 1.2](ex1_2.md) \]

# Exercise 1.1

*Objectives:*

- Make sure Python is installed correctly on your machine
- Start the interactive interpreter
- Edit and run a small program

*Files Created:* `art.py`

## (a) Launch Python

Start Python3 on your machine.  Make sure you can type simple
statements such as the "hello world" program:

```python
>>> print('Hello World')
Hello World
>>>
```

In much of this course, you'll want to make sure you can work from
the interactive REPL like this.   If you're working from a different
environment such as IPython or Jupyter Notebooks, that's fine.

## (b) Some Generative Art

Create the following program and put it in a file called `art.py`:

```python
# art.py

# art.py

import sys
import random

chars = r'\|/'

def draw(rows, columns):
    for r in rows:
        print(''.join(random.choice(chars) for _ in range(columns)))
draw(10, 20)
```

Make sure you can run this program from the command line or a terminal.

```
bash % python3 art.py 10 20
```

If you run the above command, you'll get a crash and traceback message.
Go fix the problem and run the program again.  You should get output like
this:

```
bash % python3 art.py 10 20
||||/\||//\//\|||\|\
///||\/||\//|\\|\\/\
|\////|//|||\//|/\||
|//\||\/|\///|\|\|/|
|/|//|/|/|\\/\/\||//
|\/\|\//\\//\|\||\\/
|||\\\\/\\\|/||||\/|
\\||\\\|\||||////\\|
//\//|/|\\|\//\|||\/
\\\|/\\|/|\\\|/|/\/|
bash %
```

### Important Note

It is absolutely essential that you are able to edit, run, and debug
ordinary Python programs for the rest of this course.  The choice
of editor, IDE, or operating system doesn't matter as long as you
are able to experiment interactively and create normal Python source
files that can execute from the command line.


\[ [Solution](soln1_1.md) | [Index](index.md) | [Exercise 1.2](ex1_2.md) \]



----
`>>>` Advanced Python Mastery  
`...` A course by [dabeaz](https://www.dabeaz.com)  
`...` Copyright 2007-2023  

![](https://i.creativecommons.org/l/by-sa/4.0/88x31.png). This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/)