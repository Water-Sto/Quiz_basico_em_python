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
fail.set_volume(0.20)

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

# ------------------------------------------- Alternativas base ------------------------------------------------------
opcao_1 = 'texto base'
opcao_2 = 'texto base'
opcao_3 = 'texto base'
opcao_4 = 'texto base'
enunciado = ['texto base']

opcoes = [opcao_1, opcao_2, opcao_3, opcao_4]
# ------------------------------------------- Variáveis simples: ------------------------------------------------------

recompensa = True
pontuacao = 0
moedas_obtidas = 0
ativar_random = True
total_moedas = 0
pula_pergunta = False
contagem = False
alternativa_correta = 'texto base'
contagem_perguntas = 1
erros = 0

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

class Naobutton:
    def __init__(self, x, y, largura, altura, textos):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.textos = textos

    def desenhar(self, desenha_tela):

        cor = CINZA
        pygame.draw.rect(desenha_tela, cor, self.rect)
        texto_renderizar = fonte.render(self.textos, True, PRETO)
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

# ---------------------------------------------- Perguntas ------------------------------------------------------------

def pergunta_1(): #Pergunta sobre programação de computadores antes da linguagem assembly

    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

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
    alternativa_correta = 'linguagem de maquina, como 0s e 1s.'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas < 100:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    elif total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_2(): #pergunta sobre critérios de uma linguagem de programação

    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Um dos critérios mais importantes para avaliar a",
                 "  qualidade de uma linguagem de programação é a",
                 "  sua escrita, sendo avaliados vários critérios.",
                 "  ",
                 "  Selecione qual das alternativas abaixo não é",
                 "  considerada um critério de avaliação de uma lp:"]

    opcao_1 = 'A legibilidade da linguagem, isso é, a facilidade de ser lida'
    opcao_2 = 'A simplicidade da linguagem, o quão fácil é entendida'
    opcao_3 = 'Instruções de controle, como Goto.'
    opcao_4 = 'O custo atrelado a linguagem de programação'

    alternativa_correta = 'Instruções de controle, como Goto.'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_3(): #pergunta sobre linguagens imperativas e declarativas

    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  O agrupamento por paradigmas é outra forma de",
                 "  classificar as linguagens de programação,",
                 "  agrupando aquelas com características semelhantes.",
                 " ",
                 "  Qual das alternativas demonstram a diferença entre",
                 "  paradigmas imperativos e declarativos?"]

    opcao_1 = 'Imperativas dizem como ser feito, declarativas dizem o que ser feito.'
    opcao_2 = 'Não existem mais diferenças entre elas.'
    opcao_3 = '"if" e "else" só existem em linguagens imperativas.'
    opcao_4 = 'linguagens declarativas são menos diretas.'

    alternativa_correta = 'Imperativas dizem como ser feito, declarativas dizem o que ser feito.'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_4(): #pergunta sobre tipos de dados retornados pelo input()

    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  como existem diversas linguagem de programação, é",
                 "  comum que também existam diversos tipos de entrada,",
                 "  de dados. Em python, por padrão, toda entrada de dados",
                 "  possui um tipo especifico.",
                 "  ",
                 "  Qual tipo de dado é retornado pela função input()?"]

    opcao_1 = 'Inteiro'
    opcao_2 = 'Float'
    opcao_3 = 'String'
    opcao_4 = 'Booleano'

    alternativa_correta = 'String'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_5(): #pergunta sobre a forma correta de declarar funções em python
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Funções são extremamente uteis na programação.",
                 "  Não funções matemáticas, mas funções lógicas, ",
                 "  isso é, espaços de código que 'não existem' ",
                 "  até serem chamados, logo, não ocupando memória.",
                 "  ",
                 "  Qual a forma correta de declarar uma função em python?"]

    opcao_1 = 'function minhaFuncao()'
    opcao_2 = 'def minhaFuncao():'
    opcao_3 = 'func minhaFuncao()'
    opcao_4 = 'create minhaFuncao()'

    alternativa_correta = 'def minhaFuncao():'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_6(): #pergunta sobre como declarar uma lista em python
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Com python, assim como com diversas outras linguagens",
                 "  você pode isolar elementos dentro de uma lista, ",
                 "  e chamando eles  quando necessário como no exemplo:",
                 "  listaExemplo[0] (puxa o primeiro elemento)",
                 "  ",
                 "  Qual a forma correta de se declarar uma lista em python?"]

    opcao_1 = '{1, 2, 3}'
    opcao_2 = '(0, 1, 2, 3)'
    opcao_3 = '[1, 2, 3]'
    opcao_4 = '<1, 2, 3>'

    alternativa_correta = '[1, 2, 3]'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_7(): #Pergunta sobre adicionar bibliotecas em python
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Bibliotecas são conjuntos de códigos, funções, ",
                 "  classes e recursos pré escritos que desenvolvedores",
                 "  utilizam para acelerar o desenvolvimento. Elas ",
                 "  permitem uma maior produtividade e organização. ",
                 "  ",
                 "  Como se deve adicionar bibliotecas em python?"]

    opcao_1 = 'using'
    opcao_2 = 'import'
    opcao_3 = '#include'
    opcao_4 = 'require'

    alternativa_correta = 'import'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_8(): #pergunta sobre manipulação de listas e tratamento de texto
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Entender listas e saber como manipula-las",
                 "  é um requisito importante para programadores,",
                 "  um recurso chamado de 'tratamento de texto'.",
                 " ",
                 "  .append() é um comando muito utilizado para",
                 "  este objetivo. Qual a função desse comando?"]

    opcao_1 = 'Remover um item de uma lista após indicar sua posição.'
    opcao_2 = 'Ordenar a lista com base em uma sequencia numérica.'
    opcao_3 = 'Adicionar um novo elemento ao final da lista.'
    opcao_4 = 'Substituir um item na lista.'

    alternativa_correta = 'Adicionar um novo elemento ao final da lista.'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_9(): #pergunta sobre Conversão de string para inteiro
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Existem diversas formas de se armazenar dados",
                 "  em variáveis e, para cada uma delas, aquele dado",
                 "  é interpretado de uma forma diferente, por padrão",
                 "  sendo considerado como texto.",
                 "  ",
                 "  Qual função a seguir faz da entrada de dados um inteiro?"]

    opcao_1 = 'str()'
    opcao_2 = 'input(int())'
    opcao_3 = 'float()'
    opcao_4 = 'convert(int in str)'

    alternativa_correta = 'input(int())'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_10(): #pergunta sobre verificar valores em uma lista
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Gerenciamento de listas é essencial ",
                 "  para programadores experientes, adicionando",
                 "  e removendo itens quando necessário, mas .",
                 "  isso não é tudo que um programador precisa saber.",
                 "  ",
                 "  Qual dessas opções verifica se um valor está em uma lista?"]

    opcao_1 = 'in'
    opcao_2 = 'exists'
    opcao_3 = 'has'
    opcao_4 = 'contains'

    alternativa_correta = 'in'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_11(): #pergunta sobre comentários
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Comentários são uteis quando se trabalha em grupo.",
                 "  Utilizando eles, programadores e analistas de dados",
                 "  podem se guiar pelo código a partir de dicas deixadas",
                 "  por quem organizou o código, simplificando o entendimento",
                 "  ",
                 "  Qual dessas opções é usada para comentários em python?"]

    opcao_1 = '// comentário'
    opcao_2 = '/* comentário */'
    opcao_3 = '# comentário'
    opcao_4 = '-- comentário'

    alternativa_correta = '# comentário'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_12(): # pergunta sobre o trecho de código "type"
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Em python, números podem ser interpretados como texto",
                 "  erroneamente, causando confusão no fluxo do programa.",
                 "  o código 'type' retorna o tipo daquela variável,",
                 "  facilitando o entendimento do código.",
                 "  ",
                 "  O que o trecho de código type(10) retorna?"]

    opcao_1 = '"int"'
    opcao_2 = '<int>'
    opcao_3 = 'int'
    opcao_4 = 'integer'

    alternativa_correta = 'int'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_13(): #pergunta sobre estruturas de repetição:
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Estruturas de repetição podem gerar confusão pela ",
                 "  forma como são interpretadas pelo programa em cada",
                 "  linguagem de programação, confundindo com certa",
                 "  frequência programadores e analistas novatos.",
                 "  ",
                 "  Qual dessas opções cria um loop infinito?"]

    opcao_1 = 'for i in range(10):'
    opcao_2 = 'while True:'
    opcao_3 = 'loop forever:'
    opcao_4 = 'repeat infinite:'

    alternativa_correta = 'while True:'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_14():
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Saber como utilizar as ferramentas disponíveis",
                 "  do python é extremamente importante para dominar",
                 "  a linguagem. uma dessas ferramentas tem o nome",
                 "  'range'.",
                 "  ",
                 "  O que a função range(1, 5) retorna?"]

    opcao_1 = '[1, 2, 3, 4]'
    opcao_2 = '[1, 2, 3, 4, 5]'
    opcao_3 = '[0, 1, 2, 3, 4]'
    opcao_4 = '[1, 5]'

    alternativa_correta = '[1, 2, 3, 4]'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_15():
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Após criar e formatar uma lista em python, pode ser",
                 "  uma tarefa desafiadora editar os elementos dentro dela.",
                 "  Existem diversas formas de se alterar uma lista já pronta",
                 "  em python, e uma dessas formas é o método .pop()",
                 "  ",
                 "  O que o método .pop() faz?"]

    opcao_1 = 'Remove o último item da lista.'
    opcao_2 = 'Adiciona um item no primeiro espaço da lista.'
    opcao_3 = 'Ordena a lista do menor para o maior.'
    opcao_4 = 'Duplica a lista, criando outro array'

    alternativa_correta = 'Remove o último item da lista.'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_16(): #pergunta sobre o operador %
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Os operadores da aritmética padrão podem mudar de função",
                 "  de acordo com a linguagem de programação, sendo necessário",
                 "  cuidado para utiliza-los em uma linguagem nova.",
                 "  ",
                 "  Um desses operadores é o '%'. ",
                 "  Qual a função desse operador em python?"]

    opcao_1 = 'Indicar o resto da divisão.'
    opcao_2 = 'Retornar porcentagem de uma variável.'
    opcao_3 = 'Indica a divisão.'
    opcao_4 = 'Indica a multiplicação.'

    alternativa_correta = 'Indicar o resto da divisão.'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_17(): #pergunta sobre o código "Len"
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  O código 'len' em python tem como função retornar",
                 "  quantos caracteres são ocupados por aquele bloco",
                 "  de código.",
                 "  ",
                 "  ",
                 "  O que o código len(' Python ') retorna?"]

    opcao_1 = '6'
    opcao_2 = '8'
    opcao_3 = '7'
    opcao_4 = 'Erro'

    alternativa_correta = '8'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_18(): #pergunta sobre impressão na tela
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Diferentes comandos para a entrada de dados são",
                 "  utilizados, variando juntamente com as linguagens",
                 "  de programação.",
                 "  ",
                 "  ",
                 "  Qual comando é usado para imprimir algo na tela em python?"]

    opcao_1 = 'printf()'
    opcao_2 = 'cout << '
    opcao_3 = 'print()'
    opcao_4 = 'write()'

    alternativa_correta = 'print()'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_19(): # pergunta sobre operadores lógicos
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  Na linguagem python, existem diferenças que surgem quando",
                 "  se utilizam dois operadores em sequencia, por exemplo:",
                 "  o operador '*' indica multiplicação, mas o operador '**' ",
                 "  indica uma potência.",
                 "  ",
                 "  Qual a diferença entre '=' e '==' em python?"]

    opcao_1 = 'O operador "==" indica igualdade, enquanto o "=" indica atribuição de valor.'
    opcao_2 = 'Ambos os operadores realizam a mesma função, mas o "==" é mais recomendado.'
    opcao_3 = 'O operador "=" indica igualdade, enquanto o "==" indica atribuição de valor.'
    opcao_4 = 'Nenhuma das alternativas anteriores.'

    alternativa_correta = 'O operador "==" indica igualdade, enquanto o "=" indica atribuição de valor.'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)

