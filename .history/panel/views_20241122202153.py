from django.shortcuts import render

# Create your views here.
def admin_panel(request):
    return render(request, 'panel/admin_panel.html')