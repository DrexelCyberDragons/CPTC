# Anonymous FTP

If nmap returns an anonymous ftp server then you can connect to it using:
```
ftp anonymous@IP_ADDRESS
```

## Download files
Before downloading a file, we should set the local FTP file download directory by using 'lcd' command:
```
lcd /home/user/yourdirectoryname
```
If you dont specify the download directory, the file will be downloaded to the current directory where you were at the time you started the FTP session.
Now, we can use the command 'get' command to download a file, the usage is:
```
get file
```
To download several files we can use wildcards. In this example, I will download all files with the .xls file extension.
```
mget *.xls
```

Use wget in this manner (m for mirroring):
```
wget -m ftp://username:password@ip.of.old.host
```
If your username or password contains special characters, you may need to use the format:
```
wget -m --user=username --password=password ftp://ip.of.old.host
```

## Upload files
We can upload files that are in the local directory where we made the FTP connection.
To upload a file, we can use 'put' command.
```
put file
```
When the file that you want to upload is not in the local directory, you can use the absolute path starting with "/" as well:
```
put /path/file
```
To upload several files we can use the mput command similar to the mget example from above:
```
mput *.xls
```