def pergunta_20():#pergunta sobre declaração de variáveis
    global opcao_1, opcao_2, opcao_3, opcao_4, opcoes
    global alternativa_correta, enunciado

    enunciado = ["  O python é uma linguagem que não necessita da declaração",
                 "  de variáveis no começo do programa, possibilitando a declaração",
                 "  dentro da função principal. Isso ocorre pois o python mescla",
                 "  as fases de compilação e execução para um melhor desempenho.",
                 "  ",
                 "  Qual a forma de se declarar variáveis em python?"]

    opcao_1 = 'x = 10, apenas no ínicio da função principal.'
    opcao_2 = 'x = 10 em qualquer ponto do código.'
    opcao_3 = 'int x = 10 em qualquer ponto do código.'
    opcao_4 = 'var x = 10 antes da função principal.'

    alternativa_correta = 'x = 10 em qualquer ponto do código.'
    aleatorizar_alternativas()
    botao_mostrar_moedas.desenhar(tela)
    pygame.draw.rect(tela, BRANCO, caixa_moedas, 5)

    if total_moedas >= 100:
        botao_pular_ativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
    else:
        botao_pular_desativado.desenhar(tela)
        pygame.draw.rect(tela, BRANCO, caixa_pular, 5)
# -------------------------------------------------------- Respostas -------------------------------------------------

