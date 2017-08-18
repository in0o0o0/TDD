import math
import sys
import re

def atsign_checker(splitted_data):
    return splitted_data[-2] != ''

def split_address(address, character):
    return address.split(character)

def find_last_at(address):
    return address.rfind('@')

def split_domain_local(address, split_number):
    return address[:split_number], address[split_number + 1:]

def domain_checker_d1(address):
    return re.match(r"^[a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+$",address)

def domain_checker_d2(address):
    return not address.startswith(".")

def domain_checker_d3(address):
    return not address.endswith(".")

def domain_checker_d4(splied_domain):
    return not '' in splied_domain


# def main():
#
#     split_number = find_last_at(address)
#     local, domain = split_domain_local(address, split_number)

    # domain_part(domain)
    # splied_domain = split_address(address, ".")
    # domain_checker_d4(splied_domain)


    # local_part(local)




'''
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

'''
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
