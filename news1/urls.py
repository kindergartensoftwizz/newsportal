from django.urls import path
from news1 import views
from django.contrib.auth.views import ( LoginView, LogoutView, PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView )


urlpatterns = [
    path('newsportal/',views.showhomenews),
	path('social/',views.socialpageview.as_view()),
	path('test/',views.testpageview.as_view()),
	path('test2/',views.test2pageview.as_view()),
	
	path('about/',views.aboutview.as_view()),
	path('contact/',views.contactpageview.as_view()),
	
	path('insert', views.insert),
    path('newsdetail/<int:cat>', views.shownews),
    path('detailnews/<int:id>', views.detailnewsview),
    path('videonews/<int:id>', views.videonewsview),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('sign/',views.signup),
    path('insertcomment/',views.insertcomment),
    path('comment/<int:id>',views.commentview),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('updatecomment/<int:id>', views.updatecomment),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('addnews/',views.addnewsview),
    path('insertnews/',views.insertnews),
]	