from flask import Flask, request
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)

CONFIG = {'AMQP_URI': 'pyamqp://localhost'}
 # Config contains the amqp url to indentify your messaging cluster

@app.route('/add_users', methods=['POST'])
def add_users():
        data = request.json
        token = request.headers.get('Authorization')
        with ClusterRpcProxy(CONFIG) as rpc:  
            # ClusterRpcProxy standalone proxy 
            # we can use ClusterRpcProxy block make RPC calls to any namekoh service 
            # from a non-nameko service
            response, status = rpc.user_service.add(data, token)
            #calling the add function from the adder_service
            return response, status

@app.route('/multiply_numbers', methods=['POST'])
def multiply_numbers():
        data = request.json
        token = request.headers.get('Authorization')
        with ClusterRpcProxy(CONFIG) as rpc:
            #calling the multiply function from the multiplier_service
            response, status = rpc.multiplier_service.multiply(data, token) 
            return response, status

@app.route('/login', methods=['POST'])
def login():
        data = request.json
        with ClusterRpcProxy(CONFIG) as rpc: 
            #calling the login function from the login_service
            response, status = rpc.auth_service.login(data)
            return response, status
 
 
# main driver function
if __name__ == '__main__':
    app.run()