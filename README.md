# HW2_code
##code
```
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

```
##執行結果

<img width="117" alt="image" src="https://github.com/weighing-331/HW2_hash_practice/assets/68834074/70c541cb-f6b9-445e-b072-ee5729edf56d">

*************
# HW2_code_sort
在HW2基礎上，加入讓使用者選擇排序方式的功能
##code
```
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

```

##執行結果(以default、count、length為例)

<img width="251" alt="image" src="https://github.com/weighing-331/HW2_hash_practice/assets/68834074/b35413b0-f5e0-46db-86b7-651dd9e970f2">
<img width="254" alt="image" src="https://github.com/weighing-331/HW2_hash_practice/assets/68834074/c7a4e3c0-41c0-4554-9fe9-2f331944415e">
<img width="257" alt="image" src="https://github.com/weighing-331/HW2_hash_practice/assets/68834074/282d33ab-8483-428b-938b-19bb4aa8a691">

