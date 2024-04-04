def count_unique_words(filename):

    word_count = {} # 建立dictionary {"單字":出現次數}


    # 讀檔
    with open(filename, 'r') as file:
        for line in file:

            word = line.strip() # 去除換行符號

            if word in word_count:
                word_count[word] += 1

            else:
                word_count[word] = 1

    # 輸入排序方式
    sort_by = input("排序方式（alphabet/length/count/order）：")

    if sort_by == "alphabet":
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[0])
        
    elif sort_by == "length":
        sorted_word_count = sorted(word_count.items(), key=lambda x: len(x[0]))

    elif sort_by == "count":
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    elif sort_by == "order":
        sorted_word_count = list(word_count.items())
    
    else:
        print("Invalid. Defaulting to alphabetic order.")
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[0])


    print("共有", sum(1 for line in open(filename)), "行")

    print("共有", len(word_count), "個不重複的單字")

    print("每一個單字出現次數（排序方式：{}）：".format(sort_by))
    for word, count in sorted_word_count:
        print(word, ":", count)

count_unique_words("hw2_data.txt")
