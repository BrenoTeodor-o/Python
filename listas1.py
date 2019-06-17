# @Author: Breno Ribeiro Teodoro

# Listas
# Na seção de strings, introduzimos o conceito de sequencia em Python. As listas podem ser pensadas na versão mais geral ed uma sequência em Python.
# Ao contrário das strings, elas são mutáveis, o que significa que os elementos dentro de uma lista podem ser alterados

# Nessa seção aprenderemos sobre?
# Criação de listas
# Indice e corte de listas
# Métodos basicos de lista
# Listas aninhadas

#As listas são construidas com colchetes e virgulas que separam cada elemento da lista
my_list = [1,2,3] 

# Assim como as strings, a função len() irá dizer quantos itens estão na sequencia da lista
my_list = ['string', 4, 100.245, 'lista em python']
a = len(my_list)
print(a)

# Indexação e corte
# Indexar e cortar funciona exatamente como em strings. Vamos fazer uma nova lista para nos lembrar de como isso funciona:
my_list = ['string', 4, 100.245, 'lista em python']
print(my_list[0])
print(my_list[1:])
print(my_list[:3])

#concatenação