def resposta():

    global estado, ativar_random

    if botao_alternativa_1.clicado(pos_mouse):
        if botao_alternativa_1.textos == alternativa_correta:
            som_botao.play()
            sucesso.play()
            estado = "certa_resposta"
            ativar_random = True
    if botao_alternativa_2.clicado(pos_mouse):
        if botao_alternativa_2.textos == alternativa_correta:
            som_botao.play()
            sucesso.play()
            estado = "certa_resposta"
            ativar_random = True
    if botao_alternativa_3.clicado(pos_mouse):
        if botao_alternativa_3.textos == alternativa_correta:
            som_botao.play()
            sucesso.play()
            estado = "certa_resposta"
            ativar_random = True
    if botao_alternativa_4.clicado(pos_mouse):
        if botao_alternativa_4.textos == alternativa_correta:
            som_botao.play()
            sucesso.play()
            estado = "certa_resposta"
            ativar_random = True
    if botao_alternativa_1.clicado(
            pos_mouse) and botao_alternativa_1.textos != alternativa_correta or botao_alternativa_2.clicado(
        pos_mouse) and botao_alternativa_2.textos != alternativa_correta or botao_alternativa_3.clicado(
        pos_mouse) and botao_alternativa_3.textos != alternativa_correta or botao_alternativa_4.clicado(
        pos_mouse) and botao_alternativa_4.textos != alternativa_correta:
        som_botao.play()
        fail.play()
        estado = "resposta_errada"
        ativar_random = True
    if botao_pular_ativado.clicado(pos_mouse) and total_moedas >= 100:
        som_botao.play()
        estado = 'pular'

