import jieba

"_".join(jieba.cut("k"))

def cut_word(in_word, return_list: bool = False, divide: str = "/"):
    if return_list:
        return jieba.lcut(in_word)
    else:
        return "/".join(jieba.cut(in_word))

if __name__ == "__main__":
    while True:
        st = input("输入待分词句子 : ")
        seg = jieba.cut(st, cut_all = False)
        print("/".join(seg))

