import machine
import network
import time
import ujson
import _thread
import index

try:
    import usocket as socket
except:
    import socket

class FreeIDE:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.status_LED = machine.Pin(2, machine.Pin.OUT)
        self.status_LED.value(1)
        self.wifi = network.WLAN(network.STA_IF)
        self._update = None
        self.wifi_connection()
        _thread.start_new_thread(self.run, ())
        bf = open("boot.py", "w")
        bf.write('#bootloader\r\nimport index\r\n\r\ntry:\r\n    mf = open("main.py", "r")\r\n    mprog = mf.read()\r\n    mf.close()\r\n    loge = open("log.dat", "w")\r\n    loge.write("welcome")\r\n    loge.close()\r\n    exec(mprog)\r\nexcept Exception as e:\r\n    loge = open("log.dat", "w")\r\n    while(len(str(e)) != loge.write(str(e))):\r\n        print("can not write")\r\n    loge.close()\r\n    exec(index.backup)\r\n    ')
        bf.close()
        
    def wifi_connection(self):
        self.wifi.active(True)
        while not self.wifi.isconnected():
            try:
                self.wifi.connect(self.ssid, self.password)
            except OSError as e:
                print(e)
            time.sleep(1)
        print("WiFi connected")
        print('Listening on', self.wifi.ifconfig()[0])
        self.status_LED.value(0)
        self.connection = True
        

    def urlparse(self, url):
        scheme, netloc, path, params, query, fragment = '', '', '', '', '', ''
        if '#' in url:
            url, fragment = url.split('#', 1)
        if '?' in url:
            url, query = url.split('?', 1)
        if '://' in url:
            scheme, url = url.split('://', 1)
            if '/' in url:
                netloc, path = url.split('/', 1)
                path = '/' + path
            else:
                netloc = url
        else:
            path = url
        return scheme, netloc, path, params, query, fragment

    def parse_qs(self, query):
        params = {}
        if query:
            pairs = query.split('&')
            for pair in pairs:
                if '=' in pair:
                    key, value = pair.split('=', 1)
                    if key in params:
                        params[key].append(value)
                    else:
                        params[key] = [value]
                else:
                    if pair in params:
                        params[pair].append('')
                    else:
                        params[pair] = ['']
        return params

    def handle_request(self, client):
        request = client.recv(1024).decode('utf-8')
        request_line = request.split('\r\n')[0]
        parts = request_line.split(' ')
        if len(parts) != 3:
            client.send('HTTP/1.1 400 Bad Request\r\n\r\n')
            client.close()
            return
        method, url, _ = parts

        body_start = request.find('\r\n\r\n') + 4
        if body_start > 0:
            body = request[body_start:]
        else:
            body = ''

        parsed_url = self.urlparse(url)
        query_params = self.parse_qs(parsed_url[4])

        if method == 'GET':
            if parsed_url[2] == '/':
                response = index.html.replace('{ip}', str(self.wifi.ifconfig()[0])) #config endpoints
                lastProgram = open('main.py', 'r')
                response = response.replace('{lastProgram}', lastProgram.read()) #config program
                lastProgram.close()
                logf = open('log.dat', 'r')
                response = response.replace('{welcome}', logf.read())
                print(logf.read())
                logf.close()
                client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
                client.sendall(response)
        elif method == 'POST':
            if parsed_url[2] == '/run':
                try:
                    post_data = ujson.loads(body)
                    code = post_data.get('code', '')
                    try:
                        compile(code, 'test', 'exec')
                        main = open("main.py", "w")
                        main.write(code)
                        main.close()
                        self._update = True
                        response = {'output': 'successfully uploading', 'code': code}
                    except Exception as e:
                        print(f"Syntax error : {e}")
                        response = {'output': e, 'code': code}
                    client.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n')
                    client.send(ujson.dumps(response))
                except ValueError:
                    response = {'error': 'Invalid JSON'}
                    client.send('HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n\r\n')
                    client.send(ujson.dumps(response))
                    self._update = False
            elif parsed_url[2] == '/compile':
                try:
                    post_data = ujson.loads(body)
                    code = post_data.get('code', '')
                    try:
                        compile(code, 'test', 'exec')
                        response = {'output': 'Code compiled successfully', 'code': code}
                    except Exception as e:
                        print(f"Syntax error : {e}")
                        response = {'output': e, 'code': code}
                    client.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n')
                    client.send(ujson.dumps(response))
                except ValueError:
                    response = {'error': 'Invalid JSON'}
                    client.send('HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n\r\n')
                    client.send(ujson.dumps(response))
                    self._update = False
            else:
                response = {'error': 'Not Found'}
                client.send('HTTP/1.1 404 Not Found\r\nContent-Type: application/json\r\n\r\n')
                client.send(ujson.dumps(response))
                self._update = False
        else:
            client.send('HTTP/1.1 405 Method Not Allowed\r\n\r\n')
            self._update = False
        client.close()

    def startServer(self):
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(addr)
        s.listen(5)
        try:
            client, addr = s.accept()
            print('Client connected from', addr)
            self.handle_request(client)
        except Exception as e:
            print('Error:', e)
        finally:
            s.close()

    def run(self):
        try:
            while True:
                self.startServer()
                if self._update is True:
                    machine.reset()
        except Exception as e:
            print('Server encountered an error:', e)
            time.sleep(5)  # Wait before restarting

