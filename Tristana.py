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

_controller_names = []
_controller_methods = {}
_controller_routes = {}

def route(route):
    def decorator(func):
        controller_name = func.__name__.capitalize()
        methods = func()
        if type(methods) not in [list, tuple]:
            raise Exception(u'Controller function must return a list or a tuple')

        _controller_names.append(controller_name)
        _controller_methods[controller_name] = methods
        _controller_routes[controller_name] = route

    return decorator

def app():
    controllers = []
    for name in _controller_names:
        controller = type(
            name, (tornado.web.RequestHandler,),
            {method.__name__: method for method in _controller_methods[name]}
        )
        controllers.append((_controller_routes[name], controller))


    return tornado.web.Application(controllers)
