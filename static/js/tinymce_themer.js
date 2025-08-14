//   Blorbioteca is a free and open source character and world repository.
//   Copyright (C) 2025 Hannah Kirkland

//   This program is free software: you can redistribute it and/or modify
//   it under the terms of the GNU General Public License as published by
//   the Free Software Foundation, either version 3 of the License, or
//   (at your option) any later version.

//   This program is distributed in the hope that it will be useful,
//   but WITHOUT ANY WARRANTY; without even the implied warranty of
//   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//   GNU General Public License for more details.

//   You should have received a copy of the GNU General Public License
//   along with this program.  If not, see <https://www.gnu.org/licenses/>.

// automatically matches theming 
document.addEventListener('DOMContentLoaded', function() {
    function getThemeCSS() {
        const themeToggle = document.querySelector('#theme-toggle');
        const isDarkMode = themeToggle && !themeToggle.checked;
        
        return `
            body.mce-content-body {
                background-color: ${window.getComputedStyle(document.querySelector('body')).getPropertyValue('background-color')} !important;
                color: ${window.getComputedStyle(document.querySelector('body')).getPropertyValue('color')} !important;
            }
            .mce-content-body p {
                color: ${window.getComputedStyle(document.querySelector('body')).getPropertyValue('color')} !important;
            }
            .mce-content-body * {
                color: inherit !important;
            }
        `;
    }
    
    function initTinyMCE() {
        const themeToggle = document.querySelector('#theme-toggle');
        const isDarkMode = themeToggle && !themeToggle.checked;
        
        // doesn't delete user content i checked
        if (typeof tinymce !== 'undefined') {
            tinymce.remove();
        }
        
        tinymce.init({
          selector: '#id_bio, #id_sidebar',
          height: 500,
          width: '100%',
          theme: 'silver',
          skin: isDarkMode ? 'oxide-dark' : 'oxide',
          content_style: getThemeCSS(),
          plugins: 'accordion,advlist,anchor,autolink,autosave,charmap,code,emoticons,fullscreen,link,lists,preview,searchreplace,table,visualchars,wordcount',
          toolbar: 'undo redo | bold italic underline strikethrough | bullist numlist | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent | fullscreen preview save | charmap emoticons',
          toolbar_mode: 'floating',
          menubar: true,
          statusbar: true,
          promotion: false,
        });
    }
    
    initTinyMCE();
    
    // listen for theme toggle
    const themeToggle = document.querySelector('#theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('change', function() {
            initTinyMCE();
        });
    }
});