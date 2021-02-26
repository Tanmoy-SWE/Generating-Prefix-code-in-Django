from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django import forms

def pp(request):
    from collections import defaultdict
    from heapq import heappush, heappop, heapify
    st = ""
    try :
        st = request.GET["fname"]
    except :
        pass
    def generateID(ID):
        i = 0
        s = ID[-4:]
        txt = ""
        txt += "MYIDIS"
        while i < len(s):
            if s[i] == '0':
                txt += "ZERO"
            elif s[i] == '1':
                txt += "ONE"
            elif s[i] == '2':
                txt += "TWO"
            elif s[i] == '3':
                txt += "THREE"
            elif s[i] == '4':
                txt += "FOUR"
            elif s[i] == '5':
                txt += "FIVE"
            elif s[i] == '6':
                txt += "SIX"
            elif s[i] == '7':
                txt += "SEVEN"
            elif s[i] == '8':
                txt += "EIGHT"
            elif s[i] == '9':
                txt += "NINE"
            i += 1
        return txt

    Id = st
    msg = generateID(Id)
    print("Generated String : " + msg)
    frequency = defaultdict(int)
    for j in msg:
        frequency[j] += 1

    tree = [[a, [b, ""]] for b, a in frequency.items()]

    heapify(tree)
    print(tree)
    while len(tree) > 1:
        right = heappop(tree)
        left = heappop(tree)

        for pair in right[1:]:
            pair[1] = '0' + pair[1]
        for pair in left[1:]:
            pair[1] = '1' + pair[1]
        heappush(tree, [right[0] + left[0]] + right[1:] + left[1:])
    huffman_list = right[1:] + left[1:]
    n = 0
    nam = ""
    print("Prefix Codes : (Generated using Huffman Coding)")
    while n < len(huffman_list):
        print(huffman_list[n][0] + " :", huffman_list[n][1])
        nam += (str)(huffman_list[n][0]) + " :"+ (str)(huffman_list[n][1])+ "<br>"
        n += 1

    return HttpResponse('''
    <form action="/">
      <label for="fname">Enter your student id</label><br>
      <input id="fname" type="text" name="fname" value="190042123">
     <input type="submit" value="OK">
    </form> <br> 
    '''
    "Generated String : "+msg+"<br>"
                          +"Prefix Codes : (Generated using Huffman Coding)"
                          +"<br>"+nam

    )


