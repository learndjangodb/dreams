from django.db import models as m


# Create your models here.
class DreamReal(m.Model):
    website = m.CharField(max_length=100)
    mail = m.EmailField(max_length=50)
    name = m.CharField(max_length=25)
    phonenumber = m.IntegerField()
    online = m.ForeignKey('Online', default=1)

    class Meta:
        db_table = "dreamreal"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Online(m.Model):
    domain = m.CharField(max_length=30)

    class Meta:
        db_table = 'online'


class Profile(m.Model):
    name = m.CharField(max_length=100)
    picture = m.ImageField(upload_to='pictures')

    class Meta:
        db_table = "profile"


TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class Author(m.Model):
    name = m.CharField(max_length=100)
    title = m.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = m.DateField(blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Book(m.Model):
    name = m.CharField(max_length=100)
    authors = m.ManyToManyField(Author)


class PollManager(m.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT p.id, p.question, p.poll_date, COUNT(*)
                FROM polls_opinionpoll p, polls_response r
                WHERE p.id = r.poll_id
                GROUP BY p.id, p.question, p.poll_date
                ORDER BY p.poll_date DESC
            """)
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], question=row[1], poll_date=row[2])
                p.num_responses = row[3]
                result_list.append(p)
        return result_list


class OpinionPoll(m.Model):
    question = m.CharField(max_length=200)
    poll_date = m.DateField()
    objects = PollManager()

    def __str__(self):
        return self.question


class Response(m.Model):
    poll = m.ForeignKey(OpinionPoll, on_delete=m.CASCADE)
    person_name = m.CharField(max_length=50)
    response = m.TextField()
