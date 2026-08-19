from django.urls import path
from.views import holiday_request_create, holiday_request_list, holiday_request_approve, holiday_request_reject, holiday_request_history

urlpatterns = [
    path("request/", holiday_request_create, name="holiday_request_create"),
    path("requests/", holiday_request_list, name="holiday_request_list"),
    path("requests/<int:pk>/approve/", holiday_request_approve, name="holiday_request_approve"),
    path("requests/<int:pk>/reject/", holiday_request_reject, name="holiday_request_reject"),
    path("history/", holiday_request_history, name="holiday_request_history"),
]

