# set async_mode to 'threading', 'eventlet' or 'gevent' to force a mode
# else, the best mode is selected automatically from what's installed
async_mode = 'eventlet'

import time
from flask import Flask, render_template
import socketio

sio = socketio.Server(logger=True, async_mode=async_mode)
app = Flask(__name__)
app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)
app.config['SECRET_KEY'] = 'secret!'
thread = None


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my response', {'data': 'Server generated event'},
                 namespace='/test')


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = sio.start_background_task(background_thread)
    return render_template('index.html')

@sio.on('beep')
def beep(sid):
     #sio.emit('boop',{},room = sid)
     sio.emit('boop',{})

@sio.on('question')
def test_message(sid, message):
    sio.emit('my response', {'data': message['data']}, room=sid)


@sio.on('my broadcast event')
def test_broadcast_message(sid, message):
    sio.emit('my response', {'data': message['data']})


@sio.on('join')
def join(sid, message):
    #sio.enter_room(sid, message['room'])
   # sio.emit('my response', {'data': 'Entered room: ' + message['room']},
             room=sid)


@sio.on('leave')
def leave(sid, message):
    sio.leave_room(sid, message['room'])
    sio.emit('my response', {'data': 'Left room: ' + message['room']},
             room=sid)


@sio.on('close room')
def close(sid, message):
    sio.emit('my response',
             {'data': 'Room ' + message['room'] + ' is closing.'},
             room=message['room'])
    sio.close_room(message['room'])


@sio.on('my room event')
def send_room_message(sid, message):
    sio.emit('my response', {'data': message['data']}, room=message['room'])


@sio.on('disconnect request')
def disconnect_request(sid):
    sio.disconnect(sid)


@sio.on('connect')
def test_connect(sid, environ):
    sio.emit('my response', {'data': 'Connected', 'count': 0}, room=sid
             )


@sio.on('disconnect')
def test_disconnect(sid):
    print('Client disconnected')


if __name__ == '__main__':
    if sio.async_mode == 'threading':
        # deploy with Werkzeug
        app.run(threaded=True)
    elif sio.async_mode == 'eventlet':
        # deploy with eventlet
        import eventlet
        eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)
    elif sio.async_mode == 'gevent':
        # deploy with gevent
        from gevent import pywsgi
        try:
            from geventwebsocket.handler import WebSocketHandler
            websocket = True
        except ImportError:
            websocket = False
        if websocket:
            pywsgi.WSGIServer(('127.0.0.1', 5000), app,
                              handler_class=WebSocketHandler).serve_forever()
        else:
            pywsgi.WSGIServer(('127.0.0.1', 5000), app).serve_forever()
    else:
        print('Unknown async_mode: ' + sio.async_mode)