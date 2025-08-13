<!--
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
-->

# Blorbioteca
> A free and open source character and world repository

The goal of this project is to create an easy-to-use and robust character / world repository site. It's inspired by sites like [Refsheet](https://refsheet.net/), [Toyhouse](https://toyhou.se/), and my own previous attempt at an [11ty based character repository.](https://github.com/teawizardry/blorbioteca_11ty)

## Current Features
- User accounts with 2fa
- User profiles

## Future Features

**Top Priority**
- Character sheets
- World sheets
- Image uploads
- Tagging system
- Image and character filtering

**Planned**
- Home page picture
- Image optimization
- AI scrapper mitigation
- Custom colors for profile, characters, worlds
- Family tree generator
- Offline editing
- Improve accessibility
- Improve website styling

**Long-Term**
- Optional image watermarking
- Friend / follow other users
- Custom CSS
- Linking character / world sheets

## Local Setup
This project is made with Django and assumed some base level of Python, HTML, CSS, and JavaScript knowledge.
1. Clone this repo 
    - `git clone https://github.com/teawizardry/blorbioteca.git`
2. Enter the folder, make a new Python environment, and activate it
    - `cd blorbioteca`
    - `python -m venv .venv`
    - `source .venv/bin/activate`
3. Install required packages in `requirements.txt`
    - `pip install -r requirements.txt`
4. Create a `.env` file
    ```
    SECRET_KEY = '<secret-key>'
    DEBUG = True
    ```
5. Generate a secret key and place it in the `.env` file
    ```
    from django.core.management.utils import get_random_secret_key  
    get_random_secret_key()
    ```
6. Run the project locally
   - `python manage.py runserver`