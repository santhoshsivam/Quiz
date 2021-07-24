from django.contrib import admin
from .models import questions
from .models import fifth_standard
from .models import sixth_standard
from .models import seventh_standard
from .models import signin
# Register your models here.
''' 
Here registering the data bases to admin
'''
admin.site.register(questions)
admin.site.register(fifth_standard)
admin.site.register(sixth_standard)
admin.site.register(seventh_standard)
admin.site.register(signin)
