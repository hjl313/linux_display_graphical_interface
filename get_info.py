from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # 发送HTML响应
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open('index.html', 'r') as file:
                self.wfile.write(file.read().encode('utf-8'))
        elif self.path == '/gethostIp':
            # 获取进程数量
            hostIp = os.popen("ifconfig ens33 | grep  \"inet \" | awk -F ' ' '{print $2}'").read().strip()

            # 创建JSON响应
            response = json.dumps({'hostIp': hostIp})

            # 设置HTTP响应头
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(response)))
            self.end_headers()

            # 发送响应内容
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
