import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect if player collides with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect if player reached the top 
    if player.ycor() > 300:
        player.go_to_start()
        car_manager.level_up()

    # Removing a car when it reaches the left side
    car_manager.remove_cars()        



screen.mainloop()



