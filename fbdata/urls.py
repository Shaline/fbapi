from django.conf.urls import url

from fbdata import views


app_label = 'fbdata'

urlpatterns = [
    url(r'^add-label/json/', views.AddLabelJson.as_view(), name='add-label-json'),
]
