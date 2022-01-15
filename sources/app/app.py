from flask import Flask, Blueprint, jsonify, render_template, flash, redirect, request, url_for
from .settings import *
from .models import User
from flask_login import current_user, login_required

from datetime import datetime, timedelta, timezone

from dateutil.relativedelta import relativedelta

import urllib

def display_log():
    return open("../bot/botlog.txt").read().replace("\n", "<br>")

@main.route('/')
def index():
    site = "<p>Telegram Bot Log</p>"

    site += "<div id=\"log\">" + display_log() + "</div>"

    return site


@main.route('/protected')
@login_required
def protected():
    return 'Hello, World!'

@main.route('/users')
def users():
    return jsonify([ (u.username, u.email) for u in User.query.all() ])


