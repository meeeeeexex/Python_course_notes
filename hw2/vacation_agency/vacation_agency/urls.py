from django.contrib import admin
from django.urls import path
# from agency.views import WelcomePageView, RatingView
from agency.views.UsersView import UserViewRest, ExcursionViewRest
from agency.views.RegisterView import UserRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserViewRest.as_view()),
    path('excursion/', ExcursionViewRest.as_view()),
    path('register/', UserRegisterView.as_view()),

]
