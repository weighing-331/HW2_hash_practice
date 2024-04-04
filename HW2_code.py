def count_unique_words(filename):

    word_count = {} # 建立dictionary {"單字":出現次數}
    total_lines = 0

    # 讀檔
    with open(filename, 'r') as file:
        for line in file:

            total_lines += 1
            word = line.strip() # 去除換行符號

            if word in word_count:
                word_count[word] += 1

            else:
                word_count[word] = 1

    print("共有", total_lines, "行")

    print("共有", len(word_count), "個不重複的單字")

    print("每一個單字出現次數：")
    for word, count in word_count.items():
        print(word, ":", count)

count_unique_words("hw2_data.txt")
