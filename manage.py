# -*- coding: utf-8  -*-

import urllib
from flask import current_app
from flask_script import (Manager, Shell, Server)

from geo_example.app import create_app

app = create_app()

manager = Manager(app)

manager.add_command("runserver", Server("0.0.0.0", port=8888))

def make_shell_context():
    return dict(app=current_app)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def list_routes():

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == "__main__":
    manager.run()
