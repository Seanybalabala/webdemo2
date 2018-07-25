from wsgiref import simple_server
from webdemo2.api import app


def main():
    application = app.setup_app()

    srv = simple_server.make_server('', 8081, application)
    print ('Server on port 8081, listening...')

    srv.serve_forever()


if __name__ == '__main__':
    main()
