# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''

import re

"""
def parse_sh_ip_int_br(file):
    '''
    This function takes a name of file wich contains result of command 'show ip int br'
    as an argument and returns tuple with this information:
    * Interface
    * IP-Address
    * Status
    * Protocol
    '''
    f = open(file).read().split('\n')
    final_list = []
    for line in f:
        match = re.search('(\S+\d)\s+(\S+) .+ (\S+)\s+(\S+$)', line)
        if match:
            intf, ip, stat, prot = match.groups()
            final_list.append((intf, ip, stat, prot))
    return final_list
"""

'''
def parse_sh_ip_int_br(filename):
    final_list = []
    with open(filename, 'r') as f:
        for line in f:
            match = re.search(r'(\S+\d) +(\S+) +\w+ +\w+ +(up|down|administratively down) +(up|down)\n', line)
            if match:
                final_list.append(match.groups())
    return final_list
'''

'''
def parse_sh_ip_int_br(file):
    with open(file, 'r') as f:
        regex = r'(\S+\d) +(\S+) +\w+ +\w+ +(up|down|administratively down) +(up|down)\n'
        final_list = [m.groups() for m in re.finditer(regex, f.read())]
    return final_list
'''

'''
def parse_sh_ip_int_br(file):
    with open(file, 'r') as f:
        #regex = r'(\S+\d) +(\S+) +\w+ +\w+ +(up|down|administratively down) +(up|down)\n'
        #final_list = re.findall(regex, f.read())
    return final_list
'''


def parse_sh_ip_int_br(file):
    with open(file, 'r') as f:
        final_list = re.findall(r'(\S+\d) +(\S+) +\w+ +\w+ +(up|down|administratively down) +(up|down)\n', f.read())
    return final_list


if __name__=='__main__':
    from pprint import pprint
    pprint(parse_sh_ip_int_br('/home/vagrant/GitHub/pynet_rep/exercises/15_module_re/sh_ip_int_br.txt'))