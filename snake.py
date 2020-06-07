import pygame, random
from pygame.locals import *
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
        if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
                return True
        else:
                return False
def die(screen, score, life):
        if life != 1:
                return [290, 290, 290, 290, 290], [290, 270, 250, 230, 210], True
        else:
                pygame.mixer.music.stop()
                r = 0
                while r < 255:
                        display.fill((r, 0, 0))
                        r += 3
                        pygame.display.update()
                while r > 0:
                        display.fill((r, 0, 0))
                        r -= 3
                        pygame.display.update()
                        pygame.time.delay(10)
                text = h.render('YOU DIED', True, (255, 0, 0))
                pygame.mixer.music.load('sound//Hello-hello.mp3')
                pygame.mixer.music.play()
                display.blit(text, (300, 300))
                color_g = 0
                pygame.display.update()
                pygame.time.delay(4000)
                '''pygame.time.delay(2000)
                while color_g <= 201:
                        pygame.time.delay(15)
                        pygame.draw.rect(display, (0, color_g, 0), (300 - (400 / 2), 400, 400, 60))
                        pygame.display.update()
                        color_g += 3
                text = h.render('Play Again', True, (255, 255, 255))
                display.blit(text, (210, 400))
                pygame.display.update()
                xmouse, ymouse = pygame.mouse.get_pos()
                if xmouse >= 300 - (400 / 2) and xmouse <= 300 + (400 / 2):
                        if ymouse >= 400 + 50 and ymouse <= 400 - 15:
                                print('ok')'''
                return [290, 290, 290, 290, 290], [290, 270, 250, 230, 210], False
def heart(life, x, y):
        #x = 20
        #y = 540
        heart = pygame.image.load('image//pixel-heart.png')
        heart = pygame.transform.scale(heart, (40, 48))
        display.blit(heart, (x, y))
        text = ph.render(' X ' + str(life), True, (255, 255, 255))
        display.blit(text, (x + 45, y))
