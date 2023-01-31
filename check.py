import time

print("导入数据中...")
sttime = time.time()
import cut_text
total = 3
lis = []
lis1 = []
f = None
fname = "./output.txt"
for i in range(3):
    fname = f"output{i+1}.txt"
    with open(fname, "r", encoding="utf-8") as f:
        lis1 = f.read().split("\n")
    lis += list(set(lis1))

with open("oneword.txt", "r", encoding="utf-8") as f:
    lis += f.read().split("\n")

while "" in lis:
    lis.remove("")
print("文件读取完成")
lis = list(set(lis))
replace_lis = [" ", "，", "。", "……", "！", ",", ".", "?", "？", "!"]
word_slis = "qwertyuiopasdfghjklzxcvbnm1234567890."
word_lis = list(set(list(word_slis.lower()) + list(word_slis.upper())))
k = None
wd = None
print("更新分词词库...")
for k in lis:
    if len(k) > 4:
        continue
    for wd in word_lis:
        if wd in k:
            break
        else:
            cut_text.jieba.add_word(k)
print("词库更新完成，正在释放无用内存")
del lis1
del fname
del f
del i
del word_slis
del word_lis
del k
del wd
used_time = time.time() - sttime
print(f"导入数据完成，耗时{used_time}，数据列表长度{len(lis)}")

def check_words(input_str):
    sttime = time.time()
    input_str = cut_text.cut_word(input_str, False, "/b ")
    for rp in replace_lis:
        input_str = input_str.replace(rp, "/b ")
    is_beat = False
    beat_words = []
    for k in lis:
        if k in input_str:
            is_beat = True
            beat_words += [k]
    used_times = time.time() - sttime
    ret_dict = {}
    ret_dict["divide"] = input_str
    if is_beat:
        ret_dict["pass"] = False
        beat_words = list(set(beat_words))
        ret_dict["words"] = beat_words
    else:
        ret_dict["pass"] = True
    ret_dict["time"] = used_times
    return ret_dict

if __name__ == "__main__":
    while True:
        st = input("输入词段: ")
        sttime = time.time()
        st = cut_text.cut_word(st, False, "/b ")
        for rp in replace_lis:
            st = st.replace(rp, "/b ")
        is_beat = False
        beat_words = []
        for k in lis:
            if k in st:
                is_beat = True
                beat_words += [k]
        used_times = time.time() - sttime
        print("分词结果:", st)
        if is_beat:
            print("违规")
            beat_words = tuple(set(beat_words))
            print(*beat_words)
        else:
            print("pass")
        print("检测耗时:", used_times)
