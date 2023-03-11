#views is a common name for page views
'''
to render html web pages
'''

from django.http import HttpResponse


def home_view(request):
    '''
    Take in a request(Django sends request)
    return html as a response(we pick to return the response)
    '''
    # more complex django templates
    name = "chloe"
    HTML_STRING = f"""
    <h1>Hello {name}!</h1>
    """
    return HttpResponse(HTML_STRING) #some sort of html response
