//  Blorbioteca is a free and open source character and world repository.
//  Copyright (C) 2025 Hannah Kirkland
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <https://www.gnu.org/licenses/>.

// based on:
// https://medium.com/@haxzie/dark-and-light-theme-switcher-using-css-variables-and-pure-javascript-zocada-dd0059d72fa2

// sets color theme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
    
    // update html and body colors to prevent "sticky" colors requiring refresh
    const html = document.documentElement;
    const body = document.body;
    
    if (themeName === 'theme-light') {
        html.style.backgroundColor = '#f2ecbc';
        body.style.backgroundColor = '#f2ecbc';
        body.style.color = '#545464';
    } else {
        html.style.backgroundColor = '#181616';
        body.style.backgroundColor = '#181616';
        body.style.color = '#c5c9c5';
    }
}

// theme toggle
function toggleTheme() {
   if (localStorage.getItem('theme') === 'theme-dark'){
       setTheme('theme-light');
   } else {
       setTheme('theme-dark');
   }
}

// set theme on load
(function () {
    if (localStorage.getItem('theme') === 'theme-light') {
        setTheme('theme-light');
    } else{
         setTheme('theme-dark');
    }
})();