# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import renderers
from explorer.serializer import CategorySerializer, LocationSerializer
from explorer.models import Location, Category
from django.http import JsonResponse
from models import Province
from rest_framework.response import Response
import csv
from StringIO import StringIO


class GISCSVRenderer(renderers.BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'

    def render(self, data, media_type=None, renderer_context=None):
        fp = StringIO()
        writer = csv.writer(fp)
        for idx, feature in enumerate(data["features"]):
            headers = ["latitude", "longitude"]
            vals = []
            properties = feature["properties"]["data"]
            coordinates = feature["geometry"]["coordinates"]
            vals += coordinates
            for k, v in properties.items():
                vals.append(("%s" % v).encode("utf8"))
                headers.append(k)
            if idx == 0:
                writer.writerow(headers)
            writer.writerow(vals)

        return fp.getvalue()

class CategoryProvinceView(APIView):
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (GISCSVRenderer, )

    def get(self, request, id, province_code):
        province = get_object_or_404(Province, pr_mdb_c=province_code)
        locations = Location.objects.filter(category__id=id, coordinates__within=province.geom)

        sr = LocationSerializer(many=True, context={"request": request})

        return Response(sr.to_representation(locations))
