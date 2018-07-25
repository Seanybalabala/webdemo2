from pecan import hooks
from webdemo2.db import api as db_api


class DBHook(hooks.PecanHook):

    def before(self, state):
        state.request.db_conn = db_api.Connection()
