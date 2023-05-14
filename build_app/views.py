from rest_framework import status

from .utils import get_sorted_tasks

from rest_framework.views import APIView
from rest_framework.response import Response


class BuildView(APIView):
    def post(self, request):
        build_name = request.data.get('build')
        if not build_name:
            return Response(
                {'error': 'No "build" parameter provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            tasks = get_sorted_tasks(build_name)
            return Response({'tasks': tasks})
        except ValueError as e:
            return Response(
                {'error': str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
