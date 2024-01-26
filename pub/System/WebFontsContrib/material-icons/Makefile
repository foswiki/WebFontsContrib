FOSWIKI_ROOT?=~/foswiki/core

FONT_SOURCE=\
  MaterialIcons-Regular.ttf \
  MaterialIcons-Regular.woff2

TARGET=font-face.css material.json $(FONT_SOURCE)

-include $(FOSWIKI_ROOT)/pub/System/JQueryPlugin/Makefile.include

git:
	git clone https://github.com/google/material-design-icons.git git

fonts: $(FONT_SOURCE)

#json.txt: Makefile
#	@echo fetching $@ 
#	@wget -q -O - http://fonts.google.com/metadata/icons |tail +2 > $@

ifneq (,$(wildcard git))
material.json: generate-json git/font/MaterialIcons-Regular.codepoints
	@echo "generating $@"
	@./generate-json > $@

#material-4.json: generate-json json.txt
#	@echo "generating $@"
#	@./generate-json-4 > $@

font-face.uncompressed.css: generate-css git/font/MaterialIcons-Regular.codepoints
	@echo "generating $@"
	@./generate-css > $@

MaterialIcons-Regular.%: git/font/MaterialIcons-Regular.%
	@echo "generating $@"
	@$(CAT) $< > $@
endif

MaterialIcons-Regular.woff2: MaterialIcons-Regular.ttf
	@echo "generating $@"
	@woff2_compress $<
