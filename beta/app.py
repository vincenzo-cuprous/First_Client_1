# app.py
from http.server import BaseHTTPRequestHandler, HTTPServer
from home import serve_home
from about import serve_about
from skills import serve_skills
from projects import serve_projects
from contact import serve_contact
from settings import PORT, HOST

class PortfolioHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        routes = {
            '/': serve_home,
            '/about': serve_about,
            '/skills': serve_skills,
            '/projects': serve_projects,
            '/contact': serve_contact
        }
        
        if self.path in routes:
            content = routes[self.path]()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        else:
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=PortfolioHandler, port=PORT):
    server_address = (HOST, port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
