from flask import Flask 
from flask_cors import CORS



#from dependencias import criar_access_token , verificar_token




app  = Flask(__name__)
CORS(app)
from views import *

if __name__ == "__main__":
    app.run(debug=True)

