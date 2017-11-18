from django.db import models
from django.utils import timezone


YEAR_CHOICES = []
for r in range(1995, (timezone.now().year+1)):
    YEAR_CHOICES.append((r,r))


class Travel(models.Model):
    title = models.CharField('title', max_length=100)
    author = models.ForeignKey('auth.User', verbose_name='author', related_name='travels')
    location = models.CharField('location', max_length=100)
    description = models.CharField(max_length=200)
    happened_on = models.DateField('happened on', blank=True, null=True)
    photo = models.ImageField('photo', upload_to='media/travel', blank=True)

    def __str__(self):
        return self.title


class Trip(models.Model):
    class SUBJECT:
        HOLIDAY = 1
        WORK = 2
        VOLUNTEERING = 3
        JUST_GO_AWAY = 4

        ALL = (
            (HOLIDAY, 'holiday'),
            (WORK, 'work'),
            (VOLUNTEERING, 'volunteering'),
            (JUST_GO_AWAY, 'just_go_away'),
        )

    name = models.CharField('name', max_length=100)
    travel = models.ForeignKey(Travel, related_name='trips')
    place = models.CharField('place name', max_length=100)
    subject = models.PositiveSmallIntegerField('subject', choices=SUBJECT.ALL)
    happened_on = models.DateTimeField('happened on', blank=True, null=True)
    photo = models.ImageField('photo', upload_to='media/trip', blank=True)

    def __str__(self):
        return self.name


class ArtObject(models.Model):
    class CATEGORY:
        PAINTING = 1
        LINOCUT = 2
        INSTALLATION = 3
        COLLAGE = 4
        PHOTO = 5
        SCULPTURE = 6
        ILLUSTRATION = 7
        ELSE = 8

        ALL = (
            (PAINTING, 'painting'),
            (LINOCUT, 'linocut'),
            (INSTALLATION, 'installation'),
            (COLLAGE, 'collage'),
            (PHOTO, 'photo'),
            (SCULPTURE, 'sculpture'),
            (ILLUSTRATION, 'illustration'),
            (ELSE, 'else'),
        )

    title = models.CharField('title', max_length=200)
    year = models.IntegerField('year', choices=YEAR_CHOICES, default=timezone.now().year)
    technique = models.IntegerField('technique', choices=CATEGORY.ALL, default=1)
    image = models.ImageField('image', upload_to='art', blank=True)
    description = models.CharField('description', max_length=200, null=True, blank=True)
    size = models.CharField('size', max_length=100, null=True, blank=True)
    material = models.CharField('used materials', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title