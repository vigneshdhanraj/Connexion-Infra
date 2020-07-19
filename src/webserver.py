import os
import connexion
from flask import redirect
from connexion.exceptions import OAuthProblem

TOKEN_DB = {
    'owntokenneededcreatetoken': {
        'uid': 100
    }
}

USER_DB = {
    "username": "admin",
    "password": "admin"
}


def apikey_auth(token, required_scopes):
    info = TOKEN_DB.get(token, None)

    if not info:
        raise OAuthProblem('Invalid token')

    return info


def basic_auth(username, password, required_scopes=None):
    if username == USER_DB.get(
            'username') and password == USER_DB.get('password'):
        return {'sub': 'admin'}
    else:
        raise OAuthProblem('Invalid username or password')
    return None


app = connexion.FlaskApp(
    __name__, port=int(os.environ.get('PORT', 8080)), options={
        "swagger_ui": True}, server='tornado')
app.add_api('ci_api.yaml', base_path='/ci',
            validate_responses=True, strict_validation=True)


@app.route("/")
def index():
    return redirect("/ci/ui")
