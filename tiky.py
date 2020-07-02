import requests, os, base64, sys, argparse, warnings, threading, time, multiprocessing, re, webbrowser,traceback,json
from colorama import init, Fore, Style
from tik_data.color import Color
from tik_data.license import get_info,get_hr
from halo import Halo
from urllib.parse import quote_plus as urlencode

warnings.filterwarnings("ignore")

def art(donate=False):
	if donate:
		exec(base64.b64decode("cHJpbnQoIiIpCnByaW50KCIiKQpwcmludChDb2xvcigiIOKWkeKWkeKWhOKWhOKWiOKWgOKWgOKWgOKWgOKWgOKWiOKWhOKWhOKWkSAiKS55ZWxsb3cgKyAiICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiArIENvbG9yKCIgICAgXyAgXyAgICAgICAgICAiKS5yZWQpCnByaW50KENvbG9yKCIg4paE4paI4paA4paR4paR4paE4paR4paE4paR4paR4paR4paR4paA4paI4paEIikueWVsbG93ICsgIiAgICAgICAgICBEb25hdGUgdG8gRGV4eSEgICAgICAgICAgICAgICIgKyBDb2xvcigiICAvYCBcLyBgXF8gIF8gICAgIikucmVkKQpwcmludChDb2xvcigiIOKWiOKWkeKWkeKWkeKWgOKWiOKWgOKWgOKWgOKWgOKWhOKWkeKWkeKWkeKWiCIpLnllbGxvdyArICIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiICsgQ29sb3IoIiAgXCAgICAgL2AgXC8gYFwgICIpLnJlZCkKcHJpbnQoQ29sb3IoIiDilojilpHilpHilpHilpHilojiloTiloTiloTiloTiloDilpHilpHilpHilogiKS55ZWxsb3cgKyAiICAgMUJEUWRyTDVjc3o4NEpLNVp2aDJYZW5IVzRZZkpKY01hWCAgIiArIENvbG9yKCIgICAnLiAgLlwgICAgICAvICAiKS5yZWQpCnByaW50KENvbG9yKCIg4paI4paR4paR4paR4paR4paI4paR4paR4paR4paR4paI4paR4paR4paR4paIIikueWVsbG93ICsgIiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIgKyBDb2xvcigiICAgICBcLyAgJy4gIC4nICAgIikucmVkKQpwcmludChDb2xvcigiIOKWgOKWiOKWhOKWkeKWgOKWgOKWiOKWgOKWiOKWgOKWkeKWkeKWhOKWiOKWgCIpLnllbGxvdyArICIgICAgICAgICAgICAgIFRoYW5rcyEgICAgICAgICAgICAgICAgICAiICsgQ29sb3IoIiAgICAgICAgICAgXC8gICAgICIpLnJlZCkKcHJpbnQoQ29sb3IoIiDilpHilpHiloDiloDilojiloTiloTiloTiloTiloTilojiloDiloDilpHilpEiKS55ZWxsb3cgKyAiICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiArIENvbG9yKCIgICAgICAgICAgICAgICAgICAiKS5yZWQpCnByaW50KCIiKQpwcmludCgiIik="))
		return False
	exec(base64.b64decode("cHJpbnQoIiIpCnByaW50KEZvcmUuUkVEICsgIiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIgKyBGb3JlLllFTExPVyArICIgOyAgICAgICAgIikKcHJpbnQoRm9yZS5SRUQgKyAiICAgICAgX19fX18gIF8gIF8gICAgICAgICAgICAgIiArIEZvcmUuWUVMTE9XICsgIiA7OyAgICAgICAiKQpwcmludChGb3JlLlJFRCArICIgICAgIHxfICAgX3woXyl8IHwgICAgICAgICAgICAiICsgRm9yZS5ZRUxMT1cgKyAiIDsnOy4gICAgICIpCnByaW50KEZvcmUuUkVEICsgIiAgICAgICB8IHwgICBfIHwgfCBfXyBfICAgXyAgICIgKyBGb3JlLllFTExPVyArICIgOyAgOzsgICAgIikKcHJpbnQoRm9yZS5SRUQgKyAiICAgICAgIHwgfCAgfCB8fCB8LyAvfCB8IHwgfCAgIiArIEZvcmUuWUVMTE9XICsgIiA7ICAgOzsgICAiKQpwcmludChGb3JlLlJFRCArICIgICAgICAgfCB8ICB8IHx8ICAgPCB8IHxffCB8ICAiICsgRm9yZS5ZRUxMT1cgKyAiIDsgICAgOzsgICIpCnByaW50KEZvcmUuUkVEICsgIiAgICAgICBcXy8gIHxffHxffFxfXCBcX18sIHwgICIgKyBGb3JlLllFTExPVyArICIgOyAgICA7OyAgIikKcHJpbnQoRm9yZS5SRUQgKyAiICAgICAgICAgICAgICAgICAgICAgICBfXy8gfCAgIiArIEZvcmUuWUVMTE9XICsgIiA7ICAgOycgICAiKQpwcmludChGb3JlLlJFRCArICIgIFRpa1RvayBBdXRvQ2xhaW1lciAgfF9fXy8gICAiICsgRm9yZS5ZRUxMT1cgKyAiIDsgICcgICAgICIpCnByaW50KEZvcmUuUkVEICsgIiAgICAgICAgICAgICAgICAgICAgICAgICIgKyBGb3JlLllFTExPVyArICIgICw7OzssOyAgIikKcHJpbnQoRm9yZS5SRUQgKyAiICBCeSBEZXh5IChkZXh5Izc3NDIpICAgIiArIEZvcmUuWUVMTE9XICsgIiAgOzs7Ozs7ICAiKQpwcmludChGb3JlLlJFRCArICIgICAgICAgICAgICAgICAgICAgICAgICAiICsgRm9yZS5ZRUxMT1cgKyAiICBgOzs7OycgICIpCnByaW50KCIiKQ=="))
	print(Style.RESET_ALL)
	
