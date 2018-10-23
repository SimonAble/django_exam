from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),

    # <<-------NEW USER ROUTES------>>
    url(r'^new_user$', views.new_user),
    url(r'^user_dash$', views.user_dash),

    # <<-------LOGIN/LOGOUT ROUTES------>>
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),

    # <<-------ADD ITEM ROUTES------>>
    url(r'^add_item$', views.add_item),
    url(r'^create_item$', views.create_item),

    # <<-------REMOVE ITEM ROUTES------>>
    url(r'^remove_item/(?P<item_id>\d+)$',views.remove_item),

    # <<-------FAVORITE ITEM ROUTES------>>
    url(r'^join_item/(?P<item_id>\d+)$',views.join_item),

    # <<-------UNFAVORITE ITEM ROUTES------>>
    url(r'^unjoin_item/(?P<item_id>\d+)$',views.unjoin_item),

    # <<-------#DISPLAY ITEM------>>
    url(r'^show/(?P<item_id>\d+)$', views.show)

]