# Bibliotecas
import random
import pygame
import sys

pygame.mixer.init()
som_tecla = pygame.mixer.Sound("tecla1.wav")
som_botao = pygame.mixer.Sound("botão.wav")
sucesso = pygame.mixer.Sound("sucesso.wav")
fail = pygame.mixer.Sound("fail.wav")
som_tecla.set_volume(random.uniform(0.15, 0.20))

# ------------------- CONFIG -----------------------
pygame.init()
LARGURA, ALTURA = 1200, 900

porcentagem_horizontal = LARGURA / 100
porcentagem_vertical = ALTURA / 100

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Botão em Pygame")

fonte = pygame.font.SysFont(None, 40)

# ----------------------------------------- Cores pré definidas: -----------------------------------------------------

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 120, 255)
CINZA = (180, 180, 180)
AZUL_PALIDO = (100, 149, 237)
AZUL_CLARO = (0, 191, 255)
TURQUOISE = (64, 224, 208)
AZUL_ROYAL = (65, 105, 225)
LIMA = (0, 255, 0)

# ------------------------------------------- Variáveis simples: ------------------------------------------------------

recompensa = True
pontuacao = 0
moedas_obtidas = 0
ativar_random = True
moedas_totais = 0

# ---------------------------------------- Sistema de botões clicáveis -------------------------------------------------
pos_mouse = pygame.mouse.get_pos()
class Button:
    def __init__(self, x, y, largura, altura, textos):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.textos = textos

    def desenhar(self, desenha_tela):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            cor = AZUL
        else:
            cor = AZUL_CLARO
        pygame.draw.rect(desenha_tela, cor, self.rect)
        texto_renderizar = fonte.render(self.textos, True, BRANCO)
        desenha_tela.blit(texto_renderizar, texto_renderizar.get_rect(center=self.rect.center))

    def clicado(self, pos):
        return self.rect.collidepoint(pos)

# --------------------------------- Sistema de botões não clicáveis ---------------------------------------------------

class Title:
    def __init__(self, x, y, largura, altura, textos):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.textos = textos

    def desenhar(self, desenha_tela):

        cor = PRETO
        pygame.draw.rect(desenha_tela, cor, self.rect)
        texto_renderizar = fonte.render(self.textos, True, AZUL_ROYAL)
        desenha_tela.blit(texto_renderizar, texto_renderizar.get_rect(center=self.rect.center))

# ----------------------------------- aleatorizar alternativas --------------------------------------------------------
def aleatorizar_alternativas():

    global ativar_random, texto, opcoes

    if ativar_random:
        opcoes = [opcao_1, opcao_2, opcao_3, opcao_4]
        random.shuffle(opcoes)
        ativar_random = False

    pygame.draw.rect(tela, PRETO, caixa_questao_1)
    pygame.draw.rect(tela, BRANCO, caixa_questao_1, 3)

    texto = fonte.render(enunciado[0], True, AZUL)
    tela.blit(texto, (caixa.x, caixa.y - 390))
    texto = fonte.render(enunciado[1], True, AZUL)
    tela.blit(texto, (caixa.x, caixa.y - 340))
    texto = fonte.render(enunciado[2], True, AZUL)
    tela.blit(texto, (caixa.x, caixa.y - 290))
    texto = fonte.render(enunciado[3], True, AZUL)
    tela.blit(texto, (caixa.x, caixa.y - 240))
    texto = fonte.render(enunciado[4], True, AZUL)
    tela.blit(texto, (caixa.x, caixa.y - 190))
    texto = fonte.render(enunciado[5], True, AZUL)
    tela.blit(texto, (caixa.x, caixa.y - 140))

    botao_alternativa_1.textos = opcoes[0]
    botao_alternativa_2.textos = opcoes[1]
    botao_alternativa_3.textos = opcoes[2]
    botao_alternativa_4.textos = opcoes[3]

    pygame.draw.rect(tela, BRANCO, caixa_alternativa_1)
    pygame.draw.rect(tela, BRANCO, caixa_alternativa_2)
    pygame.draw.rect(tela, BRANCO, caixa_alternativa_3)
    pygame.draw.rect(tela, BRANCO, caixa_alternativa_4)

    botao_alternativa_1.desenhar(tela)
    botao_alternativa_2.desenhar(tela)
    botao_alternativa_3.desenhar(tela)
    botao_alternativa_4.desenhar(tela)


# ------------------------------------------------ ESTADOS ------------------------------------------------------------
estado = "menu"
estado_anterior = "none"

# -------------------------------- Dialogo da tela de informações (estado "Info") -------------------------------------

