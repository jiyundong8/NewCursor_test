#While 循环：监控 TCP/80 HTTP 服务是否开放


from http.server import HTTPServer, CGIHTTPRequestHandler  # pyright: ignore[reportDeprecated]
port = 80
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()
