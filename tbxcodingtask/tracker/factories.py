import factory

from tbxcodingtask.tracker.models import Project, Ticket


class ProjectFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: f'Project {n}')

    class Meta:
        model = Project


class TicketFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: f'Ticket {n}')
    description = factory.Sequence(lambda n: f'Some description {n}')
    project = factory.SubFactory(ProjectFactory)

    class Meta:
        model = Ticket
