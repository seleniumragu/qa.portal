from django.shortcuts import render
from .forms import AutomationForm
from .models import Automation
from django.shortcuts import redirect, get_object_or_404
import xml.etree.ElementTree as ET
import os


# Create your views here.
def index(request):
    automations = Automation.objects.all()
    return render(request, 'automation/index.html', {'automation1': automations})


def add(request):
    if request.method == "POST":
        form = AutomationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                displaytrans(request)
                external1(request)
                return redirect('automation_app:index')
            except:
                pass
    else:
        form = AutomationForm()
    return render(request, 'automation/add.html', {'form': form})


def edit(request, automation_id):
    automation = get_object_or_404(Automation, id=automation_id)
    form = AutomationForm(request.POST, instance=automation)
    if form.is_valid():
        try:
            form.save()
            displaytrans(request)
            external1(request)
            return redirect('automation_app:index')
        except:
            pass
    return render(request, 'automation/edit.html', {'automation1': automation})


def delete(request, automation_id):
    automation = Automation.objects.get(id=automation_id)
    try:
        automation.delete()
    except:
        pass
    return redirect('automation_app:index')


def external1(request):
    os.system('crudexample.sh')


def displaytrans(request):
    info = Automation.objects.all().first()
    print(info.gitrepo)
    print(info.gitbranch)
    print(info.env)
    print(info.tags)
    print(info.processes)
    print(info.googlechaturl)
    tree = ET.parse('mylocalconfig.xml')
    root = tree.getroot()
    for node in root.findall('.//hudson.plugins.git.UserRemoteConfig/url'):
        node.text = info.gitrepo
        print(node.text)
    for node1 in root.findall('.//hudson.plugins.git.BranchSpec/name'):
        node1.text = info.gitbranch
        print(node1.text)
    for node1 in root.findall('.//hudson.model.StringParameterDefinition/defaultValue'):
        node1.text = info.env
        print(node1.text)
    for node1 in root.findall('.//hudson.model.StringParameterDefinition/defaultValue'):
        node1.text = info.tags
        print(node1.text)
    for node1 in root.findall('.//hudson.model.StringParameterDefinition/defaultValue'):
        node1.text = info.processes
        print(node1.text)
    for node1 in root.findall('.//hudson.model.StringParameterDefinition/defaultValue'):
        node1.text = info.googlechaturl
        print(node1.text)
    tree.write('mylocalconfig.xml')
