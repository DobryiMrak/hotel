from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
	path('resedent/new/', views.ResedentCreateView.as_view(), name='resedent_new'),
	path('resedent/list/', views.ResedentListView.as_view(), name='resedent_list'),
	path('resedent/<int:pk>/delete', views.ResedentDeleteView.as_view(), name='resedent_delete'),
	path('resedent/<int:pk>/edit/', views.ResedentEditView.as_view(), name='resedent_edit'),
	path('resedent/<int:pk>/', views.ResedentDetailView.as_view(), name='resedent_detail'),

	path('nomer/list', views.NomerListView.as_view(), name='nomer_list'),
	path('nomer/new/', views.nomer_new, name='nomer_new'),
	path('nomer/<int:pk>/', views.NomerDetailView.as_view(), name='nomer_detail'),
	path('nomer/<int:pk>/edit/', views.NomerEditView.as_view(), name='nomer_edit'),
	path('nomer/<int:pk>/delete/', views.NomerDeleteView.as_view(), name='nomer_delete'),

	path('checkin/new/', views.CheckinCreateView.as_view(), name='checkin_new'),
	path('checkin/<int:pk>/', views.CheckinDetailView.as_view(), name='checkin_detail'),
	path('checkin/<int:pk>/delete/', views.CheckinDeleteView.as_view(), name='checkin_delete'),
	path('checkin/list/', views.CheckinListView.as_view(), name='checkin_list'),
	path('checkin/<int:pk>/document', views.CheckinDocumentView.as_view(), name='checkin_document'),
	path('checkin/<int:pk>/document_out', views.CheckoutDocumentView.as_view(), name='checkout_document'),

	path('upload', views.model_form_upload, name='upload_file'),
	path('block', TemplateView.as_view(template_name='registration/block_1_minute.html'), name='block'),

	path('', TemplateView.as_view(template_name='home.html'), name='home')
]