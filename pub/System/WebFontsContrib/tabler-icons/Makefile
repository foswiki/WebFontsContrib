FOSWIKI_ROOT?=~/foswiki/core
TARGET=tabler-icons.json font-face.css 

-include $(FOSWIKI_ROOT)/pub/System/JQueryPlugin/Makefile.include

tabler-icons.json: generate-json font-face.uncompressed.css
	@echo "generating $@"
	@./generate-json > $@
