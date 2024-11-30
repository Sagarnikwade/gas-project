from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root URL to login page
def homepage(request):
    return redirect('login')  # Redirects to the login page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),  # Add this line to redirect the root URL
    path('accounts/', include('accounts.urls')),
    path('requests/', include('service_requests.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
