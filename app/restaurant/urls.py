from django.urls import path

from .views import (
    create_restaurant,
    update_restaurant,
    get_restaurants,

    create_menu,
    update_menu,
    get_menus,

    create_item,
    update_item,

)

urlpatterns = [
    path("create_restaurant/", create_restaurant),
    path("update_restaurant/<int:id>/", update_restaurant),
    path("get_restaurants/", get_restaurants),

    path("create_menu/", create_menu),
    path("update_menu/<int:id>/", update_menu),
    path("get_menus/", get_menus),

    path("create_item/", create_item),
    path("update_item/<int:id>/", update_item),
]