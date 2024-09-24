from pico2d import *
import math

# 개발에 있어서 중요한 것은 실행 가능한 가장 큰 뼈대를 만드는 것.
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
def run_rectangle():
    print('rectangle')
    pass # pass : 유보기능 - C로 따지면 아무것도 없는 빈 함수
def run_circle():
    print('Circle')
    r, cx, cy = 300, 800//2, 600//2

    for d in range(0, 360):     # d = degree
        x = r * math.cos(math.radians(d)) + cx  
        y = r * math.sin(math.radians(d)) + cy
    
        clear_canvas_now()
        #grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    pass

while(1) :
    run_circle()
    run_rectangle()
    break
    # **TOP-DOWN-DESIGN : 큰 틀을 잡고 내부를 채우는 하향식 설계 방식**

close_canvas()
