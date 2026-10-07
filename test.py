import http.server
import os


PORT = 8000


class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)


if __name__ == "__main__":
    with http.server.ThreadingHTTPServer(("", PORT), SimpleHandler) as httpd:
        print(f"Open http://localhost:{PORT} in your browser")
        httpd.serve_forever()

