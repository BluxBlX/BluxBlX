from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except:
        content = "Không có dữ liệu"
    return f"<h1>Web chạy OK!</h1><pre>{content}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