dialogos = [
    "Esse Quiz é o resultado de um trabalho do 2° semestre do curso de Análise e",
    "desenvolvimento de sistemas na Estácio, feito utilizando a linguagem python.",
    "O Objetivo é utilizar todo o conteúdo disponível no SAVA da matéria para",
    "elaborar perguntas para um Quiz, utilizando o aprendizado na prática.",
    "Para este objetivo, cada questão deve conter 5 alternativas, com apenas uma",
    "      correta. Além disso, decidi aleatorizar tanto as questões quanto as",
    "      alternativas, com o objetivo de tornar a experiencia mais divertida, ",
    "                                                    Boa Sorte!"
]

# ------------------------- Todos os botões e caixas de texto -----------------------------------------------------
# ------------------------- Botões da tela inicial (estado "Menu") ------------------------------------------------

titulo_texto = Title(porcentagem_horizontal * 40, porcentagem_vertical * 20,
                     porcentagem_horizontal * 20, porcentagem_vertical * 2, "Quiz em Python")

caixa_titulo = pygame.Rect(porcentagem_horizontal * 40, porcentagem_vertical * 16,
                           porcentagem_horizontal * 20, porcentagem_vertical * 10)

botao_iniciar = Button(porcentagem_horizontal * 40, porcentagem_vertical * 40,
                       porcentagem_horizontal * 20, porcentagem_vertical * 5, "Iniciar")

botao_informacao = Button(porcentagem_horizontal * 40, porcentagem_vertical * 50,
                       porcentagem_horizontal * 20, porcentagem_vertical * 5,"Informações")

botao_sair = Button(porcentagem_horizontal * 40, porcentagem_vertical * 60,
                       porcentagem_horizontal * 20, porcentagem_vertical * 5,"Sair")

# ------------------------- Botões da tela de informações (estado "Info") ------------------------------------------

botao_voltar = Button(porcentagem_horizontal * 5, porcentagem_vertical * 90,
                      porcentagem_horizontal * 25, porcentagem_vertical * 5, "Voltar")

botao_avancar = Button(porcentagem_horizontal * 70, porcentagem_vertical * 90,
                      porcentagem_horizontal * 25, porcentagem_vertical * 5, "Avançar")

botao_tela_anterior = Button(porcentagem_horizontal * 37, porcentagem_vertical * 90,
                      porcentagem_horizontal * 25, porcentagem_vertical * 5, "Anterior")

# ------------------------- Botões que definem as alternativas em qualquer estado ----------------------------------

botao_alternativa_1 = Button(porcentagem_horizontal * 5, porcentagem_vertical * 50, porcentagem_horizontal * 90, porcentagem_vertical * 6, "")
botao_alternativa_2 = Button(porcentagem_horizontal * 5, porcentagem_vertical * 60, porcentagem_horizontal * 90, porcentagem_vertical * 6, "")
botao_alternativa_3 = Button(porcentagem_horizontal * 5, porcentagem_vertical * 70, porcentagem_horizontal * 90, porcentagem_vertical * 6, "")
botao_alternativa_4 = Button(porcentagem_horizontal * 5, porcentagem_vertical * 80, porcentagem_horizontal * 90, porcentagem_vertical * 6, "")

# ------------------------- Caixas que envolvem os botões acima ----------------------------------------------------

caixa_alternativa_1 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical * 49.5, porcentagem_horizontal * 91, porcentagem_vertical * 7)
caixa_alternativa_2 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical * 59.5, porcentagem_horizontal * 91, porcentagem_vertical * 7)
caixa_alternativa_3 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical * 69.5, porcentagem_horizontal * 91, porcentagem_vertical * 7)
caixa_alternativa_4 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical * 79.5, porcentagem_horizontal * 91, porcentagem_vertical * 7)

# ------------------------- Caixa que envolve o enunciado da alternativa -------------------------------------------

caixa_questao_1 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical, porcentagem_horizontal * 91, porcentagem_vertical * 40)

# ------------------------- Botões e caixas auxiliares -------------------------------------------------------------
botao_ok = Button(385, 240, 80, 50, "OK")
botao_sair_transicao = Button (290, 240, 80, 50, "Sair")
caixa_transicao = pygame.Rect(275, 50, 200, 250)
botao_sim = Button(385, 190, 80, 50, "Sim")
botao_nao = Button(290, 190, 80, 50, "Não")
caixa = pygame.Rect(50, 420, 700, 150)
caixa_info = pygame.Rect(porcentagem_horizontal * 5, porcentagem_vertical * 50, porcentagem_horizontal * 90, porcentagem_vertical * 30)

