import pygame
from abc import ABCMeta, abstractmethod
import random

pygame.init()

AMARELO = (255, 255, 0)
AZUL = (25, 63, 144)
BRANCO = (255, 255, 255)
CIANO = (27, 217, 217)
LARANJA = (255, 144, 0)
PRETO = (0, 0, 0)
ROSA = (255, 161, 161)
VERMELHO = (255, 0, 0)

CIMA = 1
BAIXO = 2
DIREITA = 3
ESQUERDA = 4

JOGANDO = 0
PAUSADO = 1
GAMEOVER = 2
VITORIA = 3

ALTURA = 600
LARGURA = 800

VELOCIDADE = 1

T = 20
P = 14
M = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
     [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
     [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
     [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
     [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
     [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
     [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
     [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
     [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
     [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

T1 = 40
P1 = 7
M1 = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
      [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
      [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
      [2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2],
      [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
      [2, 1, 2, 1, 2, 2, 0, 0, 0, 2, 2, 1, 2, 1, 2],
      [2, 1, 2, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2],
      [2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1, 1, 2],
      [2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2],
      [2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2],
      [2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 2],
      [2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2],
      [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
      [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

tela = pygame.display.set_mode((LARGURA, ALTURA), 0)
fonte = pygame.font.SysFont("arial", 32, True, False)
fonte_titulo = pygame.font.SysFont("arial", 40, True, True)
fonte_instrucoes = pygame.font.SysFont("arial", 20, True, True)

pygame.mixer_music.load('sons/music.ogg')
pygame.mixer_music.play(-1)

som_comendo = pygame.mixer.Sound('sons/comendo.ogg')
som_gameover = pygame.mixer.Sound('sons/gameover.wav')
som_morte = pygame.mixer.Sound('sons/morte.ogg')
som_win = pygame.mixer.Sound('sons/win.ogg')



'''------------------------------------------- ELEMENTO JOGO --------------------------------------------------------'''


class ElementoJogo(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass


'''---------------------------------------------------- MOVIVEL -----------------------------------------------------'''


class Movivel(metaclass=ABCMeta):
    @abstractmethod
    def aceitar_movimento(self):
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes):
        pass

    @abstractmethod
    def esquina(self, direcoes):
        pass


'''--------------------------------------------------- CENARIO ------------------------------------------------------'''


class Cenario(ElementoJogo):
    def __init__(self, tamanho, pacman, matriz):
        self.tamanho = tamanho
        self.pacman = pacman
        self.moviveis = []
        self.pontos = 0
        self.total_pontos = 0
        self.vidas = 5
        self.estado = JOGANDO
        self.matriz = matriz
        self.num_linhas = 0
        self.num_colunas = 0

    def calcular_total_pontos(self, matriz):
        total = 0
        self.num_linhas = len(matriz)
        self.num_colunas = len(matriz[0])
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                if matriz[linha][coluna] == 1:
                    total += 1
        self.total_pontos = total
        print(self.total_pontos, self.num_linhas, self.num_colunas)

    def adicionar_movivel(self, obj):
        self.moviveis.append(obj)

    def pintar_infos(self, tela):
        img_titulo = fonte_titulo.render("Pac-man Py", True, AMARELO)
        img_pontos = fonte.render("Score: {}".format(self.pontos), True, AMARELO)
        img_vidas = fonte.render('Vidas: {}'.format(self.vidas), True, AMARELO)
        img_pausar = fonte_instrucoes.render('Aperte <P> para pausar', True, AMARELO)
        img_setas1 = fonte_instrucoes.render('Usar setas direcionais', True, AMARELO)
        img_setas2 = fonte_instrucoes.render('para movimentação', True, AMARELO)
        tela.blit(img_titulo, (590, 30))
        tela.blit(img_pontos, (620, 100))
        tela.blit(img_vidas, (620, 150))
        tela.blit(img_pausar, (590, 450))
        tela.blit(img_setas1, (590, 500))
        tela.blit(img_setas2, (590, 520))

    def pintar_linha(self, tela, numero_linha, linha):
        half = self.tamanho // 2
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + half, y + half), self.tamanho // 5, 0)

    def pintar(self, tela):
        if self.estado == JOGANDO:
            self.pintar_jogando(tela)
        elif self.estado == PAUSADO:
            self.pintar_jogando(tela)
            self.pintar_pausado(tela)
        elif self.estado == GAMEOVER:
            self.pintar_jogando(tela)
            self.pintar_gameover(tela)
        elif self.estado == VITORIA:
            self.pintar_jogando(tela)
            self.pintar_vitoria(tela)

    def pintar_jogando(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_infos(tela)

    def pintar_texto_centro(self, tela, texto):
        texto_img = fonte.render(texto, True, AMARELO, PRETO)
        texto_x = (tela.get_width() - texto_img.get_width()) // 2
        texto_y = (tela.get_height() - texto_img.get_height()) // 2
        tela.blit(texto_img, (texto_x, texto_y))

    def pintar_pausado(self, tela):
        self.pintar_texto_centro(tela, 'P A U S A D O')

    def pintar_gameover(self, tela):
        self.pintar_texto_centro(tela, 'G A M E   O V E R')

    def pintar_vitoria(self, tela):
        self.pintar_texto_centro(tela, 'V I T O R I A')

    def get_direcoes(self, linha, coluna):
        direcoes = []
        if self.matriz[int(linha - 1)][int(coluna)] != 2:
            direcoes.append(CIMA)
        if self.matriz[int(linha + 1)][int(coluna)] != 2:
            direcoes.append(BAIXO)
        if self.matriz[int(linha)][int(coluna - 1)] != 2:
            direcoes.append(ESQUERDA)
        if self.matriz[int(linha)][int(coluna + 1)] != 2:
            direcoes.append(DIREITA)
        return direcoes

    def calcular_regras(self):
        if self.estado == JOGANDO:
            self.calcular_regras_jogando()
        elif self.estado == PAUSADO:
            self.calcular_regras_pausado()
        elif self.estado == GAMEOVER:
            self.calcular_regras_gameover()

    def calcular_regras_jogando(self):
        for movivel in self.moviveis:
            lin = int(movivel.linha)
            col = int(movivel.coluna)
            lin_intencao = int(movivel.linha_intencao)
            col_intencao = int(movivel.coluna_intencao)
            direcoes = self.get_direcoes(lin, col)
            if len(direcoes) >= 3:
                movivel.esquina(direcoes)
            if isinstance(movivel, Fantasma) and movivel.linha == pacman.linha and movivel.coluna == pacman.coluna:
                self.vidas -= 1
                som_morte.play()
                if self.vidas <= 0:
                    self.estado = GAMEOVER
                    som_gameover.play()
                else:
                    self.pacman.linha = 1
                    self.pacman.coluna = 1
            else:
                if 0 <= col_intencao < self.num_colunas and 0 <= lin_intencao <= self.num_linhas and \
                        self.matriz[lin_intencao][col_intencao] != 2:
                    movivel.aceitar_movimento()
                    if isinstance(movivel, Pacman) and self.matriz[lin][col] == 1:
                        self.pontos += 1
                        self.matriz[lin][col] = 0
                        som_comendo.play()
                        if self.pontos >= self.total_pontos:
                            self.estado = VITORIA
                            som_win.play()
                else:
                    movivel.recusar_movimento(direcoes)

    def calcular_regras_pausado(self):
        pass

    def calcular_regras_gameover(self):
        pass

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.estado == JOGANDO:
                        self.estado = PAUSADO
                    else:
                        self.estado = JOGANDO


'''------------------------------------------------- PACMAN ---------------------------------------------------------'''


class Pacman(ElementoJogo, Movivel):

    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.raio = int(self.tamanho / 2)
        self.abertura = 0
        self.vel_abertura = 0
        self.vel_x = 0
        self.vel_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.vel_x = - VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.vel_y = - VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0

    def processar_eventos_mouse(self, eventos):
        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay

    def pintar(self, tela):
        # Desenha o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        self.abertura += self.vel_abertura
        if self.abertura > self.raio:
            self.vel_abertura = - 3 * VELOCIDADE
        elif self.abertura <= 0:
            self.vel_abertura = 3 * VELOCIDADE

        # Desenha boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.abertura)
        labio_inferior = (self.centro_x + self.raio, self.centro_y + self.abertura)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Desenha olho
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio / 1.5)
        olho_raio = int(self.raio / 6)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna

    def esquina(self, direcoes):
        pass


'''------------------------------------------------- FANTASMA ------------------------------------------------------'''


class Fantasma(ElementoJogo):
    # Blink VERMELHO
    # Clyde LARANJA
    # Pinky ROSA
    # Inky CIANO
    def __init__(self, tamanho, cor, pos):
        self.coluna = pos
        self.linha = pos
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.velocidade = 1
        self.direcao = BAIXO
        self.tamanho = tamanho
        self.cor = cor

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho),
                    (px + fatia, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho)
                    ]
        pygame.draw.polygon(tela, self.cor, contorno, 0)

        olho_raio_ext = fatia
        olho_raio_int = fatia // 2
        olho_esq_x = int(px + fatia * 2.5)
        olho_esq_y = int(py + fatia * 2.5)
        olho_dir_x = int(px + fatia * 5.5)
        olho_dir_y = int(py + fatia * 2.5)
        pygame.draw.circle(tela, BRANCO, (olho_esq_x, olho_esq_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, PRETO, (olho_esq_x, olho_esq_y), olho_raio_int, 0)
        pygame.draw.circle(tela, BRANCO, (olho_dir_x, olho_dir_y), olho_raio_ext, 0)
        pygame.draw.circle(tela, PRETO, (olho_dir_x, olho_dir_y), olho_raio_int, 0)

    def calcular_regras(self):
        if self.direcao == CIMA:
            self.linha_intencao -= self.velocidade
        elif self.direcao == BAIXO:
            self.linha_intencao += self.velocidade
        elif self.direcao == ESQUERDA:
            self.coluna_intencao -= self.velocidade
        elif self.direcao == DIREITA:
            self.coluna_intencao += self.velocidade

    def mudar_direcao(self, direcoes):
        self.direcao = random.choice(direcoes)

    def esquina(self, direcoes):
        self.mudar_direcao(direcoes)

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcao(direcoes)

    def processar_eventos(self, eventos):
        pass


'''------------------------------------------------- MAIN -------------------------------------------------------'''


def render():
    tela.fill(PRETO)
    cenario.pintar(tela)
    pacman.pintar(tela)
    blink.pintar(tela)
    clyde.pintar(tela)
    inky.pintar(tela)
    pinky.pintar(tela)
    pygame.display.update()
    pygame.time.delay(100)


if __name__ == "__main__":
    tamanho = T
    matriz = M
    pos = P

    pacman = Pacman(tamanho=tamanho)
    blink = Fantasma(tamanho=tamanho, cor=VERMELHO, pos=pos)
    clyde = Fantasma(tamanho=tamanho, cor=LARANJA, pos=pos)
    inky = Fantasma(tamanho=tamanho, cor=AZUL, pos=pos)
    pinky = Fantasma(tamanho=tamanho, cor=ROSA, pos=pos)

    cenario = Cenario(tamanho=tamanho, pacman=pacman, matriz=matriz)
    cenario.calcular_total_pontos(matriz)
    cenario.adicionar_movivel(pacman)
    cenario.adicionar_movivel(blink)
    cenario.adicionar_movivel(clyde)
    cenario.adicionar_movivel(inky)
    cenario.adicionar_movivel(pinky)

    while True:
        # Calcula regras
        pacman.calcular_regras()
        blink.calcular_regras()
        clyde.calcular_regras()
        inky.calcular_regras()
        pinky.calcular_regras()
        cenario.calcular_regras()

        # Pinta a tela
        render()

        # Eventos
        eventos = pygame.event.get()
        cenario.processar_eventos(eventos)
        pacman.processar_eventos(eventos)
