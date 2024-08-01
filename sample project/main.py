from flask import Flask
from public import public
app=Flask(__name__)
app.register_blueprint(public)
app.run(debug=True,port=5077)