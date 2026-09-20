from flask import Flask 
from flask_cors import CORS



#from dependencias import criar_access_token , verificar_token




app  = Flask(__name__)

from routes.auth import auth_users
from routes.users import users
app.register_blueprint(auth_users)
app.register_blueprint(users)

CORS(app,
     origins="http://127.0.0.1:5500",
     supports_credentials=True
     )

if __name__ == "__main__":
    app.run(debug=True)

