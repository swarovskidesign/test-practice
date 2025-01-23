from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('ap.urls', namespace='main')),
    path('mywallets/', include('usermanage.urls', namespace='usermanage')),
    path('operations/', include('transactions.urls', namespace='wallets')),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)