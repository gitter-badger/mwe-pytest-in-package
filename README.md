# Test case 1
In this case py.test fails to collect tests because import of modules fails. The failure comes in following steps:

1. I'm on Windows, py.test is a part of Anaconda scientific installation. Cannot use pip for upgrades. 
2. My current folder is D:\mwe-pytest-in-package\setting_1 
3. Run ```py.test```
4. Getting the following:

```
>py.test
============================= test session starts =============================
platform win32 -- Python 3.4.3 -- py-1.4.26 -- pytest-2.6.4
collected 0 items / 1 errors

=================================== ERRORS ====================================
________________________ ERROR collecting test_foo.py _________________________
test_foo.py:1: in <module>
    from code import foo
E   ImportError: cannot import name 'foo'
=========================== 1 error in 0.08 seconds ===========================
```

- For some reason py.test fails to import a module ```code``` while colleting a test ```test_foo.py```. 
- Googling and StackOverflow were not much help yet.
- Note that ```python code.py``` and ```python test_foo.py``` run without error. 

##Solution
Adding current working directory to PYTHONPATH helped starting py.test: 

```set "PYTHONPATH=D:\mwe-pytest-in-package\setting_1"``

Remaining questions:

- other way of making py.test do the imports?
- why python interpreter does imports modules OK and py.test doesn't?