# ------------------------------------------------ Estados ------------------------------------------------------------
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

# ------------------------- Caixas que envolvem os botões acima --------------------------------------------------------

caixa_alternativa_1 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical * 49.5, porcentagem_horizontal * 91, porcentagem_vertical * 7)
caixa_alternativa_2 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical * 59.5, porcentagem_horizontal * 91, porcentagem_vertical * 7)
caixa_alternativa_3 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical * 69.5, porcentagem_horizontal * 91, porcentagem_vertical * 7)
caixa_alternativa_4 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical * 79.5, porcentagem_horizontal * 91, porcentagem_vertical * 7)

# ------------------------- Caixa que envolve o enunciado da alternativa e a opção pular -------------------------------

caixa_questao_1 = pygame.Rect(porcentagem_horizontal * 4.5, porcentagem_vertical, porcentagem_horizontal * 91, porcentagem_vertical * 40)
caixa_pular = pygame.Rect(porcentagem_horizontal * 70, porcentagem_vertical * 89.6, porcentagem_horizontal * 25, porcentagem_vertical * 6)
caixa_tutorial = pygame.Rect(porcentagem_horizontal * 2, porcentagem_vertical * 7, porcentagem_horizontal * 95, porcentagem_vertical * 30)
caixa_moedas = pygame.Rect(porcentagem_horizontal * 5, porcentagem_vertical * 89.6, porcentagem_horizontal * 25, porcentagem_vertical * 6)
#-------------------------- Botões do sistema de moedas -----------------------------------------------------------

