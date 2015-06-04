from django.contrib import admin
from .models import (Diet, Ingredient, Meal, Recipe, Session, Ustensil,
                     MealParticipant, RecipeIngredient, SessionMeal)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class MealParticipantInline(admin.TabularInline):
    model = MealParticipant


class SessionMealInline(admin.TabularInline):
    model = SessionMeal


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'diets_str')
    exclude = ['diets']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'diets_str', 'price', 'meal_type', 'parts')
    exclude = ['diets']
    inlines = [RecipeIngredientInline, ]


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    filter_horizontal = ('recipes',)
    inlines = [MealParticipantInline, ]
    list_display = ('name', 'participants_count', 'begin', 'end',
                    'admin_roadmap')
    list_filter = ('recipes__ingredients__diets__name',)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_roadmap')
    inlines = [SessionMealInline, ]


admin.site.register(Diet)
admin.site.register(Ustensil)
# admin.site.register(MealParticipant)
# admin.site.register(RecipeIngredient)
# admin.site.register(SessionMeal)
