# one.py

def func():
    print('func() dalam ONE.PY')
print('one.py')

if __name__ == '__main__':
    print('ONE.PY sedang berjalan ')
else:
    print('ONE.py telah diimport')

# if __name__ == '__main__' dengan cara ini kita tahu module mana yang dijalankan langsung dan module mana yang diimport
# biasanya teknik ini ditaruh di line paling bawah dari file module yang berisi function dan class untuk memudahkan
# mengorganisir logic dari module