botao_pular_ativado = Button(porcentagem_horizontal * 70, porcentagem_vertical * 90,
                      porcentagem_horizontal * 25, porcentagem_vertical * 5, "Pular Questão")
botao_pular_desativado = Naobutton(porcentagem_horizontal * 70, porcentagem_vertical * 90,
                                   porcentagem_horizontal * 25, porcentagem_vertical * 5, "Pular Questão")
botao_mostrar_moedas = Naobutton(porcentagem_horizontal * 5, porcentagem_vertical * 90,
                                 porcentagem_horizontal * 25, porcentagem_vertical * 5, f"Moedas: {total_moedas}")

# ------------------------- Botões e caixas auxiliares -------------------------------------------------------------
botao_ok = Button(porcentagem_horizontal * 50, porcentagem_vertical * 33, porcentagem_horizontal * 8, porcentagem_vertical * 6, "OK")
botao_sair_transicao = Button (porcentagem_horizontal * 40, porcentagem_vertical * 33, porcentagem_horizontal * 8, porcentagem_vertical * 6, "Sair")
caixa_transicao = pygame.Rect(porcentagem_horizontal * 39, porcentagem_vertical * 10, porcentagem_horizontal * 20, porcentagem_vertical * 30)
botao_sim = Button(porcentagem_horizontal * 55, porcentagem_vertical * 25, porcentagem_horizontal * 8, porcentagem_vertical * 5, "Sim")
botao_nao = Button(porcentagem_horizontal * 35, porcentagem_vertical * 25, porcentagem_horizontal * 8, porcentagem_vertical * 5, "Não")
caixa = pygame.Rect(50, 420, 700, 150)
caixa_info = pygame.Rect(porcentagem_horizontal * 5, porcentagem_vertical * 50, porcentagem_horizontal * 90, porcentagem_vertical * 30)

# ------------------------ Define as perguntas, o numero das perguntas e as aleatoriza ------------------------------

perguntas = ["quiz_pergunta_1",
             "quiz_pergunta_2",
             "quiz_pergunta_3",
             "quiz_pergunta_4",
             "quiz_pergunta_5",
             "quiz_pergunta_6",
             "quiz_pergunta_7",
             "quiz_pergunta_8",
             "quiz_pergunta_9",
             "quiz_pergunta_10",
             "quiz_pergunta_11",
             "quiz_pergunta_12",
             "quiz_pergunta_13",
             "quiz_pergunta_14",
             "quiz_pergunta_15",
             "quiz_pergunta_16",
             "quiz_pergunta_17",
             "quiz_pergunta_18",
             "quiz_pergunta_19",
             "quiz_pergunta_20"]

indice_perguntas = 0
random.shuffle(perguntas)

# ------------------------ Controle de loop do programa principal ---------------------------------------------------

loop = 1

# -------------------------------- Loop principal do programa -------------------------------------------------------
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
                sys.exit()

            if botao_iniciar.clicado(pos_mouse):
                if estado_anterior == "numero_questao":
                    som_botao.play()
                    estado = 'numero_questao'
                if estado_anterior != "numero_questao":
                    som_botao.play()
                    estado = 'tutorial'
#----------------------------------- Tutorial --------------------------------------------

        elif estado == 'tutorial':
            if botao_avancar.clicado(pos_mouse):
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
                    pygame.quit()
                    sys.exit()
                if botao_nao.clicado(pos_mouse):
                    som_botao.play()
                    estado = "menu"

