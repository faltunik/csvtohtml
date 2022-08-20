from django.shortcuts import render
from django.shortcuts import render
import csv


def index(request):
    # opening the csv file
    main = []
    word = request.GET.get("query", "")
    ky = int(request.GET.get("key", 0))

    print(word)
    print(type(word))

    with open('mywork\example.csv', mode ='r')as csv_file:
        
        csvFile = csv.reader(csv_file)
        lst = list(csvFile)
        for i in range(len(lst)):
            if i ==0: continue
            for wrd in lst[i]:
                if word in wrd.lower():
                    main.append(lst[i])
                    break
        
    main = sorted(main, key = lambda x: x[ky])
    print("main list is: ", main)
    return render(request, "mywork/index.html", {
        "details": main,
        "query": word,
        "key": ky
    })


