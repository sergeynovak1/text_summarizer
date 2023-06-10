from django.urls import path
from .views import MethodView, LinkView

urlpatterns = [
    path("<int:id>", MethodView.as_view(), name="method"),
    path("get_link", LinkView.as_view(), name='link')
]