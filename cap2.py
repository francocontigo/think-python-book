#ex 2.2 a
r = int(input())
print(4/3 * 3.14 * r**3)

#ex 2.2 b
livro_capa = 24.95
desconto = 0.6
transporte_primeiro = 3
transporte_unidade_extra = 0.75

livros = int(input("Qual o número de exemplares? "))

if livros == 1:
  custo_entrega = (livro_capa * desconto) + transporte_primeiro
  print(f"O custo da entrega de um exemplar é : R${custo_entrega}")
if livros > 1:
  custo_entrega = transporte_primeiro + ((livro_capa * desconto) * livros) + (livros - 1) * transporte_unidade_extra
  print(f"O custo da entrega dos exemplares é : R$ {custo_entrega}")