class MyCar:
    def __init__(self, **kwargs):
        self.model = kwargs['model']
        self.color = kwargs['color']
        self.speed = kwargs['speed']
        print(f'모델명: {self.model} 색깔: {self.color} 스피드: {self.speed}')

    def accelerate(self, accel_pedal):
        if accel_pedal > self.speed:
            return '최대 스피드를 초과했습니다.'
        self.speed += accel_pedal
        return f'현재 시속 : {self.speed}'

    def brake(self, brake_pedal):
        if brake_pedal > self.speed:
            return '자신의 스피드 보다 크게 브레이크를 걸 수 없습니다!'
        self.speed -= brake_pedal
        return f'현재 시속 : {self.speed}'


miyeong_car = MyCar(model='미영카', color='red', speed=100)
print(miyeong_car.accelerate(50))