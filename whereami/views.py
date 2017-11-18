from django.http import HttpResponse
from django.views import generic
from .models import Travel, ArtObject
from django.shortcuts import render


class LandingView(generic.TemplateView):
    template_name = 'whereami/about.html'


whoami = LandingView.as_view()

def travel_list(request):
    travels = Travel.objects.all()
    return render(request, 'whereami/travel_list.html', {'travels': travels})

def art_list(request):
    arts = ArtObject.objects.all()
    return render(request, 'whereami/art_list.html', {'arts': arts})

class ArtByCategoryListView(generic.ListView):
    template_name = 'whereami/art_category_list.html'
    model = ArtObject
    technique = None


    def get_queryset(self):
        """Filter art objects by technique"""
        queryset = super(ArtByCategoryListView, self).get_queryset()
        return queryset.filter(technique=self.technique).order_by('year')


painting_list = ArtByCategoryListView.as_view(technique=ArtObject.CATEGORY.PAINTING)
collage_list = ArtByCategoryListView.as_view(technique=ArtObject.CATEGORY.COLLAGE)
lino_list = ArtByCategoryListView.as_view(technique=ArtObject.CATEGORY.PAINTING)
installation_list = ArtByCategoryListView.as_view(technique=ArtObject.CATEGORY.COLLAGE)


class TravelDetailView(generic.DetailView):
    template_name = 'whereami/travel_details.html'

    model = Travel

    def get_context_data(self, **kwargs):
        context = super(TravelDetailView, self).get_context_data(**kwargs)
        travel = context['object']

        return context

travel_details = TravelDetailView.as_view()