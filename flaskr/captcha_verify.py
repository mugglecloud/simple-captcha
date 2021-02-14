from captcha.image import ImageCaptcha
from flask import render_template
from io import BytesIO
import base64
import random

captch_cache = dict()


def image_to_base64(buffered):
    return base64.b64encode(buffered.getvalue())


def generate(n):
    image = ImageCaptcha(fonts=[])
    return image.generate(n)


def verify(href, code):
    print(href)
    if code:
        cached = captch_cache.get(href, None)
        if cached and not cached['accessed']:
            cached['accessed'] = True
            captch_cache[href] = cached
            if cached['code'] == code:
                return ''
    code = str(random.random())[2:8]
    captcha = image_to_base64(generate(code))
    captch_cache[href] = {'code': code, 'accessed': False}
    return render_template("captcha.jinja", captcha=str(captcha, 'utf-8'))
