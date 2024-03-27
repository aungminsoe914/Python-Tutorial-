def mark_add(**mark):
    print("Number of mark is ",mark)
    total =0
    for k,v in mark.items():
        total +=v
        return total

mark_is = {
    "myanmar":30,
    "English":90,
    "Match":12
}

print("Total Mark is ",mark_add(**mark_is))