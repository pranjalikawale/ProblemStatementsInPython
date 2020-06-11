# anonymous function or lambda expression

full_name=lambda fn,ln: fn.strip().title()+" "+ln.strip().title()
print(full_name("pranjal","kawale"))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