# ------------------------ Define as perguntas, o numero das perguntas e as aleatoriza ------------------------------

perguntas = ["quiz_pergunta_1",
             "quiz_pergunta_2",
             "quiz_pergunta_3"]
indice_perguntas = 0
random.shuffle(perguntas)

# ------------------------ Controle de loop do programa principal ---------------------------------------------------

loop = 1

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
                estado = "sair"

            if botao_iniciar.clicado(pos_mouse):
                som_botao.play()
                estado = perguntas[indice_perguntas]

#-------------------------------------- INFO ------------------------------------------------

        elif estado == "info":
            if botao_voltar.clicado(pos_mouse):
                som_botao.play()
                estado = "menu"
            if botao_avancar.clicado(pos_mouse):
                som_botao.play()
                estado = "info2"
#------------------------------------- INFO 2 -----------------------------------------------
        elif estado == "info2":
            if botao_voltar.clicado(pos_mouse):
                som_botao.play()
                estado = "menu"
            if botao_tela_anterior.clicado(pos_mouse):
                som_botao.play()
                estado = "info"
#------------------------------------- SAIR ------------------------------------------------
        elif estado == "sair":
            if estado_anterior == "numero_questao":
                if botao_sim.clicado(pos_mouse):
                    som_botao.play()
                    estado = "menu"
                if botao_nao.clicado(pos_mouse):
                    som_botao.play()
                    estado = estado_anterior
            if estado_anterior != "numero_questao":
                if botao_sim.clicado(pos_mouse):
                    som_botao.play()
                    loop = 0
                    sys.exit()
                if botao_nao.clicado(pos_mouse):
                    som_botao.play()
                    estado = "menu"
#------------------------------ RESPOSTA CERTA ---------------------------------------------
        elif estado == "certa_resposta":
            if botao_avancar.clicado(pos_mouse):
                som_botao.play()
                estado = "numero_questao"
                recompensa = True
#------------------------------ RESPOSTA ERRADA ---------------------------------------------
        elif estado == "resposta_errada":
            if botao_avancar.clicado(pos_mouse):
                som_botao.play()
                estado = "numero_questao"
#-------------------------------TRANSIÇÃO QUESTÕES ------------------------------------------
        elif estado == "numero_questao":
            if botao_ok.clicado(pos_mouse):
                som_botao.play()
                indice_perguntas +=1
                estado = perguntas[indice_perguntas]
            if botao_sair_transicao.clicado(pos_mouse):
                som_botao.play()
                estado_anterior = "numero_questao"
                estado = "sair"
#------------------------------------- QUIZ PERGUNTA 1 ---------------------------------------
        elif estado == "quiz_pergunta_1":
            if botao_alternativa_1.clicado(pos_mouse):
                if botao_alternativa_1.textos == 'linguagem de maquina, como 0s e 1s.':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_2.clicado(pos_mouse):
                if botao_alternativa_2.textos == 'linguagem de maquina, como 0s e 1s.':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_3.clicado(pos_mouse):
                if botao_alternativa_3.textos == "linguagem de maquina, como 0s e 1s.":
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_4.clicado(pos_mouse):
                if botao_alternativa_4.textos == 'linguagem de maquina, como 0s e 1s.':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_1.clicado(pos_mouse) and botao_alternativa_1.textos != "linguagem de maquina, como 0s e 1s." or botao_alternativa_2.clicado(pos_mouse) and botao_alternativa_2.textos != "linguagem de maquina, como 0s e 1s." or botao_alternativa_3.clicado(pos_mouse) and botao_alternativa_3.textos != "linguagem de maquina, como 0s e 1s." or botao_alternativa_4.clicado(pos_mouse) and botao_alternativa_4.textos != "linguagem de maquina, como 0s e 1s.":
                som_botao.play()
                fail.play()
                estado = "resposta_errada"
                ativar_random = True
#-------------------------------------------- QUIZ PERGUNTA 2 ----------------------------------------------------------
        elif estado == "quiz_pergunta_2":
            if botao_alternativa_1.clicado(pos_mouse):
                if botao_alternativa_1.textos == 'instruções de controle, como Goto':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_2.clicado(pos_mouse):
                if botao_alternativa_2.textos == 'instruções de controle, como Goto':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_3.clicado(pos_mouse):
                if botao_alternativa_3.textos == "instruções de controle, como Goto":
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_4.clicado(pos_mouse):
                if botao_alternativa_4.textos == 'instruções de controle, como Goto':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_1.clicado(pos_mouse) and botao_alternativa_1.textos != "instruções de controle, como Goto" or botao_alternativa_2.clicado(pos_mouse) and botao_alternativa_2.textos != "instruções de controle, como Goto" or botao_alternativa_3.clicado(pos_mouse) and botao_alternativa_3.textos != "instruções de controle, como Goto" or botao_alternativa_4.clicado(pos_mouse) and botao_alternativa_4.textos != "instruções de controle, como Goto":
                som_botao.play()
                fail.play()
                estado = "resposta_errada"
                ativar_random = True
