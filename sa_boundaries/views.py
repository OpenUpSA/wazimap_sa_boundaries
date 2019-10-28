# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from explorer.serializer import CategorySerializer, LocationSerializer
from explorer.models import Location, Category
from django.http import JsonResponse
from models import Province

class CategoryProvinceView(APIView):
    def get(self, request, id, province_code):
        province = get_object_or_404(Province, pr_mdb_c=province_code)
        locations = Location.objects.filter(category__id=id, coordinates__within=province.geom)

        sr = LocationSerializer(many=True, context={"request": request})

        return JsonResponse(sr.to_representation(locations))
