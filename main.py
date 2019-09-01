import markovify
import sys
import gensim
import setup
setup = setup.Setup()

def main():
    print('creating word_list...')
    word_list = setup.create_word_list('./output.txt')

    print('searching max_similar_word...')
    max_similar_word = search_similar_word('./model.bin', sys.argv[1], word_list)

    splited_text = open('output.txt').read()

    print('creating models...')
    text_model = markovify.NewlineText(splited_text)

    print('markov_word = ' + max_similar_word['word'])

    try:
        print('making sentence...')
        sentence = text_model.make_sentence_with_start(max_similar_word['word'], tries=300, max_overlap_ratio=0.9).replace(' ', '')
        print(sentence)
    except:
        print('文が生成できませんでした')

def search_similar_word(model_path, search_word, word_list):
    """search similar word from corpus

    Parameters
    ----------
    model_path  : @{String} path to fasttext model
    search_word : @{String} word you want know similar word
    word_list   : @{List}   you can search similar word from this
    
    Returns
    -------
    max_similar
        -- word       : @{String} similar word
        -- similarity : @{Float}  how similar search_word and return word
    
    """
    is_binary = re.match('.+bin$', model_path)
    model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=is_binary)
    max_similar = { 'word': '', 'similarity': 0 }
    tmp_similar = 0
    for word in word_list:
        try:
            tmp_similar = model.similarity(search_word, word)
        except:
            continue
        if max_similar['similarity'] < tmp_similar:
            max_similar = { 'word': word, 'similarity': tmp_similar }
    return max_similar

if __name__ == '__main__':
    main()