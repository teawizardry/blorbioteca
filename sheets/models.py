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

from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

class CharacterSheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50, blank=True, null=True)
    bio = tinymce_models.HTMLField()
    sidebar = tinymce_models.HTMLField(default="""<table style="border-collapse: collapse; width: 100.015%; height: 179.2px;" border="1"><colgroup><col style="width: 49.9242%;"><col style="width: 49.9242%;"></colgroup>
                                                <tbody>
                                                <tr style="height: 22.4px;">
                                                <th style="height: 22.4px;">Species</th>
                                                <td style="height: 22.4px;">&nbsp;</td>
                                                </tr>
                                                <tr style="height: 22.4px;">
                                                <th style="height: 22.4px;">Age</th>
                                                <td style="height: 22.4px;">&nbsp;</td>
                                                </tr>
                                                <tr style="height: 22.4px;">
                                                <th style="height: 22.4px;">Birthday</th>
                                                <td style="height: 22.4px;">&nbsp;</td>
                                                </tr>
                                                <tr style="height: 22.4px;">
                                                <th style="height: 22.4px;">Height</th>
                                                <td style="height: 22.4px;">&nbsp;</td>
                                                </tr>
                                                <tr style="height: 22.4px;">
                                                <th style="height: 22.4px;">Weight</th>
                                                <td style="height: 22.4px;">&nbsp;</td>
                                                </tr>
                                                <tr style="height: 22.4px;">
                                                <th style="height: 22.4px;">Body Type</th>
                                                <td style="height: 22.4px;">&nbsp;</td>
                                                </tr>
                                                <tr style="height: 22.4px;">
                                                <th style="height: 22.4px;">Gender</th>
                                                <td style="height: 22.4px;">&nbsp;</td>
                                                </tr>
                                                <tr style="height: 22.4px;">
                                                <th style="height: 22.4px;">Sexuality</th>
                                                <td style="height: 22.4px;">&nbsp;</td>
                                                </tr>
                                                </tbody>
                                                </table>""")
    