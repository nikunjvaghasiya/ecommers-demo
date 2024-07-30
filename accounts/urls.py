
from django.contrib import admin
from django.urls import path
from accounts import views as account_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("signin/", account_views.index, name="signin"),
    path("signup/", account_views.signup, name="signup"),
    path('dashboard/', account_views.dashboard, name="dashboard"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
