from django.urls import path, re_path, register_converter
from . import views

class YearConverter:
  regex = "20\d{2}"

  def to_python(self, value):
    return int(value)

  def to_url(self, value):
    return str(value)

register_converter(YearConverter, 'year')

app_name = 'instagram' # URL Reverse에서 namespace역할을 하게 됨

urlpatterns = [
  path('', views.post_list),
  path('<int:pk>/', views.post_detail),
  # path('archives/<int:year>/', views.archives_year),
  path('archives/<year:year>/', views.archives_year),
]