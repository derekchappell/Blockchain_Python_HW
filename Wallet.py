import subprocess
import json
import os
import web3
from bit import wif_to_key
from constants import *

command = './derive -g --mnemonic="black auto prosper select dust spirit multiply father until cabbage plastic crush" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)

pkey = keys[0]['privkey']
if pkey:
    print('success')

option = 0
while option != 0:
    option = int(input('''
        1. Get Blance in BTC
        2. Get Blance in USD
        3. Send Funds
        4. Close
        '''))
    pkey = keys[0]['privkey']
    key = wif_to_key(pkey)
    if option == 1:
        print(key.get_balance('btc'))
    elif option == 2:
        print(key.balance_as('usd'))