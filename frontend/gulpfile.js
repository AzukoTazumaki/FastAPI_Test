const { src, dest, watch } = require('gulp')
const concatCss = require('gulp-concat-css');
const cleanCSS = require('gulp-clean-css');

function css() {
  return src([
    'src/assets/css/*.css',
    'node_modules/bootstrap/dist/css/bootstrap.min.css'
  ])
    .pipe(concatCss('bundle.min.css'))
    .pipe(cleanCSS({ compatibility: 'ie8' }))
    .pipe(dest('src/public/'));
}
exports.css = function () {
  watch('src/assets/css/*.css', css);
}