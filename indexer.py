from algosdk.v2client import indexer
import json
from clients import *

indxc = get_indexer_client()
response = indxc.search_transactions() 

# Pretty Printing JSON string
print(json.dumps(response, indent=2, sort_keys=True))

# /indexer/python/account_info.py

response = indxc.account_info(address='XANGAZGP3WCFMZNPPWE4TTSFRBAPFI7IPQSLGAGXVX3ASK4XK3EDIK4BNI')
print("Account Info: " + json.dumps(response, indent=2, sort_keys=True))