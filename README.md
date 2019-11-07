# WOZiTech Ltd - CV app - Training (micro) Service

[Documentation](https://wozitech.asuscomm.com/projects/cv/training)

RESTful API:
* [GET /] - list all in reverse chronological on date achieved
* [GET /:id] - returns a specific training record
* [POST /] - creates a training record; "Authorization" Bearer JWT required
* [PUT /:id] - updates the training record; "Authorization" Bearer JWT required
* [DELETE /:id] - delete the training record; "Authorization" Bearer JWT required

Training records are store in MongoDB collection "Training".

# TODO: 
1. [GET] - limit, since, total, facetted "scope"
2. serverlesss framework
3. Docker file

# Dependencies:
* flask
* connexion