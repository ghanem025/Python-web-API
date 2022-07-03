import webbrowser
import argparse

parser = argparse.ArgumentParser(description='Enter your credentials')

parser.add_argument('Username', type=str, help='Username for bitly API')
parser.add_argument('Password', type=str, help='Password for bitly API')
parser.add_argument('token', type=str, help='Access token')

args = parser.parse_args()

auth_res = request.post(args.token, auth(args.Username,Password))
