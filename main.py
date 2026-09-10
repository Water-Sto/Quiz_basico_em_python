#Bibliotecas
import random
import time
import pygame
pygame.mixer.init()
som_tecla = pygame.mixer.Sound("tecla1.wav")
som_tecla.set_volume(random.uniform(0.15, 0.20))
som_tecla.play()

#Variavel de contagem de pontos
contagem_pontos = 0
total_pontos = contagem_pontos
numero_pergunta = 0

#Controla o sistema para permitir o reset sem fechar o cmd
loop = 1

#Variaveis globais

#Define qual a resposta certa em cada alternativa
resposta_certa = "textobase"

#Identica a variavel anterior, mas para letras minusculas
minusculo = "textobase"

#Define qual será a pergunta daquela letra em questão (Variaveis Globais)
A = "textobase"
B = "textobase"
C = "textobase"
D = "textobase"
E = "textobase"

#Define a letra da alternativa (Variaveis Globais)
letras_alternativas = ["A)", "B)", "C)", "D)", "E)"]


#Declaração de Função para aleatorizar alternativas
def alternativas():
#Puxa variaveis globais
    global letras_alternativas

#Variaveis da função
#repeat define uma letra de "A" até "E" para a questão;
#correct tem duas utilidades, primeiro a variavel indica a letra da questão
#depois ela de torna a alternativa correta da questão.

    repeat = 0
    correct = ["A:", "B:", "C:", "D:", "E:"]

#Isola todas as alternativas e as aleatoriza

    lista_alternativas = [A, B, C, D, E]
    random.shuffle(lista_alternativas)
    for t in lista_alternativas:
#Escreve as alternativas na tela
        print((letras_alternativas[0 + repeat]), t)
        correct[0 + repeat] = t
        repeat = repeat + 1
#Fim da função, ao mesmo tempo que devolve o resultado de "correct" pra pergunta em questão,
#Onde vai ser usado para definir a alternativa certa
    return correct

#Declaração de função de soma de pontos
def somar_pontos():
    global contagem_pontos
    contagem_pontos += 1

#Declaração de funções resposta
def resposta_incorreta():
    teclar("\nResposta Incorreta, verifique sua contagem atual: ")
    print("Pontos: ", contagem_pontos)
    print()

def resposta_correta():
    teclar("\nResposta Certa, Parabens! Verifique sua contagem atual: ")
    print("Pontos: ", contagem_pontos +1)
    print()
#Declaração de função de efeito de digitação
def teclar(texto, velocidade=0.000001):
    for letra in texto:
        print(letra, end='', flush=True)

        if letra !=" ":
            som_tecla.play()
        time.sleep(velocidade + random.uniform(0, 0.03))
    print()
#Declaração de perguntas
def questao1():
#Enunciado
    teclar("No final da década de 1940, Kathleen Booth deu o primeiro passo para a\nsimplificação do código da maquina, criando a linguagem Assembly.\n")
    teclar("Antes desse período, como era realizada a programação nos computadores?\n")
    time.sleep(2)
#Variaveis Globais

    global A, B, C, D, E
    global resposta_certa, letras_alternativas, minusculo

#Alternativas da questão
    A = "Utilizava linguagens rudimentares, como C e Pascal."
    B = "Utilizava linguagem de maquina, como 0s e 1s."
    C = "Não existia nenhuma linguagem especifica antes do assembly."
    D = "Os programadores faziam uso de linguagens de alto nivel de abstração."
    E = "Os computadores não utilizavam a programação de modo tradicional."

#Aleatoriza a ordem das questões, ao mesmo tempo que salva a resposta certa na variavel
    recebe = alternativas()

#Confere qual das alternativas é a resposta certa
    if recebe[0] == "Utilizava linguagem de maquina, como 0s e 1s.":
        resposta_certa = "A"
        minusculo = "a"
    if recebe[1] == "Utilizava linguagem de maquina, como 0s e 1s.":
        resposta_certa = "B"
        minusculo = "b"
    if recebe[2] == "Utilizava linguagem de maquina, como 0s e 1s.":
        resposta_certa = "C"
        minusculo = "c"
    if recebe[3] == "Utilizava linguagem de maquina, como 0s e 1s.":
        resposta_certa = "D"
        minusculo = "d"
    if recebe[4] == "Utilizava linguagem de maquina, como 0s e 1s.":
        resposta_certa = "E"
        minusculo = "e"

