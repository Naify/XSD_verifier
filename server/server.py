#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import cgi
import cgitb
import lxml
from lxml import etree


cgitb.enable()
# Извлечение данных о запросе
form_data = cgi.FieldStorage()
xml_data = form_data.getvalue('xml')
xsd_data = form_data.getvalue('xsd')
'''
	Первый вариант
	Напрямую в парсер - premature end of script
'''
# xsd_data = ('''
# <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
 # <xsd:element name="a" type="xsd:integer"/>
# </xsd:schema> ''')
# xml_data = "<a>5</a>"

print "Content-Type: text/html\r\n\r"
try:
	schema_root = etree.XML(xsd_data)
	schema = etree.XMLSchema(schema_root)
	parser = etree.XMLParser(schema = schema)
	root = etree.fromstring(xml_data, parser)

	if root :
		print 'Valid!'
	else:
		print 'Invalid!'

except:
	print 'Invalid!'
	

'''
	Второй вариант
	Сохранить присланные xml и xsd файлы на диск, потом отрыть и пропарсить...
'''
# # Запись прихоящей схемы в фаил
# xsd_file = open("schema.xsd","w")
# xsd_file.write(xsd_data)
# xsd_file.close()
# # Чтение схемы из файла
# xsd_file = open ('schema.xsd','r')
# # Парсинг схемы
# xmlschema_doc = etree.parse(xsd_file)
# xmlschema = etree.XMLSchema(xmlschema_doc)
# xsd_file.close()
# # Запись приходящего xml файла на диск
# xml_file = open('document.xml','w')
# xml_file.write(xml_data)
# xml_file.close()
# # Чтение xml файла 
# xml_file = open ('document.xml')
# # Парсинг XML и валидация 
# doc = etree.parse(xml_file)
# if not xmlschema(doc):
	# print "Content-Type: text/plain\r\n\r"
	# print "Invalid!"
# else: 
	# print "Content-Type: text/plain\r\n\r"
	# print "Valid!"
# xml_file.close()

sys.exit(0)