## Sites Monitoring Utility

---
The script to check the status of our sites

### Discription

+ Test: the server responds to the request with the status of HTTP 200
+ Test: the domain name paid for a month or more
+ You need a library [requests](http://docs.python-requests.org/en/master/user/quickstart/)
+ and library [python-whois](https://pypi.org/project/python-whois/)
+ It is recommended to use [virtualenv](https://docs.python.org/3/library/venv.html) 
+ File name with urls for check: "urls.txt" 


### How to install requests and pyton-whois
```bash
pip install -r requirements.txt
```

### Start script example

```bash
python3 check_sites_health.py
```

### Start script with your file for check
```bash
python3 check_sites_health.py --path "path to file"
``` 

### Example result
```bash
https://github.com, status: True, domain payment > month: True, date to: 2020 10 09
https://devman.org, status: True, domain payment > month: True, date to: 2018 08 28
https://python-scripts.com, status: True, domain payment > month: True, date to: 2018 09 06
https://toster.ru, status: True, domain payment > month: True, date to: 2018 08 08
https://google.com, status: True, domain payment > month: True, date to: 2020 09 14
https://habr.com, status: True, domain payment > month: True, date to: 2019 03 11
https://pypi.org; status: True; domain_payment_>_month: True; date to: 2018-07-24
```

### Example result with errors
```bash
https://toster.ru, status: True, domain payment > month: True, date to: 2018 08 08
 ERROR WHOIS response: https://pypi.org; error: [Errno 104] Connection reset by peer
https://google.com, status: True, domain payment > month: True, date to: 2020 09 14
https://habr.com, status: True, domain payment > month: True, date to: 2019 03 11
 ERROR https://pypi.org; socket timeout: timed out
```

### Requirements

```bash
Python ver 3.5 (or higher)
```

---

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
