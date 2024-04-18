from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
                  path("", ProductListView.as_view(), name="index"),
                  path("contacts/", ContactsView.as_view(), name="contacts"),
                  path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
                  path("create_product/", ProductCreateView.as_view(), name="create_product"),
                  path("update_product/<int:pk>/", ProductUpdateView.as_view(), name="update_product"),
                  path("delete_product/<int:pk>/", ProductDeleteView.as_view(), name="delete_product"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
