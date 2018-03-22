# Review API

### Note: No superuser will be created in the following those steps

```shell

user@host:~/reviewsapp$ pip install -r requirements.py

user@host:~/reviewsapp$ python manage.py makemigrations

user@host:~/reviewsapp$ python manage.py makemigrations api

user@host:~/reviewsapp$ python manage.py migrate

user@host:~/reviewsapp$ python manage.py loaddata mock.json

user@host:~/reviewsapp$ python manage.py runserver

```

* User: reviewer1
	* Password: @reviewert1
* User: reviewer2
	* Password: @reviewert2

## API Endpoints

* {host}/api/v1/login - POST
* {host}/api/v1/token/refresh - POST <- No auth required ->
* {host}/api/v1/token/verify - POST <- No auth required ->
* {host}/api/v1/reviews - GET / POST
* {host}/api/v1/reviews/{review-id} - GET / DELETE / PUT




# Login

```javascript

POST {host}/api/v1/login

Body:
{"username": "reviewer1", "password": "@reviewert1"}

Response HTTP 200:
{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJldmlld2VyX3Rlc3RfMSIsIm9yaWdfaWF0IjoxNTExMzYyNzM2LCJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE1MTEzNjMzMzZ9.nT0VuGB-wuzjJSYmmoOVdejOopHStcUDRlMqui7rvPM"}
```

# JWT Token

```javascript
POST {host}/api/v1/token/verify

Body:
{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJldmlld2VyX3Rlc3RfMSIsIm9yaWdfaWF0IjoxNTExMzYyNzM2LCJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE1MTEzNjMzMzZ9.nT0VuGB-wuzjJSYmmoOVdejOopHStcUDRlMqui7rvPM"}

Response HTTP 200 OK:
{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJldmlld2VyX3Rlc3RfMSIsIm9yaWdfaWF0IjoxNTExMzYyNzM2LCJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE1MTEzNjMzMzZ9.nT0VuGB-wuzjJSYmmoOVdejOopHStcUDRlMqui7rvPM"}

POST {host}/api/v1/token/refresh <- Reset session timeout ->

Body:
{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJldmlld2VyX3Rlc3RfMSIsIm9yaWdfaWF0IjoxNTExMzYyNzM2LCJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE1MTEzNjMzMzZ9.nT0VuGB-wuzjJSYmmoOVdejOopHStcUDRlMqui7rvPM"}

Response HTTP 200 OK:
{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJldmlld2VyX3Rlc3RfMSIsIm9yaWdfaWF0IjoxNTExMzYyNzM2LCJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE1MTEzNjMzMzZ9.nT0VuGB-wuzjJSYmmoOVdejOopHStcUDRlMqui7rvPM"}
```


## HTTP request header protected APIs

```javascript
{"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJldmlld2VyX3Rlc3RfMSIsIm9yaWdfaWF0IjoxNTExMzYyNzM2LCJ1c2VyX2lkIjoxLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJleHAiOjE1MTEzNjMzMzZ9.nT0VuGB-wuzjJSYmmoOVdejOopHStcUDRlMqui7rvPM"}
```

# Review / Reviews APIs - Protected 
```javascript
GET {host}/api/v1/reviews

Response:

[
    {
        "id": 1,
        "user": 1,
        "rating": 5,
        "title": "awesome review for a awesome topic",
        "summary": "Some text that contains a awesome review",
        "ip_address": "199.2.204.7",
        "submission": "2017-11-22T15:02:03.428683Z"
    },
    {
        "id": 2,
        "user": 1,
        "rating": 1,
        "title": "poor review",
        "summary": "Some text that contains a not good review",
        "ip_address": "200.174.55.4",
        "submission": "2017-11-22T15:02:03.429721Z"
    }
]


GET {host}/api/v1/review/1

Response:

{
	"id": 1,
	"user": 1,
	"rating": 5,
	"title": "awesome review for a awesome topic",
	"summary": "Some text that contains a awesome review",
	"ip_address": "199.2.204.7",
	"submission": "2017-11-22T15:02:03.428683Z"
}
```
