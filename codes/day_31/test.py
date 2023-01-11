import pandas as pd
words = pd.read_csv("data/french_words.csv")
words_dict = words.to_dict(orient="records")
words_dict.remove({'French': 'partie', 'English': 'part'})

words_back = pd.DataFrame.from_records(words_dict)
print(words_back)