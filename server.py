from gevent.pywsgi import WSGIServer
from flaskr.app import server as app

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
