#будет двигаться включая отрицательніе оси координат
class Car:
    def __init__(self):
        self.y=0
        self.x =0
        self.speed=0
        self.direction='stop'

    def set_speed(self,speed):
        if self.speed<0:
            print('Speed must be grater then 0')
            return
        if self.speed==0:
            self.position='stop'

        self.speed=speed

    def move_left(self):
        self.x+=self.speed
        if self.speed==0:
            self.direction='stop'
        else:
            self.direction='left'

    def move_right(self):
        self.x-=self.speed
        if self.speed==0:
            self.direction='stop'
        else:
            self.direction='right'

    def move_up(self):
        self.y+=self.speed
        if self.speed==0:
            self.direction='stop'
        else:
            self.direction='up'

    def move_down(self):
        self.y-=self.speed
        if self.speed==0:
            self.direction='stop'
        else:
            self.direction='down'
    def car_poistion(self):
        return (self.x,self.y)

if __name__=='__main__':
    car1=Car()
    car1.set_speed(2)
    car1.move_left()
    car1.move_left()
    car1.move_up()
    print('Car x={} y={}'.format(*car1.car_poistion()))
    print('Car direction',car1.direction)
    print('-------Stop car---------')
    car1.set_speed(0)
    car1.move_left()
    print('Car x={} y={}'.format(*car1.car_poistion()))
    print('Car direction', car1.direction)


print('----------------Testing------------------')
import unittest

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car=Car()
        self.car.set_speed(2)

    def test_move(self):
        self.car.move_left()
        self.car.move_left()
        self.assertEqual(self.car.car_poistion(),(4,0))

    def testStop(self):
        self.car.set_speed(0)
        self.assertEqual(self.car.position,'stop')

unittest.main()



