#!/usr/bin/pytohn3
from bs4 import BeautifulSoup
import requests
import hashlib


def request_get():
	r = requests.get(url = url)
	return r


def parse_text(r):
	soup = BeautifulSoup(r.text,"html.parser")
	return soup.find("h3").text


def hash_text(h):
	return hashlib.md5(h.encode()).hexdigest()


def send_hash(md5_hashed, cookies):
	params = { 'hash': md5_hashed}
	cookie = {'PHPSESSID': cookies[10:36]}	

	return requests.post(url, cookies = cookie, data = params)


url = "http://134.122.109.72:30364/"

r = request_get()
cookie = r.headers['Set-Cookie']
print(cookie)

value_pre_hash = parse_text(r)
md5_hashed = hash_text(value_pre_hash)
print("Hash a enviar: {}".format(md5_hashed))

resp = send_hash(md5_hashed, cookie)
print(resp.headers)
print(resp.text)