def get_args():
	args_c = {
		"log":False,
		"proxy":False,
		"threads":False,
		"proxy": False,
		"clear": False,
	}
	parser = argparse.ArgumentParser()
	parser.add_argument("-c","--clear",help="Clear all session data.",action="store_true")
	parser.add_argument("-l", "--log", help="Debug Mode. Show errors.",action="store_true")
	parser.add_argument("-d", "--donate", help="Parse dexy BTC address and send a donation.",action="store_true")
	parser.add_argument("-th", "--threads", help="Use multithreading.",action="store_true")
	parser.add_argument("-p", "--proxy", help="HTTPs proxy for debugging requests.")
	args = parser.parse_args()

	if args.clear:
		args_c['clear'] = True
		TikTokClaimer(clear=True)
		sys.exit(0)
	if args.proxy:
		args_c['proxy'] = args.proxy
	if args.donate:
		art(donate=True)
		sys.exit(0)
	if args.log:
		args_c['log'] = True
	if args.threads:
		args_c['threads'] = True
	return args_c
	
def thread_claim(new_username,tiktok,eventp):
	try:
		while True:	
			claim_request = tiktok.claim(new_username)
			if not "username is taken" in claim_request['message']:
				eventp.set()
				print(Color("\r\n[!]").alert() + " " + claim_request['message'].capitalize() + "\r\n")
				break
	except KeyboardInterrupt:
		eventp.set()
		pass
	except:
		eventp.set()
		pass
def parse_usernames(data):
	test = "^[A-Za-z0-9\_\.]+$"
	if(data.endswith(".txt")):
		with open(data,'r') as f:
			return list(set(filter(None,[u.strip() if re.match(test,u.strip()) else None for u in f.readlines()])))
	if("," in data):
		return list(set(filter(None,[u.strip() if re.match(test,u.strip()) else None for u in data.split(',')])))
	if(re.match(test,data.strip())):
		return [data.strip()]
	return []

	
def main():
	global spinner, tiktok
	try:
		init()
		get_hr()
		argsconfig = get_args()
		art()
		spinner = Halo(text='Loading', spinner='dots')
		tiktok = TikTokClaimer(log=argsconfig['log'],proxy=argsconfig['proxy'])
		tries = 0
		usernames = []
		
		#Load Usernames
		while len(usernames) == 0:
			try:
				get_usernames = str(input(Color("[$]").yellow + " Username(s) to Claim: "))
				usernames = parse_usernames(get_usernames)
			except:
				pass
			if len(usernames) == 0:
				print(Color("[?] To load usernames:").blue + "\r\n 1. You can type the username list (.txt) filename.\r\n 2. You can type a single username.\r\n 3. You can type uernames sperated by comma ','.\r\n")
		
		#Info
		print(Color("[+] ").green + "Loaded " + str(len(usernames)) + " username" + ("s" if len(usernames) > 1 else "") + ".")
		print(Color("[?] Press 'Ctrl C' to exit.",u=1).cyan)
		
		#Threading
		if argsconfig['threads']:
			if(len(usernames) > 1):
				print(Color("[!] Multi-Threading doesn't work with multiple usernames.").yellow)
				raise("Multi-Threading Error")
			eventp = multiprocessing.Event()
			threads = MultiThread(thread_claim,[usernames[0],tiktok])
			threads.create(3)
			threads.start()		
			spinner.start("Attempting to claim " + str(usernames[0]))	
			threads.kill_daemon()
		#Normal Mode
		else:		
			while True:
				for username in usernames:
					spinner.start("Attempting to claim " + str(username))
					claim_request = tiktok.claim(username)
					if not "username is taken" in claim_request['message']:
						spinner.stop()
						print(Color("[!] ").alert() + claim_request['message'])
						usernames.remove(username)
						break
				if(len(usernames) == 0):
					print("[*] Finished.")
					break
		
	except KeyboardInterrupt:
		if argsconfig['threads']:
			threads.kill()
		spinner.stop()
	except Exception as e:
		if argsconfig['log']:
			traceback.print_exc(file=sys.stdout)
			print(e)
		if argsconfig['threads']:
			threads.kill()
		print("\r\n[-] Exiting.")
		spinner.stop()
		sys.exit(0)
			
