# @Author: Breno Ribeiro Teodoro
# Strings
# As Strings são usadas em Python para registrar informações de texto, como nomes ou frases. 
# As strings em Python são na verdade uma sequencia, o que basicamente significa que o Python 
# acompanha cada elemento da string como uma sequência de caracteres. 
# Por exemplo, Python entende a string "hello" como uma sequência de letras en uma ordem específica.
# Isso significa que poderemos usar a indexação oara pegar letras particulares.

# Criando uma string
# Uma palavra
'hello'

# Uma frase inteira
'isso também é uma string'

# Também é possivel usar aspas duplas 
"Aspas duplas é topzera"


# Imprimindo uma String
# Podemos simplesmente declarar uma string
'Hello World'

# mas a maneira correta é utilizar o método print()
print('Hello World 1')
print('Hello World 2')
print('Use \n para inserir uma nova linha')
print('Nova linha')

# Nós podemos também usar uyma função chamada len() para verificar o comprimento de uma string!!
a = len('Hello World')
print(a)

#
# Indexação em Strings
# Sabemos que as strings são uma sequência, o que significa que o Python pode usar índices para chamar 
# partes da sequência. Vamos aprender como isso funciona
#  
# Em Python, usamos colchetes após um objeto para chamar seu índice.
# Devemos também notar que a indexação começa em 0 para Python. Vamos criar um novo objeto chamado "s"
# e caminharmos através de alguns exemplos de indexação

# Define s como uma string
s = 'Hello World'
#mostrar
print("\n\n\n\n\n"+s)

# Vamos começar a indexar!!!
# Mostra o primeiro elemento (nesse caso a primeira letra)
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(s[7])
print(s[8])
print(s[9])
print(s[10])

# Retorna todos os elementos a partir do elemento indice 1
print("\n"+s[1:])

# Observe que não houve mudanças no elemento s
print("\nElemento s: "+s+"\n")

# Retorna todos os elementos até o elemento indice 3
print("\n"+s[:3])

# Observe o corte acima. Aqui, estamos dizendo ao Python que pegue tudo de 0 a 3
# Não inclui o 3º indice. Notaremos muito isso em Python, onde as declarações são geralmente até o contexto
# mas não o incluindo

# Mostra tudo
print(s[:])

# Ultima Letra (um indice antes do 0, então ele começa da parte de tras)
print(s[-1])

# Pega tudo menos a ultima letra
print(s[:-1])

# Pegar de 1 em 1
print(s[::1])

# Pegar tudo, mas os espaçamentos são de 2 em 2
print(s[::2])

# Pegar tudo, mas com os passos negativos, de trás pra frente
print(s[::-1])



#Exercicios
#1. Imprima a string "Hello Python" de trás pra frente usando Indexação

#2. Usando a string "Hello Python" imprima apenas "Python"

#3. Descubra o comprimento da string "Hello Python". Use a Função len()
