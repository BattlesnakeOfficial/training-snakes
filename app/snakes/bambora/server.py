#!/usr/bin/env python3
#
# Copyright (c) 2017 - Beanstream Internet Commerce, Inc. <http://beanstream.com>
#
# MIT License. Use and abuse as you wish.
#

# Framework modules
import logging
import time

from flask import Flask
from flask import jsonify, g, request
from flask import send_from_directory
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

# Custom modules
from utils.exceptions import DatabaseException
from utils.exceptions import ServerException
from utils.crossdomain import cross_domain
from utils.redis_handler import RedisHandler

# Settings
from settings import config

# Snake blueprints

from snakes.dummy import snake as dummy
from snakes.mamba import snake as mamba
from snakes.beany import snake as beany
from snakes.hungry_snake import snake as hungry_snake
from snakes.venom.basic import snake as venom_basic
from snakes.venom.recursion import snake as venom_recursion
from snakes.venom.breadth import snake as venom_breadth

__author__ = 'Sven, Logan, Chris & Brian'


##########################
# LOGGING

logger = logging.getLogger('blacktail.dev')

# # Log output to stdout for a typical development environment
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler = logging.StreamHandler(sys.stdout)
# handler.setFormatter(formatter)
#
# logger.addHandler(handler)


##########################
# ERROR/EXCEPTION HANDLING
#
# --> http://flask.pocoo.org/snippets/83/
# Creates a JSON-oriented Flask app.
#
# All error responses that you don't specifically
# manage yourself will have application/json content
# type, and will contain JSON like this (just an example):
#
# { "message": "405: Method Not Allowed" }


def make_json_error(ex):
    if not isinstance(ex, ServerException) and not isinstance(ex, DatabaseException):
        logger.exception(ex)

    response = jsonify(message=str(ex))
    response.status_code = (ex.code
                            if isinstance(ex, HTTPException)
                            else 500)
    return response

app = Flask(__name__)
app.config['ENVIRONMENT_NAME'] = 'dev'

for code in default_exceptions.items():
        app.error_handler_spec[None][code] = make_json_error


##########################
# ROUTES


@app.route('/', methods=['GET'])
@cross_domain(origin='*')
def root():
    content = '<div style="margin-top:50px;">'\
              '<center><h1>Blacktail - Beanstream Bounty Snake 2017</h1></br>' \
              '<h2>' \
              '<a href="https://github.com/Beanstream/blacktail">https://github.com/Beanstream/blacktail</a>' \
              '</h2>' \
              '</center>' \
              '</div>'
    return content


@app.route('/swagger.json', methods=['GET'])
@cross_domain(origin='*')
def swagger():
    return send_from_directory('config', 'swagger.json', mimetype='application/json')


@app.route('/health', methods=['GET'])
@cross_domain(origin='*')
def health():
    status = 'OK'  # TODO: POTENTIALLY REPLACE WITH CODE THAT ACTUALLY CHECKS SOMETHING
    logger.info('Health status was requested. Status is ' + status)
    if status is 'OK':
        response = {'status': 'OK'}
        return jsonify(response)
    else:
        raise ServerException("Error: Server Health In Question")


##########################
# ROUTES

app.register_blueprint(hungry_snake, url_prefix='/hungry')


# HELPER FUNCTIONS

@app.before_request
def before_request():
    g.start = time.time()


@app.teardown_request
def teardown_request(exception=None):
    if exception is not None:
        print("teardown exception:", exception)

    diff = time.time() - g.start
    print("time taken: {0}ms".format(diff*1000))


@app.after_request
def after_request(response):
    return response


# Used for custom error handling
@app.errorhandler(400)
def error400(e):
    return jsonify(error=400, message=str(e)), 400


@app.errorhandler(Exception)
def error500(e):
    # Server and Database Exceptions happen as a result of situations that the server knows
    # about and as such the expectation is that the calling app will deal with these on an
    # as needed basis. We do not log or use a debug level only here.
    if isinstance(e, ServerException):
        extra = {'More info': 'something interesting'}
        logger.warning(e, extra=extra)
        error_code = 400
    elif isinstance(e, DatabaseException):
        # Database modules should log directly
        error_code = 400
    else:
        logger.exception(e)
        error_code = 500

    return jsonify(error=error_code, message=str(e)), error_code


#
# SERVER SETUP
#

# Setup class instances used here
# ...

# START SERVER

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