score_file = open('score.txt', 'r')
best_score = score_file.readline()
coin_file = open('coin.txt', 'r')
total_coin = int(coin_file.readline())
coin_file.close()
xs = [290, 290, 290, 290, 290]
ys = [290, 270, 250, 230, 210]
dirs = 0
score = 0
applepos = (random.randint(80, 560), random.randint(80, 525))
pygame.init()
display=pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')
appleimage = pygame.Surface((10, 10))
appleimage.fill((0, 255, 0))
img = pygame.Surface((20, 20))
img.fill((255, 0, 0))
p = pygame.font.SysFont('Arial', 20)
h = pygame.font.SysFont('Arial', 50)
ph = pygame.font.SysFont('Arial', 40)
clock = pygame.time.Clock()
life = open('heart.txt', 'r')
life = int(life.readline())
run = True
game_start = False
color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_i = 0
face_num = 1
snake_image_width = 150
snake_image_height = 200
shop = False
pygame.mixer.music.load('sound//drive.mp3')
pygame.mixer.music.play()
while run:
        
        if not game_start:
                if not shop:
                    pygame.time.delay(50)
                    display.fill((0, 0, 0))
                    pygame.draw.rect(display, color[color_i], (300 - (250 / 2), 400 - 20, 250, 50))
                    snake_image = pygame.image.load('image//snake.png')
                    shop_image = pygame.image.load('image//shop-icon.png')
                    shop_image = pygame.transform.scale(shop_image, (90, 90))
                    snake_image = pygame.transform.scale(snake_image, (snake_image_width, snake_image_height))
                    coin_image = pygame.image.load('image//gold-coin.png')
                    coin_image = pygame.transform.scale(coin_image, (40, 40))
                    text = h.render('Snake Game', True, (255, 255, 255))
                    display.blit(text, (300 - 120, 300))
                    text = ph.render('Play', True, (255, 255, 255))
                    display.blit(text, (300 - 30, 380))
                    text = ph.render(str(total_coin), True, (255, 255, 255))
                    display.blit(text, (90, 15))
                    text = ph.render('x', True, (255, 255, 255))
                    display.blit(text, (70, 15))
                    display.blit(snake_image, (300 - (150 / 2), 100))
                    display.blit(coin_image, (20, 20))
                    display.blit(shop_image, (70, 450))
                    if color_i == 2:
                        color_i = 0
                    else:
                        color_i += 1
                else:
                        display.fill((0, 0, 0))
                        pygame.draw.rect(display, (0, 255, 0), (100, 100, 400, 70))
                        coin_image = pygame.image.load('image//gold-coin.png')
                        coin_image = pygame.transform.scale(coin_image, (40, 40))
                        display.blit(coin_image, (20, 20))
                        text = ph.render(str(total_coin), True, (255, 255, 255))
                        display.blit(text, (90, 15))
                        text = ph.render('x', True, (255, 255, 255))
                        display.blit(text, (70, 15))
                        text = ph.render('Buy Heart = 50$', True, (255, 255, 255))
                        display.blit(text, (100 + 90, 100 + 10))
                        pygame.draw.rect(display, (255, 0, 0), (200, 400, 200, 70))
                        text = ph.render('Back', True, (255, 255, 255))
                        display.blit(text, (265, 410))
                heart(life, 450, 20)
        clock.tick(10)
        for event in pygame.event.get():
                if event.type == QUIT:
                        run = False
                elif event.type == MOUSEBUTTONDOWN:
                        (xmouse, ymouse) = event.pos
                        if xmouse >= 300 - (250 / 2) and xmouse <= 300 + (250 / 2):
                                if ymouse >= 400 - 20 and ymouse <= 400 + 10:
                                        game_start = True
                        if xmouse >= 70 and xmouse <= 70 + 90:
                                if ymouse >= 450 and ymouse <= 450 + 90:
                                        shop = True
                        if xmouse >= 100 and xmouse <= 100 + 400:
                                if ymouse >= 100 and ymouse <= 100 + 70:
                                        if total_coin >= 50:
                                                life += 1
                                                total_coin -= 50
                                                coin_file = open('coin.txt', 'w')
                                                coin_file.write(str(total_coin))
                                                coin_file.close()
                                                life_file = open('heart.txt', 'w')
                                                life_file.write(str(life + 1))
                                                life_file.close()
                        if xmouse >= 200 and xmouse <= 200 + 200:
                                if ymouse >= 400 and ymouse <= 400 + 70:
                                        shop = False
                elif event.type == KEYDOWN:
                        if event.key == K_UP and dirs != 0:
                                dirs = 2
                        elif event.key == K_DOWN and dirs != 2:
                                dirs = 0
                        elif event.key == K_LEFT and dirs != 1:
                                dirs = 3
                        elif event.key == K_RIGHT and dirs != 3:
                                dirs = 1
        if game_start:
                #pygame.mixer.music.stop()
                i = len(xs)-1
                while i >= 2:
                        if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
                                xs, ys, run = die(display, score, life)
                                if run == False:
                                        game_start = False
                                        run = True
                                life -= 1
                                #print(0)
                                face_num = 3
                        i-= 1
                if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
                        score+=1
                        total_coin += 3
                        xs.append(700)
                        ys.append(700)
                        applepos=(random.randint(180,560),random.randint(180,525))
                        face_num = random.randint(0, 1)
                if xs[0] < 0 + 5 or xs[0] > 600 - 5 or ys[0] <= 80 or ys[0] > 525 - 5:
                        xs, ys, run = die(display, score, life)
                        if run == False:
                                game_start = False
                                run = True
                        if life >= 2:
                                life -= 1
                        #print(1)
                        face_num = 3
                i = len(xs)-1
                while i >= 1:
                        xs[i] = xs[i-1]
                        ys[i] = ys[i-1]
                        i -= 1
                if dirs == 0:
                        ys[0] += 20
                elif dirs == 1:
                    xs[0] += 20
                elif dirs == 2:
                    ys[0] -= 20
                elif dirs==3:
                    xs[0] -= 20
                display.fill((0, 0, 0))
                for i in range(0, len(xs)):
                    display.blit(img, (xs[i], ys[i]))
                pygame.draw.line(display, (255, 255, 255), (0, 80), (600, 80))
                display.blit(appleimage, applepos)
                text=p.render('Your Score : ' + str(score), True, (255, 255, 255))
                display.blit(text, (150, 10))
                text=p.render('Best Score : ' + best_score, True, (255, 255, 255))
                display.blit(text, (460, 10))
                heart(life, 20, 540)
                pygame.draw.line(display, (255, 255, 255), (0, 535), (600, 535))
                if face_num == 0:
                        face = pygame.image.load('image//heart-face-emoji.png')
                elif face_num == 3:
                    face = pygame.image.load('image//sad-face-emoji.png')
                else:
                    face = pygame.image.load('image//happy-face-emoji.png')
                face = pygame.transform.scale(face, (60, 60))
                display.blit(face, (20, 10))
                fire_img = pygame.image.load('image//fire.png')
                fire_img = pygame.transform.scale(fire_img, (600, 80))
                fire_img = pygame.transform.rotate(fire_img, 180)
                display.blit(fire_img, (0, 80))
        pygame.display.update()
pygame.quit()
if int(best_score) < score:
        score_file = open('score.txt', 'w')
        score_file.write(str(score))
        score_file.close()
coin_file = open('coin.txt', 'w')
coin_file.write(str(total_coin))
coin_file.close()
life_file = open('heart.txt', 'w')
life_file.write(str(life + 1))
life_file.close()