#----------------------------------- QUIZ PERGUNTA 3 -----------------------------------------
        elif estado == "quiz_pergunta_3":
            if botao_alternativa_1.clicado(pos_mouse):
                if botao_alternativa_1.textos == 'Imp. diz como ser feito, dec. diz o que ser feito.':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_2.clicado(pos_mouse):
                if botao_alternativa_2.textos == 'Imp. diz como ser feito, dec. diz o que ser feito.':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_3.clicado(pos_mouse):
                if botao_alternativa_3.textos == "Imp. diz como ser feito, dec. diz o que ser feito.":
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_4.clicado(pos_mouse):
                if botao_alternativa_4.textos == 'Imp. diz como ser feito, dec. diz o que ser feito.':
                    som_botao.play()
                    sucesso.play()
                    estado = "certa_resposta"
                    ativar_random = True
            if botao_alternativa_1.clicado(pos_mouse) and botao_alternativa_1.textos != "Imp. diz como ser feito, dec. diz o que ser feito." or botao_alternativa_2.clicado(pos_mouse) and botao_alternativa_2.textos != "Imp. diz como ser feito, dec. diz o que ser feito." or botao_alternativa_3.clicado(pos_mouse) and botao_alternativa_3.textos != "Imp. diz como ser feito, dec. diz o que ser feito." or botao_alternativa_4.clicado(pos_mouse) and botao_alternativa_4.textos != "Imp. diz como ser feito, dec. diz o que ser feito.":
                som_botao.play()
                fail.play()
                estado = "resposta_errada"
                ativar_random = True
#-------------------------------------------- DESENHO ---------------------------------------------------------------

    if estado == "menu":

        pygame.draw.rect(tela, PRETO, caixa_titulo)
        pygame.draw.rect(tela, TURQUOISE, caixa_titulo, 3)

        botao_iniciar.desenhar(tela)
        botao_informacao.desenhar(tela)
        botao_sair.desenhar(tela)
        titulo_texto.desenhar(tela)

#------------------------------- Estado "Info" e "Info 2" fazem parte da mesma lógica --------------------------------

    elif estado == "info":

        texto = fonte.render("Informações sobre o projeto", True, LIMA)
        tela.blit(texto, (porcentagem_horizontal * 35, porcentagem_vertical * 10))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, TURQUOISE, caixa_info, 3)

        texto = fonte.render(dialogos[0], True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 6, porcentagem_vertical * 54))
        texto = fonte.render(dialogos[1], True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 6, porcentagem_vertical * 60))
        texto = fonte.render(dialogos[2], True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 6, porcentagem_vertical * 66))
        texto = fonte.render(dialogos[3], True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 6, porcentagem_vertical * 72))

        botao_voltar.desenhar(tela)
        botao_tela_anterior.desenhar(tela)
        botao_avancar.desenhar(tela)

    elif estado == "info2":

        texto = fonte.render("Informações sobre o projeto", True, LIMA)
        tela.blit(texto, (porcentagem_horizontal * 35, porcentagem_vertical * 10))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, TURQUOISE, caixa_info, 3)

        texto = fonte.render(dialogos[4], True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 6, porcentagem_vertical * 54))
        texto = fonte.render(dialogos[5], True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 6, porcentagem_vertical * 60))
        texto = fonte.render(dialogos[6], True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 6, porcentagem_vertical * 66))
        texto = fonte.render(dialogos[7], True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 6, porcentagem_vertical * 72))

        botao_voltar.desenhar(tela)
        botao_tela_anterior.desenhar(tela)
        botao_avancar.desenhar(tela)

# -------------------------------------- Estado "Sair" -----------------------------------------------------------

    elif estado == "sair":

        texto = fonte.render("Tem certeza que deseja sair? ", True, BRANCO)
        tela.blit(texto, (caixa.x + 150, caixa.y - 350))
        texto = fonte.render("Seu progresso será salvo até fechar o programa.", True, BRANCO)
        tela.blit(texto, (caixa.x + 20, caixa.y - 280))

        botao_sim.desenhar(tela)
        botao_nao.desenhar(tela)

