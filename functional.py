def flatten_and_sort(sort_func, arr):
    out = []
    for item in arr:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)

    return sort_func(out) 

first_collection = [1, [55, 17, 12],3, [22, 19, 35], 9,2]
print(flatten_and_sort(sorted, first_collection))
print(first_collection)

""""


How does this solution ensure data immutability?
    passes back a different collection than the one passed in

Is this solution a pure function? Why or why not?

yes : it does not produce side effects and does not retain state

Is this solution a higher order function? Why or why not?

NO: it does not take function as a parameter nor does it return a function

Would it have been easier to solve this problem using a different programming style?
no: this seems fine

Why in particular is functional programming a helpful paradigm when solving this problem?
 because it is side effect free and because it uses a pure function the results will be consistent




"""