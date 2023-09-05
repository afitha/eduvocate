from nameko.rpc import rpc, RpcProxy
from nameko_mongodb import MongoDatabase

class UserService:
    name = 'user_service'
    mongo = MongoDatabase()
    auth_service = RpcProxy('auth_service')
    #RpcProxy used to inter-communicate between the nameko services
    
    @rpc
    def add(self, data, token):
        username = data.get('username')
        password = data.get('password')

        print ('user:', username, 'password:',password, 'token:', token)
        
        verified = self.auth_service.verify_user(token)
        #calling the rpc function of auth_service
        
        if verified:
            
            users_collection = self.mongo.user_service.users
            result = users_collection.insert_one(data)
            
            return {"result": str(result.inserted_id) }, 200
        else:
            return "Unauthorized", 401
