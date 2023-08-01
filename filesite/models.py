from django.db import models

# add user class
class User(models.Model):
    userName = models.CharField(max_length=50,default='admin',null=False)
    password=models.CharField(max_length=50,default='root',null=False)
    def __str__(self):
        return self.userName
# add post clas     
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_field = models.FileField(upload_to='uploads/')
    desc = models.TextField()

    def __str__(self):
        return f'{self.user}=> {self.title}'