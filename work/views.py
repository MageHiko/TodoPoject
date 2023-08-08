from django.shortcuts import render, redirect
from work.models import WorkModel
from django.views.generic import View

class WorkView(View):
    def get(self, request, *args, **kwargs):
        works = WorkModel.objects.all()
        context = {
            "works": works
        }

        return render (request, "my_work.html", context)

    def post(self, request, *args, **kwargs):
        pass

# Create your views here.
