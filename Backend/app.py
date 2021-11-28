import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError
from werkzeug.utils import secure_filename

from model import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "Jx9u2Sn5Js1U1zk6txf0UQ=="
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = './profile-pics'
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024  # bytes

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

db = SQLAlchemy(app)


class Person(db.Model):
    email = db.Column(db.String(50), primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), default=False, nullable=False)
    is_professor = db.Column(db.Boolean, default=False, nullable=False)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(50), nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.Integer, nullable=False)


class StudentCourseMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_email = db.Column(db.String(50), nullable=False)
    course_code = db.Column(db.String(50), nullable=False)


@app.route('/person', methods=['POST'], endpoint='person_register')
def person_register():
    content = request.json
    req_model = RegisterReq()
    try:
        req = req_model.load(content)
        existing_person = Person.query.filter_by(email=req['email']).first()
        if not existing_person:
            new_person = Person(email=req['email'], first_name=req['firstName'],
                                last_name=req['lastName'],
                                password=req['password'],
                                is_professor=req['isProfessor'])
            try:
                db.session.add(new_person)
                db.session.commit()
                response = {"message": "Registered successfully"}, 200
            except:
                response = {"message": "Could Not Register"}, 404
        else:
            response = {"message": "Already Registered successfully"}, 200
    except ValidationError as err:
        return jsonify(err.messages), 400

    return jsonify(response)


@app.route('/course', methods=['POST'], endpoint='add_course')
def add_course():
    content = request.json
    req_model = AddCourseReq()
    try:
        req = req_model.load(content)
        existing_person = Person.query.filter_by(email=req['email'], is_professor=True).first()
        if existing_person:
            new_course = Course(course_name=req['name'], course_code=req['code'],
                                email=req['email'])
            try:
                db.session.add(new_course)
                db.session.commit()
                response = {"message": "Course added successfully", "id": new_course.id}, 200
            except:
                response = {"message": "Course not added"}, 502
        else:
            response = {"message": "Invalid professor email address"}, 400
    except ValidationError as err:
        return jsonify(err.messages), 400
    return response


@app.route('/course/register', methods=['POST'], endpoint='register_course')
def register_course():
    content = request.json
    req_model = RegisterCourseReq()
    try:
        req = req_model.load(content)
        existing_person = Person.query.filter_by(email=req['email']).first()
        existing_course = Course.query.filter_by(course_code=req['courseCode']).first()
        if existing_person and existing_course:
            new_mapping = StudentCourseMapping(course_name=req['name'], course_code=req['courseId'],
                                               email=req['email'])
            try:
                db.session.add(new_mapping)
                db.session.commit()
                response = {"message": "Course registered successfully"}, 200
            except:
                response = {"message": "Course not registered"}, 404
        else:
            response = {"message": "Invalid email address or course code"}, 400
    except ValidationError as err:
        return jsonify(err.messages), 400
    return jsonify(response)


@app.route('/person/<email>', methods=['GET'], endpoint='get_person')
def get_person(email: str):
    new_person = Person.query.filter_by(email=email).first()
    if not new_person:
        response = {"message": "Could not find."}, 404
    else:
        response = jsonify({
            "Data": new_person.first_name
        }, 200)
    return response


@app.route('/login', methods=['POST'], endpoint='login')
def login():
    content = request.json
    req_model = LoginPersonReq()
    try:
        req = req_model.load(content)
        existing_person = Person.query.filter_by(email=req['email'],
                                                 password=req['password']).first()
        if not existing_person:
            response = {"message": "Login failed"}, 401
        else:
            response = {"message": "Login successfully"}, 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    return jsonify(response)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/person/profile-pic/<email>', methods=['POST'])
def upload_file(email: str):
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    existing_person = Person.query.filter_by(email=email).first()
    if not existing_person:
        resp = jsonify({'message': 'Invalid email address'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(
            os.path.join(app.config['UPLOAD_FOLDER'],
                         existing_person.email + "_" + filename))
        print(file)
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': 'Allowed file types are  png, jpg and jpeg'})
        resp.status_code = 400
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
