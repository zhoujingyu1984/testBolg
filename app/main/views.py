#！/usr/bin/env python
#-*- coding utf8 -*-

from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
#from .forms import Namefrom
from .. import db
#from ..models import User

@main.route('/',methods=['GET','POST'])
def index():
    #form = NameFrom()
    #if form.validate_on_submit():
    pass
