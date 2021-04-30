from math import sqrt, pow, sin, pi


def ease_in_out_cubic(x: float) -> float:
    from math import pow
    if x < .5:
        return 4 * x * x * x
    else:
        return 1 - pow(-2 * x + 2, 3) / 2


def ease_in_out_elastic(x: float) -> float:
    c5 = (2 * pi) / 4.5
    if x == 0 or x == 1:
        return x

    elif x < 0.5:
        return -(pow(2, 20 * x - 10) * sin((20 * x - 11.125) * c5)) / 2
    else:
        return (pow(2, -20 * x + 10) * sin((20 * x - 11.125) * c5)) / 2 + 1


def ease_in_out_back(x: float) -> float:
    c1 = 1.70158
    c2 = c1 * 1.525

    if x < .5:
        return (pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2
    else:
        return (pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2


def ease_in_elastic(x: float) -> float:
    c4 = (2 * pi) / 3
    if x == 0 or x == 1:
        return x
    else:
        return -pow(2, 10 * x - 10) * sin((x * 10 - 10.75) * c4)


def ease_out_elastic(x: float) -> float:
    c4 = (2 * pi) / 3
    if x == 0 or x == 1:
        return x
    else:
        return pow(2, -10 * x) * sin((x * 10 - 0.75) * c4) + 1


def ease_out_bounce(x: float) -> float:
    n1 = 7.5625
    d1 = 2.75

    if x < 1 / d1:
        return n1 * x * x
    elif x < 2 / d1:
        t = x - 1.5 / d1
        return n1 * t * x + 0.75
    elif x < 2.5 / d1:
        t = x - 2.25 / d1
        return n1 * t * x + 0.9375
    else:
        t = x - 2.625 / d1
        return n1 * t * x + 0.984375


def ease_out_circ(x: float) -> float:
    return sqrt(1 - pow(x - 1, 2))


def ease_in_circ(x: float) -> float:
    return 1 - sqrt(1 - pow(x, 2))
