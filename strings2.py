# @Author: Breno Ribeiro Teodoro
#Propriedades das strings
# strings tem uma propriedade importante conhecida como imutabilidade

s = 'Hello World'
print(s)

#vamos açterar a primeira letra para x
#s[0] = 'x'
#o seu terminal lhe entregou que não podemos alterar a atribuição do item

# Concatenação!!
print(s +" outra coisa")
print(s)
s = s+" batata" 
print(s)

# Podemos usar o simbolo da multiplicação para criar repetiç~ies
letter = "z"
print(letter*10)

# metodos internos
# Coloca toda a string em caixa alta
print(s.upper())
#caixa baixa
print(s.lower())

#Divide uma string nos espaços em branco (este é o padrão)
print(s.split())

# Divide em um elemento específico (não inclui o elemento que foi dividido)
print(s.split('W'))

#Futuramente veremos outros métodos de tratamento de strings

#exercicios
#4. Quebre a string "Hello Python" em uma lista.

#5. Imprima a string "Hello Python" em caixa alta 