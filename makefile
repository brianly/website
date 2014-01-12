all:
	compass compile theme
	acrylamid compile
	rm -rf output/.sass-cache/
	rm -rf output/sass/
	rm -rf output/scss/
	rm -rf output/config.rb
	rm -rf output/bower.json
deploy:
	compass compile theme
	acrylamid compile
	rm -rf output/.sass-cache/
	rm -rf output/sass/
	rm -rf output/scss/
	rm -rf output/config.rb
	rm -rf output/bower.json
	acrylamid deploy
live:
	compass compile theme
	acrylamid compile
	rm -rf output/.sass-cache/
	rm -rf output/sass/
	rm -rf output/scss/
	rm -rf output/config.rb
	rm -rf output/bower.json
	acrylamid deploy production
clean:
	rm -rf output/*
	rm -rf output/.sass-cache/
	rm -rf output/.htaccess