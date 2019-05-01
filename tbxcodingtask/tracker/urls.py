from django.conf.urls import url

from .views import (
	my_tickets_view,
	create_project_view,
	update_project_view,
	project_view,
	create_ticket_view,
	update_ticket_view,
	project_list_view,
	update_project_view
)

urlpatterns = [
    url(r'^projects/$', project_list_view, name='project_list'),
    url(r'^projects/create/$', create_project_view, name='project_create'),
    url(
    	r'^projects/(?P<project_id>\d+)/tickets/create$',
    	create_ticket_view,
    	name='ticket_create'
	),
    url(
    	r'^projects/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/edit$',
    	update_ticket_view,
    	name='ticket_update'
	),
    url(
    	r'^projects/(?P<project_id>\d+)/edit/$',
    	update_project_view,
    	name='project_update'
	),
    url(r'^projects/(?P<project_id>\d+)/$', project_view, name='project_detail'),
    url(r'^$', my_tickets_view, name='my_tickets'),
]
