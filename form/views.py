# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def cemetery_add(request):
    if request.method=="POST":
        form=CemeteryForm(request.POST)
        if form.is_valid():
            cemetery=form.save(commit=False)
            cemetery.name=request.name
            cemetery.city=request.city
            cemetery.zipcode=request.zipcode
            cemetery.created_by=request.user
            cemetery.date_created=timezone.now()
            cemetery.save()
            return redirect('cemetery_list')
    else:
        form=CemeteryForm
    return render(request,'heaven/edit_cemetery.html',{'form':form})