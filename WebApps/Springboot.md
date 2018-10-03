# Springboot

If you see a page with **Whitelabel Error Page** or an icon of a leaf as the icon of the tab, it could be springboot with vulnerable endpoints open.

A vulnerable endpoint is **/heapdump** from the web root.  This will cause a heapdump of the program.  The heapdump couuld contain credentials that you cna use to access a server or service.

Run *strings* on the heapdump and look for credentials.
