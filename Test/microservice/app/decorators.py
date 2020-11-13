from functools import wraps                                                                                                                                                                                                                                                                                                                                    
from flask import session, jsonify

def requires_login():                                                                                                                                                                        
    def wrapper(f):                                                                                                                                                                          
        @wraps(f)                                                                                                                                                                            
        def wrapped(*args, **kwargs):                                                                                                                                                        
            if not 'user_name' in session:                                                                                                                                                   
                return jsonify({'code': 5})  
            return f(*args, **kwargs)                                                                                                                                                        
        return wrapped                                                                                                                                                                       
    return wrapper