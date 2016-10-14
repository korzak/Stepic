def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] += [value]
    elif 2*key in d.keys():
        d[2*key] += [value]
    else:
        d[2*key] = [value]




d = {'C': [14], 3: [12], 'T': [9], 8: [18]}
update_dictionary(d, 5, 2)
print(d)