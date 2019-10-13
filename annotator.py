# Takes a whitespace separated sentence
# iterates through each word
# maintains a set of all deps
# at each word takes input head
# at each word takes input dep
# writes in a JSON file

import tkinter as tk
from functools import partial
from prettytable import PrettyTable

# Open file containing sentences


sentFile = open("sents", "r")


# tkinter MainWindow

def main():

    m = tk.Tk()
    sent = sentFile.readline()
    words = sent.strip().split(' ')
    heads = []
    deps = []
    btns = []
    # t = PrettyTable()
    # for idx, word in enumerate(words):
    #     t.add_column(str(idx), [word])
    # print(t)
    insert_index_head = 0

    button_identities = []

    def insert_callback(head_index):
        nonlocal insert_index_head
        heads.insert(insert_index_head, head_index)
        insert_index_head += 1
        labelText.set(words[insert_index_head])

    # tkinter table
    for i in range(2):
        for j in range(words.__len__()):
            if i == 0:
                b = tk.Label(m, text=str(j), width=10)
                b.grid(row=i, column=j)
            elif i == 1:
                b = tk.Label(m, text=words[j], width=10)
                b.grid(row=i, column=j)

    # for i in range(words.__len__()):
    #     h = input(str("Head for " + words[i] + "=>"))
    #     heads.append(h)

    # tkinter table of buttons
    for j in range(words.__len__()):
        b = tk.Button(m, text=words[j], width=10, command=partial(insert_callback, j))
        button_identities.append(b)
        b.grid(row=5, column=j, pady=10)

    labelText = tk.StringVar()
    label = tk.Label(m, textvariable=labelText, width=10)
    label.grid(row=3, column=0)
    labelText.set(words[insert_index_head])

    # t2 = PrettyTable()
    # for idx, word in enumerate(words):
    #     t2.add_column(word, [words[int(heads[idx])]])
    # print(t2)

    m.mainloop()

if __name__ == '__main__':
    main()