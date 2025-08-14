'''
    Blorbioteca is a free and open source character and world repository.
    Copyright (C) 2025 Hannah Kirkland

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.characters, name='characters'),
    path('<int:pk>/', views.character_sheet, name='character-sheet'),
    path('<int:pk>/edit/', views.edit_character, name='edit-character'),
    path('new-character', views.new_character, name='new-character'),
    # path('<int:pk>/delete/', views.delete_character, name='delete-character'),
]