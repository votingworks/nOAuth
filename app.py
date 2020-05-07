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
        return "Need redirect_uri and state parameteres"
    
    redirect_uri = request.args["redirect_uri"]
    state = request.args["state"]
    return f"""
<h1>You're not running this in production, are you?</h1>
<iframe src='https://gfycat.com/ifr/HonorableSameCaudata' frameborder='0' scrolling='no' width='640' height='503'></iframe>
<br><br>
<form method="post" action="">
<input type="hidden" name="state" value="{state}">
<input type="hidden" name="redirect_uri" value="{redirect_uri}">
email: <input type="text" name="email">
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
    return jsonify(email=email)

if __name__ == "__main__":
    app.run(
        port=os.environ.get("PORT", 3002),
        host="0.0.0.0",
        threaded=True,
    )
