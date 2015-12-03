Py.test is a great tool, but when somethign odd happens it is hard to find out why and how to fix it. 
In my case py.test fails to collect tests because import of modules fails.

The failure comes in following steps:
1. I'm on Windows, py.test is a part of Anaconda scientific installation. Cannot use pip for upgrades. 
2. My current folder is D:\mwe-pytest-in-package\setting_1_(no_package)
3. Run ```py.test```
4. Getting the following:

```
>py.test
============================= test session starts =============================
platform win32 -- Python 3.4.3 -- py-1.4.26 -- pytest-2.6.4
collected 0 items / 1 errors

=================================== ERRORS ====================================
________________________ ERROR collecting test_pkg.py _________________________
test_pkg.py:1: in <module>
    from code import foo
E   ImportError: cannot import name 'foo'
=========================== 1 error in 0.08 seconds ===========================
```

For some reason py.test fails to import module while colleting a test. Googling and StackOverflow were not much help yet.
