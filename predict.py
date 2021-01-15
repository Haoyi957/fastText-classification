from fasttext import FastText
from text_preprocess import TextProcess
import json

model_path = "model/fasttext.bin"
model = FastText.load_model(model_path)

with open("label_dict.json", 'r') as load_f:
    label_dict = json.load(load_f)


def predict(text):
    pre_label = model.predict(TextProcess().word_preprocess(text))
    label_index = pre_label[0][0].strip().strip('__label__')
    label_name = list(label_dict.keys())[list(label_dict.values()).index(int(label_index))]

    return label_name


if __name__ == '__main__':
    text = input("Please input sentence: ")
    print("result:", predict(text))
