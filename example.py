import tornado.ioloop
import Tristana

@Tristana.route('/')
def main_handler():
    def get(self):
        self.write('Hello, world')

    return [get]

@Tristana.route('/websocket', websocket=True)
def echo_websocket():
    def check_origin(self, origin):
        return True

    def open(self):
        print("Websocket opened")

    def on_message(self, message):
        self.write_message(u"You said: {}".format(message))

    def on_close(self):
        print("Websocket closed")

    return [open, on_message, on_close, check_origin]


@Tristana.route('/websocket_test')
def socket_sample():
    def get(self):
        self.render('websocket_sample.html')

    return [get]

Tristana.add_static(r'/static/(.*)', './web/static/')

if __name__ == '__main__':
    app = Tristana.app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
