# -*- coding: utf-8 -*-

import psycopg2
import requests
import os 

from datetime import datetime
from random import randint
from time import sleep

def processing(uc):
  url = 'https://viacep.com.br/ws/'+ uc +'/json/'

  response = requests.get(url)
  status   = response.status_code
  body     = ''

  if status == 200:
    body = response.text.replace('\n', '').replace('  ', ' ')
  
  error    = ('"erro": true' in body) or (status != 200)

  fileWrite.write(str(uc) + '; ' + str(status) + '; ' + str(body) + '; ' + str(error)+ "\n")

  print (response)

dir_path = os.path.dirname(os.path.realpath(__file__))

ucs = open(dir_path + '/' + 'ENTRADA.txt')

fileWrite = open(dir_path + '/' + "SAIDA.csv", "w")
fileWrite.write("UC; Status; Body; Error\n")

for uc in ucs:
  processing(uc.replace('\n', ''))

fileWrite.close()
print ('FIM')
