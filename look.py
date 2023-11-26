# 创建一个列表，包含不适当的词汇
BAD_WORDS = ["badword1", "badword2", "badword3"]

def contains_bad_words(text):
    # 将输入的文本转换为小写
    text = text.lower()
    # 检查每一个不适当的词汇是否在文本中出现
    for bad_word in BAD_WORDS:
        if bad_word in text:
            return True
    # 如果没有不适当的词汇出现，返回False
    return False
