import os

from api.similarity_app import app


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = 7000
    app.run(host=host, port=port, threaded=True)
