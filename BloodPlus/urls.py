from django.conf.urls import url
from .views import CreateDonorAPIView,ReadDonorAPIView,UpdateDonorAPIView,DeleteDonorAPIView

urlpatterns=[
    url("createDonor",CreateDonorAPIView.as_view(),name="create-donor"),
    url("readDonor",ReadDonorAPIView.as_view()),
    url("updateDonor/(?P<pk>.+)",UpdateDonorAPIView.as_view()),
    url("deleteDonor/(?P<pk>.+)",DeleteDonorAPIView.as_view()),
]