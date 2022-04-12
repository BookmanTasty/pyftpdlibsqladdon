from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlibsqladdon import DummySqlAuthorizer

def main():
    authorizer = DummySqlAuthorizer()
    authorizer.add_sql_config('host_ip','database','sql_user','sql_password')
    authorizer.add_sql_query('table','user_column','password_column','home_path_column','permission_colum')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(('', 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()