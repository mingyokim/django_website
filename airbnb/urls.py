from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.get_city, name='get_city'),
	#url(r'^/heatmap$', views.show_heatmap, name='heatmap'),
	#url(r'^/heatmap/handler$', views.handler, name='handler'),
]
