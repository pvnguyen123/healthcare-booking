from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from healthcarebooking.models import User, dbutils
from healthcarebooking.extensions import ma, db
from healthcarebooking.commons.pagination import paginate
from healthcarebooking.commons.utils import dasherize
from healthcarebooking.commons.decorators import with_transaction, marshal_with


class UserSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    username = ma.fields.String()
    email = ma.fields.String()
    password = ma.fields.String(load_only=True)
    active = ma.fields.Bool()

    class Meta:
        type_ = 'users'
        inflect = dasherize


class UserResource(Resource):
    """Single object resource
    """
    method_decorators = [jwt_required]

    @marshal_with(UserSchema)
    def get(self, user_id):
        return User.query.get_or_404(user_id)

    @marshal_with(UserSchema)
    def patch(self, user_id):
        schema = UserSchema(partial=True)
        attributes, errors = schema.load(request.json)
        if errors:
            return errors, 422

        return dbutils.update(User, **attributes)

    @with_transaction
    @marshal_with(UserSchema)
    def delete(self, user_id):
        return dbutils.update(User, active=False)


class UserList(Resource):
    """Creation and get_all
    """
    # method_decorators = [jwt_required]

    @marshal_with(UserSchema, many=True)
    def get(self):
        query = User.query

        return query

    @marshal_with(UserSchema)
    def post(self):
        schema = UserSchema()
        attributes, errors = schema.load(request.json)
        if errors:
            return errors, 422

        user = User(**attributes)
        db.session.add(user)
        db.session.commit()
        return user
