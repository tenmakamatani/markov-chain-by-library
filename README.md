# markov-chain-by-library

引数に指定された単語からfasttextによりマルコフ連鎖のコーパスに含まれる類義語を求め、それを元に文章を生成します

## How to run

### clone this repository

```
$ git clone https://github.com/tenmakamatani/markov-chain-by-library.git
$ cd markov-chain-by-library
```

You have to prepare trained model at root

### if you use pipenv

```
$ pipenv install
$ pipenv run python main.py
```

### if you don't use pipenv

```
$ pip install janome markovify gensim
$ python main.py
```