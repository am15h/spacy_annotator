# Takes a whitespace separated sentence
# iterates through each word
# maintains a set of all deps
# at each word takes input head
# at each word takes input dep
# writes in a JSON file

import tkinter as tk
from functools import partial
import json
from prettytable import PrettyTable

# Open file containing sentences


sentFile = open("sents", "r")

TRAIN_DATA = []

# tkinter MainWindow

def main():

    for sent in sentFile:
        m = tk.Tk()
        #sent = sentFile.readline()
        words = sent.strip().split(' ')
        heads = []
        deps = []
        deps_data = ["-", "ROOT", "ST_TIME", "ST_ADJ", "EN_TIME", "EN_ADJ", "CON", "TIME_ATTR"]
        insert_index_head = 0
        insert_index_dep = 0
        button_identities = []
        deps_identities = []

        def insert_callback(head_index):
            nonlocal insert_index_head
            heads.insert(insert_index_head, head_index)
            insert_index_head += 1
            if insert_index_head < words.__len__():
                label_text.set(words[insert_index_head])
            print_heads()

        def undo():
            nonlocal insert_index_head
            insert_index_head -= 1
            heads.pop(insert_index_head)
            if insert_index_head < words.__len__():
                label_text.set(words[insert_index_head])

        def insert_deps_callback(deps_index):
            nonlocal insert_index_dep
            deps.insert(insert_index_dep, deps_data[deps_index])
            insert_index_dep += 1
            if insert_index_dep < words.__len__():
                label_text2.set(words[insert_index_dep])
            print_deps()

        def undo_dep():
            nonlocal insert_index_dep
            insert_index_dep -= 1
            deps.pop(insert_index_dep)
            if insert_index_dep < words.__len__():
                label_text2.set(words[insert_index_dep])
            print_deps()

        def write_to_list():
            TRAIN_DATA.append((sent.strip(), {"heads": heads, "deps": deps}))
            print(TRAIN_DATA)
            m.destroy()

        print_sent_table(m, words)

        # tkinter table of buttons
        print_head_buttons(button_identities, insert_callback, m, words)

        # tkinter table of deps
        print_dep_buttons(deps_data, deps_identities, insert_deps_callback, m)

        undo_button = tk.Button(m, text="undo", width=10, command=undo)
        undo_button.grid(row=4, column=int(words.__len__()/2))

        undo_button_dep = tk.Button(m, text="undo dep", width=10, command=undo_dep)
        undo_button_dep.grid(row=4, column=int(words.__len__() / 2) + 1)

        label_text = tk.StringVar()
        label = tk.Label(m, textvariable=label_text, width=10, bg="lightgreen", pady=10)
        label.grid(row=3, column=int(words.__len__()/2))
        label_text.set(words[insert_index_head])

        label_text2 = tk.StringVar()
        label2 = tk.Label(m, textvariable=label_text2, width=10, bg="red", pady=10)
        label2.grid(row=3, column=int(words.__len__() / 2)+1)
        label_text2.set(words[insert_index_dep])

        # tkinter table heads
        def print_heads():
            b = tk.Label(m, text="HEADS", width=10, bg='orange')
            b.grid(row=7, column=0)
            for i in range(2):
                for j in range(heads.__len__()):
                    if i == 0:
                        b = tk.Label(m, text=words[j], width=10)
                        b.grid(row=i + 8, column=j)
                    elif i == 1:
                        b = tk.Label(m, text=words[heads[j]], width=10)
                        b.grid(row=i + 8, column=j)

        # tkinter dep print
        def print_deps():
            for j in range(deps.__len__()):
                b = tk.Label(m, text=deps[j], width=10)
                b.grid(row=10, column=j)


        write_button = tk.Button(m, text="WRITE", command=write_to_list)
        write_button.grid(row=11, column=0)


        m.mainloop()

    with open('data.json', 'a', encoding='utf-8') as f:
        json.dump(TRAIN_DATA, f, ensure_ascii=False, indent=4)


def print_dep_buttons(deps_data, deps_identities, insert_deps_callback, m):
    for j in range(deps_data.__len__()):
        b = tk.Button(m, text=deps_data[j], width=10, command=partial(insert_deps_callback, j))
        deps_identities.append(b)
        b.grid(row=6, column=j, pady=10)


def print_head_buttons(button_identities, insert_callback, m, words):
    for j in range(words.__len__()):
        b = tk.Button(m, text=words[j], width=10, command=partial(insert_callback, j))
        button_identities.append(b)
        b.grid(row=5, column=j, pady=10)


def print_sent_table(m, words):
    # tkinter table
    for i in range(2):
        for j in range(words.__len__()):
            if i == 0:
                b = tk.Label(m, text=str(j), width=10)
                b.grid(row=i, column=j)
            elif i == 1:
                b = tk.Label(m, text=words[j], width=10)
                b.grid(row=i, column=j)


if __name__ == '__main__':
    main()
