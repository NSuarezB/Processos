from http.server import HTTPServer, BaseHTTPRequestHandler
import smtplib

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path
        print(path)
        if path == "/image.jpeg":
            print("it's all ok!")

            page = open('image.jpeg','rb')
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
            self.wfile.write(page.read())

            ipConectada = self.address_string()
            fromaddr = 'natihina30@gmail.com'
            toaddrs  = 'natihina30@gmail.com'
            msg = "Subject:Informacio persona conectada al servidor!!!"+"\n\n\nHa conectat l ip:"+ipConectada
            username = 'natihina30@gmail.com'
            password = 'Admin1234\''
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()

        else:
            self.send_error(404,"Not found","Page not found")





httpd = HTTPServer(('192.168.2.131', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
