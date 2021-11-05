# UPDATE : 19 February 2021
# https://blacknetid.pw
# github.com/zlaxtert
# Recode Only Makes You a Loser
# I'M ALONE
# Chat Me @Alone_code404 (Telegram)
# Follow Me @zlaxtert (Instagram)
# I'm a coder KENTANG
# IZROIL MY FRIEND FOREVER

import requests, socks, socket, os, shutil
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor

try: shutil.rmtree(
    'get_proxy/__pycache__'
  )
except: pass

proxy_list = []
valid_proxy = []

def prox():
  print('''
\n\033[94m UPDATE 19 February 2021
\n\033[93m
  ___ ___   _____  ___   __
 | _ \ _ \ / _ \ \/ | \ / /
 |  _/   /| (_) >  < \ V / 
 |_| |_|_\ \___/_/\_\ |_| \033[96m2021 
                          
\033[94m[1]\033[0m Auto Get the proxy \033[93mHTTP/HTTPS\033[0m From \033[92mBLACKNETID
\033[94m[2]\033[0m Auto Get the proxy \033[95mSSL\033[0m From \033[92mBLACKNETID
\033[94m[3]\033[0m Auto Get the proxy \033[94mUSA \033[0mSSL From \033[92mBLACKNETID
\033[94m[4]\033[0m Auto Get the proxy \033[91mID \033[0mSSL From \033[92mBLACKNETID
\033[94m[5]\033[0m Auto Get the proxy \033[92mELITE \033[0mSSL From \033[92mBLACKNETID
\033[94m[6]\033[0m Auto Get the proxy \033[96mANONYMOUS \033[0mSSL From \033[92mBLACKNETID
\033[94m[7]\033[0m Auto Get the proxy \033[93mTRANSPARENT \033[0mSSL From \033[92mBLACKNETID
\033[94m[8]\033[0m Auto Get the proxy \033[95mSGP \033[0mSSL From \033[92mBLACKNETID
\033[94m[9]\033[0m Auto Get the proxy \033[93mHTTP Req 2\033[0m From \033[92mBLACKNETID
\033[94m[10]\033[0m Auto Get the proxy \033[92mTH \033[0mSSL From \033[92mBLACKNETID
\033[94m[11]\033[0m Auto Get the proxy \033[96mIN \033[0mSSL From \033[92mBLACKNETID
\033[94m[12]\033[0m Auto Get the proxy \033[95mDE \033[0mSSL From \033[92mBLACKNETID
\033[94m[55] \033[0mHTTPS FROM \033[92mFILE\n
\033[94m UPDATE 19 February 2021
\033[93m
  ___  ___   ___ _  _____ _____ 
 / __|/ _ \ / __| |/ / __|_   _|
 \__ \ (_) | (__| ' <| _|  | |  
 |___/\___/ \___|_|\_\___| |_|\033[96m2021 
\n\033[90m[99]\033[0m Auto Get the SOCKS5 \033[0mSSL From \033[92mBLACKNETID
\033[90m[88]\033[0m Auto Get the SOCKS4 \033[0mSSL From \033[92mBLACKNETID
\033[90m[77]\033[0m Auto Get the SOCKS5 \033[0mSSL From \033[92mWEB-SOCKS5
\033[90m[66] \033[0mSOCKS5 FROM \033[92mFILE
\033[90m[44] \033[0mSOCKS4 FROM \033[92mFILE
  ''')
  ask = int(
    input(
      '\033[94m[?]\033[0m Number? : '
    )
  )
  if ask == 1:
    return prox_bnet_https(
    )
  elif ask == 2:
    return prox_bnet_ssl(
    )
  elif ask == 3:
    return prox_bnet_usa(
    )
  elif ask == 4:
    return prox_bnet_id(
    )
  elif ask == 5:
    return prox_bnet_elite(
    )
  elif ask == 6:
    return prox_bnet_anon(
    )
  elif ask == 7:
    return prox_bnet_trans(
    )
  elif ask == 8:
    return prox_bnet_sg(
    )
  elif ask == 9:
    return prox_bnet_http2(
    )
  elif ask == 10:
    return prox_bnet_th(
    )
  elif ask == 11:
    return prox_bnet_in(
    )
  elif ask == 12:
    return prox_bnet_de(
    )
  elif ask == 77:
    return prox_bnet_soket(
    )
  elif ask == 99:
    return prox_bnet_sok5(
    )
  elif ask == 88:
    return prox_bnet_sok4(
    )
  elif ask == 55:
    return http_file(
    )
  elif ask == 66:
    return sok_file(
    )
  elif ask == 44:
    return sok4_file(
    )
  else:
    exit(
      '\n\033[94m[!]\033[0m \033[91mNummber not found [Go to the hell bro]!\033[0m'
    )

def proxy_checker(prox):
  try:
    global valid_proxy
    if requests.get(
       'http://ip.ml.youngjoygame.com:30220/myip',
          verify=False,
          proxies=prox,
          timeout=10
        ).status_code == 200:
      valid_proxy.append(
        prox
      )
    print(
      end='\r\033[94m[+]\033[0m Searching \033[92m(%s)\033[0m proxy valid.'%(
        len(
          valid_proxy
        )
      ),
      flush=True
    )
  except: pass

