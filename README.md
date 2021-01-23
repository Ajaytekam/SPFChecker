# SPFChecker :  

Checks weather the SPF record of a domain exists or not. It basicaly uses [SPF Query Tool](https://www.kitterman.com/spf/validate.html).  

**Usage :**   

```shell  
$ SPFCheck.py -d targetdomain.com
``` 

Example :  

```shell  
./SPFCheck.py -d hackerone.com

[+] SPF record exists and secured.
[+] Data written into '/tmp/spfRecord.html'
========| SPF Configuration |=========
v=spf1 include:_spf.google.com include:amazonses.com include:mail.zendesk.com include:spf.mail.intercom.io include:mktomail.com include:registrarmail.net -all
 v=spf1 include:_spf.google.com include:amazonses.com include:mail.zendesk.com include:spf.mail.intercom.io include:mktomail.com include:registrarmail.net -all  
```  

```shell  
 ./SPFCheck.py -d nmap.org

[!] The SPF Configuration is not secure.
[!] Domain is vulnerable to email spoofing.
[+] Data written into '/tmp/spfRecord.html'
========| SPF Configuration |=========
v=spf1 a mx ptr ip4:45.33.49.119 ip6:2600:3c01::f03c:91ff:fe98:ff4e ip6:2600:3c01:e000:3e6::6d4e:7061 include:_spf.google.com ~all
 v=spf1 a mx ptr ip4:45.33.49.119 ip6:2600:3c01::f03c:91ff:fe98:ff4e ip6:2600:3c01:e000:3e6::6d4e:7061 include:_spf.google.com ~all  
``` 

