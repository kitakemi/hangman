#
def hangman(word):
    wrong = 0 #間違えた回数
    #吊られた人のリスト
    stages = ["",
              "__________   ",
              "|            ",
              "|        |   ",
              "|        O   ",
              "|       /|\  ",
              "|       / \  ",
              "|            "
              ]
    rletters = list(word) #1文字ずつの要素に分解
    board = ["_"] * len(word) #p2に見せるヒント、文字数、現段階での正解
    win = False #ゲームに勝ったかどうかのフラグ
    print("ハングマンへようこそ！")

    #ゲームの手順
    while wrong < len(stages)-1:
        print("\n") #空行を出力
        msg = "１文字を予想して入力してね："
        char = input(msg)
        if char in rletters: #正解していたら
            cind = rletters.index(char) #正解のインデックス番号を取得
            board[cind] = char #boardの値を更新
            rletters[cind] = '$' #同じアルファベットがあった場合の処理
        else:
            wrong += 1
        print(" ".join(board)) #現時点での正解状況を出力
        e = wrong + 1
        print("\n".join(stages[0:e])) #改行コードで間違った回数だけ結合
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board)) #正解の表示
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1])) #絵を全て表示
        print("あなたの負け！正解は {}.".format(word))

hangman("sapporo")
