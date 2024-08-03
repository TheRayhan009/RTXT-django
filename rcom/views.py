from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def chak(request):
    if request.method=="POST":
        st=request.POST.get("usertxt")
        c=False
        if request.POST.get("rv","off") == "on":
            c=True
            x=""
            for i in st:
                if i.lower() != "a" and i.lower() != "e" and i.lower() != "i" and i.lower() != "o" and i.lower() != "u":
                    x+=i
            st=x
        if request.POST.get("rs","off") == "on":
            c=True
            x=""
            for i in range(0,len(st)-1):
                if st[i]==" " and st[i+1]==" ":
                    st+=""
                else:
                    x+=st[i]
            st=x
        if request.POST.get("du","off") == "on":
            c=True
            st=st.upper()
        if request.POST.get("rp","off") == "on":
            c=True
            plist = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
            x=""
            for i in st:
                if i not in plist:
                    x+=i
            st=x
        if request.POST.get("rnl","off") == "on":
            c=True
            x=""
            for i in st:
                if i !="\n" and i != "\r":
                    x+=i
            st=x
        if c==True:
            ele={
                "content" : st,
            }
            return render(request,"rpac.html" ,ele)
        else:
            return render(request,"error2.html")
    else:
        return render(request,"error.html")