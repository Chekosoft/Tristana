# ^_^ coding: utf-8 ^_^

from setuptools import setup

setup(
    name=u'Tristana',
    version=u'0.1',
    description=u'A layer to build Tornado apps at a faster rate.',
    packages = ['Tristana'],
    install_requires = [
        'tornado>=4.2.1'
    ]
)