from collections import defaultdict
from fasttext import FastText
import json

MAX_LEN = 200
EMBEDDING_DIM = 32
BATCH_SIZE = 32
EPOCH = 1
NUM_CLASS = 6

dict_path = "label_dict.json"
train_data = "data/split_data_train.txt"
test_data = "data/split_data_test.txt"

with open("label_dict.json", 'r') as load_f:
    label_dict = json.load(load_f)


def load_data(path):
    x, y = [], []
    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.split('\t')

        y.append(label_dict[line[0]])
        x.append(line[1])

    return x, y


def cal_precision_and_recall(file):
    precision = defaultdict(int)
    recall = defaultdict(int)
    total = defaultdict(int)

    with open(file) as f:

        for line in f:
            label, content = line.split(',', 1)
            total[label.strip().strip('__label__')] += 1
            labels2 = model.predict(content.strip('\n'))
            pre_label, sim = labels2[0][0], labels2[1][0]

            recall[pre_label.strip().strip('__label__')] += 1

            if label.strip() == pre_label.strip():
                precision[label.strip().strip('__label__')] += 1

    for sub in precision.keys():
        pre = precision[sub] / total[sub]
        rec = precision[sub] / recall[sub]
        F1 = (2 * pre * rec) / (pre + rec)

        label_name = list(label_dict.keys())[list(label_dict.values()).index(int(sub))]
        print("{}, precison:{}, recall:{}, F1:{}".format(str(label_name.strip('/')), str(pre), str(rec), str(F1)))


if __name__ == '__main__':
    model = FastText.train_supervised(input=train_data,
                                      label_prefix="__label__",
                                      epoch=15,
                                      dim=32,
                                      lr=0.5,
                                      loss='softmax',
                                      verbose=2,
                                      minCount=3,
                                      word_ngrams=2,
                                      bucket=1000000
                                      )

    model.save_model('model/fasttext.bin')
    score = model.test(test_data)
    cal_precision_and_recall(test_data)
