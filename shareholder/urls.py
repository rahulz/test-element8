from django.urls import path

from shareholder.views import ShareHoldersView, AddShareHoldersView, ShareHoldersDetailView

urlpatterns = [
    path('', ShareHoldersView.as_view()),
    path('add/', AddShareHoldersView.as_view()),
    path('detail/<int:pk>/', ShareHoldersDetailView.as_view(), name='shareholder_detail')
]
