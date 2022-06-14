from flask import request, jsonify
from models import User

# decorator for checking auth of a request 
def check_auth(func):

    if request.method=='POST':
        api_key = request.headers.get('api_key')

        if api_key is None:
            return jsonify({'auth_error':'expected api_key'})
        
        user = User.query.filter_by(api_key=api_key).first()
        
        if user is None:
            return jsonify({'auth_error':'invalid api_key passed'})
        
        return func(user)
    return jsonify({'method not allowed':"The method is not allowed for the requested URL."})
