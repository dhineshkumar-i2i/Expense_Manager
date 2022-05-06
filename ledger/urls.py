from django.urls import path
from rest_framework.routers import DefaultRouter

from ledger.views import LedgerViewSet, split_expense, load_pdf

router = DefaultRouter()
router.register('', LedgerViewSet, basename='ledger')
urlpatterns = router.urls
urlpatterns.append(path('<int:ledger_id>/split', split_expense,
                        name='split'))
urlpatterns.append(path('loadPdf', load_pdf, name='loadPdf'))
