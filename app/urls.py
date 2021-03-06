from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register("list", views.AuctionViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('bid/<int:id>', views.bid, name="auction_detail"),
    path('auctions/', include(router.urls)),
    path('auctions/<int:id>', views.auctionDetail),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
