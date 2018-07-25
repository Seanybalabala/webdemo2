from wsme import types as wtypes
import wsme
from pecan import rest, request
from webdemo2.api.expose import expose as wsexpose
import pecan


class User(wtypes.Base):
    id = int
    user_id = wtypes.text
    name = wtypes.text
    email = wtypes.text


class Users(wtypes.Base):
    users = [User]


class UsersController(rest.RestController):

    # HTTP GET /users/
    @wsexpose(Users)
    def get(self):
        # user_info_list = [
        #     {
        #         'id': '1',
        #         'name': 'Alice',
        #         'age': 30
        #     },
        #     {
        #         'id': '2',
        #         'name': 'Bob',
        #         'age': 40
        #     }
        # ]
        # users_list = [User(**user_info) for user_info in user_info_list]
        db_conn = request.db_conn   # get 'Connection' from DBHook
        users = db_conn.list_users()
        users_list = []
        for user in users:
            u = User()
            u.id = user.id
            u.user_id = user.user_id
            u.name = user.name
            u.email = user.email
            users_list.append(u)
        return Users(users=users_list)

    # HTTP POST /users
    @wsexpose(None, body=User, status_code=201)
    def post(self, user):
        print user

    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return UserController(user_id), remainder


class UserController(rest.RestController):

    _custom_actions = {
        'kill': ['POST']
    }

    def __init__(self, user_id):
        self.user_id = user_id

    # HTTP GET /users/123456/
    @wsexpose(User)
    def get(self):
        # user_info = {
        #     'id': self.user_id,
        #     'name': 'Alice',
        #     'age': 30
        # }
        db_conn = request.db_conn
        user = db_conn.get_user(self.user_id)
        if user is None:
            raise wsme.exc.ClientSideError('user_id: \'%s\' is not exist.' % self.user_id, status_code=403)
        u = User()
        u.id = user.id
        u.user_id = user.user_id
        u.name = user.name
        u.email = user.email
        return u

    # HTTP PUT /users/123456/
    @wsexpose(User, body=User)
    def put(self, user):
        user_info = {
            'id': self.user_id,
            'name': user.name,
            'age': user.age + 1
        }
        return User(**user_info)

    # HTTP DELETE /users/123456/
    @wsexpose()
    def delete(self):
        print ('Delete user_id: %s' % self.user_id)

    # HTTP POST /users/123456/kill
    @wsexpose(status_code=202)
    def kill(self):
        print ('Kill user_id: %s' % self.user_id)
