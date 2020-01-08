from myapp import app 
from db import db
db.init_app(app)
@app.before_first_request 
def create_tables():
    # from models.user import UserModel
    # from models.item import ItemModel

    db.create_all() # sql alchemy creates the tables that it sees and this works through imports
    # admin = UserModel("bruno", "asdf")
    # test = ItemModel("test", "10.99",'1')
    # desk = ItemModel("desk", "11.99",'1')
    # db.session.add(test)
    # db.session.add(desk)
    
    # db.session.add(admin)
    # db.session.commit()