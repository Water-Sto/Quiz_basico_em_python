# Bibliotecas
import random
import time
import pygame
import sys

pygame.mixer.init()
som_tecla = pygame.mixer.Sound("tecla1.wav")
som_botao = pygame.mixer.Sound("botão.wav")
som_tecla.set_volume(random.uniform(0.15, 0.20))

# ------------------- CONFIG -----------------------
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Botão em Pygame")

fonte = pygame.font.SysFont(None, 40)

# Cores pré definidas:

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 120, 255)
CINZA = (180, 180, 180)


# Sistema de botões
pos_mouse = pygame.mouse.get_pos()
class Button:
    def __init__(self, x, y, largura, altura, textos):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.textos = textos

    def desenhar(self, tela):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            cor = AZUL
        else:
            cor = CINZA
        pygame.draw.rect(tela, cor, self.rect)
        texto_renderizar = fonte.render(self.textos, True, BRANCO)
        tela.blit(texto_renderizar, texto_renderizar.get_rect(center=self.rect.center))

    def clicado(self, pos):
        return self.rect.collidepoint(pos)

# ------------ ESTADOS ------------
estado = "menu"
estado_anterior = "none"
#botões de cada tela
botao_titulo = Button(230, 10, 320, 50, "Quiz Basico em Python")
botao_iniciar = Button(300, 300, 180, 50, "Iniciar")
botao_informacao = Button(300, 400, 180, 50, "Informações")
botao_sair = Button(300, 500, 180, 50, "Sair")
botao_voltar = Button(50, 480, 100, 50, "Voltar")
botao_avancar = Button(630, 480, 120, 50, "Avançar")
botao_tela_anterior = Button(330, 480, 120, 50, "Anterior")

# Variavel de contagem de pontos
contagem_pontos = 0
total_pontos = contagem_pontos

# Variavel que controla o numero da pergunta
numero_pergunta = 0

# Controla o sistema para permitir o reset sem fechar o cmd
loop = 1

# Variaveis globais

# Define qual a resposta certa em cada alternativa
resposta_certa = "texto base"

# Identica a variável anterior, mas para letras minúsculas
minusculo = "texto base"

# Define qual será a pergunta daquela letra em questão (Variáveis Globais)
A = "texto base"
B = "texto base"
C = "texto base"
D = "texto base"
E = "texto base"

# Define a letra da alternativa (Variáveis Globais)
letras_alternativas = ["A)", "B)", "C)", "D)", "E)"]


# Declaração de Função para aleatorizar alternativas
def alternativas():
    # Puxa variáveis globais
    global letras_alternativas

    # Variaveis da função
    # repeat define uma letra de "A" até "E" para a questão;
    # correct tem duas utilidades, primeiro a variável indica a letra da questão
    # depois ela se torna a alternativa correta da questão.

    repeat = 0
    correct = ["A:", "B:", "C:", "D:", "E:"]

    # Isola todas as alternativas e as aleatoriza

    lista_alternativas = [A, B, C, D, E]
    random.shuffle(lista_alternativas)
    for t in lista_alternativas:
        # Escreve as alternativas na tela
        print((letras_alternativas[0 + repeat]), t)
        correct[0 + repeat] = t
        repeat = repeat + 1
    # Fim da função, ao mesmo tempo que devolve o resultado de "correct" para pergunta em questão,
    # Onde vai ser usado para definir a alternativa certa
    return correct


# Declaração de função de soma de pontos
def somar_pontos():
    global contagem_pontos
    contagem_pontos += 1


# Declaração de funções resposta
def resposta_incorreta():
    teclar("\nResposta Incorreta, verifique sua contagem atual: ")
    print("Pontos: ", contagem_pontos)
    print()


def resposta_correta():
    teclar("\nResposta Certa, Parabens! Verifique sua contagem atual: ")
    print("Pontos: ", contagem_pontos + 1)
    print()


# Declaração de função de efeito de digitação
def teclar(texto, velocidade=0.0000000000000000001):
    for letra in texto:
        print(letra, end='', flush=True)

        if letra != " ":
            som_tecla.play()
        time.sleep(velocidade + random.uniform(0, 0.000000003))
    print()


