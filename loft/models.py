from django.db import models

class City(models.Model):

    country = models.CharField(max_length=50, default="Portugal")
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=6)
    description = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}, {self.country} ({self.abbreviation})'

class Loft(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='lofts')
    address = models.CharField(max_length=250)
    price = models.IntegerField()
    size = models.IntegerField()
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.city.name}, {self.name} - {self.address}'

class Contact(models.Model):

    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)
    date_of_birth = models.DateField(auto_now=False, null=True)
    loft = models.ForeignKey(Loft, on_delete=models.CASCADE, related_name="contacts")
    def __str__(self):
        return f'{self.username} ({self.phone_number}) - {self.email}: "{self.message[20]}"'

class Quizz(models.Model):

    timestamp = models.DateField(auto_now=True)
    score = models.IntegerField()
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    comments = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.username} ({self.age}) {self.score}% "{self.comments[:30]}", <{self.timestamp}>'

class Answer(models.Model):

    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE, related_name="answers")
    question = models.CharField(max_length=250)
    correct = models.BooleanField()
    answer = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.question} ({self.answer})'

class Comment(models.Model):

    username = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.username}: {self.description}'