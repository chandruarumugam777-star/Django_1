from django.http import HttpResponse 
from django.template import loader 
 
def ddd(request): 
  template = loader.get_template('index.html') 
  template = loader.get_template('styles.css')
  template = loader.get_template('script.js')

  return HttpResponse(template.render()) 