#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import cgi
import cgitb
import lxml

cgitb.enable()
# Извлечение данных о запросе
form_data = cgi.FieldStorage()
file_data = form_data.getvalue('xml')

# Извлечение полей запроса
#action = data.getvalue("action") 

# def answer():
	# fp =open('some/file','wb')
	# fp.write(file_data)
	# fp.close()

#sys.stderr.write(file_data)

print "Content-Type: text/xml"
print
print file_data

# answer()

# schema_root = etree.XML('''\
# ...   <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
# ...     <xsd:element name="a" type="xsd:integer"/>
# ...   </xsd:schema>
# ... ''')
# schema = etree.XMLSchema(schema_root)
# parser = etree.XMLParser(schema = schema)
# root = etree.fromstring("<a>5</a>", parser)

sys.exit(0)