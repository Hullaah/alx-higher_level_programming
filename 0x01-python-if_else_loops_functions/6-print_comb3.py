for i in range(9):
     for j in range(1, 10):
             print(f"{i}{j + i}", end="\n" if i == 8 else ", ")
             if j + i == 9:
                     break