# ------------------------------------- Final ---------------------------------------------------------

        elif estado == "final":
            if botao_avancar.clicado(pos_mouse):
                som_botao.play()
                pontuacao = 0
                indice_perguntas = 0
                total_moedas = 0
                botao_mostrar_moedas = Naobutton(porcentagem_horizontal * 5, porcentagem_vertical * 90,
                                                 porcentagem_horizontal * 25, porcentagem_vertical * 5,
                                                 f"Moedas: {total_moedas}")
                random.shuffle(perguntas)
                estado = "menu"

#------------------------------------ PULAR ------------------------------------------------

        elif estado == 'pular':
            if botao_sim.clicado(pos_mouse):
                som_botao.play()
                sucesso.play()
                total_moedas = total_moedas - 100
                indice_perguntas +=1
                pula_pergunta = True
                ativar_random = True
                estado = 'status_pular'
            if botao_nao.clicado(pos_mouse):
                som_botao.play()
                estado = perguntas[indice_perguntas]

#-------------------------------- TRANSIÇÃO PÓS PULAR --------------------------------------

        elif estado == 'status_pular':
            if botao_avancar.clicado(pos_mouse):
                som_botao.play()
                contagem = True
                estado = "numero_questao"

#------------------------------ RESPOSTA CERTA ---------------------------------------------
        elif estado == "certa_resposta":
            if botao_avancar.clicado(pos_mouse):
                contagem = True
                som_botao.play()
                estado = "numero_questao"
                recompensa = True
#------------------------------ RESPOSTA ERRADA ---------------------------------------------
        elif estado == "resposta_errada":
            if botao_avancar.clicado(pos_mouse):
                contagem = True
                som_botao.play()
                estado = "numero_questao"
                recompensa = True
#-------------------------------TRANSIÇÃO QUESTÕES ------------------------------------------
        elif estado == "numero_questao":
            if botao_ok.clicado(pos_mouse):
                som_botao.play()
                if not pula_pergunta:
                    indice_perguntas +=1
                    if indice_perguntas == 20:
                        estado = "final"
                    elif indice_perguntas < 20:
                        estado = perguntas[indice_perguntas]
                if pula_pergunta:
                    pula_pergunta = False
                    estado = perguntas[indice_perguntas]
            if botao_sair_transicao.clicado(pos_mouse):
                som_botao.play()
                estado_anterior = "numero_questao"
                estado = "sair"
#------------------------------------------ QUIZ PERGUNTAS -----------------------------------------------------------
        elif estado == "quiz_pergunta_1":
            resposta()

        elif estado == "quiz_pergunta_2":
            resposta()

        elif estado == "quiz_pergunta_3":
            resposta()

        elif estado == "quiz_pergunta_4":
            resposta()

        elif estado == "quiz_pergunta_5":
            resposta()

        elif estado == "quiz_pergunta_6":
            resposta()

        elif estado == "quiz_pergunta_7":
            resposta()

        elif estado == "quiz_pergunta_8":
            resposta()

        elif estado == "quiz_pergunta_9":
            resposta()

        elif estado == "quiz_pergunta_10":
            resposta()

        elif estado == "quiz_pergunta_11":
            resposta()

        elif estado == "quiz_pergunta_12":
            resposta()

        elif estado == "quiz_pergunta_13":
            resposta()

        elif estado == "quiz_pergunta_14":
            resposta()

        elif estado == "quiz_pergunta_15":
            resposta()

        elif estado == "quiz_pergunta_16":
            resposta()

        elif estado == "quiz_pergunta_17":
            resposta()

        elif estado == "quiz_pergunta_18":
            resposta()

        elif estado == "quiz_pergunta_19":
            resposta()

        elif estado == "quiz_pergunta_20":
            resposta()
#-------------------------------------------- DESENHO ---------------------------------------------------------------

    if estado == "menu":

        pygame.draw.rect(tela, PRETO, caixa_titulo)
        pygame.draw.rect(tela, TURQUOISE, caixa_titulo, 3)

        botao_iniciar.desenhar(tela)
        botao_informacao.desenhar(tela)
        botao_sair.desenhar(tela)
        texto = fonte.render("Quiz em Python", True, AZUL_ROYAL)
        tela.blit(texto, (porcentagem_horizontal * 41, porcentagem_vertical * 19.5))

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
        tela.blit(texto, (porcentagem_horizontal * 33, porcentagem_vertical * 5))
        texto = fonte.render("Seu progresso será salvo até fechar o programa.", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 22, porcentagem_vertical * 15))

        botao_sim.desenhar(tela)
        botao_nao.desenhar(tela)
