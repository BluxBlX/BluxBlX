from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = {}

@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        user = request.form.get("username", "")
        pw = request.form.get("password", "")

        if user in users and users[user]["password"] == pw:
            return f"<h2>Đăng nhập thành công: {user}</h2>"
        else:
            error = "Sai tài khoản hoặc mật khẩu"

    return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    error_pw = None
    error_agree = None
    error_user = None

    if request.method == "POST":
        user = request.form.get("username", "").strip()
        pw = request.form.get("password", "")
        confirm = request.form.get("confirm", "")
        phone = request.form.get("phone", "")
        agree = request.form.get("agree")

        # check trống
        if not user or not pw:
            error_user = "Không được để trống"

        # check trùng
        elif user in users:
            error_user = "Tài khoản đã tồn tại"

        # check mật khẩu
        elif pw != confirm:
            error_pw = "Mật khẩu không khớp"

        elif len(pw) < 6 or len(pw) > 20:
            error_pw = "Mật khẩu 6-20 ký tự"

        # check checkbox
        elif not agree:
            error_agree = "Phải xác nhận"

        # OK
        else:
            users[user] = {
                "password": pw,
                "phone": phone
            }
            return redirect("/")

    return render_template(
        "register.html",
        error_pw=error_pw,
        error_agree=error_agree,
        error_user=error_user
    )


if __name__ == "__main__":
    app.run(debug=True)
