import firebase_admin
from firebase_admin import firestore
import json

# Application Default credentials are automatically created.
cred = firebase_admin.credentials.Certificate('cred.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

ref = db.collection('users').document('alovelace')
ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1815
})  # Set the data


# with open('transactions.txt') as f:
#     # Read each line in the file
#     for line in f:
#         # Parse the JSON data from the line
#         data = json.loads(line)

#         # Push the data to the database
#         db.set(data)
