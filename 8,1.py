
l = [i% for i in range(10)]
print()
it = iter(l)
while it:
    try:
        print(next(it))
    except:
        break