from flask import request, jsonify, session, redirect
from bank_account import BankAccount
from crypto_wallet import CryptoWallet
from argon2 import PasswordHasher


import database

db = database.connect()["bank"]["customers"]

class Account:

    def start_session(self, user):
        del user["password"], user["_id"]
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200

    def login(self):
        user_account = db.find_one({"cpr_number": request.form.get("CPR")})
        
        if user_account is not None:
            if self.verify_password(user_account["password"], request.form.get("password")):
                return self.start_session(user_account)
        return jsonify({"error": "Invalid login credentials"}), 401

    def logout(self):
        session.clear()
        return redirect("/user/login")

    def register(self):
        user = self.create_user_object(request)
        if request.form.get("password") != request.form.get("confirm_password"):
            return jsonify({"error": "Passwords did not match"}), 400
        db.insert_one(user)
        return self.start_session(user)

    def create_user_object(self, request):
        user = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "age": request.form.get("age"),
            "cpr_number": request.form.get("CPR"),
            "email": request.form.get("email"),
            "phone_number": request.form.get("phone_number"),
            "password": PasswordHasher().hash(request.form.get("password")),
            "bank_account": str(BankAccount("Savings", 100.00).store_account().inserted_id),
            "crypto_wallet": str(CryptoWallet("Bitcoin", 0.00075).store_account().inserted_id)
        }
        return user

    def verify_password(self, hash, password):
        try:
            PasswordHasher().verify(hash, password)
            return True
        except:
            return False
        
