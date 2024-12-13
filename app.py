from flask import Flask, request, jsonify, render_template 
from pymongo import MongoClient 
from os import environ
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

mongourl=environ.get('MONGO_URI')
client = MongoClient(mongourl)
db = client['user_database']
collection = db['users']


@app.route('/register', methods=['POST'])
def register_user():
    registration_id = request.form['email']
    password = request.form['password']
    if not registration_id or not password:
        return jsonify({"error": "Missing required fields"}), 400
    if collection.find_one({"registration_id": registration_id}):
        return jsonify({"error": "User with this registration ID already exists"}), 400
    user = {
        "registration_id": registration_id,
        "password": password
    }
    collection.insert_one(user)
    return render_template('GangaBhumiClublogin.html'), 200


@app.route('/login', methods=['POST'])
def login_user():
    registration_id = request.form['loginEmail']
    password = request.form['loginPassword']
    if not registration_id or not password:
        return jsonify({"error": "Missing required fields"}), 400
    user = collection.find_one({"registration_id": registration_id})
    if not user or user['password'] != password:
        return jsonify({"error": "Invalid registration ID or password"}), 401
    return jsonify({"message": "Login successful"}), 200

@app.route('/', methods=['GET'])
def home():
    return render_template('GangaBhumiClubsignup.html'), 200

if __name__ == '__main__':
    app.run()
