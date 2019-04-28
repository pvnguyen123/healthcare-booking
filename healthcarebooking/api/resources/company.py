from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from healthcarebooking.models import Company, dbutils
from healthcarebooking.extensions import ma
from healthcarebooking.commons.utils import dasherize
from healthcarebooking.commons.decorators import with_transaction, marshal_with


class CompanySchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()
    email = ma.fields.String()
    phone = ma.fields.String()
    active = ma.fields.Bool()
    address_id = ma.fields.Integer()
    created = ma.fields.DateTime()
    last_updated = ma.fields.DateTime()

    clients = ma.fields.Relationship(
        related_url='/api/v1/profiles?company={company_id}&type=client',
        related_url_kwargs={'company_id': '<id>'},
        many=True,
        attribute='id',
        type_='profiles',
    )
    providers = ma.fields.Relationship(
        related_url='/api/v1/profiles?company={company_id}&type=provider',
        related_url_kwargs={'company_id': '<id>'},
        attribute='id',
        many=True,
        type_='profiles',
    )
    class Meta:
        type_ = 'companies'
        inflect = dasherize


class CompanyResource(Resource):
    """Single object resource
    """
    # method_decorators = [jwt_required]

    @marshal_with(CompanySchema)
    def get(self, _id):
        return Company.query.get_or_404(_id)

    @marshal_with(CompanySchema)
    def patch(self, _id):
        schema = CompanySchema(partial=True)
        attributes, errors = schema.load(request.json)
        if errors:
            return errors, 422

        return dbutils.update(Company, **attributes)

    @with_transaction
    @marshal_with(CompanySchema)
    def delete(self, _id):
        return dbutils.update(Company, active=False)


class CompanyList(Resource):
    """Creation and get_all
    """
    # method_decorators = [jwt_required]

    @marshal_with(CompanySchema, many=True)
    def get(self):
        query = Company.query
        return query

    @marshal_with(CompanySchema)
    def post(self):
        schema = CompanySchema()
        attributes, errors = schema.load(request.json)
        if errors:
            return errors, 422

        return dbutils.create(Company, **attributes)
