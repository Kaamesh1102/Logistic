from flask import current_app as app,jsonify
from flask_security import auth_required,roles_required

@app.route('/admin')
@auth_required('token')
@roles_required('admin')
def admin_home():
    return {
        "message" : "admin logged in"
    }
    
@app.route('/user')
def user_home():
    return jsonify({
        
    })