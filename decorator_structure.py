def hello():
    print('Hi Yosua')

def func_lain(func_berikutnya):
    print('Some function')
    print(func_berikutnya())

hello()
func_lain(hello)


