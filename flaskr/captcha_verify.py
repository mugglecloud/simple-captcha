from captcha.image import ImageCaptcha
from flask import render_template
import base64
import random
import time

captch_cache = dict()


def image_to_base64(buffered):
    return base64.b64encode(buffered.getvalue())


def generate(n):
    image = ImageCaptcha(fonts=[])
    return image.generate(n)


def verify(client_ip, code):
    client_ip = str(client_ip)
    now = time.time()
    if code:
        cached = captch_cache.get(client_ip, None)
        if cached and cached['code'] == code and cached['expired_at'] > now:
            return ''
    code = str(random.random())[2:8]
    captcha = image_to_base64(generate(code))
    captch_cache[client_ip] = {'code': code, 'expired_at': now + 300}
    return render_template("captcha.jinja", captcha=str(captcha, 'utf-8'), client_ip=client_ip or '')
