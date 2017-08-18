import math
import sys
import re

def atsign_checker(splitted_data):
    return len(splitted_data)>1 and splitted_data[-2] != ''

def split_address(address, character):
    return address.split(character)

def find_last_at(address):
    return address.rfind('@')

def split_domain_local(address, split_number):
    return address[:split_number], address[split_number + 1:]

def checker_d1(domain):
    return re.match(r"^[a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+$",domain)

def checker_d2(domain):
    return not domain.startswith(".")

def checker_d3(domain):
    return not domain.endswith(".")

def checker_d4(splied_domain):
    return not '' in splied_domain

def checker_d5(domain):
    return len(domain) > 0

def checker_lq1(local):
    return local.startswith('"')

def checker_lq2(local):
    return local.endswith('"')

def strip_double_quotation(local):
    return local[1:-1]

def checker_lq5(local):
    return len(local) >= 2

def output_boolean(boo):
    return 'ok' if boo else 'ng'


def main(io):

    addresses = io.input_data()
    result_list = []

    for address in addresses:

        split_number = find_last_at(address)
        local, domain = split_domain_local(address, split_number)

        splitted_domain = split_address(domain, ".")
        domain_boolean = all([checker_d1(domain), checker_d2(domain), checker_d3(domain),
                             checker_d4(splitted_domain), checker_d5(domain)])

        splitted_ld = split_address(local, ".")
        ld_boolean = all([checker_d1(local), checker_d2(local), checker_d3(local),
                         checker_d4(splitted_ld), checker_d5(local)])
        splitted_lq = strip_double_quotation(local)
        lq_boolean = all([checker_lq1(local), checker_lq2(local), checker_d1(splitted_lq), checker_lq5(local)])
        local_boolean = ld_boolean or lq_boolean

        splitted_data = split_address(address, '@')
        address_boolean = all([atsign_checker(splitted_data), domain_boolean, local_boolean])

        result_list.append(output_boolean(address_boolean))

    io.output_data(result_list)


class IO:
    def input_data(self):
        data = sys.stdin.readlines()
        return data

    def output_data(self,result):
        for x in result:
            print x





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
    main(io)
