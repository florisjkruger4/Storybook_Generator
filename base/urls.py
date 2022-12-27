from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.fantasyPage, name="fantasy"),
    path('sportsPage', views.sportsPage, name="sports"),
    path('adventurePage', views.adventurePage, name="adventure"),
    path('spookyPage', views.spookyPage, name="spooky"),
    path('storyPage', views.storyPage, name="storyPage"),
    path('test', views.test, name="test"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)