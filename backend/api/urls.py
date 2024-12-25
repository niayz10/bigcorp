
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from . import views

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="BigCorp API ",
        default_version="v1",
        description="BigCorp API description",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="admin@bigcorp.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    # Products API
    path('products/', views.ProductListApiView.as_view()),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view()),
    # Reviews API
    path('reviews/create', views.ReviewCreateView.as_view(), name='review-create'),
    # Users API
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # Docs
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]