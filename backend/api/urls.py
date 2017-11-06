from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import StopsView, TripsView

urlpatterns = {
    url(r'^stops/$', StopsView.as_view()),
    url(r'^trips/$', TripsView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
