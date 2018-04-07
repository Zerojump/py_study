from django.db import models


class BlobChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('BlobQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blob_choice'


class BlobQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blob_question'
