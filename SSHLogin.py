#!/usr/bin/python3

import pexpect


prompt = ['# ', '\$', '>>> ', '> ']


def send_commands(connection, command):
    connection.sendline(command)
    connection.expect(prompt)
    print(connection.before, end='\n')


def connect(host, user, password):
    ssh_prompt = "Are you sure you want to"         # Expected
    conn = "ssh " + user + "@" + host + ' -p 22'
    child = pexpect.spawn(conn)
    ret = child.expect([pexpect.TIMEOUT, ssh_prompt, '[P|p]assword: '])

    if ret == 0:
        print("[-] Error Connecting...!")
        return
    if ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print("[-] Error Connecting...!")
            return

    child.sendline(password)
    child.expect(prompt)

    return child


def main():
    host = input("Enter the host IP: ")
    user = input("Enter the user name: ")
    password = input("Enter the password: ")

    child = connect(host, user, password)
    send_commands(child, 'ls -al')


main()
