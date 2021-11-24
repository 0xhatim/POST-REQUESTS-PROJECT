
from pro import db
from pro.model import User
db.create_all()

user_1 = User(username="admin",password="123123")
db.session.add(user_1)
db.session.commit()