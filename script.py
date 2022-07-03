import webbrowser
import argparse
import requests
import logging
import sanic

parser = argparse.ArgumentParser(description='Enter your credentials')

parser.add_argument('Username', type=str, help='Username for bitly API')
parser.add_argument('Password', type=str, help='Password for bitly API')
parser.add_argument('url', type=str, help='Enter url you want to shorten')

args = parser.parse_args()

auth_res = requests.post('https://api-ssl.bitly.com/oauth/access_token', auth=(args.Username,args.Password))

if auth_res.status_code ==200:
	access_token = auth_res.content.decode()
	print('Access token worked', access_token)
else:
	logging.error('Did not get Access token, exiting...')
	exit()

headers = {'Authorization': f'Bearer {access_token}'}

# now we need to get the guid

group_res = requests.get('https://api-ssl.bitly.com/v4/groups', headers=headers)

if group_res.status_code == 200:
	groups_data = group_res.json()['groups'][0]
	guid = groups_data['guid']
else:
	logging.error('Cannot get GUID, exiting program...')
	exit()


url = args.url

shorten_res = requests.post('https://api-ssl.bitly.com/v4/shorten', json={"group_guid": guid, "long_url": url}, headers=headers)

if shorten_res.status_code == 200:
	link = shorten_res.json().get('link')
	print('Shortened URL', link)
else:
	logging.error("Didnt shorten URL")
	exit()