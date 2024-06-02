from zhipuai import ZhipuAI
from flask import Flask, render_template
from flask_socketio import SocketIO

# 初始化Flask应用和SocketIO
app = Flask(__name__, template_folder='web')
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# 初始化ZhipuAI客户端
client = ZhipuAI(api_key="xx.xx")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('收到消息：', message)
    
    client = ZhipuAI(api_key="xx.xx")
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": message},
        ],
        stream=True,
    )
    for chunk in response:
        print(chunk.choices[0].delta)
        print(f"Delta type: {type(chunk.choices[0].delta)}")  # 检查delta的类型
        socketio.emit('response', chunk.choices[0].delta.model_dump())
    
    socketio.emit('response', 'done')

if __name__ == '__main__':
    # 在这里指定总是无效，需要通过 flask run --reload --host=0.0.0.0 才可以。
    # socketio.run(app, debug=True, host='0.0.0.0')
    socketio.run(app)
