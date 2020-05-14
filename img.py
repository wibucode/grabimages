# Copyright Wibucode
# ------------------
import requests, os, sys
from bs4 import BeautifulSoup as bs
os.system("clear")
print """
 __         __
/  \.-----./  \

\    -   -    /
 |   o   o   |	Grab Images
 \  .-'''-.  /	Author	: WibuCode
  '-\__Y__/-'	Github	: https://github.com/wibucode
     `---`

"""
url = raw_input("Url: ")
fn = raw_input("Nama Folder: ")
os.system("mkdir "+fn)
os.chdir(fn)
r = requests.get(url)
soup = bs(r.text, "html.parser")
tag = soup.find_all("img")
for img in tag:
	internal = img.get("src")
	if not "http" in internal:
		res = url+"/"+internal
		result = requests.get(res)
		img = res.split("/")[-1]
		print "Mendownload gambar "+img
                f = open(img, "wb")
                f.write(result.content)
                f.close()
	elif "http" in internal:
		res = internal
		result = requests.get(res)
		img = res.split("/")[-1]
		print "Mendownload gambar "+img
		f = open(img, "wb")
		f.write(result.content)
		f.close()
	else:
		print "Gambar tidak ditemukan"
pass
print "\nHasil download berada di folder "+fn
