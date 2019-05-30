
from django.test import TestCase

from tbxcodingtask.tracker.forms import CommentForm
from tbxcodingtask.tracker.models import Comment, Project, Ticket


class CommentFormTestCase(TestCase):
    def test_valid_form(self):
        prj = Project.objects.create(title="A Test")
        ticket = Ticket.objects.create(title="Item", description="desc", project=prj)
        content  = 'some content'
        obj = Comment.objects.create(content=content, ticket=ticket)
        data = {"content": content, "ticket":ticket}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('content'), obj.content)
        self.assertNotEqual(form.cleaned_data.get("content"), "Another item")

    def test_invalid_form(self):
        prj = Project.objects.create(title="A Test")
        ticket = Ticket.objects.create(title="Item", description="desc", project=prj)
        content  = 'some content'
        obj = Comment.objects.create(content=content, ticket=ticket)
        data = {"content": ""}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
