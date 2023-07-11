## LAB - Class 32-34: Authentication & Production Server

## Project: Movie-API

## Author: ***Rakan M. Al-Madani***

## How to initialize/run your application (where applicable)


```
python manage.py runserver
```
---

## Tests:

- Access token route: 

you use this route to get access token for the first time and then use the access token in the request body to get the access permission.
``` 
'api/token/' 
```

- Refresh token route: 

use this route to get access token after expiration to generate a new access token, make sure to use the POST on that route and in the body namefield to put refresh and the value set to the refresh token.

```
'api/token/refresh/'
``` 



- CRUD Operations:

 use this route for any CRUD operations of your choosing to add data to the database.

```
'api/v1/carsApp/'
```

**Note that all testing were done on ThunderClient.**

---

## Example Access and Refresh tokens:
```
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTE0NjA4MywiaWF0IjoxNjg5MDU5NjgzLCJqdGkiOiI2MzQzODg3NjczZjM0MDdkYmUxOTk2ZjAwYjg4NGNjNyIsInVzZXJfaWQiOjF9.PEOF2Mxhsy6zs1XoWnONnexrDHvdU98-VaFrDTVt7Bo",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MDU5OTgzLCJpYXQiOjE2ODkwNTk2ODMsImp0aSI6IjQzNGMxOGEyZDZmMzQyMjhiOWZhOTc1Y2RiOWM2NDcyIiwidXNlcl9pZCI6MX0.Im6yQVHOP98fjx57IOpLX7223I3En4017XoKazcNqtI"
}


New Access token:

{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MDYxMDAzLCJpYXQiOjE2ODkwNTk2ODMsImp0aSI6ImFmMjI2NDM2NzlhZDQwYTg4OGZhMGM4MDIyNzg4ZGE2IiwidXNlcl9pZCI6MX0.YMfK1y0MF_RL_9rcUUout4CnEBP4v-JzrWpytpitJkg"
}

```

---