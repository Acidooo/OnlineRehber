from django.http import request
from .models import Contact
from django.db.models import Q
from django.contrib import messages
from django.db.models import manager
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager = self.request.user)
        

class ContactDetailView(LoginRequiredMixin, DetailView):    
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'


@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(isim__icontains=search_term ) | Q(soyisim__icontains=search_term )  | Q(email__icontains=search_term ) | Q(telefon__icontains=search_term )
            )
        context = {
            'search_term': search_term,
            'contacts': search_results.filter(manager = request.user)
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['isim','soyisim','email','telefon','cinsiyet','bilgi','foto','etiket']
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        # messages.error()
        messages.success(self.request, 'Kayıt Başarılı')
        return redirect('home')


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Kayıt Silindi')
        return super().delete(self, request, *args, **kwargs)
    

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['isim','soyisim','email','telefon','cinsiyet','bilgi','foto','etiket']

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, 'Güncelleme Başarılı')
        return redirect('detail', instance.pk) 


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    




# def home(request):
#     context = {
#         'contacts':Contact.objects.all()
#     }
#     return render(request, 'index.html',context)

# def detail(request,id):
#     context = {
#         'contact':get_object_or_404(Contact, pk=id)
#     }
#     return render(request,'detail.html',context)