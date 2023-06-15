import unittest
from django.test import TestCase, Client
from django.urls import reverse
from quiz.models import Quiz, Question, Choice, UserResponse
from quiz.views import QuizListView, QuizDetailView, QuizSubmitView

class QuizModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Quiz.objects.create(title='Test Quiz', description='This is a test quiz.')

    def test_title_label(self):
        quiz = Quiz.objects.get(id=1)
        field_label = quiz._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        quiz = Quiz.objects.get(id=1)
        field_label = quiz._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_title_max_length(self):
        quiz = Quiz.objects.get(id=1)
        max_length = quiz._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_object_name(self):
        quiz = Quiz.objects.get(id=1)
        expected_object_name = quiz.title
        self.assertEqual(str(quiz), expected_object_name)

if __name__ == '__main__':
    unittest.main()

class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        quiz = Quiz.objects.create(title='Test Quiz', description='This is a test quiz.')
        question = Question.objects.create(quiz=quiz, question_text='Test question')
        choice = Choice.objects.create(choice_text='Test choice', question=question)
        question.correct_choice = choice
        question.save()

    def test_question_text_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('question_text').verbose_name
        self.assertEqual(field_label, 'question text')

    def test_question_text_max_length(self):
        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('question_text').max_length
        self.assertIsNone(max_length)  # Assuming there is no explicit max_length set

    def test_quiz_foreign_key(self):
        question = Question.objects.get(id=1)
        related_quiz = question.quiz
        self.assertIsInstance(related_quiz, Quiz)

    def test_correct_choice_foreign_key(self):
        question = Question.objects.get(id=1)
        related_choice = question.correct_choice
        self.assertIsInstance(related_choice, Choice)
        self.assertEqual(related_choice.question, question)

    def test_object_name(self):
        question = Question.objects.get(id=1)
        expected_object_name = question.question_text
        self.assertEqual(str(question), expected_object_name)

if __name__ == '__main__':
    unittest.main()

class ChoiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        quiz = Quiz.objects.create(title='Test Quiz', description='This is a test quiz.')
        question = Question.objects.create(quiz=quiz, question_text='Test question')
        Choice.objects.create(question=question, choice_text='Test choice', is_correct=False)

    def test_choice_text_label(self):
        choice = Choice.objects.get(id=1)
        field_label = choice._meta.get_field('choice_text').verbose_name
        self.assertEqual(field_label, 'choice text')

    def test_choice_text_max_length(self):
        choice = Choice.objects.get(id=1)
        max_length = choice._meta.get_field('choice_text').max_length
        self.assertEqual(max_length, 250)

    def test_question_foreign_key(self):
        choice = Choice.objects.get(id=1)
        related_question = choice.question
        self.assertIsInstance(related_question, Question)

    def test_is_correct_default_value(self):
        choice = Choice.objects.get(id=1)
        is_correct = choice.is_correct
        self.assertFalse(is_correct)

    def test_object_name(self):
        choice = Choice.objects.get(id=1)
        expected_object_name = choice.choice_text
        self.assertEqual(str(choice), expected_object_name)

class UserResponseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        quiz = Quiz.objects.create(title='Test Quiz', description='This is a test quiz.')
        question = Question.objects.create(quiz=quiz, question_text='Test question')
        choice = Choice.objects.create(question=question, choice_text='Test choice', is_correct=False)
        UserResponse.objects.create(question=question, choice=choice)

    def test_question_foreign_key(self):
        user_response = UserResponse.objects.get(id=1)
        related_question = user_response.question
        self.assertIsInstance(related_question, Question)

    def test_choice_foreign_key(self):
        user_response = UserResponse.objects.get(id=1)
        related_choice = user_response.choice
        self.assertIsInstance(related_choice, Choice)

    def test_object_name(self):
        user_response = UserResponse.objects.get(id=1)
        expected_object_name = f"User response: {user_response.question.question_text} - Choice: {user_response.choice.choice_text}"
        self.assertEqual(str(user_response), expected_object_name)


class QuizListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('quiz_list')

    def test_quiz_list_view(self):
        quiz = Quiz.objects.create(title='Test Quiz', description='This is a test quiz.')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/quiz_list.html')
        self.assertContains(response, quiz.title)

class QuizDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.quiz = Quiz.objects.create(title='Test Quiz')
        self.url = reverse('quiz_detail', args=[self.quiz.id])

    def test_quiz_detail_view(self):
        question = Question.objects.create(quiz=self.quiz, question_text='Test question')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/quiz_detail.html')
        self.assertContains(response, question.question_text)


class QuizSubmitViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.quiz = Quiz.objects.create(title='Test Quiz')
        self.url = reverse('submit_quiz', args=[self.quiz.id])

    def test_quiz_submit_view(self):
        question = Question.objects.create(quiz=self.quiz, question_text='Test question')
        choice = Choice.objects.create(question=question, choice_text='Test choice', is_correct=True)
        response = self.client.post(self.url, {str(question.id): str(choice.id)})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/quiz_result.html')
        self.assertContains(response, 'feedback')
        self.assertContains(response, 'Your Answers')
        self.assertContains(response, 'Correct Answers')