# two.py
import one

print("TOP LEVEL in TWO.py")
one.func()

if __name__ == '__main__':
    print('TWO.Py sedang berjalan')
else:
    print('TWO.PY telah diimport')