# ------------------------------ Respostas certas e erradas ------------------------------------------------------

    elif estado == "certa_resposta":
        texto = fonte.render("Resposta certa, parabéns!", True, BRANCO)
        tela.blit(texto, (caixa.x + 150, caixa.y - 350))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, BRANCO, caixa_info, 3)

        moedas_obtidas = 100
        if recompensa:
            pontuacao = pontuacao + 1
            moedas_totais = moedas_totais + moedas_obtidas
            recompensa = False

        texto = fonte.render(f"Sua pontuação é: {pontuacao}", True, AZUL)
        tela.blit(texto, (caixa.x + 50, caixa.y - 150))

        texto = fonte.render(f"Moedas obtidas: {moedas_obtidas}", True, AZUL)
        tela.blit(texto, (caixa.x + 50, caixa.y - 100))

        texto = fonte.render(f"Moedas totais: {moedas_totais}", True, AZUL)
        tela.blit(texto, (caixa.x + 50, caixa.y - 50))

        botao_avancar.desenhar(tela)

    elif estado == "resposta_errada":
        texto = fonte.render("Resposta errada, mais sorte na próxima!", True, BRANCO)
        tela.blit(texto, (caixa.x + 75, caixa.y - 350))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, BRANCO, caixa_info, 3)

        texto = fonte.render(f"Sua pontuação é: {pontuacao}", True, AZUL)
        tela.blit(texto, (caixa.x + 49, caixa.y - 150))

        texto = fonte.render(f"Moedas obtidas: {moedas_obtidas}", True, AZUL)
        tela.blit(texto, (caixa.x + 49, caixa.y - 100))

        texto = fonte.render(f"Moedas totais: {moedas_totais}", True, AZUL)
        tela.blit(texto, (caixa.x + 49, caixa.y - 50))

        botao_avancar.desenhar(tela)

# -------------------------------- definição do número das perguntas --------------------------------------------

    elif estado == "numero_questao":

        pygame.draw.rect(tela, PRETO, caixa_transicao)
        pygame.draw.rect(tela, BRANCO, caixa_transicao, 3)

        texto = fonte.render(f"Questão: {indice_perguntas + 1}", True, AZUL)
        tela.blit(texto, (caixa.x + 250, caixa.y - 350))

        botao_ok.desenhar(tela)
        botao_sair_transicao.desenhar(tela)

# ----------------------------- Declaração das perguntas ---------------------------------------------------------

    elif estado == "quiz_pergunta_1":
        desativar = True

        enunciado = ["  Hoje em dia, existem diversas linguagens de programação para os mais ",
                     "  variados usos, como c++, python, java e inúmeras outras opções, mas",
                     "  o mundo nem sempre foi assim.",
                     "  No final da década de 1940, Kathleen Booth deu o primeiro passo para a",
                     "  simplificação do código da maquina, criando a linguagem assembly.",
                     "  Antes desse período, como era realizada a programação nos computadores?"]

        opcao_1 = 'linguagem de maquina, como 0s e 1s.'
        opcao_2 = 'linguagens como C e Pascal.'
        opcao_3 = 'linguagens com alto nível de abstração.'
        opcao_4 = 'não existia nenhuma linguagem especifica.'

        opcoes = [opcao_1, opcao_2, opcao_3, opcao_4]

        aleatorizar_alternativas()

    elif estado == "quiz_pergunta_2":
        desativar = True

        enunciado = ["  Um dos critérios mais importantes para avaliar a",
                     "  qualidade de uma linguagem de programação é a",
                     "  legibilidade.",
                     "  Selecione qual das alternativas abaixo não é",
                     " a ",
                     "  considerada um critério de avaliação de uma lp:"]

        opcao_1 = 'Redibilidade'
        opcao_2 = 'Simplicidade'
        opcao_3 = 'instruções de controle, como Goto'
        opcao_4 = 'Custo atrelado a linguagem'

        aleatorizar_alternativas()

    elif estado == "quiz_pergunta_3":
        desativar = True

        enunciado = ["  O agrupamento por paradigmas é outra forma de",
                     "  classificar as linguagens de programação,",
                     "  agrupando aquelas com características semelhantes.",
                     "  Qual das alternativas demonstram a diferença entre",
                     " a",
                     "  paradigmas imperativos e declarativos?"]

        opcao_1 = 'Imp. diz como ser feito, dec. diz o que ser feito.'
        opcao_2 = 'Não existem mais diferenças entre elas.'
        opcao_3 = '"if" e "else" só existem em linguagens imperativas.'
        opcao_4 = 'linguagens declarativas são menos diretas.'

        aleatorizar_alternativas()


    pygame.display.flip()
pygame.quit()


