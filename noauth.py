from flask import Flask, request, jsonify, redirect
import os
from urllib.parse import urlencode

app = Flask(__name__)

@app.route('/')
def index():
    return """
<h1>nOAuth: a Mock OAuth Server you shouldn't ever use in production</h1>
"""

@app.route('/authorize', methods=["GET"])
def authorize():
    if ("redirect_uri" not in request.args) or ("state" not in request.args):
        return "Need redirect_uri and state parameters"
    
    redirect_uri = request.args["redirect_uri"]
    state = request.args["state"]
    return f"""
<h1>You're not running this in production, are you?</h1>
<img src="https://media.tenor.com/Rj0tlPRW080AAAAC/curb-your-enthusiasm-larry-david.gif" />
<br><br>
<form method="post" action="">
<input type="hidden" name="state" value="{state}">
<input type="hidden" name="redirect_uri" value="{redirect_uri}">
email: <input type="text" name="email" autofocus>
<input type="submit">
</form>"""

@app.route('/authorize', methods=["POST"])
def authorize_post():
    redirect_uri = request.form["redirect_uri"]
    params = urlencode({"state": request.form["state"], "code": request.form["email"]})
    return redirect(f"{redirect_uri}?{params}")

@app.route('/oauth/token', methods=["POST"])
def token():
    email = request.form["code"]
    return jsonify(
        access_token = email,
        token_type = "Bearer"
    )

@app.route('/userinfo')
def userinfo():
    email = request.headers['Authorization'].split(' ')[1]
    return jsonify(email=email.lower())

@app.route('/.well-known/openid-configuration')
def openid_configuration():
    """
    OpenID Connect Discovery endpoint
    Returns the OpenID Connect configuration for this mock server
    """
    # Get the base URL from the request
    base_url = request.url_root.rstrip('/')
    
    return jsonify({
        "issuer": base_url,
        "authorization_endpoint": f"{base_url}/authorize",
        "token_endpoint": f"{base_url}/oauth/token",
        "userinfo_endpoint": f"{base_url}/userinfo",
        "jwks_uri": f"{base_url}/.well-known/jwks.json",
        "response_types_supported": ["code"],
        "subject_types_supported": ["public"],
        "id_token_signing_alg_values_supported": ["none"],
        "scopes_supported": ["openid", "email", "profile"],
        "token_endpoint_auth_methods_supported": ["client_secret_post", "client_secret_basic"],
        "claims_supported": ["email", "sub"],
        "code_challenge_methods_supported": ["plain", "S256"]
    })

@app.route('/.well-known/jwks.json')
def jwks():
    """
    JSON Web Key Set endpoint
    Returns an empty key set since this is a mock server that doesn't use real JWTs
    """
    return jsonify({
        "keys": []
    })

if __name__ == "__main__":
    app.run(
        port=os.environ.get("PORT", 3002),
        host="0.0.0.0",
        threaded=True,
    )
