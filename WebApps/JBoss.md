# JBoss
Once you identify a web service as JBoss you can then look for the endpoint: 
```
/jmx-console 
```

Under the jboss.system heading, you should find a link for the *MainDeployer* service. If it exists exploiting the server will be relatively easily 
Using the *MainDeployer* service take advantage of is the *deploy()*. 
Host a malicious **WAR** file and set the **java.net.url** to the war files location. 
Then execute commands using: 
```
Address:8080/cmd/cmd.jsp?cmd=whoami
```
