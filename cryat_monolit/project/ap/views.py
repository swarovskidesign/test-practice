from django.shortcuts import render
from django.views import View

class Main(View):
    def get(self, request):
        # if not request.session.session_key:
        #     request.session.create()
        return render(request, 'ap/main_page.html', status=200)
    
class Feedback(View):
    def get(self, request):
        return render(request, 'ap/feedback.html', status=200)