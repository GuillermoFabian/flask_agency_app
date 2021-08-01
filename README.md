# Discography

### URL:

```bash
https://discography-app.herokuapp.com/
```


## Start the project locally

This section will introduce you to how to run and setup the app locally.

### Dependencies

This project is based on `Python 3.6` and `Flask`.

To install project dependencies:

```bash
$ pip install -r requirements.txt
```

### Local Database connection

- You need to install and start `postgres` database.
- You need to update the database_params variable found in `config.py` file as shown below:

```python
database_params = {
    "username": "USER_NAME",
    "password": "YOUR_DB_PASSWORD",
    "db_name": "DB_NAME",
    "dialect": "postgresql"
}
```


Note: you can create a db named `DB_NAME` by using `createdb` command as shown below:

```bash
createdb -U postgres casting_agency
```


### Auth0 configs

You need to update auth0_params variable found in `config.py` with auth0 configurations

```python
auth0_params = {

    "AUTH0_DOMAIN": "dev-fkoly682.us.auth0.com",
    "ALGORITHMS": "['RS256']",
    "API_AUDIENCE": "discography"


}

```


### Run the app locally

You can run the app using the below commands:

```bash
export FLASK_APP=app.py
flask run
```

### Run test cases

You can run the unit test cases that are defined in `test_app.py` using the below command:

```bash
python test_app.py
```

## API Documentation

This section will introduce you to API endpoints and error handling


### Error handling

Errors are returned as JSON in the following format:

```json
{
  "success": False,
  "error": 404,
  "message": "resource not found"
}
```

The API will return the types of errors:

- 400 – bad request
- 404 – resource not found
- 422 – unprocessable
- 500 - internal server error
- 401 - unauthorized


### API Endpoints

This API supports two types of resources `/singers` and `/songs`. Each resource support four HTTP methods; `GET, POST, PATCH, DELETE`

<b>Notes</b>
- <b>You need to update the ACCESS_TOKEN in the below requests with JWT valid token.</b>
- <b>The below requests assumes you are running the app locally, so you need to update the requests with the base URL or your URL after deployment.</b>

#### GET /singer

- General: returns a list of all singers
- Sample request:

```bash
curl -X GET http://127.0.0.1:5000/singer -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response:

```json

{
  "singers": [
    { "age": 90, "gender": "Male", "id": 1, "name": "Joao Gilberto" },
    { "age": 58, "gender": "Male", "id": 2, "name": "Seu Jorge" },
    { "age": 62, "gender": "Female", "id": 3, "name": "Maria Bethania" }
  ],
  "success": true
}
```

#### GET /song

- General: returns a list of all songs
- Sample request:

```bash
curl -X GET http://127.0.0.1:5000/songs -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response:

```json
{
  "songs": [
    {
      "singers": ["Joao", "Gilberto"],
      "id": 1,
      "release_date": "Mon, 15 Jun 2021 00:00:00 GMT",
      "title": "Samba do Bencao"
    },
    {
      "singers": ["Maria Bethania"],
      "id": 2,
      "release_date": "Mon, 18 Jun 2021 00:00:00 GMT",
      "title": "Samba do Bencao"
    }
  ],
  "success": true
}
```

#### POST /singer

- General: create a new singer
- Sample request:

```bash
curl -X POST http://127.0.0.1:5000/singer -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"  -d '{"name" : "New_singer_1", "age" : "30", "gender":"Male"}'
```

- Sample response: <i>returns the new singer id</i>

```json
{ "created": 4, "success": true }
```

#### POST /song

- General: create a new song
- Sample request:

```bash
curl -X POST http://127.0.0.1:5000/songs -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{"title" : "New_song_1", "release_date" : "12/6/2020"}'
```

- Sample response: <i>returns the new song id</i>

```json
{ "created": 3, "success": true }
```

#### PATCH /singer/\<int:singer_id\>

- General: update an existing singer
- Sample request:
  <i>you can update singer's name, gender and age</i>

```bash
curl -X PATCH http://127.0.0.1:5000/singers/1 -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{"name" : "Mohamed Khalaf"}'
```

- Sample response: <i>returns the updated singer object</i>

```json
{
  "singer": { "age": 25, "gender": "Male", "id": 1, "name": "Joao Gilberto" },
  "success": true
}
```

#### PATCH /song/\<int:song_id\>

- General: update an existing song
- Sample request:
  <i>you can update songs's title and release date</i>

```bash
curl -X PATCH http://127.0.0.1:5000/songs/1 -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{"title" : "UPDATE_NAME", "release_date" : "12/6/2020"
}'
```

- Sample response: <i>returns the updated song object which includes the singers acting in this song</i>

```json
{
  "song": {
    "singers": ["Joao", "Gilberto"],
    "id": 1,
    "release_date": "Mon, 15 Jun 2020 00:00:00 GMT",
    "title": "song_Title"
  },
  "success": true
}
```

#### DELETE /singer/\<int:singer_id\>

- General: delete an existing singer
- Sample request:

```bash
curl -X DELETE http://127.0.0.1:5000/singer/1 -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response: <i>returns the deleted singer id</i>

```json
{ "delete": 1, "success": true }
```

#### DELETE /song/\<int:song_id\>

- General: delete an existing song
- Sample request:

```bash
curl -X DELETE http://127.0.0.1:5000/song/1 -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response: <i>returns the deleted song id</i>

```json
{ "delete": 1, "success": true }
```

## Authentication and authorization

This API uses Auth0 for authentication, you will need to setup Auth0 application and API. You will need to update auth0_params variable found in config.py.

You can use the below links to setup auth0:

[Auth0 Applications](https://auth0.com/docs/applications)
<br>
[Auth0 APIs](https://auth0.com/docs/api/info)

### Existing user roles



1. Assistant:

- GET /singer (get:singer): can get all singers
- GET /song (get:song): can get all songs

2. Manager:
- All permissions of `Assistant`
- PATCH /singer (update:singer): can update existing singers
- PATCH /song (update:song): can update existing songs

3. Owner:
- All permissions of `Manager`
- POST /song (create:song): Can create new songs
- POST /singer (create:song): Can create new songs
- DELETE /song (delete:song): Can delete songs from database
- DELETE /singer (delete:song): Can delete singers from database