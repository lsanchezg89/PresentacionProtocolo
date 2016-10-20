# Makefile for LaTeX
##################################################################
# Use:
# make
# make clean
# options for ps2pdf: http://pages.cs.wisc.edu/~ghost/doc/AFPL/6.50/Ps2pdf.htm

TEX:=$(shell ls *.tex)
FILES= *.tex Makefile *.bst *.pdf *.bib
FOLDER= Seminario/
OTHER = *~ *.aux *.dvi *.toc *.blg *.out *.idx *.ilg *.ind *.tdo *.pdf *.tar.gz *.log *.spl *.synctex.gz
LATEX	= latex
BIBTEX	= bibtex
MAKEINDEX = makeindex
XDVI	= xdvi -gamma 4
DVIPS	= dvips
DVIPDF  = dvipdft
L2H	= latex2html
GH	= gv
FILES= *.tex *.sty *.png *.pdf Makefile
NAMETAR1:= $(shell date '+%Y%b%d_%H_%M')
NAMETAR="$(NAMETAR1)_Seminario.tar.gz"
NAMEZIP="$(NAMETAR1)_Seminario.zip"

pdflatex: demo.tex
	pdflatex --synctex=1 demo.tex
	pdflatex --synctex=1 demo.tex

clean:
	rm -f $(OTHER) $(PS)
	
tar: $(FILES)
	(cd .. && tar -cvf $(NAMETAR) $(FOLDER))

zip: $(FILES)
	(cd .. && zip -r $(NAMEZIP) $(FOLDER))
