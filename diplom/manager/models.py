



# class Requests(models.Model):
#     date = models.DateField(auto_now_add=True)
#     name = models.CharField(max_length=250, verbose_name='name')
#     description = models.TextField(max_length=250)
#     phone = models.CharField(max_length=250)
#     email = models.EmailField()
#     client = models.ForeignKey(Clients, on_delete=models.PROTECT)
#     service = models.CharField(max_length=250)