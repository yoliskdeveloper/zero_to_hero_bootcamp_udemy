from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

def func(x):
    return x

interact(func,x=10)     # akan menghasilkan slider interaction
interact(func,x=True)   # akan menghasilkan check box
interact(func,x='string')   # akan menghasilkan empty box input

# cara lain dengan cara decorator
@interact(func, x=True, y=1.0)
def g(x, y):
    return (x,y)

# mengganti widget value, dengan apa yang kita inginkan
interact(func, x=widgets.IntSlider(min=-100, max=100, step=1, value=0))
interact(func, x=(-100, 100, 1))        # sama dengan yang diatas
interact(func, x=(-10.0, 10.0, .1))     # sama dengan yang diatas dengan floating point

# dropdown widget
interact(func, x=['option1', 'option2', 'option3']) # use with dictionary juga bisa

# ===================================================================================
w = widgets.IntSlider()
display(w)