#Recebe a resposta do usuario e guia caso seja a resposta correta ou incorreta
    resposta = input("\nSelecione a alternativa correta: ")
    if resposta != resposta_certa and resposta != minusculo:
        resposta_incorreta()
        time.sleep(1.5)
    if resposta == resposta_certa or resposta == minusculo:
        resposta_correta()
        somar_pontos()
        time.sleep(1.5)

def questao2():
    #Enunciado
    teclar("Um dos critérios mais importantes para avaliar a qualidade de uma linguagem de programação é a legibilidade, ")
    teclar("que se refere a facilidade de um programa ser lido e entendido pela sintaxe.\n")
    teclar("Selecione qual das alternativas abaixo não é considerada um critério de avaliação de uma lp: \n")
    time.sleep(2)
    #Variaveis Globais
    global A, B, C, D, E
    global resposta_certa, letras_alternativas, minusculo

    #Alternativas da questão

    A = "A simplicidade da linguagem de programação."
    B = "A redibilidade, isso é, a facilidade de escrita da linguagem."
    C = "A possibilidade de se usar instruções de controle, como Goto."
    D = "O suporte para abstração, isso é, como os dados e processos podem ser interpretados."
    E = "O custo da linguagem de programação."

    recebe = alternativas()
    #Confere qual das alternativas é a certa

    if recebe[0] == "A possibilidade de se usar instruções de controle, como Goto.":
        resposta_certa = "A"
        minusculo = "a"
    if recebe[1] == "A possibilidade de se usar instruções de controle, como Goto.":
        resposta_certa = "B"
        minusculo = "b"
    if recebe[2] == "A possibilidade de se usar instruções de controle, como Goto.":
        resposta_certa = "C"
        minusculo = "c"
    if recebe[3] == "A possibilidade de se usar instruções de controle, como Goto.":
        resposta_certa = "D"
        minusculo = "d"
    if recebe[4] == "A possibilidade de se usar instruções de controle, como Goto.":
        resposta_certa = "E"
        minusculo = "e"

#Recebe a resposta do usuario e guia caso seja correta ou incorreta

    resposta = input("\nSelecione a alternativa correta: ")
    if resposta != resposta_certa and resposta != minusculo:
        resposta_incorreta()
        time.sleep(1.52)
    if resposta == resposta_certa or resposta == minusculo:
        resposta_correta()
        somar_pontos()
        time.sleep(1.52)

def questao3():

#Enunciado

    teclar("O agrupamento por paradigmas é outra forma de classificar as linguagens de programação.\nUm paradigma agrupa linguagens com caracteristicas semelhantes que surgiram na mesma época.\n")
    teclar("Qual das alternativas a seguir demonstram a diferença entre paradigmas imperativos e declarativos?\n")

#Variaveis globais

    global A, B, C, D, E
    global resposta_certa, letras_alternativas, minusculo

    A = "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como."
    B = "Os paradigmas da classe imperativa utilizam desvios incondicionais (Goto), enquanto os de classe declarativa não o fazem."
    C = "A grande diferença entre paradigmas imperativos e declarativos se deve ao fato de somente a programação declarativa utilizar variaveis."
    D = "Ia's só podem ser desenvolvidas com paradigmas do tipo imperativo."
    E = "A separação entre linguagens imperativas e declarativas perdeu o sentido desde que a linguagem python foi lançada em 1991."

    recebe = alternativas()

    if recebe[0] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "A"
        minusculo = "a"
    if recebe[1] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "B"
        minusculo = "b"
    if recebe[2] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "C"
        minusculo = "c"
    if recebe[3] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "D"
        minusculo = "d"
    if recebe[4] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "E"
        minusculo = "e"

#Recebe a resposta do usuário e guia através do caminho correto ou incorreto
    resposta = input("\nSelecione a alternativa correta: ")
    if resposta != resposta_certa and resposta != minusculo:
        resposta_incorreta()
        time.sleep(1.51)
    if resposta == resposta_certa or resposta == minusculo:
        resposta_correta()
        somar_pontos()
        time.sleep(1.51)

