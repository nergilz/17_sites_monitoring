## Sites Monitoring Utility

---
The script to check the status of our sites

### Discription

+ Test: the server responds to the request with the status of HTTP 200
+ Test: the domain name paid for a 30 days or more
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

### Start script with your parameters
```bash
python3 check_sites_health.py --path example.txt --days 500
``` 

### Example result
```bash
https://github.com; status: True; domain_check_payment: True ; date_to: 2020-10-09 18:20:50
https://devman.org; status: True; domain_check_payment: False ; date_to: 2018-08-28 11:49:42
http://www.jhkgjhkgjhgk.com; status: None; domain_check_payment: None ; date_to: False
https://python-scripts.com; status: True; domain_check_payment: False ; date_to: 2018-09-06 20:18:03
https://google.com; status: True; domain_check_payment: True ; date_to: 2020-09-14 04:00:00
http://www.telegram.com; status: False; domain_check_payment: True ; date_to: 2021-07-25 04:00:00
https://habr.com; status: True; domain_check_payment: False ; date_to: 2019-03-11 17:04:56
https://pypi.org; status: True; domain_check_payment: False ; date_to: 2018-07-24 15:13:23
```

### For get help
```bash
python3 check_sites_health.py --help
```

### Requirements

```bash
Python ver 3.5 (or higher)
```

---

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
