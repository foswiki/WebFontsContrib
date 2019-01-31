FOSWIKI_ROOT?=~/foswiki/core
TARGET=font-face.css material.json

FONT_SOURCE=\
  MaterialIcons-Regular.eot \
  MaterialIcons-Regular.ttf \
  MaterialIcons-Regular.woff \
  MaterialIcons-Regular.woff2

-include $(FOSWIKI_ROOT)/pub/System/JQueryPlugin/Makefile.include

git:
	git clone https://github.com/google/material-design-icons.git git

fonts: $(FONT_SOURCE)

ifneq (,$(wildcard git))
material.json: generate-json git/iconfont/codepoints
	@echo "generating $@"
	@./generate-json > $@

font-face.uncompressed.css: generate-css git/iconfont/codepoints
	@echo "generating $@"
	@./generate-css > $@

MaterialIcons-Regular.%: git/iconfont/MaterialIcons-Regular.%
	@echo "generating $@"
	@$(CAT) $< > $@

nestedSortable.uncompressed.js: git/jquery.mjs.nestedSortable.js
	@echo "generating $@"
	@$(CAT) $< > $@
endif
