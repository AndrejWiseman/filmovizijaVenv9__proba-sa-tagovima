from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Filmovi(models.Model):
    title = models.CharField(max_length=200)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    category = models.ManyToManyField(Category, related_name="filmovi")
    slug = models.SlugField(default="", null=False)
    # image = CloudinaryField('image', default='')
    # tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detaljno', kwargs={'slug': self.slug})




class Serije(models.Model):
    title = models.CharField(max_length=120)
    # originalni_naziv = models.CharField(max_length=120, null=False)
    slug = models.SlugField(default="", null=False)
    category = models.ManyToManyField(Category, related_name="serije")
    # godina = models.CharField(max_length=120, null=False, blank=False)
    # zanr = models.CharField(default='', max_length=120, null=False, blank=False)
    # imdb_ocena = models.CharField(max_length=120, null=False)
    # description = models.TextField()
    # tags = TaggableManager()
    # image = models.FileField(upload_to='movie-images', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def get_absolute_url(self):
        return reverse('serija-detaljno', kwargs={'slug': self.slug})

    # def get_episodes(self):
    #     return self.epizoda_set.all()

    def get_episodes_by_season(self):
        episodes = self.epizoda_set.all()
        seasons = {}
        for episode in episodes:
            if episode.sezona not in seasons:
                seasons[episode.sezona] = []
            seasons[episode.sezona].append(episode)
        return seasons


class Epizoda(models.Model):
    epizode = models.ForeignKey(Serije, on_delete=models.CASCADE)
    epizode_date = models.DateField(auto_now_add=True)
    sezona = models.CharField(max_length=120, null=True, blank=True)
    ep = models.CharField(max_length=120, null=True, blank=True)
    # epizode_link = models.CharField(max_length=300)
    # epizode_preuzmi = models.CharField(default='', max_length=300)

    def __str__(self):
        return self.ep

