# chat
基于 WebSocket 的实时在线聊天室
- 可多人实时在线聊天
- 可切换聊天室
- 使用了 Flask 及 Flask-SocketIO, 部署上线可以用eventlet，它是最好的高性能选择，支持长轮询和WebSocket传输，很快。
- 我是开发用的Werkzeug 的 Flask 开发服务器，只应用于简单的开发环境，仅支持长轮询传输。

![演示图片](https://github.com/tangrenyue/chat/blob/master/chat_app/chat.png)
