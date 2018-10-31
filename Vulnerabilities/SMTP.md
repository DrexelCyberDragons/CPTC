# Telnet
First use telnet to get onto the box using:
```
telnet <IP/HOSTNAME> 25
```
If your relays are closed, you will receive an error that you cannot connect, similar to the following error:
```
Trying IP address...
Connected to mail.myserver.com.
Escape character is '^]'.
...
554 : Relay access denied
```

If the server does not require authentication then to view the commands you can do use:
```
ehlo <NAME_OF_MACHINE/IP>
```

If *vrfy* is shown by the ehlo command, then you can verify users on the machine using *vrfy <USERNAME>*

## Authentication
Run *ehlo <NAME_OF_MACHINE/IP>* If you do not see line like 250-AUTH ... line, then your server may not support authentication. Most likely you will see this when trying with telnet or openssl without startls.

For *admin@example.com* and *password*, generate base64 encoded string like below:
```
echo -ne '\0admin@example.com\0password' | base64
```
Please note use of *\0* before username and password. It must be used as it is. Also, use single-quotes to avoid escaping special characters in your password.

It will output a string like below:
```
AGFkbWluQGV4YW1wbGUuY29tAHBhc3N3b3Jk
```
Use above string with AUTH command:
```
AUTH PLAIN AGFkbWluQGV4YW1wbGUuY29tAHBhc3N3b3Jk
```
## SMTP Commands to send test email
Type/paste following commands 1-by-1. They are interactive and needs input.
```
ehlo example.com
mail from: admin@example.com
rcpt to: admin@other.com
data
quit
```

# Open-Relay Test with SWAKS
# swaks
Installation
```
sudo apt-get install swaks
```

### Open-relay
If your localhost cannot send mail, you can specify a reliable SMTP server using:
```
swaks --to user@example.com --server smtp.example.com
```

If `smtp.example.com` accepts your mail, a case of open-relay, your mail will be through. Or you will see error/reason for not sending mail in output.

### Sending a test mail using Gmail’s SMTP server
```
swaks -t user@example.com -s smtp.gmail.com:587 -tls -a LOGIN
```

Above will prompt your gmail username and password. Mail will be delivered from authenticated Gmail account. You can verify this by checking your Gmail’s sent folder! 😉

### Send EICAR Virus Test Email
Test a virus scanner using EICAR in an attachment.  Don’t show the message DATA part.
```
swaks -t user@example.com --attach --suppress-data < /path/to/eicar.txt
```

`--attach` switch can be used to specify attachment.
