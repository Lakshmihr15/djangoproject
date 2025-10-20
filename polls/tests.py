from django.test import TestCase

# Create your tests here.from django.test import TestCase
from .models import Question


class QuestionModelTests(TestCase):
    def test_str_returns_question_text(self):
        q = Question(question_text="Is this used?", pub_date=None)
        self.assertEqual(str(q), "Is this used?")
