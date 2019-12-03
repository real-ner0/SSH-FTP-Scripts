***** VIEW IN RAW *****
#SSH-FTP-Scripts
Tried some automation on SSH and FTP.

Usages:

#1. SSHLogin.py
  Simply takes host IP, username and password as the input and runs "ls -al" command on the server and prints the output.
  I'm still working on it to add more functionality and make it more useful.
  
  root@kali:~# python3 SSHLogin.py
  
  Enter the host IP: 8.8.8.8
  Enter the user name: username
  Enter the password: password
  
  total 32
  drwxr-xr-x 4 root root 4096 Dec  3 18:29 .
  drwxr-xr-x 7 root root 4096 Dec  3 12:11 ..
  -rwxr-xr-x 1 root root  939 Dec  2 16:16 FTP.py
  drwxr-xr-x 3 root root 4096 Dec  2 16:48 .idea
  -rwxr-xr-x 1 root root   92 Dec  2 16:01 pass.txt
  -rwxr-xr-x 1 root root 1478 Dec  2 15:02 SSHBrute.py
  -rwxrwxrwx 1 root root 1089 Dec  3 18:24 SSHLogin.py
  drwxr-xr-x 5 root root 4096 Dec  2 14:05 venv


---------------------------------------------------------------------------------------------------------------------------------


#2. SSHBrute.py
  Uses a pass.txt file to brute the SSH login. The send_commands function isn't that good, still on it.
  
   root@kali:~# python3 SSHLogin.py
  
  Enter the host IP: 8.8.8.8
  Enter the username: username
  
  [-] Wrong Password: 11111
  [-] Wrong Password: abc
  [-] Wrong Password: abcd
  [-] Wrong Password: abc123
  [-] Wrong Password: abcd123
  [+] Password Found. Login Successful: 123456Seven
  
  
  -------------------------------------------------------------------------------------------------------------------------------
  
  
  #3. FTP.py
    Again, a FTP Brute Forcer using a pass.txt file.
    
    root@kali:~# python3 FTP.py
    
    [*] Enter the IP Address: 8.8.8.8
    [*] Enter the path of Password File: pass.txt
    [*] Trying: user/abcd
    [*] Trying: admin/admin
    [*] Trying: john/p4ssw0rd
    [*] Trying: msfadmin/msfadmin
    [+] Login Succeeded with msfadmin/msfadmin
    
    
---------------------------------------------------------------------------------------------------------------------------------
