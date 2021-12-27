import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados["ip"]
hostname = dados["hostname"]
cidade = dados["city"]
regiao = dados["region"]
pais = dados["country"]
local = dados["loc"]
organizacao = dados["org"]
cep = dados["postal"]
horalocal = dados["timezone"]
leiame = dados["readme"]

print('Detalhes do IP externo:\n')
print('IP: {4}\nHostname: {5}\nPais: {2}\nRegião: {1}\nCidade: {3}\nCep: {7}\nlocalizacao: {6}\nOrganizacao: {0}\nHora Local: {8}\nLeia-me: {9}'
      .format(organizacao, regiao, pais, cidade, ip, hostname, local, cep, horalocal, leiame))

