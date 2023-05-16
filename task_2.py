import socketserver

from request import Request

HOST, PORT = '127.0.0.1', 1025


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        request = Request(file=self.rfile)

        print(
            f'Method: {request.method}\n'
            f'URI: {request.uri}\n'
            f'Protocol: {request.protocol}\n'
        )

        if request.method == 'GET':
            if request.uri == '/':
                response_body = '''
                           <!DOCTYPE html>
                           <html>
                           <head>
                           <style>
                           body {
                               display: flex;
                               justify-content: center;
                               align-items: center;
                               height: 100vh;
                               margin: 0;
                               background-color: #f0f0f0;
                               font-family: Arial, sans-serif;
                           }

                           h1 {
                               text-align: center;
                           }
                           </style>
                           </head>
                           <body>

                           <h1>Follow the white rabbit</h1>

                           </body>
                           </html>
                           '''
                response_status = 'HTTP/1.1 200 OK'
            elif request.uri == '/white_rabbit':
                response_body = '''
                           <!DOCTYPE html>
                           <html>
                           <head>
                           <style>
                           body {
                               display: flex;
                               justify-content: center;
                               align-items: center;
                               height: 100vh;
                               margin: 0;
                               background-color: #f0f0f0;
                               font-family: Arial, sans-serif;
                           }

                           h1 {
                               text-align: center;
                           }
                           </style>
                           </head>
                           <body>

                           <h1>You are living in the matrix</h1>

                           </body>
                           </html>
                           '''
                response_status = 'HTTP/1.1 200 OK'
            else:
                response_body = '<h1>501 Not Implemented </h1>'
                response_status = 'HTTP/1.1 501 Not implemented'
        else:
            response_body = '<h1>501 Not Implemented </h1>'
            response_status = 'HTTP/1.1 501 Not implemented'

        response_body_length = str(len(response_body.encode()))

        response = (
            response_status,
            'Content-Type: text/html',
            f'Content-Length: {response_body_length}',
            'Connection: close',
            '',
            response_body
        )

        self.wfile.write('\r\n'.join(response).encode())


socketserver.TCPServer.allow_reuse_address = True

with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
