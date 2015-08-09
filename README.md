Tristana
========
![SD Tristana by sinrisk](http://i.imgur.com/oFtkdmF.png)

## About

Tristana is a layer which provides a faster way to write Tornado web applications.
Think of it as a way to build Tornado apps using Flask/Bottle syntax.

Still in development. Use at your own risk.

## How?

The Tornado "Hello world" application

```syntax=Python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

Can be written as:

```syntax=Python
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
```

## Caveats

- Not tested using the coroutine or asynchronous decorators.
- Only generates WebRequestHandler subclasses.


## Why?

I just got bored of writing lots of code to add one route for an application I am currently developing using Tornado.
So, I thought about a way to write Tornado apps as Flask (sort of) apps.

## License

Tristana is licensed under the Apache Software License v2.0 (just like Tornado). You can read the LICENSE file for
a copy of it.

## One more thing...
Apologies to the BDFL, if required.
