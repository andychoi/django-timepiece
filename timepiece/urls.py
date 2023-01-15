from django.conf.urls import include
from django.urls import reverse_lazy, re_path
from django.views.generic import RedirectView


urlpatterns = [
    # Redirect the base URL to the dashboard.
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('dashboard'), permanent=False)),

    re_path('', include('timepiece.crm.urls')),
    re_path('', include('timepiece.contracts.urls')),
    re_path('', include('timepiece.entries.urls')),
    re_path('', include('timepiece.reports.urls')),
]
