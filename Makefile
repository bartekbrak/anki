.PHONY: default
default: compile ;

compile:
	python to_deck.py *.cards.md

push:
	python to_deck.py *.cards.md
	git add *.txt *.cards.md
	git commit *.txt *.cards.md -mup
	git pull --rebase
	git push
