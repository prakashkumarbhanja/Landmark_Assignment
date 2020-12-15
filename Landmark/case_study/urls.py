from django.urls import path
from .views import Case_study, load_item_id

urlpatterns = [
    path('', Case_study.as_view(), name='case_study'),
    path('ajax/load_item_id/', load_item_id, name='load_item_id'),
]
