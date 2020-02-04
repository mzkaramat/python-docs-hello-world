from flask import Flask, render_template, request
from werkzeug import secure_filename
import subprocess
import os
import uuid
import cv2
import math
from shutil import copyfile
import json
import Augmentor
from distutils.dir_util import copy_tree

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
