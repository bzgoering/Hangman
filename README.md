# Hangman

A command-line version of Hangman. Random words come from the NLTK words library, and you can add your own words or play with a custom word list.

## Tech
- Python 3
- [NLTK](https://www.nltk.org/) (`words` corpus)

## How to run
```bash
pip install nltk
python -c "import nltk; nltk.download('words')"
python Main.py
```

## How to play
At startup you choose whether to use a custom word list (y/n). This choice can't be changed later. If the custom list is left empty, the default list is used.

Menu options:
- `1`: play a round
- `2`: add a word to the word list
- `3`: add a word to your custom list
- `0`: quit

In a round, type a letter or guess the whole word. You get 6 wrong guesses.
