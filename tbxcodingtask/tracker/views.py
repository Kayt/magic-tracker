from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from werkzeug.utils import redirect

from .forms import CommentForm, ProjectForm, TicketForm
from .models import Project, Ticket, Comment


class ProjectContextMixin(object):
    project = None

    def get_project(self):
        if not self.project:
            self.project = get_object_or_404(Project, pk=self.kwargs['project_id'])

        return self.project

    def get_context_data(self, **kwargs):
        context = super(ProjectContextMixin, self).get_context_data(**kwargs)
        context['current_project'] = self.get_project()
        return context


class MyTicketsView(TemplateView):
    template_name = "tracker/my_tickets.html"

    def get_context_data(self):
        if self.request.user.is_authenticated:
            tickets = (
                Ticket.objects
                .filter(assignees=self.request.user.pk)
                .order_by('-modified')
            )
        else:
            tickets = []

        return {
            'tickets': tickets
        }


my_tickets_view = MyTicketsView.as_view()


class ProjectListView(ListView):
    model = Project
    template_name = "tracker/project_list.html"
    ordering = ['-tickets']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Project.objects.annotate(num_tickets=Count('tickets')).order_by('-num_tickets')
        return context



project_list_view = ProjectListView.as_view()


class CreateProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "tracker/project_form.html"

    def get_success_url(self):
        return reverse("project_list")

    def get_form_kwargs(self):
        kwargs = super(CreateProjectView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['title'] = 'Create project'
        return kwargs


create_project_view = login_required(CreateProjectView.as_view())


class UpdateProjectView(ProjectContextMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    pk_url_kwarg = 'project_id'
    template_name = "tracker/project_form.html"

    def get_success_url(self):
        return reverse("project_list")

    def get_form_kwargs(self):
        kwargs = super(UpdateProjectView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['title'] = "Edit {0}".format(self.object.title)
        return kwargs


update_project_view = login_required(UpdateProjectView.as_view())


class ProjectView(ProjectContextMixin, TemplateView):
    template_name = "tracker/project_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        project = self.get_project()
        context.update({
            "project": project,
            "tickets": project.tickets.all()
        })
        return context


project_view = ProjectView.as_view()

class DeleteProjectView(ProjectContextMixin, DeleteView):
    model = Project
    pk_url_kwarg = 'project_id'
    success_url = reverse_lazy("project_detail")

    def get_success_url(self):
        return reverse("project_list")

delete_project_view = login_required(DeleteProjectView.as_view())


class CreateTicketView(ProjectContextMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "tracker/ticket_create.html"

    def get_success_url(self):
        return reverse("project_detail", kwargs={"project_id": self.kwargs['project_id']})

    def get_form_kwargs(self):
        kwargs = super(CreateTicketView, self).get_form_kwargs()
        kwargs['project'] = self.get_project()
        kwargs['user'] = self.request.user
        kwargs['title'] = 'Create ticket'
        return kwargs


create_ticket_view = login_required(CreateTicketView.as_view())


class UpdateTicketView(ProjectContextMixin, UpdateView):
    model = Ticket
    form_class = TicketForm
    pk_url_kwarg = 'ticket_id'
    template_name = "tracker/ticket_form.html"

    def get_success_url(self):
        return reverse("project_detail", kwargs={"project_id": self.kwargs['project_id']})

    def get_form_kwargs(self):
        kwargs = super(UpdateTicketView, self).get_form_kwargs()
        kwargs['project'] = self.project
        kwargs['user'] = self.request.user
        kwargs['title'] = "Edit {0}".format(self.object.title)
        return kwargs


update_ticket_view = login_required(UpdateTicketView.as_view())

class DeleteTicketView(ProjectContextMixin, DeleteView):
    model = Ticket
    pk_url_kwarg = 'ticket_id'
    success_url = reverse_lazy("project_detail")

    def get_success_url(self):
        return reverse("project_detail", kwargs={"project_id": self.kwargs['project_id']})

delete_ticket_view = login_required(DeleteTicketView.as_view())



class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "tracker/comment_form.html"

    def get_ticket(self):
        self.ticket = get_object_or_404(Ticket, pk=self.kwargs['pk'])
        return self.ticket

    def get_success_url(self):
        print(dir(self))
        return reverse("project_detail", kwargs={"project_id": self.ticket.project.id})

    def get_form_kwargs(self):
        kwargs = super(CreateCommentView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['ticket'] = self.get_ticket()
        return kwargs

add_comment = login_required(CreateCommentView.as_view())



# @login_required
# def add_comment(request, pk):
#     ticket = get_object_or_404(Ticket, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.ticket = ticket
#             comment.save()
#             return redirect('ticket_update')
#     else:
#         form =CommentForm()
#     return render(request, 'tracker/comment_form.html',{'form':form})
