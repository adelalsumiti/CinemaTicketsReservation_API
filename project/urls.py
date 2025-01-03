from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.viewsets_movie)
router.register('reservation', views.viewsets_reservation)
    
    
    


urlpatterns = [
    path('admin/', admin.site.urls),
    
#  1. WithOut Rest AND No model Query FBV
    path('django/jsonresponsenomodel/', views.no_rest_no_model),
    
# 2. model Data Default django no rest
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),

# 3.1 GET POST From Rest FrameWork Function based view @api_view
    path('rest/fbv/', views.FBV_List),
    
# 3.2 'GET','PUT','DELETE' From Rest FrameWork Function based view @api_view
    path('rest/fbv/<int:pk>', views.FBV_pk),

# 4.1 GET POST From Rest FrameWork Class based view APIView
    path('rest/cbv/', views.CBV_List.as_view()),
    
# 4.2 'GET','PUT','DELETE' From Rest FrameWork Class based view APIView
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),


# 5.1 GET POST From Rest FrameWork Class based view mixins
    path('rest/mixins/', views.mixins_list.as_view()),
    
# 5.2 'GET','PUT','DELETE' From Rest FrameWork Class based view generics
    path('rest/mixins/<int:pk>', views.mixins_pk.as_view()),

# 6.1 GET POST From Rest FrameWork Class based view mixins
    path('rest/generics/', views.generics_list.as_view()),
    
# 6.2 'GET','PUT','DELETE' From Rest FrameWork Class based view generics
    path('rest/generics/<int:pk>', views.generics_pk.as_view()),

# 7 Viewsets  
    path('rest/viewsets/', include(router.urls)),
    
# 8 Find Movie  
    path('fbv/findmovie/', views.find_movie),
    
# 9 New Reservation 
    path('fbv/newreservation/', views.new_reservation),

    

]