# Declaração de perguntas
def questao1():
    # Enunciado
    teclar(
        "No final da década de 1940, Kathleen Booth deu o primeiro passo para a\nsimplificação do código da maquina, criando a linguagem Assembly.\n")
    teclar("Antes desse período, como era realizada a programação nos computadores?\n")
    time.sleep(2)
    # Variaveis Globais

    global A, B, C, D, E
    global resposta_certa, letras_alternativas, minusculo

    # Alternativas da questão
    A = "Utilizava linguagens rudimentares, como C e Pascal."
    B = "Utilizava linguagem de maquina, como 0s e 1s."
    C = "Não existia nenhuma linguagem especifica antes do assembly."
    D = "Os programadores faziam uso de linguagens de alto nível de abstração."
    E = "Os computadores não utilizavam a programação de modo tradicional."

    # Aleatoriza a ordem das questões, ao mesmo tempo que salva a resposta certa na variável
    recebe = alternativas()

    # Confere qual das alternativas é a resposta certa
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

    # Recebe a resposta do usuário e guia caso seja a resposta correta ou incorreta
    resposta = input("\nSelecione a alternativa correta: ")
    if resposta != resposta_certa and resposta != minusculo:
        resposta_incorreta()
        time.sleep(1.5)
    if resposta == resposta_certa or resposta == minusculo:
        resposta_correta()
        somar_pontos()
        time.sleep(1.5)


def questao2():
    # Enunciado
    teclar(
        "Um dos critérios mais importantes para avaliar a qualidade de uma linguagem de programação é a legibilidade, ")
    teclar("que se refere a facilidade de um programa ser lido e entendido pela sintaxe.\n")
    teclar("Selecione qual das alternativas abaixo não é considerada um critério de avaliação de uma lp: \n")
    time.sleep(2)
    # Variaveis Globais
    global A, B, C, D, E
    global resposta_certa, letras_alternativas, minusculo

    # Alternativas da questão

    A = "A simplicidade da linguagem de programação."
    B = "A redibilidade, isso é, a facilidade de escrita da linguagem."
    C = "A possibilidade de se usar instruções de controle, como Goto."
    D = "O suporte para abstração, isso é, como os dados e processos podem ser interpretados."
    E = "O custo da linguagem de programação."

    recebe = alternativas()
    # Confere qual das alternativas é a certa

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

    # Recebe a resposta do usuário e guia caso seja correta ou incorreta

    resposta = input("\nSelecione a alternativa correta: ")
    if resposta != resposta_certa and resposta != minusculo:
        resposta_incorreta()
        time.sleep(1.52)
    if resposta == resposta_certa or resposta == minusculo:
        resposta_correta()
        somar_pontos()
        time.sleep(1.52)


def questao3():
    # Enunciado

    teclar(
        "O agrupamento por paradigmas é outra forma de classificar as linguagens de programação.\nUm paradigma agrupa linguagens com características semelhantes que surgiram na mesma época.\n")
    teclar("Qual das alternativas a seguir demonstram a diferença entre paradigmas imperativos e declarativos?\n")

    # Variaveis globais

    global A, B, C, D, E
    global resposta_certa, letras_alternativas, minusculo

    A = "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como."
    B = "Os paradigmas da classe imperativa utilizam desvios incondicionais (Goto), enquanto os de classe declarativa não o fazem."
    C = "A grande diferença entre paradigmas imperativos e declarativos se deve ao fato de somente a programação declarativa utilizar variáveis."
    D = "Ia's só podem ser desenvolvidas com paradigmas do tipo imperativo."
    E = "A separação entre linguagens imperativas e declarativas perdeu o sentido desde que a linguagem python foi lançada em 1991."

    recebe = alternativas()

    if recebe[
        0] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "A"
        minusculo = "a"
    if recebe[
        1] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "B"
        minusculo = "b"
    if recebe[
        2] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "C"
        minusculo = "c"
    if recebe[
        3] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "D"
        minusculo = "d"
    if recebe[
        4] == "Os paradigmas da classe imperativo especificam passo a passo o que deve ser feito para a execução do código, enquanto os de classe declarativa só explicam o que deve ser feito e não como.":
        resposta_certa = "E"
        minusculo = "e"

    # Recebe a resposta do usuário e guia através do caminho correto ou incorreto

    resposta = input("\nSelecione a alternativa correta: ")
    if resposta != resposta_certa and resposta != minusculo:
        resposta_incorreta()
        time.sleep(1.51)
    if resposta == resposta_certa or resposta == minusculo:
        resposta_correta()
        somar_pontos()
        time.sleep(1.51)


def questao4():
    # Enunciado
    teclar(
        "Todo código, exceto se estiver em linguagem de maquina, deve ser traduzido antes de ser\nrepassado para a maquina, normalmente resumimos esse processo chamando de compilação.")
    teclar(
        "\nEsse processo se divide em 4 processos para o tratamento do código, sendo eles: Compilação, montagem, carga e ligação.\n")
    teclar("O Que ocorre durante o processo de compilação?\n")
    # Variaveis globais

    global A, B, C, D, E
    global resposta_certa, minusculo, letras_alternativas

    # Alternativas

    A = "O compilador traduz o código assembly para um código de maquina intermediário (Código-objeto)."
    B = "O compilador torna o código-objeto relocável."
    C = "O compilador analisa o código-fonte e, se não houver erros, o converte para o código assembly."
    D = "O compilador converte o código-fonte em linguagem de maquina."
    E = "O compilador realiza apenas a análise léxica, isso é, remove espaços em branco e os agrupa em unidades chamadas de token(ex: if, numero)."

    recebe = alternativas()

    # Define qual a alternativa correta

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

    # Recebe a resposta do usuário e guia pelo caminho correto/incorreto

    resposta = input("\nSelecione a alternativa correta: ")
    if resposta != resposta_certa and resposta != minusculo:
        resposta_incorreta()
        time.sleep(1.53)
    if resposta == resposta_certa or resposta == minusculo:
        resposta_correta()
        somar_pontos()
        time.sleep(1.53)


