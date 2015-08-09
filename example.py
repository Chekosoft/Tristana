import tornado.ioloop
import Tristana

@Tristana.route('/')
def main_handler():
    def get(self):
        self.write('Hello, world')

    return [get]

if __name__ == '__main__':
    app = Tristana.app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()