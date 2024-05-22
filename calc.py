import plyplus
import math

# operaciones trigonométricas
def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)

def acos(x):
    return math.acos(x)

def atan(x):
    return math.atan(x)

# evalua el árbol de sintaxis
def evalExpresion(tree):
    if tree.head == 'NUMBER':
        return float(tree.tail[0])
    elif tree.head == 'expr':
        left = evalExpresion(tree.tail[0])
        if len(tree.tail) == 1:
            return left
        op = tree.tail[1]
        right = evalExpresion(tree.tail[2])
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
    elif tree.head == 'term':
        left = evalExpresion(tree.tail[0])
        if len(tree.tail) == 1:
            return left
        op = tree.tail[1]
        right = evalExpresion(tree.tail[2])
        if op == '*':
            return left * right
        elif op == '/':
            return left / right
    elif tree.head == 'factor':
        if len(tree.tail) == 1:
            return evalExpresion(tree.tail[0])
        elif tree.tail[0] == '-':
            return -evalExpresion(tree.tail[1])
        elif tree.tail[0] == 'sin':
            return sin(evalExpresion(tree.tail[1]))
        elif tree.tail[0] == 'cos':
            return cos(evalExpresion(tree.tail[1]))
        elif tree.tail[0] == 'tan':
            return tan(evalExpresion(tree.tail[1]))
        elif tree.tail[0] == 'asin':
            return asin(evalExpresion(tree.tail[1]))
        elif tree.tail[0] == 'acos':
            return acos(evalExpresion(tree.tail[1]))
        elif tree.tail[0] == 'atan':
            return atan(evalExpresion(tree.tail[1]))


with open("calc.g") as grm:
  parser = plyplus.Grammar(grm)
  tree = parser.parse("-((1 + (3 * 2)) + (2 + 3) - (5 / -4))")
  # parser.parse("((1 + (3 * 2)) + (2 + 3) - (5 / 4))")
  # parser.parse("4")
  result = evalExpresion(tree)
  print(result)