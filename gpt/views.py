from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.views.generic.edit import FormView
from django.views import View
from django.http import JsonResponse
import openai
from .models import Chat
from django.utils import timezone

openai_api_key = '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'
openai.api_key = openai_api_key

# class ChatView(View):
#     def ask_openai(self, message):
#         try:
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are an helpful assistant."},
#                     {"role": "user", "content": message},
#                 ]
#             )
#             answer = response.choices[0].message["content"]
#         except Exception as e:
#             print(e)
#             answer = "Something went wrong."
#         return answer
#
#     def post(self, request, *args, **kwargs):
#          message = request.POST.get('textarea')
#         response = ask_openai(message)
#         chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
#         chat.save()
#         return JsonResponse({'message': message, 'response': response})
#
#     def get(self, request, *args, **kwargs):
#          chats = Chat.objects.filter(user=request.user)
#         returnreturn render(request, 'gpt/chat/chat.html', {'chats': chats})


class Login(LoginView):
    template_name = 'gpt/auth/login.html'
    authentication_form = CustomAuthenticationForm
    next_page = 'home'


class Register(FormView):
    template_name = 'gpt/auth/register.html'
    form_class = CustomUserCreationForm
    success_url = '/gpt/chat/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Logout(LogoutView):
    next_page = 'login'
    template_name = 'gpt/auth/login.html'

# def home(request):
#     return render(request, 'gpt/chat/chat.html')
