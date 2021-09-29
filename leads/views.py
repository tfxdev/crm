from django.http import request
from django.shortcuts import render, redirect, reverse
from django.views import generic
from . models import *
from . forms import *
 
class BangladeshView(generic.TemplateView):
	template_name = 'lead/bangladesh.html'

class SignupView(generic.CreateView):
	template_name = 'registration/signup.html'
	form_class = CustomUserCreationForm

	def get_success_url(self):
		return reverse('login')

class HomepageView(generic.TemplateView):
	template_name = "site-home.html"


class LeadHomepageView(generic.ListView):
	template_name = "lead/home.html"
	queryset = Leads.objects.all()
	context_object_name = "leads"

class LeadDetailsPageView(generic.DetailView):
	template_name = "lead/details.html"
	queryset = Leads.objects.all()
	context_object_name = 'lead'


class CreateLeadsView(generic.CreateView):
	template_name = 'lead/create.html'
	form_class = LeadModelform
	context_object_name = 'form'

	def get_success_url(self):
		return reverse("leads:lead_page")

class LeadUpdateView(generic.UpdateView):
	template_name = 'lead/create.html'
	form_class = LeadModelForm
	context_object_name = 'lead'

	def get_success_url(self):
		return reverse("leads:lead_page")


class CreateUserView(generic.CreateView):
	template_name = 'lead/create-user.html'
	form_class = UserModelForm

	def get_success_url(self):
		return reverse("leads:lead_page")

class DeleteUserView(generic.DeleteView):
	x = 10

class AgentUpdateView(generic.UpdateView):
	template_name = 'lead/agent-update.html'
	queryset = Agent.objects.all()
	form_class = LeadModelForm
	context_object_name = 'agent'

	def get_success_url(self):
		return reverse("leads:agents")

class AgentDeleteView(generic.DeleteView):
	template_name = 'lead/delete-agent.html'
	queryset = Agent.objects.all()

	def get_success_url(self):
		return reverse("leads:agents")


class TestView(generic.TemplateView):
	template_name = 'lead/test.html'

def UpdateLead(request, pk):
	lead = Leads.objects.get(id=pk)
	form = LeadModelForm(instance=lead)

	if request.method == 'POST':
		form = LeadModelForm(request.POST, instance=lead)
		if form.is_valid:
			form.save()
		return redirect("/leads")
	context = {
		"form" : form
	}
	return render(request, "lead/update-leads.html", context)

def Agents(request):
	agents = Agent.objects.all()
	context = {
		"agents":agents
	}
	return render(request, "lead/agents.html", context)

def Create_agent_p(request):
	form = CreateAgentModelForm()
	
	if request.method == "POST":
		form = CreateAgentModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/agents')

	context = {
		"form": form
	}
	return render(request, "lead/create-agents.html", context)

def Agent_details(request, pk):
	agent = Agent.objects.get(pk=pk)
	context = {
		"agent": agent
	}
	return render(request, "lead/agent-details.html", context)

def Agent_update(request, pk):
	agent = Agent.objects.get(id=pk)
	form = AgentModelForm(instance=agent)

	if request.method == "POST":
		form = AgentModelForm(request.POST, instance=agent)
		if form.is_valid:
			form.save()
			return redirect('/agents')
	context = {
		"agent": agent,
		"form" :form
	}

	return render(request, "lead/agent-update.html", context)

def Delete_agent_p(request, pk):
	Agent.objects.get(id=pk).delete()
	return redirect('/agents')
	


