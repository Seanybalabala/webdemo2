from pecan import rest, expose
from wsme import types as wtypes
from webdemo2.api.controllers.v1 import controller as v1_controller
from webdemo2.api.expose import expose as wsexpose


class RootController(rest.RestController):

    # All supported API versions
    _versions = ['v1']

    # The default API version
    _default_version = 'v1'

    v1 = v1_controller.V1Controller()

    # @wsexpose(wtypes.text)
    # def get(self):
    #     return 'webdemo2'

    @expose()
    def _route(self, args):
        """When the API version is not specified in the url, v1 is used as the default version."""
        if args[0] and args[0] not in self._versions:
            args = [self._default_version] + args
        return super(RootController, self)._route(args)
