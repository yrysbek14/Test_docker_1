from rest_framework import routers
from django.urls import path, include
from .views import (UserProfileListAPIView, UserProfileDetailAPIView,
                    CategoryListAPIView, CategoryDetailAPIView,
                    StoreListAPIView, StoreListDitailAPIView,
                    OrderViewSet, CourierProductViewSet,
                    ReviewCreateAPIView, ReviewEditAPIView, OrderStatusListView,
                    OrderStatusDitailView, StoreViewSet, RegisterView,
                    LogoutView, LoginView)


router = routers.SimpleRouter()
router.register(r'store_create', StoreViewSet)
router.register('orders', OrderViewSet)
router.register('couriers', CourierProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreListDitailAPIView.as_view(), name='store_detail'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_crate'),
    path('review/create/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),
    path('order_status/', OrderStatusListView.as_view(), name='order_list'),
    path('order_status/<int:pk>/', OrderStatusDitailView.as_view(), name='order_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]