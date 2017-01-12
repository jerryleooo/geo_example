# -*- coding: utf-8 -*-

from flask import render_template, request
from geo_example.models.point import ExamplePoint


def index():
    if request.method == 'GET':
        center = ExamplePoint.query_by_member("center")
        if not center:
            center = ExamplePoint.create(120, 40, 'center')
        else:
            center = center[0]
    else:
        form = request.form
        center = ExamplePoint.create(form["longitude"],
                                     form["latitude"],
                                     form["member"])

    points = ExamplePoint.query_by_pos(center.longitude,
                                       center.latitude, 10000, 'km')
    for point in points:
        point.distance = ExamplePoint.dist(point, center)

    points = [p.as_dict() for p in points]

    return render_template("index.html", **locals())
