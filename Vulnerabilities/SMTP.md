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

# telnet
```
telnet [server IP] 25
helo me
mail from: testfrom@coolexample.com
rcpt to: testrcpt@coolexample.com
```

If your relays are closed, you will receive an error that you cannot connect, similar to the following error:
```
Trying IP address...
Connected to mail.myserver.com.
Escape character is '^]'.
...
554 : Relay access denied
```
