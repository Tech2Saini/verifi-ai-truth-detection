# ----------------------- Python basic Modules -------------------
from datetime import datetime
import pytz,requests
import re,json

# ----------------------- Django Modules -------------------
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from rest_framework.response import Response
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# ----------------------- machine learning Modules -------------------
import nltk
import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# ----------------------- App modules -------------------
from home.models import Profile
from mainserver import settings
from .forms import FeedbackForm,ContactForm

# Set-ExecutionPolicy Unrestricted -Scope Process
# .\newsenv\Scripts\activate

# Load the trained model and vectorizer (loaded once globally)
model = joblib.load(settings.BASE_DIR/ 'trained models/fake_news_detector_model.pkl')
vectorizer  = joblib.load(settings.BASE_DIR/ 'trained models/tfidf_vectorizer.pkl')

# Preprocessing function (same as in training)  
preprocess_text_data = ''

def preprocess_text(text):
    
    nltk.data.path.append('Server/nltk_data')  # Path to your NLTK data
    
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    words = word_tokenize(text)

    processed_text = [stemmer.stem(word) for word in words if word not in stop_words]

    return ' '.join(processed_text)

def identifySentences(text):
    # Process the text with spaCy
    # Process the text with spaCy
    final_text = str(text).split('.')
    print(final_text)
    final_text = [text for new_text in final_text for text in new_text.split(',') ]
#    print("the final text is :" ,final_text)

    return final_text

def fetchFacts(text):
    # ------------------------------------ Api Response Code ------------------------------------------------------------------
    url = "https://fact-checker.p.rapidapi.com/search"

    querystring = {"query":text,"limit":"20","offset":"0","language":"en"}

    headers = {
        "x-rapidapi-key": "4c2908ae2amsh6b6989e349dc9e0p167900jsn5d5bce0e0cca",
        "x-rapidapi-host": "fact-checker.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    return data

def checkFacts(text):
    global preprocess_text_data

    final_facts = []
    # print(preprocess_text_data)
    # sentences_list =  identifySentences(text=preprocess_text_data)

    # for text in sentences_list:
    #     final_facts.append(fetchFacts(text=text))

    file =  open("D:\A123\Python 3.6\Python Projects\Fake news Detection\example_response.json","r",encoding="utf8")
    data =  json.load(file)


    
    # ------------------------------------------------------------------------------------------------------

    data = data['data']
    
    for item in data:
        timestamp_str = item['claim_datetime_utc']
        if timestamp_str is not None:
            datetime_obj = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            item['claim_datetime_utc'] = datetime_obj.replace(tzinfo=pytz.UTC)

        else:
            item['claim_datetime_utc'] = datetime.now()

    return data[:10]

# View to handle predictions
def detect_fake_news(request):
    global preprocess_text_data

    if request.method == 'POST':
        try:
            news_text = request.POST.get('news_text', '')

            if not news_text:
                    return Response({"error": "News text is required"})
            preprocess_text_data  = news_text


            respon = request.POST.get('check')

            if news_text:
                # Preprocess the news text
                processed_text = preprocess_text(news_text)
                # Vectorize the text
                text_tfidf = vectorizer.transform([processed_text])
                # Predict using the trained model
                prediction = model.predict(text_tfidf)
                # Convert prediction to a human-readable format
                result = "Real News" if prediction[0] == 1 else "Fake News"
                print("the model classes :",model.classes_,prediction)


                input_vector = vectorizer.transform([news_text])
                confidence = model.predict_proba(input_vector)[0]

                # return JsonResponse({'result': result})
                print("Probability :",confidence)

                facts =  checkFacts('')

                return render(request, 'index.html',{
                    "text": news_text,
                    "result": result,
                    "fake":int(round(confidence[0],2)*100),
                    "real":int(round(confidence[1],2)*100),
                    "facts":facts,
                }, status=status.HTTP_200_OK)

                # return render(request, 'index.html',{'result':result,'text':news_text})

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        facts =  checkFacts('')
        return render(request, 'index.html',{"facts":facts})
    
def Content(request):
    return render(request,'about.html')

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['profile_image','username','first_name','last_name','gender','city', 'bio']
    # fields = ['profile_image']
    template_name = 'account/profile.html'

    def get_form(self, form_class=None):
        """
        Override get_form to add custom classes to the form fields.
        """
        form = super().get_form(form_class)
        # form.fields['profile_image'].widget.attrs.update({'class': 'form-control custom-profile-image'})

        # Add custom classes to each field
        form.fields['gender'].widget.attrs.update({'class': 'form-control custom-gender'})
        form.fields['profile_image'].widget.attrs.update({'class': 'form-control custom-profile-image'})
        form.fields['city'].widget.attrs.update({'class': 'form-control custom-city'})
        form.fields['bio'].widget.attrs.update({'class': 'form-control custom-bio'})
        form.fields['username'].widget.attrs.update({'class': 'form-control custom-username'})
        form.fields['first_name'].widget.attrs.update({'class': 'form-control custom-first-name'})
        form.fields['last_name'].widget.attrs.update({'class': 'form-control custom-last-name'})

        return form

    def get_object(self, queryset=None):
        return Profile.objects.get(username=self.request.user.username)

    def post(self, request, *args, **kwargs):
        self.success_url = f'/accounts/{self.request.user.username}/profile'

        print("The profile image is ",request.POST.get('profile_image'))

        return super().post(request, *args, **kwargs)

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Assuming Profile is linked to User
            feedback.save()
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX request
                return JsonResponse({"message": "Feedback submitted successfully!"}, status=200)
            
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX request
                return JsonResponse({"errors": form.errors}, status=400)
    
    return render(request, 'feedback_form.html', {'form': FeedbackForm()})

def contact_view(request):


    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
    

            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            # Render the email template with dynamic data
            email_html_content = render_to_string("contact_email.html", {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message,
            })

            email_message = EmailMessage(
            subject=f"New Contact Request: {subject}",
            body=email_html_content,
            from_email="hackingkali789@gmail.com",
            to=["monusainideveloper@gmail.com"],
    
            )

            email_message.content_subtype = "html"

            try:
                # Send the email
                email_message.send()
                messages.add_message(request, messages.SUCCESS, "Your message send successfully.")
                messages.add_message(request, messages.INFO, "Our team will connect you soon...")
                
                # return JsonResponse({"success": True, "message": "Email sent successfully."})
            except Exception as e:
                # return JsonResponse({"success": False, "message": str(e)})
                messages.add_message(request, messages.DEBUG, str(e))


            form = ContactForm()
        

    else:
        form = ContactForm()

    return render(request,'contact.html',{'form':form})