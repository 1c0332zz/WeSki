from django.shortcuts import render,redirect
from .models import Review,ReviewImage
from .form import Review_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from places.models import Place
# Create your views here.
@login_required
def create(request):
    if request.method=="POST":
        createreq=Review_form(request.POST)
        photo_list=request.FILES.getlist("image[]")
        if createreq.is_valid():
            newreview=createreq.save(commit=False)
            newreview.user=request.user
            newreview.save()
            for photo in photo_list:
                nreviewimage=ReviewImage.objects.create(review=newreview,image=photo)
                nreviewimage.save()
        return redirect("reviews:index")
    else:
        form=Review_form()
        context={"Review_form":form}
        return render(request,"reviews/create.html",context)
@login_required
def update(request,review_pk):
    old_review=Review.objects.get(pk=review_pk)
    if request.user.pk==old_review.user.pk:
        if request.method=="POST":
            createreq=Review_form(request.POST,instance=old_review)
            photo_list=request.FILES.getlist("image[]")
            del_photo_list=request.POST.getlist("dellist")
            if createreq.is_valid():
                newreview=createreq.save(commit=False)
                newreview.user=request.user
                newreview.save()
                for photo in photo_list:
                    nreviewimage=ReviewImage.objects.create(review=newreview,image=photo)
                    nreviewimage.save()
                for delphoto in del_photo_list:
                    delreviewimage=ReviewImage.objects.get(pk=delphoto)
                    delreviewimage.delete()
            return redirect("reviews:index")
        else:
            form=Review_form(instance=old_review)
            photo=ReviewImage.objects.filter(review=old_review.pk)
            context={"form":form,"photos":photo}
            return render(request,"reviews/update.html",context)
    else:
        return redirect("reviews:index")
@login_required
def delete(request,review_pk):
    old_review=Review.objects.get(pk=review_pk)
    if(request.user.pk==old_review.user.pk):
        if(request.method=="POST"):
            old_review.delete()
    return redirect("reviews:index")
def index(request):
    reviewobjects=Review.objects.order_by("-pk")
    contextlist=[]
    for reviewobject in reviewobjects:
        userobject=get_user_model().objects.get(pk=reviewobject.user.pk)
        contextlist.append({"review":reviewobject,"Writer":userobject})
    context={"Reviews":contextlist}
    return render(request,"reviews/index.html",context)
@login_required
def likes(request,review_pk):
    if request.method=="POST":
        user=request.user
        review=Review.objects.get(pk=review_pk)
        if review.likes.filter(pk=user.pk).exists():
            review.likes.remove(user)
            review.likes_num=review.likes_num-1
            review.save()
        else:
            review.likes.add(user)
            review.likes_num=review.likes_num+1
            review.save()
    return redirect("reviews:detail",review_pk)
    
def detail(request,review_pk):
    reviewobject=Review.objects.get(pk=review_pk)
    Writerobject=get_user_model().objects.get(pk=reviewobject.user.pk)
    reviewplaceobject=Place.objects.get(pk=reviewobject.place.pk)
    context={"Review":reviewobject,"Place":reviewplaceobject,"User":Writerobject}
    return render(request,"reviews/detail.html",context)
@login_required
def image_add(request,review_pk):
    reviewobj=Review.objects.get(pk=review_pk)
    if request.method=="POST" and request.user==reviewobj.user:
        photo_list=request.FILES.getlist("image[]")
        for photo in photo_list:
            nreviewimage=ReviewImage.objects.create(review=reviewobj,image=photo)
            nreviewimage.save()
    return redirect("reviews:detail",review_pk)
@login_required
def image_delete(request,review_pk,reviewimage_pk):
    reviewobj=Review.objects.get(pk=review_pk)
    if request.method=="POST" and request.user==reviewobj.user:
        delobj=ReviewImage.objects.get(pk=reviewimage_pk)
        delobj.delete()
    return redirect("reviews:detail",review_pk)
