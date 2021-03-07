import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import base64
import json
import os
import tkinter as tk
import time
import subprocess
from selenium import webdriver
import threading
from time import sleep
import importlib




DEFAULT_OAUTH_URL = 'https://allegro.pl/auth/oauth'
DEFAULT_REDIRECT_URI = 'http://localhost:80'
CLIENT_ID = 'e53fed87464f450e8bd418455a20ddd2'
CLIENT_SECRET = 'YXXdGDioEfhLBSqcTFZKEuFOpQZpPNTlOqtuDqjtv83XxIsdujZK04lryDOTEaHR'
API_KEY = 'e53fed87464f450e8bd418455a20ddd2'

class Auth:

    
    def get_access_code(client_id, api_key, redirect_uri=DEFAULT_REDIRECT_URI, oauth_url=DEFAULT_OAUTH_URL):

        auth_url = '{}/authorize' \
                   '?response_type=code' \
                   '&client_id={}' \
                   '&api-key={}' \
                   '&redirect_uri={}'.format(oauth_url, client_id, api_key, redirect_uri)
         
        parsed_redirect_uri = requests.utils.urlparse(redirect_uri)

        server_address = parsed_redirect_uri.hostname, parsed_redirect_uri.port

        class AllegroAuthHandler(BaseHTTPRequestHandler):
            def __init__(self, request, address, server):
                super().__init__(request, address, server)

            def do_GET(self):
                self.send_response(200, 'OK')
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                self.server.path = self.path
                self.server.access_code = self.path.rsplit('?code=', 1)[-1]
  
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s -n --incognito'
        webbrowser.get(chrome_path).open_new(auth_url)
            
        httpd = HTTPServer(server_address, AllegroAuthHandler)
        

        httpd.handle_request()
        global access_code
        access_code = httpd.access_code
        return access_code

        httpd.server_close()

    def sign_in(client_id, client_secret, access_code, api_key=API_KEY, redirect_uri=DEFAULT_REDIRECT_URI, oauth_url=DEFAULT_OAUTH_URL):
        token_url = 'https://allegro.pl/auth/oauth/token'

        access_token_data = {'grant_type': 'authorization_code',
                             'code': access_code,
                             'api-key': api_key,
                             'redirect_uri': redirect_uri}
        response = requests.post(url=token_url,
                                 auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
                                 data=access_token_data)
        global sign1
        sign1 = response.json()
        return sign1
       
    def refresh_token(client_id, client_secret, refresh_token, api_key, redirect_uri=DEFAULT_REDIRECT_URI, oauth_url=DEFAULT_OAUTH_URL):
        token_url = 'https://allegro.pl/auth/oauth/token'

        access_token_data = {'grant_type': 'refresh_token',
                             'api-key':  api_key,
                             'refresh_token': refresh_token,
                             'redirect_uri': redirect_uri}
        response = requests.post(url=token_url,
                                 auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
                                 data=access_token_data)
        global sign2
        sign2 = response.json()
        return sign2

  
Auth.get_access_code(CLIENT_ID,API_KEY)
Auth.sign_in(CLIENT_ID,CLIENT_SECRET,access_code,API_KEY)
Auth.refresh_token(CLIENT_ID,CLIENT_SECRET,sign1['refresh_token'],API_KEY)


headers = {}
headers['charset'] = 'UTF-8'
headers['Accept-Language'] = 'pl-PL'
headers['Content-Type'] = 'application/vnd.allegro.public.v1+json'
headers['Api-Key'] = API_KEY
headers['Accept'] = 'application/vnd.allegro.public.v1+json'
headers['Authorization'] = "Bearer {}".format(sign2['access_token'])



with requests.Session() as session:
    session.headers.update(headers)

    response = session.get('https://api.allegro.pl/order/checkout-forms')
    responsee = session.get('https://api.allegro.pl/order/checkout-forms?limit=100&offset=100')
    responseee = session.get('https://api.allegro.pl/order/checkout-forms?limit=100&offset=200')
    responseee3 = session.get('https://api.allegro.pl/order/checkout-forms?limit=100&offset=300')
    responseee4 = session.get('https://api.allegro.pl/order/checkout-forms?limit=100&offset=400')
    responseee5 = session.get('https://api.allegro.pl/order/checkout-forms?limit=100&offset=500')


    
    wyswietl = response.json()
    wyswietl2 = responsee.json()
    wyswietl3 = responseee.json()
    wyswietl4 = responseee3.json()
    wyswietl5 = responseee4.json()
    wyswietl6 = responseee5.json()

 
    with open('jsons/data.json','w') as outfile:
        json.dump(wyswietl, outfile)

    with open('jsons/data2.json','w') as outfile2:
        json.dump(wyswietl2, outfile2)
    with open('jsons/data3.json','w') as outfile3:
        json.dump(wyswietl3,outfile3)
    with open('jsons/data4.json','w') as outfile4:
        json.dump(wyswietl4,outfile4)
    with open('jsons/data5.json','w') as outfile5:
        json.dump(wyswietl5,outfile5)
    with open('jsons/data6.json','w') as outfile64:
        json.dump(wyswietl6,outfile64)

    


headers = {}
headers['charset'] = 'UTF-8'
headers['Accept-Language'] = 'pl-PL'
headers['Content-Type'] = 'application/vnd.allegro.public.v1+json'
headers['Api-Key'] = API_KEY
headers['Accept'] = 'application/vnd.allegro.public.v1+json'
headers['Authorization'] = "Bearer {}".format(sign2['access_token'])

                                                                 
with requests.Session() as sesja:
    sesja.headers.update(headers)
    
    response = sesja.get('https://api.allegro.pl/payments/payment-operations?limit=100')
    responsee = sesja.get('https://api.allegro.pl/payments/payment-operations?limit=100&offset=100')
    response2 = sesja.get('https://api.allegro.pl/payments/payment-operations?limit=100&offset=200')
    response3 = sesja.get('https://api.allegro.pl/payments/payment-operations?limit=100&offset=300')
    response4= sesja.get('https://api.allegro.pl/payments/payment-operations?limit=100&offset=400')
    response5= sesja.get('https://api.allegro.pl/payments/payment-operations?limit=100&offset=500')
    wyswietl = response.json()
    wyswietl2 = responsee.json()
    wyswietl3 = response2.json()
    wyswietl4 = response3.json()
    wyswietl5 = response4.json()
    wyswietl6 = response5.json()

 
    with open('jsons_platnosci/data_platnosci.json','w') as outfile:
        json.dump(wyswietl, outfile)
        
    with open('jsons_platnosci/data_platnosci2.json','w') as outfile2:
        json.dump(wyswietl2, outfile2)


    with open('jsons_platnosci/data_platnosci3.json','w') as outfile3:   
        json.dump(wyswietl3, outfile3)

    with open('jsons_platnosci/data_platnosci4.json','w') as outfile4:   
        json.dump(wyswietl4, outfile4)

    with open('jsons_platnosci/data_platnosci5.json','w') as outfile44:   
        json.dump(wyswietl5, outfile44)
        


importlib.reload(requests)

