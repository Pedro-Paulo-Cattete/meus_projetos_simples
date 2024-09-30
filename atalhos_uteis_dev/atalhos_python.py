# Lista  de comandos e atalhos úteis:

# Maiúscula, minúscula e título:
print("Exemplo 1:")
palavra_exemplo1 = "   pYThOn "

#Transformar todas as letras da string para Maiúsculas:
print(palavra_exemplo1.upper())
#Transformar todas as letras da string para Minúsculas:
print(palavra_exemplo1.lower())
#Transformar para título, primeiras maiúscula e restante minúscula:
print(palavra_exemplo1.title())

# Eliminando espaços em branco com strip:

#Retira todos os espaços:
print(palavra_exemplo1.strip())
#Retira os espaços da esquerda (Left Strip)
print(palavra_exemplo1.lstrip())
#Retira os espaços da direita (Right Strip)
print(palavra_exemplo1.rstrip())

#Junções e Centralização
print("Exemplo 2:")
palavra_exemplo2 = "Python"

#Centralização:
print(palavra_exemplo2.center(10, "#"))
#Resultado: "##Python##"

#Junção:
print(".".join(palavra_exemplo2))
#Resultado: "P.y.t.h.o.n"

#Formatando com F string:

#Utilização de Width e limitação de casas decimais
print("Exemplo 3:")
#Dentro de {} e logo depois da váriavel: O número representa quantos espaços vão ser pulados (Width) e logo depois .2f representa quantas casas decimais após a vírgula serão apresentados.
pi = 3.14159
print(f"Valor de PI: {pi:10.2f}")

#Filameto de String:
print("Exemplo 4:")

nome = "Pedro Paulo Cattete Neto"
#Puxa o caracter no local selecionado:
print(nome[0])
#Puxa todos os caracteres até a posição citada:
print(nome[:5])
#Puxa todos os caracteres da posição citada pra frente:
print(nome[20:])
#Puxa todos os caracteres entre a posição selecionada:
print(nome[12:19])
#Puxa todos os caracteres entre a posição selecionada e logo depois estipula os intervalos:
print(nome[12:19:2])
#Puxa todos os caracteres:
print(nome[:])
#Espelha todos os caracteres da string:
print(nome[::-1])

#String Múltiplas/multilinhas:
print("Exemplo 5:")

nome = "Pedro"

mensagem = f'''
Olá meu nome é {nome},
nessa configuração conseguimos manter os recuos,
     por exemplo essa frase.
'''
print(mensagem)