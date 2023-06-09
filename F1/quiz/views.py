from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quiz, UserResponse, Choice, Question

class QuizListView(LoginRequiredMixin, View):
    def get(self, request):
        quizzes = Quiz.objects.all()
        return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

class QuizDetailView(LoginRequiredMixin, View):
    def get(self, request, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})


class QuizSubmitView(View):
    def post(self, request, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        total_questions = questions.count()
        score = 0
        user_responses = []

        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                user_response = UserResponse(question=question, choice=choice)

                if choice.is_correct:
                    score += 1

                user_responses.append(user_response)

        correct_choices = {}
        for question in questions:
            if question.correct_choice:
                correct_choices[question.id] = question.correct_choice
            else:
                correct_choices[question.id] = "No correct answer specified"

        if score >= 13:
            feedback = "Wow! You are the Formula One expert! Nothing can surprise you!"
        elif score >= 9:
            feedback = "Nice job! You are definitely a F1 enthusiast! Keep up the good work!"
        elif score >= 5:
            feedback = "Could be better! You know some facts about Formula One, but it's not you favorite sport!"
        else:
            feedback = "Truly catastrophic result! Have you ever heard about F1 or even watched a single race?"

        context = {
            'score': score,
            'total_questions': total_questions,
            'feedback': feedback,
            'user_responses': user_responses,
            'correct_choices': correct_choices
        }

        return render(request, 'quiz/quiz_result.html', context)