# ^_^ coding: utf-8 ^_^

# Copyright 2015 Joaquín Muñoz M.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import tornado.web
import tornado.websocket

_handler_names = []
_handler_methods = {}
_handler_routes = {}
_static_folders = {}

def route(route, websocket=False):
    def decorator(func):
        handler_name = func.__name__.capitalize()
        methods = func()
        if type(methods) not in [list, tuple]:
            raise Exception(u'Handler function must return a list or a tuple')

        if websocket:
            handler_name = 'WS' + handler_name

        _handler_names.append(handler_name)
        _handler_methods[handler_name] = methods
        _handler_routes[handler_name] = route

    return decorator

def add_static(static_url, static_folder):
    _static_folders[static_url] = static_folder


def app():
    handlers = []
    for name in _handler_names:
        handler_type = tornado.websocket.WebSocketHandler \
            if name.startswith('WS') else tornado.web.RequestHandler

        handler = type(
            name, (handler_type,),
            {method.__name__: method for method in _handler_methods[name]}
        )
        handlers.append((_handler_routes[name], handler))

    for url, folder in _static_folders.iteritems():
        handlers.append((url, tornado.web.StaticFileHandler, {'path': folder}))

    return tornado.web.Application(handlers)
