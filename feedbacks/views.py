from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.http import Http404
from django.views import generic
from django.db import IntegrityError
from django.contrib import messages

from braces.views import SelectRelatedMixin

from .forms import feedbackForm
from . import models
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model
User = get_user_model()


class Userfeedbacks(LoginRequiredMixin, SelectRelatedMixin, generic.ListView):
    model = models.feedback
    template_name = "feedbacks/user_feedback_list.html"

    def get_queryset(self):
        try:
            self.user = models.Student.objects.prefetch_related("feedbacks").get(
                user__username__iexact=self.kwargs.get("username")
            ).user
        except User.DoesNotExist:
            raise Http404
        else:
            return self.user.student.feedbacks.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feedback_user"] = self.user
        return context


class feedbackDetail(LoginRequiredMixin, SelectRelatedMixin, generic.DetailView):
    model = models.feedback
    select_related = ("student","teacher","subject")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            student__user__username__iexact=self.kwargs.get("username")
        )


class Createfeedback(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.feedback
    form_class = feedbackForm

    def get(self, request, *args, **kwargs):
        if self.request.user.student.feedbacks.count()>=6:
            return HttpResponseRedirect(reverse_lazy('feedbacks:completed'))
        return super(Createfeedback, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
            username = self.request.user.username
        except IntegrityError:
            messages.add_message(request, messages.ERROR,
                                 'You have already provided feedback for the following teacher/ subject.')
            return render(request, 'feedbacks/feedback_form.html', context=self.get_context_data())
        else:
            return HttpResponseRedirect(reverse_lazy( 'feedbacks:for_user', kwargs={'username': username}))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.student = self.request.user.student
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(Createfeedback, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class FeedbackCompletedView(generic.TemplateView):
    template_name = "feedbacks/feedback_completed.html"

def load_teachers(request):
    subject_id = request.GET.get('subject')
    teachers = models.Teacher.objects.filter(subject__id=subject_id,
                                            department__department_id=request.user.student.department)
    return render(request, 'feedbacks/teacher_dropdown_list_options.html', {'teachers': teachers})
