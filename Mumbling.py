def accum(s):
    result = ''
    for i, e in enumerate(s):
        if i == (len(s)-1):
            result = result + (f"{e.upper()}{e.lower()*(i)}")
        else:
            result = result + (f"{e.upper()}{e.lower()*(i)}-")
    return result


print(accum("ZpglnRxqenU"))
print(accum("NyffsGeyylB"))
print(accum("HbideVbxncC"))
