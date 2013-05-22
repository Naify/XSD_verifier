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
	# Функция для комплексной валидации
	'''
		Первый вариант
		Текст xml и xsd в парсер сразу
	'''

	print "Content-Type: text/html\r\n\r"
	try:
		schema_root = etree.XML(xsd_data)
		# Создает из документа валидатор
		schema = etree.XMLSchema(schema_root)
		# Создает парсер против напротив которого идет валидация
		parser = etree.XMLParser(schema = schema)
		# Валидация с использованием заданного парсера
		root = etree.fromstring(xml_data, parser)
		print 'Validation succeed!'

	except Exception, e:
		# Вывод ошибки (код ошибки, строка, сама ошибка)
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
	# Функция для валидации только xml файла
	print "Content-Type: text/html\r\n\r"
	try:
		xmlcheck = etree.XML(xml_data)
		print 'XML Valid!'

	except Exception, e:
		log = e.error_log.filter_from_level(etree.ErrorLevels.ERROR)
		print log

def xsdval():
	# Функция для валидации только xsd файла
	print "Content-Type: text/html\r\n\r"
	try:
		xsdcheck = etree.XML(xsd_data)
		print 'XSD Valid!'

	except Exception, e:
		log = e.error_log.filter_from_level(etree.ErrorLevels.ERROR)
		print log


def func_select():
	if func == "comlpval":
		# Функция для комплексной валидации
		complval()
	elif func == "xmlval":
		# Функция для валидации только xml файла
		xmlval()
	elif func == "xsdval":
		# Функция для валидации только xsd файла
		xsdval()

func_select()

sys.exit(0)