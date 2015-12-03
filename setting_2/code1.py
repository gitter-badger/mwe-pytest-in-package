def foo():
   return 1

def test_foo():
   assert foo() == 1
   print ("Test OK.")

if __name__ == "__main__":
    test_foo()
