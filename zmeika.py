#Pygame - модуль, движок
import random, time

#Набор инструментов этого модуля для создания игр:
# 1. Рисовать графические объекты
# 2. Отслеживать действия пользователя (движение мышью, клавиатура, таймер и тд.)
# 3. Отслеживание поведения графических объектов (столкновения и тд)
# 4. Быстрая отрисовка
# 5. Работа со звуком

#pip install pygame --pre

import pygame
pygame.init() #инициализация модуля pygame

#В игре используется палитра цвет RGB (Red Green Blue)
blue = (0,0,255) #код синего цвета
red = (255, 0, 0) #код красного цвета
white = (255, 255, 255) #код белого цвета
purp = (255, 0, 255)
blak = (0, 0, 0)
white1 = (200, 200, 200)
dis = pygame.display.set_mode((600, 400)) #создали игровое окно размером 800 на 500 пикселей
dis1 = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Змейка') #подпись игрового окна
game_over = False #флажок проигрыша. Если он в положении True, то игра окончена

window_size = pygame.display.get_window_size() #запоминаю размеры экрана

#Координаты змейки:
x_1 = 100 #координата по горизонтали
y_1 = 300 #по вертикали
x_1_change = 0 #на сколько пикселей сдвигается змейка (влево-вправо)
y_1_change = 0 #на сколько пикселей сдвигается змейка (вниз-вверх)
#Координаты яблока:
apple_x = random.randrange(10,window_size[0]-10,1)
apple_y = random.randrange(10,window_size[1]-10,1)

blok_x = random.randrange(50,window_size[0]-50,1)
blok_y = random.randrange(50,window_size[1]-50,1)

game_over_sound = pygame.mixer.Sound('Game_over.mp3')
eating_sound = pygame.mixer.Sound('apple_biting.mp3')
blok_sound = pygame.mixer.Sound('udar.mp3')
#Объявляем переменную clock (объект clock), через которую будем отслеживать время в игре
clock = pygame.time.Clock()

snake_spisok = []
Dlina_zmei = 1

width_snake = 10

speed_snake = 30
speed_ = speed_snake
score = 0 #объявляем счетчик очков
font = pygame.font.Font(None,28) #font - объект класса Font, шрифт 36 размера

def snake(width_snake, snake_spisok):
    for x in snake_spisok:
        pygame.draw.rect(dis,blue,[x[0],x[1],width_snake,width_snake]) #отрисовка прямоугольника синего цвета на игровом дисплее
while not game_over: #начало основного цикла игры. Пока True, игра продолжается
    if apple_x == blok_x or apple_y == blok_y:
        continue
    elif x_1_change == blok_x or y_1_change == blok_y:
        continue
    elif x_1 == blok_x or y_1 == blok_y:
        continue
    for event in pygame.event.get(): #цикл обработки событий
        if event.type == pygame.QUIT: #проверяем, не является ли текущее событие выходом из игры
            game_over = True
        if event.type == pygame.KEYDOWN: #задаем вопрос, не нажата ли какая-то клавиша
            if event.key == pygame.K_LEFT: #если нажата клавиша стрелка влево
                x_1_change = -width_snake*0.1 #змейка будет ползти влево на 10 пикселей каждый фрейм игры
                y_1_change = 0 #в таком случае, вверх или влево ползти не нужно
            if event.key == pygame.K_RIGHT:
                x_1_change = width_snake*0.1 #змейка будет ползти вправо на 10 пикселей каждый фрейм игры
                y_1_change = 0
            if event.key == pygame.K_UP:
                y_1_change = -width_snake*0.1 #змейка будет ползти вверх на 10 пикселей каждый фрейм игры
                x_1_change = 0
            if event.key == pygame.K_DOWN:
                y_1_change = width_snake*0.1 #змейка будет ползти вниз на 10 пикселей каждый фрейм игры
                x_1_change = 0

    if x_1 > window_size[0] or y_1 > window_size[1] or x_1 < 0 or y_1 < 0:
        game_over_sound.play()
        time.sleep(2)
        game_over = True

    x_1 += x_1_change  # изменение фактических координат змейки
    y_1 += y_1_change

    # clock.tick(speed_snake)
    time_elapsed = pygame.time.get_ticks() // 1000

    dis.fill(white) #заполняю экран белым цветом, чтобы очистить всё, что до этого там находилось
    dis1.fill(white1)
    snake(width_snake, snake_spisok)
    nadpis_score = font.render('Очки: ' + str(score),True,red) #создали переменную nadpis, которая хранит надпись
    nadpis_speed = font.render('Скорость : ' + str(speed_), True, purp)
    nadpis_cloc = font.render('Время : ' + str(time_elapsed), True, blak)
    dis1.blit(nadpis_score,(5,5))
    dis1.blit(nadpis_speed, (5, 25))
    dis1.blit(nadpis_cloc, (5, 50))
    pygame.draw.rect(dis, blak, [blok_x, blok_y, 30, 30])
    pygame.draw.rect(dis, red, [apple_x, apple_y, 10, 10]) #отрисовка яблока
    pygame.display.update() #обновление экрана для отображения изменений


    if x_1 in range(blok_x,blok_x+30,1) and y_1 in range(blok_y,blok_y+30,1):
        blok_sound.play()
        time.sleep(2)
        print('Удар!')
        game_over_sound.play()
        time.sleep(2)
        game_over = True

    if x_1 in range(apple_x,apple_x+10,1) and y_1 in range(apple_y,apple_y+10,1):
        eating_sound.play()
        print('Съел!')
        apple_x = random.randrange(50, window_size[0]-50, 1)
        apple_y = random.randrange(50, window_size[1]-50, 1)
        blok_x = random.randrange(50, window_size[0]-50, 1)
        blok_y = random.randrange(50, window_size[1]-50, 1)
        score += 1
        speed_snake += 1.5
        speed_ = round(speed_snake, 1)
        Dlina_zmei += 10

    snake_Head = []
    snake_spisok.append((x_1, y_1))
    if len(snake_spisok) > Dlina_zmei:
        del snake_spisok[0]
    for x in snake_spisok[:-1]:
        if x == (x_1, y_1):
            game_over_sound.play()
            time.sleep(2)
            game_over = True

    clock.tick(speed_snake) #ограничение кадров в секунду (фреймов)
pygame = quit()
quit()

#ДЗ на понедельник (Ivanov_Lesson_23.py)
# 1. Увеличить змейку после поедания каждого яблока
## 2. Увеличить очки после каждого съеденного яблока
##3. Усложнять игру по мере поедания яблок
# 4. Добавить препятствия
# 5. Игра заканчивается, если змейка врежется в свой хвост
## 6. Добавить звуки поедания яблок и game over
# eating_sound = pygame.mixer.Sound('eating.mp3')
# game_over_sound = pygame.mixer.Sound('game_over.mp3')
# eating_sound.play()
