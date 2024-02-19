from django.http import JsonResponse
from django.views import View
from .models import Feedback, News, Users


class FeedbackView(View):
    def get(self, request):
        feedback = Feedback.objects.all()
        data = [{'id': fb.id, 'news_id': fb.news_id, 'user_id': fb.user_id, 'comment': fb.comment,
                 'feedback_date': fb.feedback_date} for fb in feedback]
        return JsonResponse(data, safe=False)


class UsersView(View):
    def get(self, request):
        users = Users.objects.all()
        data = [{'id': u.id, 'nickname': u.nickname, 'hash_password': u.hash_password} for u in users]
        return JsonResponse(data, safe=False)


class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        data = [{'id': n.id, 'title': n.title, 'description': n.description, 'news_date': n.news_date,
                 'address': n.address, 'url': n.url, 'img': n.img} for n in news]
        return JsonResponse(data, safe=False)
