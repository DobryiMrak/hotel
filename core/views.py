from django.shortcuts import render, redirect
from .models import Resedent, Nomer, Checkin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import NomerForm, DocumentForm
from users.models import CustomUser
import pyexcel
import os
from .models import Hotel
# Create your views here.


class ResedentCreateView(CreateView):
    model = Resedent
    template_name = 'resedent_new.html'
    fields = (
        "first_name",
        "second_name",
        "father_name",
        "burn_date",
        "gender",
        "phone_number",
        "pasport_seria",
        "pasport_number"
    )


class ResedentListView(ListView):
    model = Resedent
    template_name = 'resedent_list.html'


class ResedentDetailView(DetailView):
    model = Resedent
    template_name = 'resedent_detail.html'


class ResedentEditView(UpdateView):
    model = Resedent
    template_name = 'resedent_edit.html'
    fields = (
        "first_name",
        "second_name",
        "father_name",
        "burn_date",
        "gender",
        "phone_number",
        "pasport_seria",
        "pasport_number"
    )


class ResedentDeleteView(DeleteView):
    model = Resedent
    template_name = 'resedent_delete.html'
    success_url = reverse_lazy('resedent_list')


class NomerListView(ListView):
    model = Nomer
    template_name = 'nomer_list.html'


class NomerDeleteView(DeleteView):
    model = Nomer
    template_name = 'nomer_delete.html'
    success_url = reverse_lazy('nomer_list')


class NomerEditView(UpdateView):
    model = Nomer
    template_name = 'nomer_edit.html'
    fields = (
        "number",
        "square",
        "count_of_rooms",
    )


class NomerDetailView(DetailView):
    model = Nomer
    template_name = 'nomer_detail.html'


def nomer_new(request):
    if request.method == "POST":
        form = NomerForm(request.POST)
        if form.is_valid():
            nomer = form.save(commit=False)
            nomer.hotel = request.user.hotel
            nomer.save()
            return redirect('nomer_detail', pk=nomer.pk)
    else:
        form = NomerForm()
    return render(request, 'nomer_new.html', {'form': form})


class NomerCreateView(CreateView):
    model = Nomer
    template_name = 'nomer_new.html'
    fields = (
        "number",
        "square",
        "count_of_rooms",
    )


class CheckinCreateView(CreateView):
    model = Checkin
    template_name = 'checkin_new.html'
    fields = '__all__'


class CheckinListView(ListView):
    model = Checkin
    template_name = 'checkin_list.html'


class CheckinDeleteView(DeleteView):
    model = Checkin
    template_name = 'checkin_delete.html'
    success_url = reverse_lazy('checkin_list')


class CheckinDetailView(DetailView):
    model = Checkin
    template_name = 'checkin_detail.html'


class CheckinDocumentView(DetailView):
    model = Checkin
    template_name = 'checkin_document.html'


class CheckoutDocumentView(DetailView):
    model = Checkin
    template_name = 'checkout_document.html'


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            add_admins()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'simple_upload.html', {
        'form': form
    })


def add_admins(name_file='nti'):
    r = pyexcel.get_array(file_name='./media/documents/nti.xls')

    for row in r:
        user = CustomUser.objects.create_user(row[3], "nothing@mail.com", row[4])
        user.first_name = row[1]
        user.last_name = row[0]
        user.father_name = row[2]
        user.hotel = Hotel.objects.filter(number=row[6]).get()
        user.phone_number = row[5]
        user.save()
    os.remove('./media/documents/nti.xls')
