import os
from bottle import route, run

@route('/hello/:name')
def index(name='World'):
    return '<b>Hello %s!</b>' % name


if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)

    run(host='127.0.0.1', port=port)
