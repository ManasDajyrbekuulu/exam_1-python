# Генератор

def simple_generator(val):
   while val > 0:
       val -= 1
       yield 1

gen_iter = simple_generator(6)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
