from flask import Blueprint
from flask_restful import Api
from healthcarebooking.api.resources import (
    UserResource,
    UserList,
    AddressResource,
    AddressList,
    ProfileResource,
    ProfileList,
    CompanyResource,
    CompanyList)


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(AddressResource, '/addresses/<int:_id>')
api.add_resource(AddressList, '/addresses')
api.add_resource(ProfileResource, '/profiles/<int:_id>')
api.add_resource(ProfileList, '/profiles')
api.add_resource(CompanyResource, '/companies/<int:_id>')
api.add_resource(CompanyList, '/companies')