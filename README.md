# WOZiTech Ltd - CV app - Training (micro) Service

[Documentation](https://wozitech.asuscomm.com/projects/cv/training)

RESTful API:
* [GET /api] - list all in reverse chronological on date achieved
* [GET /api/:id] - returns a specific training record
* [POST /api] - creates a training record; "Authorization" Bearer JWT required
* [PUT /api/:id] - updates the training record; "Authorization" Bearer JWT required
* [DELETE /api/:id] - delete the training record; "Authorization" Bearer JWT required

Training records are store in MongoDB collection "Training".

# TODO: 
1. [GET] - limit, since, total, facetted "scope"
2. [POST], [PUT], [DELETE] - authorization (JWT)
3. serverlesss framework
4. Docker file

# Dependencies:
* flask
* connexion