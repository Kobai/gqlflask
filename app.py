import os, redis
from flask import Flask, abort, request, Response, render_template, send_from_directory, jsonify, make_response, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from raven.contrib.flask import Sentry
from models import *
from schema import *

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView

app = Flask(__name__)
app.config['SQLALCHEMY_POOL_SIZE'] = 10
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/gql?user=kobai&password=kobai'

db.init_app(app)
db.app = app

@app.route('/')
def home():
	return 'hello world'

app.add_url_rule(
	'/graphql',
	view_func=GraphQLView.as_view(
		'graphql',
		schema=schema,
		graphiql=True
	)
)

manager = Manager(app)
migrate= Migrate(app,db)
manager.add_command('db', MigrateCommand)

sentry = Sentry(app, dsn=os.getenv('SENTRY_DSN'))
sentry.init_app(app, wrap_wsgi=(os.getenv('ENV') != 'test'))

if __name__ == '__main__':
	manager.run()
