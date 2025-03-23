from flask import current_app as app
from flask_security import auth_required

@app.route('/admin')
@auth_required('token')
def admin_home():
    return "<h1>this is admin <\h1>"\
    