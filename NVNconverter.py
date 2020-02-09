#!/usr/bin/python

import sys
import re

f = open(sys.argv[1], 'r')
content = f.read()
content_new = re.sub(r'^(.*)WARNING(.*)$', r'', content, flags = re.M)
content_new2 = re.sub(r'^void(.*)$', r'', content_new, flags = re.M)
content_new3 = re.sub(r'^(.*)local_(.*)$', r'', content_new2, flags = re.M)
content_new4 = re.sub(r'  return(.*)', r'', content_new3, flags = re.M)
content_new5 = re.sub(r'  QWORD_', r'0x', content_new4, flags = re.M)
content_new5 = re.sub(r'  DWORD_', r'0x', content_new4, flags = re.M)
content_new6 = re.sub('= (.*),"', '', content_new5, flags = re.M)
content_new7 = re.sub(r'"(.*);', r'', content_new6, flags = re.M)
content_new8 = re.sub(r'([A-Za-z0-9]\w+)\ ([A-Za-z0-9]\w+)', r'\2 \1', content_new7, flags = re.M)
content_new9 = re.sub(r'{', r'', content_new8, flags = re.M)
content_new10 = re.sub(r'}', r'', content_new9, flags = re.M)
content_new11 = re.sub(r'return;', r'', content_new10, flags = re.M)
content_new12 = re.sub(r'  ', r'', content_new11, flags = re.M)
content_new13 = re.sub(r'^\r\n', r'', content_new12, flags = re.M)
content_new14 = re.sub(r'^\n', r'', content_new13, flags = re.M)
content_new15 = re.sub(r'^nvn', r'ptr_nvn', content_new14, flags = re.M)
f.close
n = open(sys.argv[1], 'w')
n.write(content_new15)
n.close