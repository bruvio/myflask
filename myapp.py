from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from security_class import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# from db import db
from datetime import timedelta

# import unittest

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:///data.db"  # where to find the database
app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False  # sql alchemy has its own modification tracker
app.secret_key = "br1"
api = Api(app)


# config JWT to expire within half an hour
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=1800)
jwt = JWT(app, authenticate, identity)  # allows authentication of users /auth
# this will crate a new endpoint /auth
# when we run this endpoint this will create a username and password and send it over
# if username and password match with the one stored


# in postman we created the tests for the endpoint which are going to help
# in the design of the api
# we have created 5 endpoints

# get items - will give a list of the items
# get item<name> - will give the item uniquely identified by its name
# del item<name> - will delete the item uniquely identified by its name
# post item<name> - will create a new item identified by its name and it will fail if there is already an item with that name
# put item<name> - will create an item uniquely identified if the item does not exists. if the item exist it will update it.


# as per the endpoints we have created we need two resources:
# a list of items
# an item

api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(
    UserRegister, "/register"
)  # a post request to register will call the post method


@app.route("/")  # we are specifying the endopoint ##'http://www.google.com
def home():
    return "Hello, world!"


if __name__ == "__main__":

    db.init_app(app)
    app.run(port=3000, debug=True)  # enable debug
# if __name__ == "__main__":
#     ############# Add these lines #############
#     import xmlrunner
#
#     runner = xmlrunner.XMLTestRunner(output="test-reports")
#     unittest.main(testRunner=runner)
#     ###########################################
#     unittest.main()
