from django.contrib import admin

from blog.models import Category, Location, Post, Comment


@admin.register(Post) # Декоратор регистрирует модель Post в админке
class PostAdmin(admin.ModelAdmin):
    list_display = (  # Какие поля показывать в списке публикаций
        'title',
        'is_published',
        'category',
        'author',
        'location',
        'text',
        'pub_date',
        'created_at',
    )
    list_editable = (  # Какие поля можно редактировать прямо в списке
        'is_published',
        'category'
    )
    search_fields = ('title',) # Поиск по заголовку - строка поиска
    list_filter = ('category', 'is_published',) # Фильтры справа
    list_display_links = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'slug',
        'description',
        'created_at',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('is_published',) # Фильтр по статусу
    list_display_links = ('title',) # Клик на названии откроет форму


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('name',)
    list_filter = ('is_published',)
    list_display_links = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'post',
        'created_at',
        'author'
    )


admin.site.empty_value_display = 'Не задано'