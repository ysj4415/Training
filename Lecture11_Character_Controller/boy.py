from pico2d import *

RD, LD, RU, LU = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT)  : RU,
    (SDL_KEYUP, SDLK_LEFT)   : LU
}


class IDLE:
    @staticmethod
    def enter():    #상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        pass

    @staticmethod
    def exit():     #상태를 나올 때 행하는 액션
        print('EXIT IDLE')
        pass

    @staticmethod
    def do():       #상태에 있을 때 지속적으로 행하는 행위
        pass

    @staticmethod
    def draw():
        pass

class RUN:
    @staticmethod
    def enter():
        print('ENTER RUN')
        pass

    @staticmethod
    def exit():
        print('EXIT RUN')
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}



class Boy:
    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.q.insert(0, key_event)
        
        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir += 1
        #             boy.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir -= 1
        #             boy.face_dir = 1
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter()

    def update(self):
        self.cur_state.do()

        # 이벤트 확인
        if self.q:
            event = self.q.pop()
            self.cur_state.exit()
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter()

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
       self.cur_state.draw()

        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
