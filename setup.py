from janome.tokenizer import Tokenizer
import gensim
import re

# setup class
class Setup:

    def separate_text(self, text_path, output_path):
        """separate text to fit markovify

        Parameters
        ----------
        text_path  : @{String} path to text
        output_path: @{String} path to output path

        Returns
        -------
        None

        """
        # read text
        text = open(text_path, 'rb').read()
        text = text.decode('utf-8')

        # delete disturbing word
        unwanted_chars = ['\r', '\u3000', '-', '｜']
        for uc in unwanted_chars:
            text = text.replace(uc, '')
        unwanted_patterns = [re.compile(r'《.*》'), re.compile(r'［＃.*］')]
        for up in unwanted_patterns:
            text = re.sub(up, '', text)

        # morphological analysis of text and break disturbing words
        words = Tokenizer().tokenize(text, wakati=True)
        breaking_chars = [
            '(',
            ')',
            '[',
            ']',
            '"',
            "'",
        ]
        splited_text = ''
        for word in words:
            if word not in breaking_chars:
                splited_text += word
            if word != '。' and word != '、':
                splited_text += ' '
            if word == '。':
                splited_text += '\n'
        
        # write into output file
        with open(output_path, 'w') as f:
            f.write(splited_text)
        print('finished!')
    
    def create_word_list(self, text_path):
        """create word list from wakati text
    
        Parameters
        ----------
        text_path : @{String} path to wakati text

        Returns
        -------
        new_list  : @{List} word list which is no duplicating

        """
        words = open('./output.txt', 'rb').read()
        words = words.decode('utf-8')
        word_list = re.split('[。(\n)(\s)]', words)
        new_list = []
        for word in word_list:
            if word not in new_list:
                new_list.append(word)
        return new_list