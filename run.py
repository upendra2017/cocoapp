# -*- encoding: utf-8 -*-

from cocoapp import app
from cocoapp.cocomodel import *  # clunky for now - needs to be this path for unpickling model

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
