import webbrowser
import argparse
import requests
import logging

parser = argparse.ArgumentParser(description='Enter your credentials')

parser.add_argument('Username', type=str, help='Username for bitly API')
parser.add_argument('Password', type=str, help='Password for bitly API')

args = parser.parse_args()

auth_res = requests.post('https://api-ssl.bitly.com/oauth/access_token', auth=(args.Username,args.Password))

if auth_res.status_code ==200:
	access_token = auth_res.content.decode()
	print("Access token worked", access_token)
else:
	logging.error("Did not get Access token, exiting...")
	exit()

