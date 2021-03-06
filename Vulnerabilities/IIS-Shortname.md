# IIS-ShortName-Scanner

```
https://github.com/irsdl/IIS-ShortName-Scanner
```

Examples:
```
- Example 0 (to see if the target is vulnerable):
 java -jar iis_shortname_scanner.jar http://example.com/folder/

- Example 1 (uses no thread - very slow):
 java -jar iis_shortname_scanner.jar 2 0 http://example.com/folder/new%20folder/

- Example 2 (uses 20 threads - recommended):
 java -jar iis_shortname_scanner.jar 2 20 http://example.com/folder/new%20folder/

- Example 3 (saves output in a text file):
 java -jar iis_shortname_scanner.jar 0 20 http://example.com/folder/new%20folder/ > c:\results.txt

- Example 4 (bypasses IIS basic authentication):
 java -jar iis_shortname_scanner.jar 2 20 http://example.com/folder/AuthNeeded:$I30:$Index_Allocation/

- Example 5 (using a new config file):
 java -jar iis_shortname_scanner.jar 2 20 http://example.com/folder/ newconfig.xml 
 
- Example 6 (scanning multiple targets using a linux box):
 ./multi_targets.sh scope.txt 1
```
