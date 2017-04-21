import base64
import json
import urllib2
import sys

pid = int(sys.argv[1])

charmap = { 
"0":"A",
"1":"B",
"2":"C",
"3":"D",
"4":"E",
"5":"F",
"6":"G",
"7":"H",
"8":"I",
"9":"J",
"10":"K",
"11":"L",
"12":"M",
"13":"N",
"14":"O",
"15":"P",
"16":"Q",
"17":"R",
"18":"S",
"19":"T",
"20":"U",
"21":"V",
"22":"W",
"23":"X",
"24":"Y",
"25":"Z",
"26":"a",
"27":"b",
"28":"c",
"29":"d",
"30":"e",
"31":"f",
"32":"g",
"33":"h",
"34":"i",
"35":"j",
"36":"k",
"37":"l",
"38":"m",
"39":"n",
"40":"o",
"41":"p",
"42":"q",
"43":"r",
"44":"s",
"45":"t",
"46":"u",
"47":"v",
"48":"w",
"49":"x",
"50":"y",
"51":"z",
"52":"0",
"53":"1",
"54":"2",
"55":"3",
"56":"4",
"57":"5",
"58":"6",
"59":"7",
"60":"8",
"61":"9",
"62":"-",
"63":"_"}

def b102b64(b10):
  b64 = []
  while b10 > 0:
    b64.append(b10 % 64)
    b10 = b10 / 64
  return b64

def id2code(media_id):
  b64 = b102b64(media_id)
  shortcode = ''
  for item in b64:
    shortcode = (charmap[str(item)]) + shortcode
  
  return shortcode

def generateUrl(media_id):
  shortcode = id2code(media_id)
  url = 'https://api.instagram.com/oembed/?url=http://instagram.com/p/' + shortcode
  rsp = json.loads(urllib2.urlopen(url).read())
  return rsp['thumbnail_url']

print id2code(pid)
print generateUrl(pid)
# print generateUrl(1467331451728886737)