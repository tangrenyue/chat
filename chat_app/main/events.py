from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    room = message['msg']
    join_room(room)
    session['room'] = room
    name = session.get('name')
    message = '用户:**{}** -----进入了房间-----'.format(name)
    emit('status', {'msg': message}, room=room)


@socketio.on('sent', namespace='/chat')
def sent(message):
    # print("room", session.get("room"))
    room = message.get('room')
    name = session.get('name')
    emit('message', {'msg': name + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    name = session.get('name')
    leave_room(room)
    message = '用户:**{}** -----离开了房间-----'.format(name)
    emit('status', {'msg': message}, room=room)

