# Nmaps to run at the start

## Scan Remote - Ryan:
nmap -sV -sC -p22,5800,5900,5901,3389,1723,5631 --open -oA remote_initial -iL <RANGE_FILE>

## Scan Databases - Nahid:
nmap -sV -sC -p1433,1521,1526,3306,523 --open -oA database_initial -iL <RANGE_FILE>

## FTP & Telnet - DJ:
nmap -sV -sC --script ftp-anon,banner -p20,21,23 --open -oA ftp_telnet_initial -iL <RANGE_FILE>

## SMB - Colbert:
nmap -sV -sC --script=smb<code>&amp;</code> -p445,139 --open -oA smb_initial -iL <RANGE_FILE>

## Web - Nick:
nmap -sV -v -sC -p80,443,8080,8081,8443 --open -oA web_initial -iL <RANGE_FILE>

## Top 1000:
nmap -sV -sC -v --top-ports 1000 --open -oA top1000 -iL <RANGE_FILE>

## All-cleanup:
nmap -sV -v -sC -p- --open -oA theIp_top1000 <ONE_IP>

## Parser:
Take the results and use this python script to get a neatly formatted csv
**https://github.com/laconicwolf/Nmap-Scan-to-CSV**
Run the script using:
```
python3 nmap_xml_parser.py -f INPUT_RESULTS.xml -csv OUTPUT_RESULTS.csv
```
