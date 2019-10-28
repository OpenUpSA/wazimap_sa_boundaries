from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^api/v1/categories/(?P<id>\d+)/province/(?P<province_code>\w+)$", views.CategoryProvinceView.as_view(), name="category_province"),
]
