slides:
	postcss src/css.css --use autoprefixer > css.css

clean:
	rm -rf css.css
