# -*-coding:utf-8-*-

import sys


def get_process_port(pid):
    command = 'netstat -nap | grep '
    command += str(pid)

    import commands

    status, output = commands.getstatusoutput(command)

    addr_list = []

    for i in output.split(' '):
        if i.find(':') == -1:
            pass
        else:
            addr_list.append(i)

    # print addr_list.split(':')[1]
    port_list = []

    for i in addr_list:
        result = i.split(':')
        port_list.append(result[1])

    del addr_list
    return port_list

if __name__ == "__main__":
    try:
        pid = sys.argv[1]
    except IndexError:
        print 'Argv Error'
        exit()
    port_list = get_process_port(pid)

