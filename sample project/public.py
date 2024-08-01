from flask import*
from database import*
public=Blueprint('public',__name__)
@public.route('/')
def home():
   return render_template('home.html')
@public.route('/login',methods=['get','post'])
def login():
	if 'login' in request.form:
		u=request.form['uname']
		s=request.form['pword']
 	return render_template('login.html')
@public.route('/register',methods=['get','post'])
def register():
	if 'register'in request.form:
		f=request.form['fname']
		l=request.form['lname']
		a=request.form['age1']
		x=request.form['t1']
		p=request.form['place']
		e=request.form['email']
		u=request.form['uname']
		s=request.form['pword']
		d="insert into login values(null,'%s','%s','user')"%(u,s)
		h=insert(d)
		i="insert into register values(null,'%s','%s','%s','%s','%s','%s','%s')"%(h,f,l,a,x,p,e)
		insert(i)
	return render_template('register.html')
