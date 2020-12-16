from django.urls import path
from .views import Case_study, load_territory_id

urlpatterns = [
    path('', Case_study.as_view(), name='case_study'),
    path('ajax/load_territory_id/', load_territory_id, name='load_territory_id'),
]
