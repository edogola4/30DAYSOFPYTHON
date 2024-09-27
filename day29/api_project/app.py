from flask import Flask, Response, request, jsonify
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

# Securely Connect to MongoDB
MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb+srv://username:password@cluster-url/database-name?retryWrites=true&w=majority')
client = pymongo.MongoClient(MONGODB_URI)
db = client['students']  # replace with your database name
collection = db['Students']  # replace with your collection name

@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    try:
        # Fetch all students from the MongoDB collection
        students = list(collection.find())
        return Response(dumps(students), mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/v1.0/students/<id>', methods=['GET'])
def get_student(id):
    try:
        # Fetch a single student by ID
        student = collection.find_one({'_id': ObjectId(id)})
        if student:
            return Response(dumps(student), mimetype='application/json')
        else:
            return jsonify({"error": "Student not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    try:
        data = request.json
        name = data.get('name')
        country = data.get('country')
        city = data.get('city')
        skills = data.get('skills', []).split(', ')  # Assuming skills are comma-separated
        bio = data.get('bio')
        birthyear = data.get('birthyear')
        created_at = datetime.now()

        student = {
            'name': name,
            'country': country,
            'city': city,
            'skills': skills,
            'bio': bio,
            'birthyear': birthyear,
            'created_at': created_at
        }
        result = collection.insert_one(student)
        return jsonify({"result": "Student created", "id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    try:
        data = request.json
        query = {"_id": ObjectId(id)}

        name = data.get('name')
        country = data.get('country')
        city = data.get('city')
        skills = data.get('skills', []).split(', ')  # Assuming skills are comma-separated
        bio = data.get('bio')
        birthyear = data.get('birthyear')
        updated_at = datetime.now()

        student = {
            'name': name,
            'country': country,
            'city': city,
            'birthyear': birthyear,
            'skills': skills,
            'bio': bio,
            'updated_at': updated_at
        }
        result = collection.update_one(query, {'$set': student})
        
        if result.matched_count:
            return jsonify({"result": "Student updated"}), 200
        else:
            return jsonify({"error": "Student not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"result": "Student deleted"}), 200
        else:
            return jsonify({"error": "Student not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
