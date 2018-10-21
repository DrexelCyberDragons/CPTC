# TCPDUMP crash course

Generously taken from https://hackertarget.com/tcpdump-examples/




## Simple

    sudo tcpdump -i eth0 -nn -s0 -v port 80

nn : A single (n) will not resolve hostnames. A double (nn) will not resolve hostnames or ports.

-s0 : Snap length, is the size of the packet to capture. -s0 will set the size to unlimited

Adding -A to the command line will have the output include the ascii strings from the capture

## Capture all plain text pwds

    sudo tcpdump port http or port ftp or port smtp or port imap or port pop3 or port telnet -l -A | egrep -i -B5 'pass=|pwd=|log=|login=|user=|username=|pw=|passw=|passwd=|password=|pass:|user:|username:|password:|login:|pass |user '







