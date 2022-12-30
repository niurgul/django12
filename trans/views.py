from django.shortcuts import render
import googletrans

# Create your views here.
def index(request):
    bf = request.GET.get("bf", "")
    fr = request.GET.get("fr", "")
    to = request.GET.get("to", "")
    context = {
            "ndict" : googletrans.LANGUAGES
    }

    if bf:
        trans = googletrans.Translator()
        af = trans.translate(bf, src=fr, dest=to).text
        context.update({
            "bf" : bf,
            "fr" : fr,
            "to" : to,
            "af" : af
        })
    return render(request, "trans/index.html", context)