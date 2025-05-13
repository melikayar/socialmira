from flask import Blueprint, render_template, request, redirect, url_for, session
import json
import os
import bcrypt

auth_bp = Blueprint("auth", __name__)

# JSON dosyasının yolu
user_file = os.path.join(os.path.dirname(__file__), "..", "users.json")
user_file = os.path.abspath(user_file)

# Fonksiyonlar
def load_users():
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(user_file, "w") as f:
        json.dump(users, f, indent=4)

# Başlangıçta kayıtlı kullanıcıları yükle
registered_users = load_users()

# Sabit kullanıcılar
users = {
    "admin": "1234",
    "melika": "mira123"
}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Sabit kullanıcılar
        if email in users and users[email] == password:
            session["user_email"] = email
            return redirect(url_for("home.home"))

        # JSON'dan gelen kullanıcıları kontrol et
        for user in registered_users:
            if user["email"] == email and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
                session["user_email"] = email
                return redirect(url_for("home.home"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Şifreyi hash'le
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Kaydet
        registered_users.append({
            "name": name,
            "email": email,
            "password": hashed_password
        })
        save_users(registered_users)

        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user_email", None)
    return redirect(url_for("auth.login"))
