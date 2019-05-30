from django.test import TestCase

from tbxcodingtask.tracker.factories import ProjectFactory, TicketFactory
from tbxcodingtask.tracker.models import Project, Ticket


class TestProject(TestCase):
    def test_can_delete_project(self):
        project = ProjectFactory()
        self.assertEquals(Project.objects.all().count(), 1)
        project.delete()
        self.assertEquals(Project.objects.all().count(), 0)


class TestTicket(TestCase):
    def test_can_delete_ticket(self):
        ticket = TicketFactory()
        self.assertEquals(Ticket.objects.all().count(), 1)
        ticket.delete()
        self.assertEquals(Ticket.objects.all().count(), 0)


