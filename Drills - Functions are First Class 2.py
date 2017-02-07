def makeSuffixer(suffix):
   def f(x):
       return x + suffix
   return f

a = makeSuffixer('foo')('bar')
print(a)
