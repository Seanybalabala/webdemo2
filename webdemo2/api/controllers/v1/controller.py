from pecan import rest
from wsme import types as wtypes
from webdemo2.api.expose import expose as wsexpose
from webdemo2.api.controllers.v1.users import UsersController


class V1Controller(rest.RestController):

    users = UsersController()

    @wsexpose(wtypes.text)
    def get(self):
        return 'webdemo2 v1controller'
