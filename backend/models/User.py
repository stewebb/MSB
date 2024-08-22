from app import db
from werkzeug.security import generate_password_hash, check_password_hash

'''
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(63), unique=True, nullable=False)
    password = db.Column(db.String(63), nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'
'''


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(63), unique=True, nullable=False)
    password = db.Column(db.String(63), nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        #print(self.password)
        #print(generate_password_hash(password))
        return check_password_hash(self.password, password)