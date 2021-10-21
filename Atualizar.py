# Import modules

import os
import time
import shutil
import urllib.request
from tqdm import tqdm


versao = urllib.request.urlopen('https://raw.githubusercontent.com/manteguinha/teste/main/Versao/Versao.txt').read().decode('utf8').splitlines()[0] # Link do RAW do arquivo contendo a versao
changelogs = urllib.request.urlopen('https://raw.githubusercontent.com/manteguinha/teste/main/Versao/Changelogs.txt').read().decode('utf8') # Link do RAW do arquivo contendo o changlog
link = 'https://github.com/manteguinha/teste/archive/refs/heads/main.zip'
path = 'teste.zip' 


# Checking version Telegram-RAT

if versao == '0.2.0':
	print('Nenhuma nova versão encontrada.')
	input()
else:
	if os.path.exists('Atualizado para a versão ' + versao):
		print('A atualização foi instalada.')
		input()
	else:
		print('Atualização disponível.')
		print('\n=-==-==-==-==-==-==-=')
		print('Changelogs:\n' + changelogs)
		print('=-==-==-==-==-==-==-=\n')
		print('Atualizar agora? s/n\n')
		if input().lower() == 's'.lower():
			print('\nBaixando atualização...')
			urllib.request.urlretrieve(link, path)
			print('Descompactando arquivo...')
			shutil.unpack_archive(path, 'Atualizado para a versão ' + versao)
			os.remove(path)
			for i in tqdm(range(100)):
    				time.sleep(0.1)
			print('A atualização foi instalada, aperte qualquer tecla para sair.')
			input()