dialogos = [
    "Esse Quiz é o resultado de um trabalho do",
    "2° semestre do curso de Análise e",
    "desenvolvimento de sistemas na Estácio, feito",
    "Utilizando a linguagem python.",
    "O Objetivo é utilizar todo o conteúdo ",
    "disponível no SAVA da matéria para elaborar",
    "perguntas para um Quiz, utilizando o aprendizado",
    "na prática. Para este objetivo, cada questão deve",
    "conter 5 alternativas, com apenas uma correta.",
    "Boa Sorte!"
]

# Inicio do programa

teclar("\n\n\n\n\n\n\n\n\n\n\n\n\n\n--- Bem vindo ao Quiz da matéria paradigmas de linguagem em python! ---")

botao_seta = Button(710, 525, 20, 20, "")
botao_seta2 = Button(710, 525, 20, 20, "")
botao_funciona = True
botao_funciona2 = False
caixa = pygame.Rect(50, 420, 700, 150)
caixa_info = pygame.Rect(50, 210, 700, 250)
caixa_titulo = pygame.Rect(240, 50, 300, 80)
fala = 0

# ------------------------- LOOP PRINCIPAL DO PROGRAMA ---------------------------------------
while loop != 0:
    tela.fill(PRETO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = 0
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()



#-------------------------------------- MENU -----------------------------------------------
        if estado == "menu":
            if botao_informacao.clicado(pos_mouse):
                som_botao.play()
                estado = "info"

            if botao_sair.clicado(pos_mouse):
                som_botao.play()
                loop = 0
                sys.exit()

#-------------------------------------- INFO ------------------------------------------------

        elif estado == "info":
            if botao_voltar.clicado(pos_mouse):
                som_botao.play()
                estado = "menu"
            if botao_avancar.clicado(pos_mouse):
                som_botao.play()
                estado = "info2"
#-------------------------------------INFO 2 ------------------------------------------------
        elif estado == "info2":
            if botao_voltar.clicado(pos_mouse):
                som_botao.play()
                estado = "menu"
            if botao_tela_anterior.clicado(pos_mouse):
                som_botao.play()
                estado = "info"

#----------------------------------- DESENHO -------------------------------------------------

    if estado == "menu":
        pygame.draw.rect(tela, PRETO, caixa_titulo)
        pygame.draw.rect(tela, BRANCO, caixa_titulo, 3)
        titulo = fonte.render("Quiz em Python", True, BRANCO)
        tela.blit(titulo, (caixa.x + 230, caixa.y - 350))

        botao_iniciar.desenhar(tela)
        botao_informacao.desenhar(tela)
        botao_sair.desenhar(tela)

    elif estado == "info":

        texto = fonte.render("Informações sobre o projeto", True, BRANCO)
        tela.blit(texto, (caixa.x + 150, caixa.y - 350))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, BRANCO, caixa_info, 3)

        texto = fonte.render(dialogos[0], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y - 200))
        texto = fonte.render(dialogos[1], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y - 150))
        texto = fonte.render(dialogos[2], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y - 100))
        texto = fonte.render(dialogos[3], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y - 50))
        texto = fonte.render(dialogos[4], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y))

        botao_voltar.desenhar(tela)
        botao_tela_anterior.desenhar(tela)
        botao_avancar.desenhar(tela)

    elif estado == "info2":

        texto = fonte.render("Informações sobre o projeto", True, BRANCO)
        tela.blit(texto, (caixa.x + 150, caixa.y - 350))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, BRANCO, caixa_info, 3)

        texto = fonte.render(dialogos[5], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y - 200))
        texto = fonte.render(dialogos[6], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y - 150))
        texto = fonte.render(dialogos[7], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y - 100))
        texto = fonte.render(dialogos[8], True, BRANCO)
        tela.blit(texto, (caixa.x + 10, caixa.y - 50))
        texto = fonte.render(dialogos[9], True, BRANCO)
        tela.blit(texto, (caixa.x + 270, caixa.y))

        botao_voltar.desenhar(tela)
        botao_tela_anterior.desenhar(tela)
        botao_avancar.desenhar(tela)

    pygame.display.flip()
pygame.quit()


