def most_frequent(string):
    d = {}
    for key in string:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    dl = set(d.values())
    for i in range(len(dl)):
      max_ = max(dl)
      for k, v in d.items():
          if v == max_:
              print(k, '=', v)
      dl.remove(max_)

string = str(input('Please enter a string :'))
most_frequent(string)
