# @Author: Breno Ribeiro Teodoro

# Exemplo mais basico de uma declaração de impressao
print('isso é uma string')

# Strings
# Podemos utilizar o %s para formatar strings em suas instruções de impressão.
s = 'STRING'
print('Place another string with a mod and s: %s' %(s))

# Numeros de ponto flutuante (FLOAT)
# Os numeros de ponto flutuante usam o formato %n1.n2f, onde o n1 é o numero minimo total 
# de digitos que a cadeia deve conter (estes podem ser preenchidos com espaço em branco se o numero inteiro não tiver esses muitos digitos)
# O espaço reservado n2 significa quantos numeros para mostrar após o ponto decimal. 
# Vamos ver alguns exemplos:

print('numero de ponto flutuante: %1.2f' %(13.144))
print('numero de ponto flutuante: %1.0f' %(13.144))
print('numero de ponto flutuante: %1.5f' %(13.144))
print('numero de ponto flutuante: %10.2f' %(13.144))
print('numero de ponto flutuante: %25.2f' %(13.144))

# Métodos de formato de conversão
# Deve notar-se que os dois métodos %s e %r realmente convertem quase qualquer objeto Python em uma string
# usando dois métodso separados: str() e repr():
print('\n\n\n\naqui é um numero: %s. Aqui é uma string: %s \n\n\n\n' %(123.1, 'hi'))
print('\n\n\n\naqui é um numero: %r. Aqui é uma string: %r \n\n\n\n' %(123.1, 'hi'))

# Formatação multipla
# Passe uma tupla para junto com o símbolo do módulo para colocar vários formatos nas suas declarações de impressão:
print("primeiro: %s, segundo: %1.2f, terceiro: %r" %('hello!!', 3.14, 22))


#Usando o método string.format()
# A melhor maneira de formatar objetos em suas strings para instruções de impressão é usar o método format(). Sua sintaxe é:
# 'String aqui {var1} e também {var2}'.format(var1 = 'alguma coisa', var2 = 'batata')
print('String aqui:> {var1} < e também: > {var2} <'.format(var1 = 'alguma coisa', var2 = 'batata'))

print('String aqui:> {p} < e também: > {p} <'.format(p = 'alguma coisa'))

print('\nbatatatatatata->{a}, batatatatatta->{b}, batatatattata->{c} \n'.format(a = 1, b='dois', c=12.05))



# Exercicios:
#1. Dada as variáveis: 
# planeta = "Terra"
# diametro = 12742
# use format() para printar em tela a seguinte frase: "O diâmetr da terra é de 12742 kilômetros."
planeta = "Terra"
diametro = 12742
