all: out/formalization.pdf

out/:
	mkdir -p out

out/formalization.pdf: out/
	pandoc -o out/formalization.pdf src/formalization.md

clear:
	rm -rf out
