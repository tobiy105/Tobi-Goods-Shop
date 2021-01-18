import os
import unittest
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from shop import app, db, bcrypt, photos
from flask_wtf.file import FileField
from shop.admin.forms import RegistrationForm, LoginForm
from shop.admin.models import User
import io

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()
        pass

    def test_register_message(self):
        hash_password = bcrypt.generate_password_hash('pass')
        client = app.test_client(self)
        response = client.post('/register', data = dict(name='test', username='Tests',
                               email='email2@gmail.com', password=hash_password),
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_login(self):
        hash_password = bcrypt.generate_password_hash('pass')
        client = app.test_client(self)
        response = client.post('/login', data = dict(email='email2@gmail.com', password=hash_password),
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_no_email(self):
        hash_password = bcrypt.generate_password_hash('pass')
        client = app.test_client(self)
        response = client.post('/login', data = dict(email='', password=hash_password),
                               follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_login_no_password(self):
        hash_password = bcrypt.generate_password_hash('pass')
        client = app.test_client(self)
        response = client.post('/login', data = dict(email='email2@gmail.com', password=''),
                               follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_login_no_fields(self):
        hash_password = bcrypt.generate_password_hash('pass')
        client = app.test_client(self)
        response = client.post('/login', data = dict(email='', password=''),
                               follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_brand(self):
        client = app.test_client(self)
        response = client.post('/addbrand', data=dict(name='test_b'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        client = app.test_client(self)
        response = client.post('/addbrand', data=dict(name='test_c'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_product(self):

        data1 = FileField('Users\tobiy\OneDrive\Pictures\food.png')
        data2 = FileField('Users\tobiy\OneDrive\Pictures\food2.png')
        data3 = FileField('Users\tobiy\OneDrive\Pictures\food3.png')
        client = app.test_client(self)
        response = client.post('/addproduct', data=dict(name="food", price=2, discount=0, stock=10,
                               allergy="nuts", desc="help", brand_id=1, category_id=1, image_1=data1,
                               image_2=data2, image_3=data3), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_register_customer(self):
        client = app.test_client(self)
        response = client.post('/customer/register', data = dict(name='test_cus', username='Customer',
                               email='custumer@gmail.com', password='pass888', country='England', city='Leeds',
                               contact='07484286269', address='152 Burley Rd', zipcode='LS4 2EU'),
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_customer(self):
        hash_password = bcrypt.generate_password_hash('pass888')
        client = app.test_client(self)
        response = client.post('/customer/login', data = dict(email='custumer@gmail.com', password=hash_password),
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_customer_no_email(self):
        hash_password = bcrypt.generate_password_hash('pass888')
        client = app.test_client(self)
        response = client.post('/customer/login', data = dict(email='', password=hash_password),
                               follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_login_customer_no_password(self):
        hash_password = bcrypt.generate_password_hash('pass888')
        client = app.test_client(self)
        response = client.post('/customer/login', data = dict(email='custumer@gmail.com', password=''),
                               follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_login_customer_no_fields(self):
        hash_password = bcrypt.generate_password_hash('pass888')
        client = app.test_client(self)
        response = client.post('/customer/login', data = dict(email='', password=''),
                               follow_redirects=False)
        self.assertEqual(response.status_code, 200)



    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()