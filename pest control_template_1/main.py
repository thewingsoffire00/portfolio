from flask import *
from admin import admin
from public import public
from customer import customer
from staff import staff
from courier import courier
790000790000
app=Flask(__name__)
app.secret_key="hai"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(staff,url_prefix='/staff')
app.register_blueprint(customer,url_prefix='/customer')
app.register_blueprint(courier,url_prefix='/courier')

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")


app.run(debug=True,port=5355)