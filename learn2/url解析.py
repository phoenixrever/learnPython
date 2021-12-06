# coding: utf-8
import urllib.parse

url = "http://www.example.org/jj/JJ903FC012/?ido=35.6880477934067&keido=139.862920249812"
o = urllib.parse .urlparse(url)

# params= urllib.parse.parse_qs(o.query, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&')
params= urllib.parse.parse_qs(o.query)

print(params.get('ido')[0])
print(params.get('keido')[0])
