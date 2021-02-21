from django.shortcuts import render
from movies.models import Actor, Movie
from django.views.generic import CreateView, ListView
from movies.forms import MovieForm, ActorForm


class Create_actor(CreateView):
    model = Actor
    form_class = ActorForm
    template_name = "create_actor.html"
    success_url = "/actor/list"


class Create_movie(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "create_movie.html"
    success_url = "/movie/list"


class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"


class ActorListView(ListView):
    model = Actor
    template_name = "actor_list.html"