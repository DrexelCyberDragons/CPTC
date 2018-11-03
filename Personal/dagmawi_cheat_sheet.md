# To-Dos
## On Arrival Checklist (before attacking)

    1) Do you all the required tools installed ( ../Tools.md ) 
    2) Did you find the relevant pages
        - Google docs
        - Google mail
        
    4) Setup the Google drive
        - Download the zip from here
        - Unzip and upload
        - Make sure all the .txt files are changed to google doc
    5) Inform anyone if there is anything particularly interesting about the machines

    
## Picking up a machine, before attacking
    1) Read up on the machine notes
    2) If no one has worked on it before, communicate and see if it is a common web app
    3) If it is running a new product, check the version number and do a little recon before attacking
    4) Update the machine notes as you move through

## During the attack
### General
    1) Run a full port scan on the machine, if ports look sus
        i) One without using UDP
        ii) One using UDP 
    2) Run nikto against the web app
    3) Do a dir traversal check
    wordlist - /usr/share/wordlists/dirbuster/directory-list-2....
        - dirb/gobuster

        ./dirb URL WORDLIST –o OUTFILE.txt
            Add –x if the site uses some kind of extension, ex (-x .html,php, etc...)
             
             	'n' -> Go to next directory.
              	'q' -> Stop scan. (Saving state for resume)
              	'r' -> Remaining scan stats.
             
            -N <nf_code>: Ignore responses with this HTTP code.
            Can use to ignore 301

    4) Search metasploit for services running, webapp names etc..
    5) Check the sources of the pages!
    6) Check the application storage, cookies etc..
    7) Check robots.txt, files/, media/ etc..
    8) if x-debug in header, might be vulnerable to running debug code...(install xdebug app ext in chrome )
    9) Upload file to klin using a nginx server, among other things
    10) 

### Upload files
    1) if extension black/whitelisted brute force available extensions to use (.config?)

### Text fields
    
    1) Check for sql injection
        - ' OR 1=1 --
        - run sqlmap
            - Blind (Totally blind injectoions)
        - if database write is possible (no need to sql inject?)
            - create new user to access resources
            - 

    2) Check for RCE
        - Through the UI ( try using $(code) )
        - Through BURP
        - If this seems likely, as for a second pair of eyes

    3) If there is a session id, it might be susceptible for session hijack
    4) Check for LFI/RFI
        - Check for usual files of interest(passwd, shadow)
        - Check for log files
        - Check for source code files ( Object Serialization/Change contet-type to text )
        - Check for SSH Keys
    5) 


### Login fields
    
    1) Run the checks for text fields
    2) Check for default credentials

### Post exploit
    
    1) Run whoami, get as much info on current user (role, group etc..)
    2) Try spawning a tty shell
    3) Do some manual enumeration before running the priv esc script
        - Try sudo sh
    4) Check for Source Control(.git, .svn)
        - commit log for interesting commits
    5) Check for SSH Keys
    6) If all else fails, run the priv esc script
    7)

## Dropping a machine, before moving off

    1) Try and get one other person's opinion on what you have  
    2) Make sure you have crossed off all possible enumerations
    3) Should you try brute forcing the machine? 
    4) Kill off any scanning/probing you have on that machine
    5) Update the machine notes and findings with work 
    6)


