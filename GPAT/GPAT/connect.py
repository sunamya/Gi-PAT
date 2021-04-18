import pyrebase

config={
	'apiKey': "AIzaSyBfokMPiCPofK6osSCixsOdGsoX3-AhX4g",
    'authDomain': "gpat-91256.firebaseapp.com",
    'databaseURL': "https://gpat-91256.firebaseio.com",
    'projectId': "gpat-91256",
    'storageBucket': "gpat-91256.appspot.com",
    'messagingSenderId': "1007096476481",
    'appId': "1:1007096476481:web:b07441e59cd7394e"
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()