def func_sample():
    yield('おはよう')
    yield('こんにちは')
    yield('こんばんは')



for i in func_sample():
    print(i)

f = func_sample()
print(next(f))
print(next(f))

gen_sample = (i for i in 'おはよう　こんにちは　こんばんは'.split())
print(gen_sample)
for i in gen_sample:
    print(i)