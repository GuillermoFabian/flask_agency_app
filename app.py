import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import setup_db, db_drop_and_create_all, \
    Singer, Song, Performance, db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    # Should be uncommeted if we want to drop and re-create the db
    #db_drop_and_create_all()
    CORS(app)


# ROUTES

    # GET /singer get singer endpoint
    @app.route('/singer', methods=['GET'])
    @requires_auth('get:singer')
    def retrieve_singer(self):
        selection = Singer.query.order_by(Singer.id).all()

        if len(selection) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'singers': [singer.format() for singer in selection]
        }), 200



    # GET /song get song with their singer endpoint
    @app.route('/song', methods=['GET'])
    @requires_auth('get:song')
    def retrieve_song(self):
        selection = Song.query.order_by(Song.id).all()

        if len(selection) == 0:
                abort(404)

        return jsonify({
                'success': True,
                'songs': [song.format() for song in selection]
            }), 200

    # POST /singer create a new singer
    @app.route('/singer', methods=['POST'])
    @requires_auth('create:singer')
    def create_singer(self):
        body = request.get_json()
        new_age = body.get('age', None)
        new_name = body.get('name', None)
        new_gender = body.get('gender', None)
        if ((new_age is None) or (new_name is None) or (new_gender is None)):
            abort(422)
        try:
            singer = Singer(name=new_name, gender=new_gender, age=new_age)
            singer.insert()

            return jsonify({
                    'success': True,
                    'created': singer.id
                }), 200

        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()

    # POST /song create a new song
    @app.route('/song', methods=['POST'])
    @requires_auth('create:song')
    def create_song(self):
        body = request.get_json()
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        if ((new_title is None) or (new_release_date is None)):
            abort(422)
        try:
            song = Song(title=new_title, release_date=new_release_date)
            song.insert()

            return jsonify({
                'success': True,
                'created': song.id
            }), 200

        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()


    # PATCH /singer/<id> update a singer

    @app.route('/singer/<int:singer_id>', methods=['PATCH'])
    @requires_auth('update:singer')
    def update_singer(self, singer_id):
        singer = Singer.query.filter(Singer.id == singer_id).one_or_none()

        if singer is None:
            abort(404)
        body = request.get_json()
        new_age = body.get('age', None)
        new_name = body.get('name', None)
        new_gender = body.get('gender', None)

        if ((new_name is None) and (new_age is None) and (new_gender is None)):
            abort(422)
        try:
            if new_name is not None:
                singer.name = new_name
            if new_age is not None:
                singer.age = new_age
            if new_gender is not None:
                singer.gender = new_gender

            singer.update()

            return jsonify({
                'success': True,
                'singer': singer.format()
            }), 200

        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()


    # PATCH /song/<id> update a song

    @app.route('/song/<int:song_id>', methods=['PATCH'])
    @requires_auth('update:song')
    def update_song(self, song_id):
        song = Song.query.filter(Song.id == song_id).one_or_none()

        if song is None:
            abort(404)
        body = request.get_json()
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        if ((new_title is None) and (new_release_date is None)):
            abort(422)
        try:
            if new_title is not None:
                song.title = new_title
            if new_release_date is not None:
                song.release_date = new_release_date

            song.update()

            return jsonify({
                'success': True,
                'song': song.format()
            }), 200

        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()


    # Delete /singer/<id> delete a singer
    @app.route('/singer/<int:singer_id>', methods=['DELETE'])
    @requires_auth('delete:singer')
    def delete_singer(self, singer_id):
        try:
            singer = Singer.query.filter(
                Singer.id == singer_id).one_or_none()

            if singer is None:
                abort(404)

            singer.delete()

            return jsonify({
                'success': True,
                'delete': singer.id
            }), 200
        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()


    # Delete /song/<id> delete a song

    @app.route('/song/<int:song_id>', methods=['DELETE'])
    @requires_auth('delete:song')
    def delete_song(self, song_id):
        try:
            song = Song.query.filter(
                Song.id == song_id).one_or_none()

            if song is None:
                abort(404)

            song.delete()

            return jsonify({
                'success': True,
                'delete': song.id
            }), 200
        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()

            # Health check endpoint

    @app.route('/health-check', methods=['POST', 'GET'])
    def health_check():
        return jsonify("Health Check for the API")

    # Error Handling
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": """Not Found. Resource Not found or
            Web page doesn't exist"""
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": """Bad Request. The request may be
            incorrect or corrupted"""
        }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": """Unprocessable Entity.
            An error occured while processing your request"""
        }), 422

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error Occured"
        }), 500

    # error handler for AuthError
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



