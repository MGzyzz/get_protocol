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

        if request.uri == '/hello_world':
            response_body = '<h1>Hello World</h1>'
        else:
            response_body = '<h1>Not Found</h1>'

        response_body_length = str(len(response_body.encode()))

        response = (
            'HTTP/1.1 200 OK',
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