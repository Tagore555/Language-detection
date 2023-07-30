from django.shortcuts import render
from . import detect
import fitz
#from . import check_value











# Create your views here.
def home(request):
   text = request.GET.get('language','') 
   prediction =detect.lang_detect(text)
   if request.method == 'POST' and request.FILES.get('lang'):
        uploaded_file = request.FILES['lang']

        # Check if the uploaded file is a PDF
        if uploaded_file.name.endswith('.pdf'):
            pdf_content = extract_pdf_content(uploaded_file)
            prediction =detect.lang_detect(pdf_content)
            return render(request, 'base/home.html', {'content': prediction})
        else:
            return render(request, 'base/home.html', {'message': 'Uploaded file is not a PDF.'})
    
   #return render(request, 'base/home.html')
   return render(request,'base/home.html',{"text":text,"prediction":prediction})

def extract_pdf_content(uploaded_file):
    pdf_text = ''
    try:
        pdf_reader = fitz.open(stream=uploaded_file.read(), filetype='pdf')
        num_pages = pdf_reader.page_count
        for page_num in range(num_pages):
            page = pdf_reader[page_num]
            pdf_text += page.get_text()
    except Exception as e:
        pdf_text = 'Error: Unable to extract text from the PDF.'

    return pdf_text




def about(request):
    return render(request,'base/about.html')
def service(request):
   return render(request,'base/service.html')
def contact(request):
    return render(request,'base/contact.html')
def feed(request):
    v=request.GET.get('sub','')
    return render(request,'base/feed.html',{'v':v})



















"""def text(request):
   #text = request.GET.get('language','') 
   #prediction =detect.lang_detect(text)
   return render(request,'base/text.html'#,{'prediction':prediction}
                 )
def scan(request):
   #img=request.GET["imagepic"]
   #imga=cam(img)
   return render(request,'base/scan.html')"""

"""def output(request):
   text = request.GET.get('language','') 
   prediction =detect.lang_detect(text)
   data=request.GET.get('lang','') 
   extraction=read.extract(data)
   #predicition1=detect.lang_detect(extraction)
  # text=request.GET["language"]
   #text=check_value.value_c(text)
   #predictios=check_value.prediction_model(text)
   return render(request,'base/output.html',{'prediction':prediction,#'prediction1':predicition1,
                                             'extraction':extraction,
                                             'data':data})"""