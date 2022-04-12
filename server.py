from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlibsqladdon import DummySqlAuthorizer

def main():
    authorizer = DummySqlAuthorizer()
    authorizer.add_sql_config('192.168.88.176','ftp_server','root','leluca')
    authorizer.add_sql_query('usuarios','usuario','contra','ruta','permisos')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(('', 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()