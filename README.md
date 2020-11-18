https://github.com/VaileyXO/Apache-Fragment

Language: Python 3

Others  : import re for re.findall, re.sub to collect url / domain / email and calculate the frequecies of each elements.

Hints   : line 34 customize domain

Sample apache: 

vailey.xxx.xxx.ac.uk:80 156.53.200.217 - - [08/May/2016:06:28:50 +0100] "GET / HTTP/1.1" 200 304 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4 (Applebot/0.1; +http://www.apple.com/go/applebot)"
vailey.xxx.xxx.ac.uk:80 156.53.200.217 - - [08/May/2016:06:29:02 +0100] "GET / HTTP/1.1" 200 304 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4 (Applebot/0.1; +http://www.apple.com/go/applebot)"

Sample output:

/////// URLs    ///////

1 .      'www.apple.com/go/applebot' : 2


/////// DOMAINS ///////

1 |      '80 156.53.200.217' : 2

/////// EMAILs  ///////

1 .      'vailey.xxx.xxx.ac.uk' : 2


URLS:  1        DOMAINS:  1     EMAILS:  1
