
from django.urls import path
from user.api.views import RegisterView

urlpatterns = [
 path('api1/',RegisterView.as_view(),name='registro')


]