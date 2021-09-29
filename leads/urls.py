from django.urls import path
from . views import *

app_name = 'leads'

urlpatterns = [
    path('', HomepageView.as_view(), name="home_page"),
    path('leads/', LeadHomepageView.as_view(), name="lead_page"),
    path('lead/<int:pk>', LeadDetailsPageView.as_view(), name="lead_details"),
    path('leads/create', CreateLeadsView.as_view(), name="create_leads"),
    path('lead/edit/<int:pk>', LeadUpdateView.as_view(), name="Update-leads"),
    path('agents', Agents, name="agents"),
    path('agent/<int:pk>', Agent_details, name="agent_details"),
    path('agent/edit/<int:pk>', AgentUpdateView.as_view(), name="agent_update"),
    path('agents/create', Create_agent_p, name="agent_create"),
    path('agent/delete/<int:pk>', AgentDeleteView.as_view(), name="Agent_delete"),
    path('user/create', CreateUserView.as_view(), name="create_user"),
    path('bd', BangladeshView.as_view())


] 