import pygame
import sys
import random

# ゲームの初期化
pygame.init()

# 画面のサイズ
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("スロットゲーム")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# スロットのシンボル
symbols = ["7", "Cherry", "Bar", "Bell", "Plum"]

# リールの設定
reel_width = 100
reel_height = 300
reel_padding = 20
reel_x = screen_width // 2 - reel_width // 2
reel_y = screen_height // 2 - reel_height // 2
symbol_size = 80
symbol_padding = 20
reel_speed = 10

# 初期シンボル配置
reels = []
for i in range(3):
    reel = []
    for j in range(3):
        symbol = random.choice(symbols)
        reel.append(symbol)
    reels.append(reel)

# スピンボタンの設定
button_width = 100
button_height = 50
button_x = screen_width // 2 - button_width // 2
button_y = screen_height - 100
button_color = (0, 255, 0)
button_text_color = WHITE
button_font = pygame.font.SysFont(None, 36)

# スコアの設定
score = 1000
score_font = pygame.font.SysFont(None, 48)

# ゲームループ
clock = pygame.time.Clock()
spinning = False
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not spinning:
                spinning = True
                reels = [[random.choice(symbols) for _ in range(3)] for _ in range(3)]
                score -= 10  # スピンのコスト
    
    # リールの描画とアニメーション
    for i in range(3):
        for j in range(3):
            symbol = reels[i][j]
            symbol_rect = pygame.Rect(reel_x + i * (symbol_size + symbol_padding),
                                      reel_y + j * (symbol_size + symbol_padding),
                                      symbol_size, symbol_size)
            pygame.draw.rect(screen, WHITE, symbol_rect)
            symbol_text = button_font.render(symbol, True, BLACK)
            screen.blit(symbol_text, symbol_rect.topleft)
    
    # スピンボタンの描画
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = button_font.render("SPIN", True, button_text_color)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)
    
    # スコアの描画
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # リールを回転させるアニメーション
    if spinning:
        for i in range(3):
            for j in range(3):
                reels[i][j] = random.choice(symbols)
        reel_speed -= 1
        if reel_speed <= 0:
            spinning = False
            reel_speed = 10
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
