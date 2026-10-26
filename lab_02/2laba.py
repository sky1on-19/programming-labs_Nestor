def neutralize_ph(start_ph):
    cur_ph = start_ph
    d = 0
    while cur_ph < 6.5 or cur_ph > 7.5:
        if cur_ph < 6.5:
            cur_ph +=0.5
            d += 1
        elif cur_ph > 7.5:
            cur_ph -= 0.5
            d -= 1
    return d

ifs = input("Введите начальные значения: ")
ph_val = list(map(float, ifs.split()))
for ph in ph_val:
    r = neutralize_ph(ph)
    print("Для значения", ph , "требуется", r, "доз.")