# ----------------------------------------- Estado "Tutorial" ----------------------------------------------------

    elif estado == 'tutorial':

        pygame.draw.rect(tela, PRETO, caixa_tutorial)
        pygame.draw.rect(tela, BRANCO, caixa_tutorial, 3)

        texto = fonte.render("Você esta começando agora um quiz de python sobre python!", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 15, porcentagem_vertical * 10))

        texto = fonte.render("A cada questão respondida corretamente, você ganhará 1 ponto e 50 moedas.", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 5, porcentagem_vertical * 15))

        texto = fonte.render("Sempre que tiver 100 ou mais moedas, poderá optar por pular ",True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 15, porcentagem_vertical * 20))

        texto = fonte.render("uma pergunta, gastando assim 100 moedas.", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 25, porcentagem_vertical * 25))

        texto = fonte.render("Quando estiver pronto, clique em 'avançar' para a primeira pergunta, boa sorte!", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 5, porcentagem_vertical * 30))

        botao_avancar.desenhar(tela)
# ----------------------------------------- Estado "Pular" -------------------------------------------------------

    elif estado == 'pular':

        texto = fonte.render("Você vai gastar 100 moedas para pular essa questão, tem certeza? ", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 12, porcentagem_vertical * 5))
        texto = fonte.render("Retornar agora não irá gastar suas moedas.", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 25, porcentagem_vertical * 15))

        botao_sim.desenhar(tela)
        botao_nao.desenhar(tela)
