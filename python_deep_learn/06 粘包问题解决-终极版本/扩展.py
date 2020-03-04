import struct
import json


header_dict = {
	'filename' : 'a.txt',
	'md5' : 'xxxfxx',
	'total_size' : 33333333333333333333333333333333333333
}
header_json = json.dumps(header_dict)
print(header_json, type(header_json))
header_bytes = header_json.encode('utf-8')
# print(header_bytes)
print(len(header_bytes))

struct.pack('i', len(header_bytes))
