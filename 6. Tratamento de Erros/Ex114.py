#Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:

    site = urllib.request.urlopen('https://www.pudim.com.br')
    
except:

    print(f'\033[31mO site Pudim não está acessível no momento!\033[m')

else:

    print(f'\033[32mConsegui acessar o site Pudim com sucesso!\033[m')    