# --------------------------------------- Estado após "Pular" ----------------------------------------------------

    elif estado == 'status_pular':

        texto = fonte.render(f"Você pulou a questão {indice_perguntas}, se prepare para a próxima!", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 20, porcentagem_vertical * 10))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, BRANCO, caixa_info, 3)

        texto = fonte.render(f"Sua pontuação é: {pontuacao}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 58))

        texto = fonte.render(f"Moedas obtidas: 0", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 65))

        texto = fonte.render(f"Moedas totais: {total_moedas}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 72))

        botao_avancar.desenhar(tela)

# ------------------------------ Respostas certas e erradas ------------------------------------------------------

    elif estado == "certa_resposta":
        texto = fonte.render("Resposta certa, parabéns!", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 35, porcentagem_vertical * 10))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, BRANCO, caixa_info, 3)

        moedas_obtidas = 50
        if recompensa:

            pontuacao = pontuacao + 1
            total_moedas = total_moedas + moedas_obtidas
            recompensa = False

        texto = fonte.render(f"Sua pontuação é: {pontuacao}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 58))

        texto = fonte.render(f"Moedas obtidas: {moedas_obtidas}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 65))

        texto = fonte.render(f"Moedas totais: {total_moedas}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 72))

        botao_mostrar_moedas = Naobutton(porcentagem_horizontal * 5, porcentagem_vertical * 90,
                                         porcentagem_horizontal * 25, porcentagem_vertical * 5,
                                         f"Moedas: {total_moedas}")

        botao_avancar.desenhar(tela)

    elif estado == "resposta_errada":
        texto = fonte.render("Resposta errada, mais sorte na próxima!", True, BRANCO)
        tela.blit(texto, (porcentagem_horizontal * 25, porcentagem_vertical * 10))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, BRANCO, caixa_info, 3)

        texto = fonte.render(f"Sua pontuação é: {pontuacao}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 58))

        texto = fonte.render(f"Moedas perdidas: {moedas_obtidas}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 65))

        texto = fonte.render(f"Moedas totais: {total_moedas}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 72))


        if recompensa:

            erros +=1
            total_moedas = total_moedas - moedas_obtidas
            recompensa = False


        botao_mostrar_moedas = Naobutton(porcentagem_horizontal * 5, porcentagem_vertical * 90,
                                         porcentagem_horizontal * 25, porcentagem_vertical * 5,
                                         f"Moedas: {total_moedas}")



        botao_avancar.desenhar(tela)

# -------------------------------- definição do número das perguntas --------------------------------------------

    elif estado == "numero_questao":

        if contagem:
            contagem_perguntas += 1
            contagem = False

        pygame.draw.rect(tela, PRETO, caixa_transicao)
        pygame.draw.rect(tela, BRANCO, caixa_transicao, 3)

        texto = fonte.render(f"Questão: {contagem_perguntas}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 43, porcentagem_vertical * 12))

        botao_ok.desenhar(tela)
        botao_sair_transicao.desenhar(tela)

# ----------------------------- Declaração das perguntas ---------------------------------------------------------

    elif estado == "quiz_pergunta_1":
        pergunta_1()

    elif estado == "quiz_pergunta_2":
        pergunta_2()

    elif estado == "quiz_pergunta_3":
        pergunta_3()

    elif estado == "quiz_pergunta_4":
        pergunta_4()

    elif estado == "quiz_pergunta_5":
        pergunta_5()

    elif estado == "quiz_pergunta_6":
        pergunta_6()

    elif estado == "quiz_pergunta_7":
        pergunta_7()

    elif estado == "quiz_pergunta_8":
        pergunta_8()

    elif estado == "quiz_pergunta_9":
        pergunta_9()

    elif estado == "quiz_pergunta_10":
        pergunta_10()

    elif estado == "quiz_pergunta_11":
        pergunta_11()

    elif estado == "quiz_pergunta_12":
        pergunta_12()

    elif estado == "quiz_pergunta_13":
        pergunta_13()

    elif estado == "quiz_pergunta_14":
        pergunta_14()

    elif estado == "quiz_pergunta_15":
        pergunta_15()

    elif estado == "quiz_pergunta_16":
        pergunta_16()

    elif estado == "quiz_pergunta_17":
        pergunta_17()

    elif estado == "quiz_pergunta_18":
        pergunta_18()

    elif estado == "quiz_pergunta_19":
        pergunta_19()

    elif estado == "quiz_pergunta_20":
        pergunta_20()


# ------------------------------------------- Final do Quiz ---------------------------------------------------------

    elif estado == "final":

        if pontuacao < 20:
            texto = fonte.render("Parabéns, você concluiu o quiz!",True, BRANCO)
            tela.blit(texto, (porcentagem_horizontal * 30, porcentagem_vertical * 10))

            texto = fonte.render("Espero que você tenha aproveitado a experiencia e que eu tenha", True, BRANCO)
            tela.blit(texto, (porcentagem_horizontal * 12, porcentagem_vertical * 20))

            texto = fonte.render("ajudado no seu desenvolvimento, muito obrigado e até a proxima!", True, BRANCO)
            tela.blit(texto, (porcentagem_horizontal * 12, porcentagem_vertical * 30))

        if pontuacao == 20:
            texto = fonte.render("Parabéns, você concluiu o quiz com pontuação perfeita!", True, BRANCO)
            tela.blit(texto, (porcentagem_horizontal * 17, porcentagem_vertical * 10))

            texto = fonte.render("Simplesmente incrível, você alcançou um excelente feito!", True, BRANCO)
            tela.blit(texto, (porcentagem_horizontal * 17, porcentagem_vertical * 20))

            texto = fonte.render("espero ter ajudado no seu desenvolvimento, muito obrigado e até a proxima!", True, BRANCO)
            tela.blit(texto, (porcentagem_horizontal * 8, porcentagem_vertical * 30))

        pygame.draw.rect(tela, PRETO, caixa_info)
        pygame.draw.rect(tela, BRANCO, caixa_info, 3)

        texto = fonte.render(f"Sua pontuação foi: {pontuacao}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 58))

        texto = fonte.render(f"Questões erradas: {erros}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 65))

        texto = fonte.render(f"Total de moedas restantes: {total_moedas}", True, AZUL)
        tela.blit(texto, (porcentagem_horizontal * 9, porcentagem_vertical * 72))

        botao_avancar.desenhar(tela)

    pygame.display.flip()
pygame.quit()


