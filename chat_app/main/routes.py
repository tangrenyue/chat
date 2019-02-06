from flask import session, redirect, url_for, render_template, request
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/enter', methods=['POST'])
def enter():
    # 加入聊天室, name 保存在 session 里面
    name = request.form.get('name')  # name
    if name is not None:
        session['name'] = name
        return redirect(url_for('.chat'))
    else:
        return redirect(url_for('.index'))


@main.route('/chat')
def chat():
    # Chat room---name 和room 存session
    name = session.get('name', '')
    if name == '':
        return redirect(url_for('.index'))
    return render_template('chat.html')
