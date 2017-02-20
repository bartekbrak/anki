.PHONY: default
default: compile ;

compile:
	python to_deck.py *.cards.md

push:
	python to_deck.py *.cards.md
	git add *.deck.txt *.cards.md
	git commit *.deck.txt *.cards.md -mup
	git pull --rebase
	git push

help:
	@echo "make [compile] - Compile *.cards.md to Anki importable *.deck.txt TSVs. Create all.deck.txt"
	@echo "make push      - Commit and push all changes in *.deck.txt *.cards.md."
	@echo "make help      - This help"

