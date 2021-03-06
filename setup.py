from setuptools import setup
from SimpleWebEditor import __version__

setup(
    # Application name:
    name = "SimpleWebEditor",

    # Version number:
    version = __version__,

    # Application author details:
    author = "Brahm Lower",
    author_email = "bplower@gmail.com",

    # License
    license = "GPL-3.0",

    # Packages:
    packages = ["SimpleWebEditor"],

    package_dir = {'SimpleWebEditor': 'SimpleWebEditor'},

    package_data = {
        "SimpleWebEditor": [
            "static/index.html",
            "static/vendor/jquery.min.js",
            "static/vendor/bootstrap.min.css",
            "static/vendor/bootstrap.min.js",
            "static/fonts/glyphicons-halflings-regular.ttf",
            "static/fonts/glyphicons-halflings-regular.woff",
            "static/fonts/glyphicons-halflings-regular.woff2",
            "static/vendor/bootstrap-treeview.min.css",
            "static/vendor/bootstrap-treeview.min.js",
            "static/vendor/ace.js",
            "static/simplewebeditor.css",
            "static/simplewebeditor.js"
        ]
    },

    scripts = ['scripts/simplewebeditor'],

    # Details:
    url = "http://github.com/bplower/SimpleWebEditor/",
    bugtrack_url = "https://github.com/bplower/SimpleWebEditor/issues",
    download_url = 'https://github.com/bplower/SimpleWebEditor/tarball/{}'.format(__version__),

    # Description:
    description = "A simple server for editing remote files in a browser.",
    long_description = open("README.rst").read(),

    # Dependant packages:
    install_requires = [
        "Flask>=0.11.1",
        "docopt"
    ],

    zip_safe = False,
)
