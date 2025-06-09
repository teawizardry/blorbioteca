# Blorbioteca
> _An Eleventy based character repository_

The goal of this project is to create an easy to use static site generator for character sheets. It's inspired by sites like [Refsheet](https://refsheet.net/) and [Toyhouse](https://toyhou.se/) and my own desire for a self-hosted option.

## Installation
First, make sure you have [Node.js](https://nodejs.org/en/download/) installed. You can check this by running `node --version`. It is also advisable to have a look at the [Eleventy docs](https://www.11ty.dev/) to familiarize yourself with the workflow.
1. Clone this repository via `git clone https://github.com/teawizardry/blorbioteca`
2. Install dependencies via `npm install`
3. Build with `gulp --tasks && npx @11ty/eleventy` or serve with `gulp --tasks && npx @11ty/eleventy --serve`

Now you can take a look at the template output! All character information is stored under the `characters` folder in markdown files. Images are stored in `character_images`. Check out `characters/template.md` for available css and sidebar options!

Host the site either via self-hosting or by uploading the `_site/` output folder to some place like [neocities.](https://neocities.org/)

## Features

### Image Gallery
To include an image in a character's image gallery, add the image path to the `character_images/images.json` file. Here you can also specify the image's description and whether or not it should be blacked out until clicked on (important to comply with certain art trade event rules). Images are optimized for the web automagically via Eleventy's Image plugin.

### Fonts
To include custom fonts, place the font files in `assets/fonts/`. The command `gulp --tasks` will automatically optimize included fonts for the web and generate the css font headers for you. You can then specify these fonts per page via the front matter. Only `ttf` fonts are currently supported. Default font is [Hack.](https://github.com/source-foundry/Hack_)

### Custom Colors
You can specify different colors per page in the front matter. Default colors based on [Kanagawa](https://github.com/rebelot/kanagawa.nvim)

### Character Index Page
The homepage lists all characters in alphabetical order.

## Future Work
This is a new project for me, so there's a lot to add! 
- Improve accessibility (especially for images)
- Add more theme customization
- Improve theming of homepage
- Add character relations map / family tree

## Feedback and Suggestions
If you have a suggestion or encounter a bug, open a issue on this repository!