def questao4():
#Enunciado
    teclar("Todo código, exceto se estiver em linguagem de maquina, deve ser traduzido antes de ser\nrepassado para a maquina, normalmente resumimos esse processo chamando de compilação.")
    teclar("\nEsse processo se divide em 4 processos para o tratamento do código, sendo eles: Compilação, montagem, carga e ligação.\n\n")
    teclar("O Que ocorre durante o processo de compilação?\n")
#Variaveis globais

    global A, B, C, D, E
    global resposta_certa, minusculo, letras_alternativas

#Alternativas

    A = "O compilador traduz o código assembly para um código de maquina intermediário (Código-objeto)."
    B = "O compilador torna o código-objeto relocável."
    C = "O compilador analisa o código-fonte e, se não houver erros, o converte para o código assembly."
    D = "O compilador converte o código-fonte em linguagem de maquina."
    E = "O compilador realiza apenas a análise léxica, isso é, remove espaços em branco e os agrupa em unidades chamadas de token(ex: if, numero)."

    recebe = alternativas()

#Define qual a alternativa correta

    if recebe[0] == "O compilador analisa o código-fonte e, se não houver erros, o converte para o código assembly.":
        resposta_certa = "A"
        minusculo = "a"
    if recebe[1] == "O compilador analisa o código-fonte e, se não houver erros, o converte para o código assembly.":
        resposta_certa = "B"
        minusculo = "b"
    if recebe[2] == "O compilador analisa o código-fonte e, se não houver erros, o converte para o código assembly.":
        resposta_certa = "C"
        minusculo = "c"
    if recebe[3] == "O compilador analisa o código-fonte e, se não houver erros, o converte para o código assembly.":
        resposta_certa = "D"
        minusculo = "d"
    if recebe[4] == "O compilador analisa o código-fonte e, se não houver erros, o converte para o código assembly.":
        resposta_certa = "E"
        minusculo = "e"

#Recebe a resposta do usuário e guia pelo caminho correto/incorreto
    resposta = input("\nSelecione a alternativa correta: ")
    if resposta != resposta_certa and resposta != minusculo:
        resposta_incorreta()
        time.sleep(1.53)
    if resposta == resposta_certa or resposta == minusculo:
        resposta_correta()
        somar_pontos()
        time.sleep(1.53)




#Inicio do programa
teclar("--- Bem vindo ao Quiz da matéria paradigmas de linguagem em python! ---")

while loop != 0:
#Opções de segmento de código
    print("1 - Entrar no Quiz")
    print("2 - Informações")
    print("0 - Sair")

#Entrada da opção
    opcao = int(input("Selecione a opção desejada: "))
    match opcao:

#Caminho padrão do programa, segmento do Quiz
        case 1:
            print()
            lista_perguntas = [questao1, questao2, questao3, questao4]
            random.shuffle(lista_perguntas)
            for f in lista_perguntas:
                print("Questão", numero_pergunta +1, end = ') ')
                numero_pergunta += 1
                f()
            teclar("\nParabéns, você chegou ao final do Quiz!\nEssa mensagem não deveria estar aqui nesse momento, porém, o quiz está incompleto, peço desculpas pelo inconveniente.\nEspero ve-lo novamente em breve, quando o quiz estiver completo!")
            loop = 0


#Mais informações sobre o programa e sua criação
        case 2:
            print()
            teclar("Esse Quiz é o resultado de um trabalho do 2° semestre do curso de ")
            teclar("Análise e desenvolvimento de sistemas na faculdade estácio, feito ")
            teclar("Utilizando a linguagem python.")
            print()
            teclar("O Objetivo é utilizar todo o conteúdo disponível no SAVA da matéria ")
            teclar("Paradigmas de linguagens de programação em python para elaborar ")
            teclar("perguntas para um Quiz, utilizando o aprendizado na prática.")
            teclar("Cada questão deve conter 5 alternativas, com apenas uma correta.")
            print()
#Saida do programa
        case 0:
            print()
            print("Sua pontuação dessa vez foi:", contagem_pontos)
            teclar("Obrigado pela sua participação, até a próxima!")
            loop = 0

#Entrada não esperada
        case default:
            print("Entrada não identificada, tente novamente.")
