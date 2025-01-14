from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    courses= {
            'course_name': 'python',
            'learn': {'flask', 'django', 'Tornado', 'fastapi'},
            'course_provider' : 'risav'
        }
    
    if request.method == 'GET':
        print("it's a get response" )
        return Response(courses)
    elif request.method == 'POST':
        print("you hit a post method")
        return Response()
        

    
    
