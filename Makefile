# Makefile

# Create lists for chapter filenames
CHAPTER_NAMES = chapter1 chapter2
CHAPTER_DIRECTORIES = $(addprefix chapters/, $(addsuffix /, $(CHAPTER_NAMES)))
CHAPTER_PDFS = $(join $(CHAPTER_DIRECTORIES), $(addsuffix .pdf, $(CHAPTER_NAMES)))
CHAPTER_TEXS = $(CHAPTER_PDFS:.pdf=.tex)

# Eventually, we might have more PDFs/TEXs
SUBFILE_PDFS = $(CHAPTER_PDFS)
SUBFILE_TEXS = $(CHAPTER_TEXS)

# Command for latexmk to generate pdf only
LATEXMK = latexmk -pdf -dvi- -ps- -quiet -silent
CLEAR = latexmk -c

# Handling the extremely verbose output of latexmk
OUT = logs/log.out
ERR = logs/log.err
HIDE = >> $(OUT) 2>> $(ERR)

thesis: thesis.pdf $(SUBFILE_PDFS)
	mkdir -p ./pdfs
	find . -path ./pdfs -prune -o -name "*.pdf" -exec cp {} pdfs \;

.PHONY: thesis

thesis.pdf: thesis.tex $(SUBFILE_TEXS)
	rm -f $(OUT) $(ERR)
	$(LATEXMK) thesis.tex $(HIDE); $(CLEAR) $(HIDE)

%.pdf: %.tex
	cd $(<D); $(LATEXMK) $(<F) $(HIDE); $(CLEAR) $(HIDE)
