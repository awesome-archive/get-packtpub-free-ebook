# get-packtpub-free-ebook
get your packtpub free ebook easily
![screenshot](https://github.com/a4m/get-packtpub-free-ebook/raw/master/screenshot-for-script.png)

## why do I write this script

Packtpub offers [freelearning ebook](https://www.packtpub.com/packt/offers/free-learning)  every day. I often forget to check ,which makes me kind of sad . So I write this script to do this job.

## how to use

1 .  You need to install the dependencies . As the script use `Python3`,so you need to run the following command in terminal
```bash
sudo pip3 install bs4 requests
```

2 .  I will never provide my account , so you need to use you own email and password by changing the script at line 8 & 9. 
``` python3
EMAIL = 'ENTER YOUR EMAIL HERE'
PASSWORD = 'ENTER YOUR PASSWORD HERE'
```
If you don't have a packtpub account , you may [register at here](https://www.packtpub.com/register).

3 . remember to run the script with `Python3`
``` bash
python3 get_free_ebook_from_packtpub.py
```

## others
what about using `crontab` to make it even more convinient ?
