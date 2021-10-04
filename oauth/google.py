from flask import request, Blueprint, jsonify, redirect
from decouple import config
import requests

bp = Blueprint("google_login", __name__, url_prefix="/")

client_id = config("GOOGLE_CLIENT")
client_secret = config("GOOGLE_CLIENT_SECRET")
redirect_uri = "http://localhost:5000/oauth/google/callback"

#http://localhost:5000/oauth/google
@bp.route('/oauth/google')
def redirect_google_login_page():
    google_redirect_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=token&scope=https://www.googleapis.com/auth/contacts.readonly"
    return redirect(google_redirect_url)

@bp.route('/ouath/google/callback')
def get_authentication_code():
    print(request.get)
    return "ok"