def prox_bnet_https():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/https.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
  
def prox_bnet_ssl():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/ssl.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
  
def prox_bnet_usa():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/usa.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
  
def prox_bnet_id():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/id.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
  
def prox_bnet_elite():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/elite.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
def prox_bnet_anon():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/anon.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
def prox_bnet_trans():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/trans.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
  
def prox_bnet_sg():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/sg.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
 
def prox_bnet_http2():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/http2.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )

def prox_bnet_th():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/th.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip()
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=100
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )

def prox_bnet_in():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/india.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip()
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=100
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
  
def prox_bnet_de():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/de.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip()
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=100
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
def prox_bnet_sok5():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/sok5.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'socks5://'+e.strip(),
      'https':'socks5://'+e.strip()
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=20
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
def prox_bnet_soket():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://socks-proxy.net/',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'socks5://'+e.strip(),
      'https':'socks5://'+e.strip()
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=20
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
def prox_bnet_sok4():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://blacknetid.pw/tools/allin1/proxy/admin/sok4.php',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'socks4://'+e.strip(),
      'https':'socks4://'+e.strip()
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
def sok_file():
  print(
    '\n[!] Delim Proxy (ip:port)'
  )
  list = input(
    '[+] List proxy (ex: proxy.txt) : '
  )
  if os.path.exists(
    list
  ):
    for data in open(
      list,
      'r',
      encoding='utf-8'
    ).readlines(
      ):
      prox = data.strip(
      ).split(
        ':'
      )
      try:
        if prox[0] and prox[1]:
          proxy_list.append({
            'http': 'socks5://'+data.strip(),
            'https': 'socks5://'+data.strip(),
          })
      except: pass
    if len(
      proxy_list
    ) != 0:
      print(
        '[+] Total (%s) proxy' %(
          str(
            len(
              proxy_list
            )
          )
        )
      )
      print(
        '[+] Searching Proxy'
      )
      with ThreadPoolExecutor(
        max_workers=20
      ) as thread:
        [
          thread.submit(
            proxy_checker,(
              prox
            )
          ) for prox in proxy_list
        ]
      if len(
        valid_proxy
      ) != 0:
        print(
          '\n'
        )
        return valid_proxy
      else: exit(
        '[+] Sorry, Proxy Not Found . Try Again '
      )
    else: exit(
      '[!] Sorry, Proxy Not Found '
    )
  else: exit(
    '[!] File Not Found "{0}"'.format(
      list
    )
  )
def http_file():
  print(
    '\n[!] Delim Proxy (ip:port)'
  )
  list = input(
    '[+] List proxy (ex: proxy.txt) : '
  )
  if os.path.exists(
    list
  ):
    for data in open(
      list,
      'r',
      encoding='utf-8'
    ).readlines(
      ):
      prox = data.strip(
      ).split(
        ':'
      )
      try:
        if prox[0] and prox[1]:
          proxy_list.append({
            'http': 'http://'+data.strip(),
            'https': 'https://'+data.strip(),
          })
      except: pass
    if len(
      proxy_list
    ) != 0:
      print(
        '[+] Total (%s) proxy' %(
          str(
            len(
              proxy_list
            )
          )
        )
      )
      print(
        '[+] Searching Proxy'
      )
      with ThreadPoolExecutor(
        max_workers=20
      ) as thread:
        [
          thread.submit(
            proxy_checker,(
              prox
            )
          ) for prox in proxy_list
        ]
      if len(
        valid_proxy
      ) != 0:
        print(
          '\n'
        )
        return valid_proxy
      else: exit(
        '[+] Sorry, Proxy Not Found . Try Again '
      )
    else: exit(
      '[!] Sorry, Proxy Not Found '
    )
  else: exit(
    '[!] File Not Found "{0}"'.format(
      list
    )
  )
def sok4_file():
  print(
    '\n[!] Delim Proxy (ip:port)'
  )
  list = input(
    '[+] List proxy (ex: proxy.txt) : '
  )
  if os.path.exists(
    list
  ):
    for data in open(
      list,
      'r',
      encoding='utf-8'
    ).readlines(
      ):
      prox = data.strip(
      ).split(
        ':'
      )
      try:
        if prox[0] and prox[1]:
          proxy_list.append({
            'http': 'socks4://'+data.strip(),
            'https': 'socks4://'+data.strip(),
          })
      except: pass
    if len(
      proxy_list
    ) != 0:
      print(
        '[+] Total (%s) proxy' %(
          str(
            len(
              proxy_list
            )
          )
        )
      )
      print(
        '[+] Searching Proxy'
      )
      with ThreadPoolExecutor(
        max_workers=20
      ) as thread:
        [
          thread.submit(
            proxy_checker,(
              prox
            )
          ) for prox in proxy_list
        ]
      if len(
        valid_proxy
      ) != 0:
        print(
          '\n'
        )
        return valid_proxy
      else: exit(
        '[+] Sorry, Proxy Not Found . Try Again '
      )
    else: exit(
      '[!] Sorry, Proxy Not Found '
    )
  else: exit(
    '[!] File Not Found "{0}"'.format(
      list
    )
  )