from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return '%s / %s' % (self.question_text, self.pub_date)         # '' % : formatting 이라는데 뭐지 


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return '%s / %s / %d' % (self.question, self.choice_text, self.votes)   # 모르겠으면 %s
        # return self.question + str(self.votes)