from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = {}  # lưu tạm (không phải database thật)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pw = request.form.get("password")

        if user in users and users[user]["password"] == pw:
            return f"<h2>Đăng nhập thành công: {user}</h2>"
        else:
            return "<h3>Sai tài khoản hoặc mật khẩu</h3>"

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form.get("username")
        pw = request.form.get("password")
        confirm = request.form.get("confirm")
        phone = request.form.get("phone")
        agree = request.form.get("agree")

        if not agree:
            return "<h3>Bạn phải xác nhận quy định</h3>"

        if pw != confirm:
            return "<h3>Mật khẩu không khớp</h3>"

        users[user] = {
            "password": pw,
            "phone": phone
        }

        return redirect("/")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
