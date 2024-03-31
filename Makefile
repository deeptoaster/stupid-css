all: css.css

css.css: src/css.css
	postcss src/css.css --use autoprefixer > css.css

clean:
	rm -rf css.css
