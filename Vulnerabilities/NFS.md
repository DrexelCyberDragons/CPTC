# NFS
If nfs is accessable on a machine you ccan look for mountable directories using:
```
nmap -sV --script=nfs-showmount <target>
```

Then you can mouse the drive using:
# mount XXX.XXX.XXX.XXX:<THE/LOCATION> /mnt/<SOME_NAME>/
