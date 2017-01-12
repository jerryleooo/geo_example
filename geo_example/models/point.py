# -*- coding: utf-8 -*-

import os
from geo_python import Point


class ExamplePoint(Point):

    __key__ = 'example_point'

    def as_dict(self):
        return {
            "member": self.member,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "distance": self.distance,
            "geohash": self.geo_hash()
        }

    config = {
        "GEO_REDIS_HOST": os.getenv("GEO_REDIS_HOST") or "localhost",
        "GEO_REDIS_PORT": os.getenv("GEO_REDIS_PORT") or 6379,
        "GEO_REDIS_PASSWORD": os.getenv("GEO_REDIS_PASSWORD") or None,
        "GEO_REDIS_DB": os.getenv("GEO_REDIS_DB") or 0
    }
