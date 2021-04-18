import pyrebase

config={
	'apiKey': "<YOUT_KEY>",
    'authDomain': "<YOUR_DOMAIN>",
    'databaseURL': "https://gpat-91256.firebaseio.com",
    'projectId': "<ID>",
    'storageBucket': "<ID>",
    'messagingSenderId': "<ID>",
    'appId': "<APP_ID>"
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()
