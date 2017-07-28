#!/usr/bin/env python
from app import app
import os

myPort = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0',debug=True, port=myPort)
