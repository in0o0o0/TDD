import math


def calc_area(r):
    return round(r * r * math.pi)

def all_method(io):

    data = io.input_data()
    result = []

    for x in data:
        result.append(calc_area(x))

    io.output_data(result)
