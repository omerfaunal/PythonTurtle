from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    def __init__(self, screen_width, screen_height, car_speed, car_speed_increase):
        self.all_cars = []
        self.move_distance = car_speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.car_speed = car_speed
        self.car_speed_increase = car_speed_increase
        
    def create_car(self, level):
        chance = random.randint(1,6)
        if  level > 5:
            chance = random.randint(1,3)
        if chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.turtlesize(stretch_len=2)
            x_cor, y_cor = self.screen_width//2, random.randint(-self.screen_height//2+80, self.screen_height//2-80)
            new_car.goto(x_cor, y_cor)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())
    
    def increase_speed(self):
        self.move_distance += self.car_speed_increase
