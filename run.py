from algosdk.v2client import algod, indexer
from algosdk import account, mnemonic, kmd
import json, base64

acc = 'KZEAJKQIADHBKGI6QWDNZJAEW2NDBJ7E7YHU5RQRQJEIHS5PXYNNWGAW3Y'
algod_address = 'http://localhost:4001'
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)
account_info = algod_client.account_info(acc)
print(account_info.get('amount'))

# # build transaction
# from algosdk.future import transaction
# from algosdk import constants


# private_key = 'ZDzrfI1glNSif0nkN08vn+siwmZ1DDUdBRy859lGEG3iygPIUGOi5QKStNqiSg4lFkXaaNfJRA1eMTAIZVT6w'.encode()

# params = algod_client.suggested_params()
# # comment out the next two (2) lines to use suggested fees
# params.flat_fee = True
# params.fee = constants.MIN_TXN_FEE 
# receiver = "7M77BCG4YUW6WUFIJFOP7PFMYFPHA3OTVGSGSYXE332ASMGV47PBFV4NII"
# note = "Hello World".encode()
# amount = 1000000
# unsigned_txn = transaction.PaymentTxn(acc, params, receiver, amount, None, note)
# signed_tx = unsigned_txn.sign(private_key)
# txid = algod_client.send_transaction(signed_tx)

# myindexer = indexer.IndexerClient(indexer_token="", indexer_address="http://localhost:4001")
# response = myindexer.search_transactions() 

# # Pretty Printing JSON string
# print(json.dumps(response, indent=2, sort_keys=True))

# # /indexer/python/account_info.py

# response = myindexer.account_info(address=acc)
# print("Account Info: " + json.dumps(response, indent=2, sort_keys=True))