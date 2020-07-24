from browser import document
from browser import alert
from browser import html

def ins(e):
    global inp
    inp.value += e.target.dataset.val


a = document['a']
b = document['b']
c = document['c']
d = document['d']
e = document['e']
f = document['f']
g = document['g']
h = document['h']
i = document['i']
j = document['j']
k = document['k']
l = document['l']
m = document['m']
n = document['n']
o = document['o']
p = document['p']
q = document['q']
r = document['r']

buttons = [b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r]


for i, x in enumerate(buttons):
    x.addEventListener('click', ins)

inp = document["inp"]


def clear_inp():
    inp_value = ""


document["a"].bind("click", clear_inp)


def clear_inp_1():
    inp.value = inp_value[0:-1]


document["b"].bind("click", clear_inp_1)


def calc():
    try:
        inp.value = eval(inp.value)
    except:
        inp.value = "Error"


document["s"].bind("click", calc)
