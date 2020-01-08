## Design:
the union and intersection functions have been implemented using a combination of arrays and sets, array conversion was chosen for ease of manipulation and sets have been used to remove duplicates


## Time Complexity
* union:
union uses the helper function to list, this iterates through the linked list and returns a list in linear proportion to the input, a further 2 more loops of the input are done in linear fashion meaning this function overall is 0(n)

* intersection:
intersection is quadratic as there is a loop over one list for containment in another and this dominated the other loops 

## Space Complexity
space is a linear concern 0(n) as it will grow depending on the size linked lists specified