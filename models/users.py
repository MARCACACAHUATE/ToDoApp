from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(40), nullable = False, unique = True)
    password = db.Column(db.String(40), nullable = False)
    te_va_al_america = db.Column(db.String(10), nullable = True)