# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

class Province(models.Model):
    pr_mdb_c = models.CharField(max_length=5, verbose_name="Province code")
    pr_code = models.FloatField()
    pr_code_st = models.CharField(max_length=1)
    pr_name = models.CharField(max_length=25)
    albers_are = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=-1)

    def __str__(self):
        return str(self.pr_name)

# Auto-generated `LayerMapping` dictionary for province model
province_mapping = {
    'pr_mdb_c' : 'PR_MDB_C',
    'pr_code' : 'PR_CODE',
    'pr_code_st' : 'PR_CODE_st',
    'pr_name' : 'PR_NAME',
    'albers_are' : 'ALBERS_ARE',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}
