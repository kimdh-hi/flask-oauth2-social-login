from flask import Blueprint, request, jsonify, redirect
import requests
from decouple import config

bp = Blueprint("naver_login", __name__, url_prefix="/")

client_id = config("NAVER_CLIENT")
client_secret = config("NAVER_CLIENT_SECRET")
redirect_uri = "http://localhost:5000/oauth/naver/callback"

# localhost:5000/oauth/naver
@bp.route("/oauth/naver")
def redirect_naver_login_page():
    naver_redirect_url=f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={client_id}&state=STATE_STRING&redirect_uri={redirect_uri}"
    return redirect(naver_redirect_url)

@bp.route("/oauth/naver/callback")
def access():
    code = request.args.get('code')

    token_request_url=f"https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&code={code}"
    token_response = requests.get(token_request_url)
    token_json = token_response.json()
    token = token_json['access_token']

    user_info_request_url="https://openapi.naver.com/v1/nid/me"
    user_info = requests.get(user_info_request_url, headers={"Authorization":f"Bearer {token}"})

    return jsonify(user_info.json())