class MultiThread:
	def __init__(self, function, args,eventp=False):
		self.target = function
		self.threads = []
		self.eventp = eventp
		self.args = args
		if not self.eventp:
			self.eventp = multiprocessing.Event()
		self.args.append(self.eventp)
			
	def create(self,n):
		for i in range(0,n):
			t = multiprocessing.Process(target=self.target,args=self.args)
			self.threads.append(t)
		return self.threads
	
	def start(self):
		spinner.start("Starting threads")
		for thread in self.threads:
			time.sleep(2)
			thread.start()
		spinner.stop()
	def join(self):
		for thread in self.threads:
			time.sleep(2)
			thread.join()
		spinner.stop()
	def kill_daemon(self):
		while True:
			time.sleep(1)
			if self.eventp.is_set():
				raise Exception("Killing threads.")
	def kill(self):
		print("\r\n[~] Trying to kill threads.")
		for pr in self.threads:
			pr.terminate()
		
	
class TikTokClaimer():
	
	def __init__(self,clear=False,proxy=False,log=False):
		self.endpoint = "https://tiktokapi.xyz/api"
		self.captcha = "https://tiktokapi.xyz/captcha"
		self.data = os.path.dirname(os.path.realpath(__file__)) + "/tik_data/"
		self.password = False
		self.clear = clear
		self.apikey = False
		self.proxy = proxy
		self.log = log
		self.did_captcha = 0
		self.s = requests.Session()
		self.s.verify = False
		if self.proxy:
			self.proxy = {'http':'http://' + self.proxy, 'https':'https://' + self.proxy}
			self.s.proxies = self.proxy
		
		self.get_key()
		if not self.clear:
			self.login()
		else:
			self.clear_all()
					
	def login(self,username=False,password=False):
			self.username = str(input("[+] TikTok Login Email or Username: ")) if not username else username
			try:
				with open(self.data + self.username + ".sess","r") as f:
					self.account = f.read().strip()
				print("[+] Session Loaded.")
			except:
				self.password = str(input("[+] TikTok Login Password: ")) if not password else password
				self.account = self._login()
				with open(self.data + self.username + ".sess","w") as f:
					f.write(self.account)
	def _login(self):
		spinner.start("Logging in")
		try:
			params = {
				"username": self.username,
				"password": self.password,
				"key": self.apikey
			}
			login = self.s.get(self.endpoint + "/login",params=params).json()
			spinner.stop()
			if login['status'] == 'error':
				print(Color("[-] ").red + login['message'])
				return self.login()
			if login['status'] == 'data' and login['type'] == 'captcha' and self.did_captcha == 0:
				self.did_captcha = 1
				
				captcha_solve_link = login['data']['link']
				
				'''
					Open browser here w/ captcha_solve_link as url
				'''
				webbrowser.open(captcha_solve_link,new=2)
				done = input("Press enter after you have solved the captcha...")
				return self._login() #We call login again, since now the user session should be already in db.
			if login['status'] == 'success':
				print(Color("[+] ").green + "Logged in.")
				return login['message']['account_key']
		except Exception as e:
			spinner.stop()
			if self.log:
				print(e)
				traceback.print_exc(file=sys.stdout)

			print(Color("[-] ").red + "Something went wrong.")
		self.did_captcha = 0
		return self.login()
		
	def claim(self,new_username):
		if not self.account:
			self.login()

		params = {
			'account': self.account,
			'new_username': new_username,
			'key': self.apikey
		}
			
		try:
			send_req = self.s.get(self.endpoint + "/claim",params=params).json()
			return send_req
		except Exception as e:
			if self.log:
				print(e)
				traceback.print_exc(file=sys.stdout)
			return {"message":"Something went wrong."}
		
		
	def get_key(self):
		try:
			with open(self.data + "apikey.sess","r") as f:
				self.apikey = str(f.read())
		except:
			while True:
				self.apikey = str(input("[!] Enter your API Key: "))
				if self.check_key(self.apikey):
					break
			with open(self.data + "apikey.sess","w") as f:
				f.write(self.apikey)
	
	def check_key(self,key):
		spinner.start("Checking key")
		params = {
			'key': str(key),
			'machine': get_info()['hex'],
		}
		check = self.s.get(self.endpoint + "/key",params=params).json()
		spinner.stop()
		return check['status'] == "success"
	
	def cleard(self,account):
		req = self.s.get(self.endpoint + "/remove?account=" + account + "&key=" + self.apikey)
		return True
		
	def clear_all(self):
		try:	
			for session in os.listdir(self.data):
				if session.endswith(".sess"):
					session_name = os.path.join(self.data, session)
					if session != "apikey.sess":
						try:
							with open(session_name,"r") as f:
								self.account = str(f.read())
							#print(self.account)
							self.cleard(self.account)
						except Exception as e:
							print(e)
							pass
					os.remove(session_name)
		except:
			print("[-] Clearing sessions failed.")
			return False
		print("[+] All data cleared.")
		
	
if __name__ == "__main__":
	sys.exit(main())
	