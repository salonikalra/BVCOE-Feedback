from django.forms import ModelForm, RadioSelect
from feedbacks.models import feedback, Subject, Teacher

choices = (
            (1,'Unsatisfactory'),
            (2,'Satisfactory'),
            (3,'Good'),
            (4,'Very Good'),
            (5,'Outstanding')
            )

class feedbackForm(ModelForm):

    class Meta:
        model = feedback
        fields = ("subject","teacher","param1","param2","param3","param4",
                    "param5","param6","param7","param8","param9","param10","message")
        widgets = {
            'param1': RadioSelect(attrs={}),
            'param2': RadioSelect(attrs={}),
            'param3': RadioSelect(attrs={}),
            'param4': RadioSelect(attrs={}),
            'param5': RadioSelect(attrs={}),
            'param6': RadioSelect(attrs={}),
            'param7': RadioSelect(attrs={}),
            'param8': RadioSelect(attrs={}),
            'param9': RadioSelect(attrs={}),
            'param10': RadioSelect(attrs={}),
        }

    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user')
        super (feedbackForm,self ).__init__(*args,**kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(semester__semester_number=self.user.student.semester,
                                                                department__department_id=self.user.student.department)
        self.fields['teacher'].queryset = Teacher.objects.none()

        if 'subject' in self.data:
            try:
                subject_id = int(self.data.get('subject'))
                self.fields['teacher'].queryset = Teacher.objects.filter(subject__id=subject_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Teacher queryset
        elif self.instance.pk:
            self.fields['teacher'].queryset = self.instance.subject.teacher.all()
