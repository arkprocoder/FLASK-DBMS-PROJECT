from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='aneesrehmankhan'

# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hms'
db=SQLAlchemy(app)



# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))


# here we will pass endpoints and run the fuction
@app.route('/')
def index():
    return render_template('index.html')
    


@app.route('/doctors')
def doctors():
    return render_template('doctor.html')

@app.route('/patients')
def patient():
    return render_template('patient.html')


@app.route('/bookings')
def bookings():
    return render_template('booking.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('login.html')



@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'
    



app.run(debug=True)    