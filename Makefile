serve:
	docker run --rm -it \
		--volume="$(CURDIR):/srv/jekyll" \
		--volume="$(CURDIR)/vendor/bundle:/usr/local/bundle" \
		--publish=4000:4000 \
		jekyll/jekyll jekyll serve

update:
	docker run --rm -it \
		--volume="$(CURDIR):/srv/jekyll" \
		--volume="$(CURDIR)/vendor/bundle:/usr/local/bundle" \
		jekyll/jekyll bundle update
