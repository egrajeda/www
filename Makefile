serve:
	docker run --rm -it \
		--volume="$(CURDIR):/srv/jekyll" \
		--volume="$(CURDIR)/vendor/bundle:/usr/local/bundle" \
		--publish=4000:4000 \
		--publish=35729:35729 \
		jekyll/jekyll jekyll serve --livereload

update:
	docker run --rm -it \
		--volume="$(CURDIR):/srv/jekyll" \
		--volume="$(CURDIR)/vendor/bundle:/usr/local/bundle" \
		jekyll/jekyll bundle update

deploy:
	docker run --rm -it \
		--volume="$(CURDIR):/srv/jekyll" \
		--volume="$(CURDIR)/vendor/bundle:/usr/local/bundle" \
		--publish=4000:4000 \
		jekyll/jekyll jekyll build

	aws s3 sync --acl public-read --delete _site/ s3://egrajeda.com/
