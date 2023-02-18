from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from newspaper.models import EmailSubscribe
from newspaper.forms import EmailSubscribeForm
from newspaper.tasks import send_email_task



class SuccessView(View):
    def get(self, request):
        return HttpResponse("Success")


class EmailSubscribeView(View):
    form_class = EmailSubscribeForm
    template_name = 'email_subscribe_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            subscription = EmailSubscribe(email=form.data.get('email'))
            subscription.save()
            send_email_task.delay(
                recipent_list=[form.data.get('email')],
                subject='Email subscription is success',
                message='Thank you to join email newspaper.'
            )
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
