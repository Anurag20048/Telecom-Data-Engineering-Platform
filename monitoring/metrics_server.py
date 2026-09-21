from http.server import BaseHTTPRequestHandler, HTTPServer
class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body=b'telecom_pipeline_up 1\n'
        self.send_response(200)
        self.send_header('Content-Type','text/plain; version=0.0.4')
        self.send_header('Content-Length',str(len(body)))
        self.end_headers()
        self.wfile.write(body)
if __name__=='__main__': HTTPServer(('0.0.0.0',8000),MetricsHandler).serve_forever()
