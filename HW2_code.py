def count_unique_words(filename):

    word_count = {} #建立dictionary儲存單字、紀錄次數

    #讀檔
    with open(filename, 'r') as file:
        
        for line in file:
            word = line.strip()

            if word in word_count:
                word_count[word] += 1

            else:
                word_count[word] = 1


    print("總共有", len(word_count), "個不重複的英文字")


    print("每一個英文字出現次數為何：")
    for word, count in word_count.items():
        print(word, ":", count)


count_unique_words("hw2_data.txt")
