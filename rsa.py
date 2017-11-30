import random
import sys

#dois numeros primos bem grandes
#p=84217061
#q=20443601639



#exponenciacao modular
#implementada apenas para exemplificar de forma mais didatica.
#a implementaçao mais funcional dessa funcao é encontrada  na funcao encripta()
def modular_exp(a,b,n):
    c=0
    d=1
    while b>0:
        print(b)

        if b%2==0:
            a=(a*a)%n
            print(a)
            b=b//2
        else:
            d=(a*d)%n
            b=b-1

    return d



#funcao maximo multiplo comum
def mmc(a,b):
    while b!=0:
        a, b=b,a % b; #atribuição multipla: a=b e b=a%b.
    return a




#algoritmo extendido de euclides
def euclidesextendido(a,b):
    if a==0:
        return (b,0,1) #retorno multiplo caso encontre um resto 0. Nesse caso ele retorna o b que foi utilizado como resto na conta anteriro
    else:
        g,x,y = euclidesextendido(b%a,a)#retorno multiplo.g recebe o primeiro parametro, x o segundo e y o terceiro
        return (g,y-(b//a)*x,x)#espeficicaçao multipla de retorno. o primeiro parametro eh o g, o segundo é y - (a//b) * x, onde // é o resultado de uma divisao inteira e o ultimo parametro recebe x


#Usa o algoritmo extendido de euclides para retornar um inverso modular
def inversomultiplicativo(b,n):
    g,x,_ =euclidesextendido(b,n)#atribuiçao multipla no retorno. O sinal _ serve pra dizer que esta jogando fora um valor recebido.
    if g==1:
        return x % n


#retorna numero primo
def primo(x):
    if x==2:#chega paridade
        return True
    if x < 2 or x % 2 == 0:
        return False#se nao for 2 e for par, nao é primo
    for n in range(3,int(x**0.5)+2, 2):#fatora o x por todos os valores de 3 até raiz quadrada de x+2
        if x % n == 0:#se em algum momento o resto for 0, o numero retorna falso pois é composto
            return False
    return True



#gerar p e q

def gerar_chaves(p,q):
    if not(primo(p) and primo(q)):#checa se os dois numeros sao primos
        raise ValueError('ambos os numeros precisam ser primos')

    elif p == q:#chega se os dois numeros sao iguais
        raise ValueError('p e q nap podem ser iguais ')
    n = p * q

    #calculo do phi: quantidades de numeros coprimos ou inversiveis em em Zn
    phi=(p-1)*(q-1)

    #Encontra aleatoriamente um numero 'e' tal que 'e' é menor do que phi.
    e=random.randrange(1,phi)

    #verifica se 'e' é coprimo de n
    g=mmc(e,phi)#g recebe o mmc de 'e' e phi
    while g!=1:#enquanto o mmc de 'e' e phi nao for 1
        e = random.randrange(1,phi)#busca um numero aleatorio entre 1 e phi
        g = mmc(e,phi)#testa se esse numero é coprimo

    #usa algoritmo extendido de euclides para achar o inverso multiplicativo
    d=inversomultiplicativo(e,phi)#guarda o inverso multiplicativo em d

    #retorna duas tuplas que correspondem a chave publica (e,n) e chave secreta (d,n)
    return((e,n),(d,n))

#esse método é uma forma aprimorada da exponenciaçao modular apresentada no começo
#encripta uma mensagem
def encripta(tupla,texto):

    chave,n=tupla #guarda os valores da tupla em chave e 'n'

        #converte cada letra do texto em um numero
        #esse numero é elevado pela chave 'e' guardada na variavel chave, obtida por gerar_chaves(p,q)
        #e em seguida o resto do caractere de texto, que foi transformado em inteiro e foi elevado a 'chave' é concatenado na string msgcodificada
    msgcodificada=[(ord(char) ** chave) % n for char in texto]

        #retorna msg
    return msgcodificada


#decripta mensagem
def decripta(tupla,msgcodificada):
    chave,n=tupla#guarda os valores da tupla em chave e em 'n'

        #converte cada o numero da msg em caracteres.
        #cada caractere é elevado pela chave e o resto dele é salvo numa lista
        #onde cada componente é um caractere da msgdecodificada
    msgdecodificada=[chr((char ** chave)% n) for char in msgcodificada]

        #concatena cada componente da lista msgdecodificada em uma string.
        #isso é necessário pois python salva as variaveis em listas quando há retorno multiplo
    return ''.join(msgdecodificada)


#numeros primos enormes, caso o usuário deseje alguma coisa
#utilize numeros primos pequenos, por exemplo, 13, 11, 17, etc
#numeros primos maiores que 1100 podem demorar muito devido a ineficiencia para calcular o 'e'.
#os dois maiores numeros testados como p e q foram 1093 e 1097

p=int(input("entre com um numero primo"))
q=int(input("entre com outro numero primo"))

#gera chave publica

publica,privada=gerar_chaves(p,q)

print("sua chave publica é ", publica," sua chave privada é ", privada)
mensagem =input("digite sua mensagem ")


#mensagem é encriptada e salva.
mensagem_encriptada=encripta(privada,mensagem)

print("Mensagem encriptada é")
print(''.join(map(lambda x: str(x), mensagem_encriptada)))


print("decriptifica mensagem com chave publica", publica)

print("mensagem decriptada é: ")
print( decripta(publica,mensagem_encriptada))





