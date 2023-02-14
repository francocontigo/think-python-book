#ex 3.1
# def right_justify(s):
#   s_final = s
#   while len(s_final) < 70:
#     s_final = " " + s_final
#   print(s_final)

# right_justify(input("digite uma palavra"))



#ex 3.2
# def do_twice(f, value):
#   f(value)
#   f(value)

# def print_twice(bruce):
#   print(bruce)
#   print(bruce)

# def print_spam():
#   print("spam")

# def do_four(f, value):
#   do_twice(f, value)
#   do_twice(f, value)

# do_four(print_twice, "spam")



#ex 3.3
# def do_twice(f):
#   f()
#   f()

# def do_thrice_do_one(f1,f2):
#   f1()
#   f1()
#   f1()
#   f2()

# def do_four(f):
#   do_twice(f)
#   do_twice(f)

# def linha_inicial():
#   print("+ - - - -", end=" ")

# def linha_final():
#   linha_inicial()
#   print("+")

# def linha_completa():
#   do_thrice_do_one(linha_inicial, linha_final)

# def coluna_inicial():
#   print("|        ", end=" ")

# def coluna_final():
#   coluna_inicial()
#   print("|")

# def coluna_completa():
#   do_thrice_do_one(coluna_inicial, coluna_final)

# def colunas():
#   do_four(coluna_completa)

# def grid_primeira_parte():
#   linha_completa()
#   colunas()

# def grid_completo():
#   do_four(grid_primeira_parte)
#   linha_completa()

# grid_completo()