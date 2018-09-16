from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from healthcarebooking.models import User
from healthcarebooking.extensions import ma, db
from healthcarebooking.commons.pagination import paginate
from healthcarebooking.commons.utils import dasherize

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

    def get(self, user_id):
        schema = UserSchema()
        user = User.query.get_or_404(user_id)
        return {"user": schema.dump(user).data}

    def patch(self, user_id):
        schema = UserSchema(partial=True)
        user = User.query.get_or_404(user_id)
        user_input, errors = schema.load(request.json)
        if errors:
            return errors, 422

        attributes = user_input.get('attributes')

        return {"msg": "user updated", "user": schema.dump(user).data}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "user deleted"}


class UserList(Resource):
    """Creation and get_all
    """
    # method_decorators = [jwt_required]

    def get(self):
        schema = UserSchema(many=True)
        query = User.query
        return paginate(query, schema)

    def post(self):
        schema = UserSchema()
        user, errors = schema.load(request.json)
        if errors:
            return errors, 422

        attributes = user.get('attributes')

        user_obj = User(**attributes)
        db.session.add(user_obj)
        db.session.commit()

        return {"msg": "user created", "user": schema.dump(user).data}, 201
