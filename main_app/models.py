from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

BOOK_STATUS = (
  ('A', 'Available'),
  ('B', 'Borrowed'),
)

REQUEST_STATUS = (
  ('A', 'Accepted'),
  ('P', 'Pending'),
  ('R', 'Rejected'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=225, blank=True)
    
    
# Create your models here.
class Author(models.Model):
   name = models.CharField(max_length=100)
   avatar_url = models.CharField(max_length=200)
   
   def __str__(self):
       return f'{self.name} ({self.id})'
    
class BookRequest(models.Model):
    status = models.CharField(
            max_length=1,
            choices=REQUEST_STATUS,
            default=REQUEST_STATUS[0][0]
        )
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
  
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    published_date = models.DateField('Published Date')
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    owner = models.ForeignKey(Customer,on_delete=models.CASCADE) 
    cover_image = models.CharField(max_length=225,default='')
    book_requests =  models.ManyToManyField(BookRequest)
    status = models.CharField(
            max_length=1,
            choices=BOOK_STATUS,
            default=BOOK_STATUS[0][0]
        )
    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
 
class Photo(models.Model):
    url = models.CharField(max_length=200)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_cover = models.BooleanField(default=False)
    def __str__(self):
        return f"Photo for book_id: {self.book_id} @{self.url}"
  

