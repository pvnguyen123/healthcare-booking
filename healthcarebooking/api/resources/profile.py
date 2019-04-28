from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from webargs import fields
from webargs.flaskparser import use_args

from healthcarebooking.models import Profile, AssociationCompanyProfile, dbutils
from healthcarebooking.extensions import ma
from healthcarebooking.commons.utils import dasherize
from healthcarebooking.commons.decorators import with_transaction, marshal_with


class ProfileSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    firstname = ma.fields.String()
    lastname = ma.fields.String()
    phone = ma.fields.String()
    active = ma.fields.Bool()

    addresses = ma.fields.Relationship(
        related_url='/api/v1/addresses?profile_id={profile_id}',
        related_url_kwargs={'profile_id': '<id>'},
        many=True,
        type_='addresses',
    )

    class Meta:
        type_ = 'profiles'
        inflect = dasherize


class ProfileResource(Resource):
    """Single object resource
    """
    # method_decorators = [jwt_required]

    @marshal_with(ProfileSchema)
    def get(self, _id):
        return Profile.query.get_or_404(_id)

    @marshal_with(ProfileSchema)
    def patch(self, _id):
        schema = ProfileSchema(partial=True)
        attributes, errors = schema.load(request.json)
        if errors:
            return errors, 422

        return dbutils.update(Profile, **attributes)

    @with_transaction
    @marshal_with(ProfileSchema)
    def delete(self, _id):
        return dbutils.update(Profile, active=False)


class ProfileList(Resource):
    """Creation and get_all
    """
    # method_decorators = [jwt_required]
    args = {
        "company_id": fields.Int(),
        "type": fields.Str()
    }

    @marshal_with(ProfileSchema, many=True)
    @use_args(args)
    def get(self, args):
        company_id = args.get('company_id')
        profile_type = args.get('type')

        query = Profile.query

        if company_id:
            query = query.join(AssociationCompanyProfile, Profile.id == AssociationCompanyProfile.profile_id)\
                         .filter(AssociationCompanyProfile.company_id == company_id)

            if profile_type:
                query.filter(AssociationCompanyProfile.association_type == profile_type)

        return query

    @marshal_with(ProfileSchema)
    def post(self):
        schema = ProfileSchema()
        attributes, errors = schema.load(request.json)
        if errors:
            return errors, 422

        return dbutils.create(Profile, **attributes)
