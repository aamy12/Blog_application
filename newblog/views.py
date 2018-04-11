from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Post
from .models import Blogs


class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)


class RegisterPageView(TemplateView):
	template_name = "register.html"


class LoginPageView(TemplateView):
	template_name = "login.html"


class DashboardPageView(TemplateView):
	template_name = "dashboard.html"


class CreateBlogPageView(TemplateView):
	template_name = "createblog.html"


class ViewBlogPageView(TemplateView):
	template_name = "viewblog.html"


class ResetPassPageView(TemplateView):
	template_name = "reset.html"



from django.contrib.auth import authenticate


def resetPassword(request):
	if request.method == 'POST':
		print('hi')
		emailid=request.POST.get('emailid')
		movie=request.POST.get('movie')
		dessert=request.POST.get('dessert')
		password=request.POST.get('newpassword')
		rpassword = request.POST.get('copynpass')
		x=Post.objects.filter(emailid=emailid)
		try:
			if x[0].movie==movie and x[0].dessert==dessert:
				request.session['emailid'] =x[0].emailid
				if password==rpassword:
					Post.objects.filter(emailid=emailid).update(password=password)
					output = render(request,'login.html')
				else:
					output = render(request,'reset.html')
			else:
				output=render(request,'reset.html')
		except:
			output = render(request,'failed.html')

	return output

'''
def resetPassword(request):
	print("say hi")
	if request.method == 'POST':
		emailid = request.POST.get('emailid')
		movie = request.POST.get('movie')
		dessert = request.POST.get('dessert')
		password = request.POST.get('newpassword')
		#rpassword = request.POST.get('copynpass')

		try:
			user = authenticate(emailid=emailid, movie=movie, dessert=dessert)
			if user is not None:
				Post.objects.filter(emailid=emailid).update(password=password)
				output = render(request, 'login.html')
			else:
				output = render(request, 'reset.html')
		except:
			output = render(request, 'failed.html')

		return output

'''

def register(request):
	if request.method == 'POST':
		if request.POST.get('name') and request.POST.get('emailid') and request.POST.get('password'):
			post = Post()
			post.name = request.POST.get('name')
			post.emailid = request.POST.get('emailid')
			post.password = request.POST.get('password')
			post.movie = request.POST.get('movie')
			post.dessert = request.POST.get('dessert')
			post.save()

			return render(request, 'login.html')

		else:
			return render(request, 'failed.html')


def validate(request):
	emailid = request.POST.get('emailid')
	password = request.POST.get('password')

	x = Post.objects.filter(emailid=emailid)
	try:
		if x[0].password == password:
			request.session['emailid'] = x[0].emailid
			print('yasss')
			output = render(request, 'dashboard.html')
		else:
			output = render(request, "login.html")
	except:
		output = render(request, 'login.html')

	return output


def viewBlog(request):
	user = request.session['emailid']
	print(user)
	userblog = Blogs.objects.filter(emailid=user)
	return render(request, 'viewblog.html', {'blogs': userblog})


# Create your views here.
def createBlog(request):
	if request.method == 'POST':
		if request.POST.get('title') and request.POST.get('content'):
			blogs = Blogs()
			blogs.title = request.POST.get('title')
			blogs.content = request.POST.get('content')
			blogs.emailid = request.session['emailid']
			blogs.save()

			return render(request, 'successpage.html')

		else:
			return render(request, 'failed.html')
'''
def resetPassword(request):
	if request.method == 'POST':
		print('hi')
		emailid=request.POST.get('emailid')
		movie=request.POST.get('movie')
		dessert=request.POST.get('dessert')
		password=request.POST.get('newpassword')
		rpassword = request.POST.get('copynpass')
		x=Post.objects.filter(emailid=emailid)
		try:
			if x[0].movie==movie and x[0].dessert==dessert:
				request.session['emailid'] =x[0].emailid
				if password==rpassword:
					Post.objects.filter(emailid=emailid).update(password=password)
					output = render(request,'login.html')
				else:
					output = render(request,'reset.html')
		except:
			output = render(request,'failed.html')

	return output

'''

