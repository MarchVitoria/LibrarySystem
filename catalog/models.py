from django.db import models
from django.urls import reverse
import uuid
from datetime import date
from django.conf import settings


    
class GenreModel(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        )
    
    def get_absolute_url(self):
        """When get_absolute_url() is called on a model instance, it yields the specific URL for that instance, 
        utilizing the named URL pattern 'genre-detail' and incorporating the instance's ID as part of the URL."""
        return reverse('genre-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    
    
class LanguageModel(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        )
    
    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name
    

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)
    # books = models.ManyToManyField('BookModel')

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.RESTRICT, null=True)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=100, unique=True)
    genre = models.ManyToManyField(GenreModel)
    language = models.ForeignKey(LanguageModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['title', 'author']

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
    

class BookInstanceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(BookModel, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
        )
    
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
        )
    
    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"))

    def get_absolute_url(self):
        return reverse('bookinstance-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.id} ({self.book.title})'