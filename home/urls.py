from django.urls import path
from .views import home_view, about_view, education_view, experience_view, project_view, contact_view, skill_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('education/', education_view, name='education'),
    path('experience/', experience_view, name='experience'),
    path('project/', project_view, name='project'),
    path('contact/', contact_view, name='contact'),
    path('skill/', skill_view, name='skill'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
