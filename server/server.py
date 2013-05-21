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
func = form_data.getvalue('func')

def complval():
	'''
		Первый вариант
		Текст xml и xsd в парсер сразу
	'''

	print "Content-Type: text/html\r\n\r"
	try:
		schema_root = etree.XML(xsd_data)
		schema = etree.XMLSchema(schema_root)
		parser = etree.XMLParser(schema = schema)
		root = etree.fromstring(xml_data, parser)
		print 'Valid!'

	except Exception, e:
		log = e.error_log.filter_from_level(etree.ErrorLevels.ERROR)
		print log
		
	'''
	Второй вариант
	Сохранить присланные xml и xsd файлы на диск, потом отрыть и пропарсить...
	
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
	'''

def xmlval():
	print "Content-Type: text/html\r\n\r"
	try:
		xmlcheck = etree.XML(xml_data)
		print 'Valid!'

	except Exception, e:
		log = e.error_log.filter_from_level(etree.ErrorLevels.ERROR)
		print log

def xsdval():
	print "Content-Type: text/html\r\n\r"
	try:
		xsdcheck = etree.XML(xsd_data)
		print 'Valid!'

	except Exception, e:
		log = e.error_log.filter_from_level(etree.ErrorLevels.ERROR)
		print log


def func_select():
	if func == "comlpval":
		complval()
	elif func == "xmlval":
		xmlval()
	elif func == "xsdval":
		xsdval()

func_select()

sys.exit(0)