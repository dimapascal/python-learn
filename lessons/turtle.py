import turtle as tu
import math

tu.shape('turtle')
tu.speed(10)

''' Упражнение №2: буква S '''


def turtle_2():
    tu.forward(50)
    tu.left(90)
    tu.forward(50)
    tu.left(90)
    tu.forward(50)
    tu.right(90)
    tu.forward(50)
    tu.right(90)
    tu.forward(50)


''' Упражнение №3: квадрат '''


def turtle_3():
    for _ in range(4):
        tu.forward(50)
        tu.left(90)


''' Упражнение №4: окружность '''


def turtle_4():
    tu.speed(0.001)
    for _ in range(360):
        tu.forward(1)
        tu.left(1)


''' Упражнение №5: больше квадратов '''


def turtle_5():
    squares_count = 40;
    for current_square in range(1, squares_count + 1):
        for __ in range(4):
            tu.forward(12 * current_square)
            tu.left(90)
        tu.penup()
        tu.right(135)
        tu.forward(8.5)
        tu.left(135)
        tu.pendown()


''' Упражнение №6: паук '''


def turtle_6():
    paws_count = 12
    paw_length = 60
    for _ in range(1, paws_count + 1):
        tu.forward(paw_length)
        tu.stamp()
        tu.left(180)
        tu.forward(paw_length)
        tu.right(180 - 360 / paws_count)


''' Упражнение №7: спираль '''


def turtle_7():
    tu.speed(0.00003)
    for distance in range(500):
        tu.forward(1 + distance / 200)
        tu.left(4)


''' Упражнение №8: квадратная «спираль» '''


def turtle_8():
    distance = 10
    for _ in range(500):
        tu.forward(distance)
        tu.left(90)
        distance += 2


''' Упражнение №9: правильные многоугольники '''


def draw_figure(sides_number, side_length):
    one_side_angle = ((sides_number - 2) * 180) / sides_number
    for _ in range(sides_number):
        tu.right(180 - one_side_angle)
        tu.forward(side_length)


def turtle_9():
    distance_increase_value = 15
    side_radius = 15
    for side_count in range(3, 11):
        """ '2*pi' is entire circle in radians so 2*pi/side_count is equal to radian value of one side """
        radian_of_one_side = (math.pi * 2) / side_count

        """ math.sin(radian_of_one_side) is coefficient between forward line and hypotenuse.
         hypotenuse is side_radius so we will get one side line height or 'side_length' """
        side_length = side_radius * math.sin(radian_of_one_side)

        """ Here is formula to get full radius of figure for any sides number """
        figure_full_radius = (side_count - 2) * 180

        """ Here is one single side angle """
        one_side_angle = figure_full_radius / side_count

        turn_radius_of_each_figure = one_side_angle / 2

        tu.right(turn_radius_of_each_figure)
        draw_figure(side_count, side_length)
        tu.left(turn_radius_of_each_figure)

        tu.penup()
        tu.forward(distance_increase_value)
        tu.pendown()

        side_radius += distance_increase_value


''' Упражнение №10: «цветок» '''


def turtle_10():
    petal_number = 8
    turn_angle = 360 / petal_number
    for current_petal_count in range(1, petal_number + 1):
        tu.circle(120)
        tu.right(turn_angle)


''' Упражнение №11: «бабочка» '''


def turtle_11():
    circle_radius = 20
    tu.right(90)
    for _ in range(20):
        tu.circle(circle_radius)
        tu.right(180)
        tu.circle(circle_radius)
        tu.right(180)
        circle_radius += 5


''' Упражнение №12: пружина '''


def draw_half_of_circle():
    for _ in range(45):
        tu.left(4)
        tu.forward(2)


def draw_half_of_circle_small():
    for _ in range(15):
        tu.left(12)
        tu.forward(1)


def turtle_12():
    for _ in range(10):
        draw_half_of_circle()
        draw_half_of_circle_small()


''' Упражнение №13: смайлик '''


def goto_without_trace(x: int, y: int):
    tu.penup()
    tu.goto(x, y)
    tu.pendown()


def turtle_13():
    tu.speed(10000)

    tu.color("yellow")
    tu.begin_fill()
    goto_without_trace(0, -200)
    tu.circle(200)
    tu.end_fill()

    tu.color("blue")
    tu.begin_fill()
    goto_without_trace(80, 50)
    tu.circle(40)
    tu.end_fill()

    tu.color("blue")
    tu.begin_fill()
    goto_without_trace(-80, 50)
    tu.circle(40)
    tu.end_fill()

    tu.color("red")
    tu.width("20")
    goto_without_trace(100, -70)
    tu.right(120)
    for _ in range(120):
        tu.right(1)
        tu.forward(2)
    tu.speed(1)

    tu.penup()
    tu.forward(99999)


"""" Упражнение №14: звезды """


def turtle_14():
    tu.speed(100)
    star_sides_count = 11;
    for _ in range(star_sides_count):
        tu.forward(300)
        tu.left(180 + (180 / star_sides_count))


def turtle_main():
    turtle_14()
