from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [
    path('dashboard/',views.index, name="index"),
    path('about/',views.about,name="about"),
    path('about/hindi',views.hindi,name="hindi"),
    path('coming-soon/',views.comingsoon, name="comingsoon"),
    path('reviews-page/',views.reviewspage, name="reviewspage"),
    path('add-events/',views.addevents, name="addevents"),
    path('add-past-events/',views.addpastevents, name="addpastevents"),
    path('events/',views.events, name="events"),
    path('past-events/',views.past_events, name="past_events"),
    path('feedback/',views.feedback, name="feedback"),
    path('updatefeedback/<int:pk>/',views.updatefeedback, name="updatefeedback"),
    path('contact-page/',views.contactuspage, name="contactuspage"),
    path('login/', views.handleLogin, name='login'),
    path('', views.homepage, name='homepage'),
    path('contact/', views.contactpage, name='contactpage'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('signup/', views.signUp, name='signUp'),
    path('profile/', views.profile, name='profile'),
    path('payment/', views.payment, name='payment'),
    path('response/', views.response, name='response'), 
    path('admin-home/', views.admin_home, name='admin_home'),
    path('admin-all-transactions/', views.admin_all_transactions, name='admin_all_transactions'),
    path('all-transactions/', views.all_transactions, name='all_transactions'),
    path('admin-all-users/', views.admin_all_users, name='admin_all_users'),
    path('regular-update/', views.regular_update, name='regular_update'), 
    path('fixed-rate-update/', views.fixed_rate_update, name='fixed_rate_update'), 
    path('fixed-rate-page/', views.fixed_rate_page, name='fixed_rate_page'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('company-capital/', views.company_capital_page, name='company_capital'),
    path('admin-withdrawal-requests/', views.admin_withdrawal_requests, name='admin_withdrawal_requests'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset/done', views.password_reset_done, name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
     path('pdf-all-transactions/', views.pdf_all_transactions, name='pdf_all_transactions'),
     path('update-withdraw-status/checkby/nobackallowed/be72fa80-f77c-11ec-b939-0242ac120002/<int:id>/',views.update_withdrawl_requests,name="update_withdrawl_requests"),
     path('delete-withdraw-status/checkby/nobackallowed/be72fa80-f77c-11ec-b939-0242ac120002/<int:id>/',views.delete_withdrawl_requests,name="delete_withdrawl_requests"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin settings
admin.site.site_header = 'GD Capital'                    # default: "Django Administration"
admin.site.index_title = 'Major Admin Panel'                 # default: "Site administration"
admin.site.site_title = 'GD Capital' # default: "Django site admin"
