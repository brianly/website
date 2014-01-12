all:
	acrylamid compile
	rm -rf output/.sass-cache/
	rm -rf output/sass/
	rm -rf output/scss/
	rm -rf output/config.rb
	rm -rf output/bower.json
deploy:
	acrylamid compile
	acrylamid deploy
live:
	acrylamid compile
	acrylamid deploy production
clean:
	rm -rf output/*
	rm -rf output/.sass-cache/
	rm -rf output/.htaccess