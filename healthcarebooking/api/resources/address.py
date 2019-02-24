from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from healthcarebooking.models import Address, dbutils
from healthcarebooking.extensions import ma
from healthcarebooking.commons.utils import dasherize
from healthcarebooking.commons.decorators import with_transaction, marshal_with


class AddressSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    line1 = ma.fields.String()
    line2 = ma.fields.String()
    city = ma.fields.String()
    state = ma.fields.String()
    zipcode = ma.fields.String()
    active = ma.fields.Bool()

    class Meta:
        type_ = 'address'
        inflect = dasherize


class AddressResource(Resource):
    """Single object resource
    """
    # method_decorators = [jwt_required]

    @marshal_with(AddressSchema)
    def get(self, _id):
        return Address.query.get_or_404(_id)

    @marshal_with(AddressSchema)
    def patch(self, _id):
        schema = AddressSchema(partial=True)
        attributes, errors = schema.load(request.json)
        if errors:
            return errors, 422

        return dbutils.update(Address, **attributes)

    @with_transaction
    @marshal_with(AddressSchema)
    def delete(self, _id):
        return dbutils.update(Address, active=False)


class AddressList(Resource):
    """Creation and get_all
    """
    # method_decorators = [jwt_required]

    @marshal_with(AddressSchema, many=True)
    def get(self):
        query = Address.query
        return query

    @marshal_with(AddressSchema)
    def post(self):
        schema = AddressSchema()
        attributes, errors = schema.load(request.json)
        if errors:
            return errors, 422

        return dbutils.create(Address, **attributes)
