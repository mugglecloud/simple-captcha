from .captcha_verify import verify
from flask import Flask, request
server = Flask(__name__)


@server.route("/verify")
@server.route('/verify/<code>')
def route_verify(code=None):
    return verify(client_ip=request.args.get('client_ip'), code=code or request.args.get('captcha'))
