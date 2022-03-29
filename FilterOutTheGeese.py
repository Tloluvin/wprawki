geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    result = []
    for i in birds:
        if i not in geese:
            result.append(i)
    return result


print(goose_filter(["Mallard", "Hook Bill", "African",
      "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))
