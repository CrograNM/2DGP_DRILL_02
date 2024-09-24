from pico2d import *
import math

#개발에 있어서 중요한 것은 실행 가능한 가장 큰 뼈대를 만드는 것.
def run_rectangle():
    print('rectangle')
    pass #유보기능 - C로 따지면 아무것도 없는 빈 함수
def run_circle():
    print('Circle')
    pass

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

while(1) :
    run_circle()
    run_rectangle()
    #TOP-DOWN-DESIGN : 큰 틀을 잡고 내부를 채우는 하향식 설계 방식

close_canvas()
