from django.contrib import admin
from catalog.models import BookModel, AuthorModel, BookInstanceModel, GenreModel, LanguageModel


admin.site.register(BookModel)
admin.site.register(GenreModel)
admin.site.register(AuthorModel)
admin.site.register(LanguageModel)
admin.site.register(BookInstanceModel)