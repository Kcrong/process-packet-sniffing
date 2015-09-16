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
    try:
        if port_list[len(port_list) - 1] == '*':
            port_list.pop()
    except IndexError:
        print "PROCESS ISN'T USING PORT! OR, WRONG PID"
        exit(1)
    return port_list


def make_command(interface, port_list, file_name):
    comm = "sudo tcpdump -i %s -w %s " % (interface, file_name)

    for port in port_list:
        comm += "port %s or " % port

    comm = comm[:len(comm) - 4]

    return comm


if __name__ == "__main__":
    DEBUG = False

    # get pid from argv
    try:
        pid = sys.argv[1]
        interface = sys.argv[2]
        file_name = sys.argv[3]
    except IndexError:
        print '%s [PID] [INTERFACE] [FILE_NAME]' % sys.argv[0]
        print "Ex) %s 1234 eth0 packets.pcap" % sys.argv[0]
        if DEBUG is True:
            pid = 6191
            interface = "wlan0"
        else:
            exit()
    port_list = get_process_port(pid)

    comm = make_command(interface, port_list, file_name)

    import os

    os.system(comm)

# sudo tcpdump -w packets.pcap -i eth0 port 8080
# sudo tcpdump -i wlan0 -w asdf.pcap port 8080 or port 80
