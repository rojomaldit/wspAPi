# Essentials programs for windows
# Python 3
# pip install selenium 
# ChromeDriver https://chromedriver.chromium.org/downloads, donde descargar cualquier version de chromedriver
# Libraries
import pdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import time
import threading
import math
import os

initial_number = 3571299999
quantity_numbers = 99999 # Aca estoy enviando los casi 100000mil mensajes
remaining_numbers = quantity_numbers+1

# numbers = [{"number": "+54 9 (351) 000-000"} or {"number": "+54 9 (3571) 00-000"}]
numbers = [{"number": f"+54 9 3571 {str(x)[4:6]}-{str(x)[6:10]}"} for x in range(initial_number, initial_number+quantity_numbers)]
print(numbers)

my_text = "*Este es un mensaje auto-dirigido de AutoSystems*.\n*Realizamos publicidad en cualquier red social, manejo automático de sistemas, envió y respuesta de mensajes automáticos.*\n*Para la comodidad del usuario!*"
text = "*Stuxnet MantenimientosPc*\nSe hacen formateos de PC, netbooks, notebooks y celulares.\nFormateo e Instalación de Windows, Linux, etc.\nInstalación de drivers.\nInstalación de programas básicos (Microsoft office, google, Avast, java, y mucho más).\nLimpieza de gabinetes, interiores de netbooks y notebooks.\nCambios de pasta térmica.\nTambién se realizan limpiezas de impresoras, contadoras de dinero, entre otras.\nPara más información dirigirse al contacto que se muestra en la tarjeta.\nComunicarse al número 3571611777"
my_text = my_text.split('\n')
text = text.split('\n')
is_logged = False


driver = webdriver.Chrome('./chromedriver.exe')  # Optional argument, if not specified will search path.


def worker(i, remaining_numbers):
	number = numbers[i]["number"]
	print('trabajando en el numero: ', number, 'faltan', remaining_numbers)
	url = 'https://web.whatsapp.com/send?phone=' + numbers[i]['number']
	driver.get(url)
	
	global is_logged
	if(not is_logged):
		is_logged = True
		sleep(5) # 5 segundos para pasar el loggin de wsp
	
	send_menssage = ''
	for i in range(0, 10):
		try:
			send_menssage = driver.find_elements_by_class_name('_3FRCZ.copyable-text.selectable-text')[1]
			break
		except:
			send_menssage = driver.find_elements_by_class_name('S7_rT.FV2Qy')
			if(len(send_menssage) > 0):
				print("Este numero no tiene cuenta de wsp")
				return False
			sleep(1)
				 
	for i in my_text:
		try:
			send_menssage.send_keys(i)
		except:
			print("Este numero no tiene cuenta de wsp")
			return False
		send_menssage.send_keys(Keys.SHIFT,'\n')

	send_button = driver.find_element_by_class_name('_1U1xa')
	send_button.click()

	sleep(1)

	# sending text msj
	for i in text:
		send_menssage.send_keys(i)
		send_menssage.send_keys(Keys.SHIFT,'\n')

	send_button = driver.find_element_by_class_name('_1U1xa')
	send_button.click()
	sleep(1)
	
	# sending img
	image_path=os.path.abspath('a.jpeg') # imagen a.jpeg en el root de este archivo
	driver.find_element_by_css_selector("span[data-icon='clip']").click();
	sleep(1)
	driver.find_element_by_css_selector("input[type='file']").send_keys(image_path);
	sleep(1)
	driver.find_element_by_css_selector("span[data-icon='send']").click();
	sleep(1)

	f = open("Cordoba-RioTercero.txt", "a")
	f.write(f"{number}")
	f.close()

	return True

medium_time = []

count = 0 # numero de contactos encontra2
for j in range(0, len(numbers)):
	st = time()
	if(worker(j, remaining_numbers)):
		count+=1
	remaining_numbers-=1
	et = time()
	print(et-st)
	medium_time.append(et - st)

print(sum(medium_time)/len(medium_time))

driver.close()
print("La cantidad de numeros encontrados fue:", count, "de:", quantity_numbers+1)
