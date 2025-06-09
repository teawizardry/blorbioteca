import gulp from 'gulp';
import fontfacegen from 'gulp-fontfacegen';
import ttf2woff from 'gulp-ttf2woff';
import fs from 'fs';

function fonts(folder, done) {
    gulp.src([folder], {
        encoding: false, // Important!
        removeBOM: false,
        })
        .pipe(ttf2woff({ clone: false }))
        .pipe(gulp.dest('_site/assets/fonts'))
        .pipe(
            fontfacegen({
                filepath: "assets/css",
                filename: "fontFaces.css",
		csspath: "fonts",
             })
        )
        .on('end', function () {
        if (done) {
            done(); // callback to signal end of build
        }
        });
}

fs.unlink('assets/css/fontFaces.css', (err) => {
    if (err) {
        console.log('No fontFaces.css to delete...');
    } else {
        console.log('Current fontFaces.css deleted...');
    }
});

fs.readdir("assets/fonts", { withFileTypes: true}, (err, folders) => {
    if (err) {
        console.log(err);
    }
    else {
        console.log("Fonts Found:");
        folders.forEach(folder => {
            if (folder.isDirectory()) {
                console.log(folder.name);
                fonts('assets/fonts/' + folder.name + '/*.ttf', function () {

                });
            }

        });
    }
});
