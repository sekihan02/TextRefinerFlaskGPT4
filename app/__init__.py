from flask import Flask, render_template
from .routes.chat import chat_bp
import logging

app = Flask(__name__)
app.register_blueprint(chat_bp)

app.logger.setLevel(logging.DEBUG)  # ログレベルをDEBUGに設定

stream_handler = logging.StreamHandler()

# debugモード　本番時には以下コード削除
if __name__ == "__main__":
    app.run(debug=True)