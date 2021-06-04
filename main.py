from predictor import Predictor

if __name__ == '__main__':
    data = 'data/' + 'train.txt'
    predictor = Predictor(data)
    
    print("Number of Unigrams", len(predictor.unigrams.keys()))
    print("Number of Bigrams", len(predictor.bigrams.keys()))
    print("Number of trigrams", len(predictor.trigrams.keys()))
    print("Number of four grams", len(predictor.fourgrams.keys()))
    print("Number of five grams", len(predictor.fivegrams.keys()))
    
    
    print("finished")
