from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect


time=""
name=""
graph1=""

class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')
        
class user1(View):
    def post(self,request):
        global name
        name=request.POST.get("topic")
        print(name)
        #return render(request,'index.html',locals())
        # post = Post(caption=age, postedBy=name)
        # post.save()
        return HttpResponseRedirect("/")

class zone(View):
    def post(self,request):
        global time
        time=request.POST.get("zone")
        print(time)
        #return render(request,'index.html')
        return HttpResponseRedirect("/")



class types(View):
    def post(self,request):
        t=request.POST.get("graph")
        myVars={'time':time,'name':name,'graph1':t}
        exec(open('plots.py').read(),myVars)
       # k=5
        #exec(open('plots.py').read())
        # import subprocess
        # subprocess.Popen("plots.py", shell=True)
        
       # import plots
        #return render(request,'1.html')
        return HttpResponseRedirect("/")
        #subprocess.run(['python','plots.py', name,time,t], shell=True)

