from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path

        if path == "/practica.html":
            print("it's all ok!")
            page = open('practica.html')
            read=page.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(read,'utf-8'))

        else:
            self.send_error(404,"Not found","Page not found")





httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
