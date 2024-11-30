from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def new_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/new_request.html', {'form': form})

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_requests/request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'service_requests/request_detail.html', {'service_request': service_request})
