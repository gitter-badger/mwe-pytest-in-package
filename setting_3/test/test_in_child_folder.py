# what import here?

try:
   from ..code3 import foo
except:
   print("Did not work")
   
try:
   from .code3 import foo
except:
   print("Did not work")
try:
   from setting_3.code3 import foo
except:
   print("Did not work")

def test_foo():
   assert foo() == 1
   print ("Test OK.")

if __name__ == "__main__":
    test_foo()
