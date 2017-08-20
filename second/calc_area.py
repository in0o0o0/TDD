import math
import sys

def calc_area(r):
    return int(round(r * r * math.pi))

def all_method(io):

    data = io.input_data()
    result = []

    data = to_float(data)

    for x in data:
        result.append(calc_area(x))

    io.output_data(result)


def to_float(number):
    return map(float, number)


class IO:
    def input_data(self):
        data = sys.stdin.readlines()
        return data

    def output_data(self,result):
        for x in result:
            print x

if __name__ == "__main__":
    io = IO()
    all_method(io)
