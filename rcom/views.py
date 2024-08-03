from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def chak(request):
    if request.method=="GET":
        st=request.GET.get("usertxt")
        if request.GET.get("rv","off") == "on":
            x=""
            for i in st:
                if i.lower() != "a" and i.lower() != "e" and i.lower() != "i" and i.lower() != "o" and i.lower() != "u":
                    x+=i
            st=x
        if request.GET.get("rs","off") == "on":
            x=""
            for i in range(0,len(st)-1):
                if st[i]==" " and st[i+1]==" ":
                    st+=""
                else:
                    x+=st[i]
            st=x
        if request.GET.get("du","off") == "on":
            st=st.upper()
        if request.GET.get("rp","off") == "on":
            plist = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
            x=""
            for i in st:
                if i not in plist:
                    x+=i
            st=x

        ele={
            "content" : st,
        }
        return render(request,"rpac.html" ,ele)
    return render(request,"rpac.html")