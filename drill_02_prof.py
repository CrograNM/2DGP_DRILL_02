from pico2d import *
import math

# 개발에 있어서 중요한 것은 실행 가능한 가장 큰 뼈대를 만드는 것.
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
def draw_boy(x, y):
    clear_canvas_now()
    character.draw_now(x, y)
    delay(0.01)
def run_top():
    print('top')
    for x in range(0, 800, 10):
        draw_boy(x, 550)
    pass
def run_right():
    print('right')
    pass
def run_bottom():
    print('bottom')
    pass
def run_left():
    print('left')
    pass
def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass # pass : 유보기능 - C로 따지면 아무것도 없는 빈 함수
def run_circle():
    print('Circle')
    r, cx, cy = 300, 800//2, 600//2

    for d in range(0, 360):     # d = degree
        x = r * math.cos(math.radians(d)) + cx  
        y = r * math.sin(math.radians(d)) + cy
        draw_boy(x, y) 
    pass

while(1) :
    # run_circle()
    run_rectangle()
    break
    # **TOP-DOWN-DESIGN : 큰 틀을 잡고 내부를 채우는 하향식 설계 방식**

close_canvas()
