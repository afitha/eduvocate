# from flask import request
from nameko.rpc import rpc, RpcProxy
from nameko.extensions import DependencyProvider
from nameko_mongodb import MongoDatabase

class AuthService:
    name = 'auth_service' 
    #defining the name of the service
    #by using this name we can call any rpc function in this service
    mongo = MongoDatabase()

    @rpc
    def login(self, data):
        username = data.get('username')
        password = data.get('password')
        #verify the  username and password if its correct then return the authtoken
        #we can use the jwt to encode the data and generate the authtoken
        users_collection = self.mongo.user_service.users
        user = users_collection.find_one(data)
        print('user', user)
        if username == user['username'] and password == user['password']:
            return "random_auth_token", 200
        else:
            return 'Not authenticated', 401
    
    @rpc  
    #defining it as the RPC function so that it can be called from other services 
    def verify_user(self, token):   
        #verify the data from the auth_token, if its correct then return the True
        #we can use the jwt to decode the auth_token
        if token == 'random_auth_token':
            return True
        else:
            return False

    @rpc    
    def create_user(self, user_data):
        users_collection = self.mongo.db.users
        result = users_collection.insert_one(user_data)
        return result.inserted_id
        