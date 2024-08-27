from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated



GPT_MODEL = 'gpt-3.5-turbo'
GPT_URL = 'https://api.openai.com/v1/chat/completions'

def stream_response(completion_stream):
    """ Read chunks from stream """ 
    for chunk in completion_stream:
        content = chunk.choices[0].delta.content
        if content is None:
            return
        yield content



class DashboardView(APIView):
    permission_classes = [IsAuthenticated]


class AskGptStreamView(APIView):

    def post(self, req):

        req_data = GptSerializer(data=req.data)

        # Check if request is valid
        if req_data.is_valid():

            # Do the request to open API
            messages = [{"role": "user", "content": req_data.validated_data.get('message')}]

            # Create the OpenAi client
            client = OpenAI()

            # Request GPT stream
            res = client.chat.completions.create(model=GPT_MODEL, messages=messages, stream=True, max_tokens=500)

            print(res)

            # Return a streaming response
            return StreamingHttpResponse(stream_response(res), content_type='text/plain')

        else:
            # Return 400 and validation errors
            return Response(req_data.errors, status=status.HTTP_400_BAD_REQUEST)

class AskGptView(APIView):
    """
    API View to interact with the GPT model. It accepts POST requests with 
    user messages, sends them to the GPT model, and returns the model's responses.
    """

    def post(self, req):
        """
        Handles POST requests. Sends user message to GPT model and 
        returns model's response.
        """

        openai_api_key = settings.OPENAI_API_KEY

        req_data = GptSerializer(data=req.data)

        # Check if request is valid
        if req_data.is_valid():

            # Do the request to open API
            data = {
                'model': GPT_MODEL,
                "messages": [{"role": "user", "content": req_data.validated_data.get('message')}]
            }
            try:
                res = request("POST", GPT_URL,
                          headers={'Authorization': 'Bearer ' + openai_api_key},
                          json=data, timeout=15)
                # Parse GPT response
                parsed_json = json.loads(res.text)

            except Timeout:
                return Response({"error": "The request timed out."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            except RequestException as e:
                return Response({"error": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Access GPT message
            choices = parsed_json['choices']
            gpt_message = choices[0]['message']['content']

            # Return GPT message
            return Response({'message': gpt_message})

        # Return 400 and validation errors
        return Response(req_data.errors, status=status.HTTP_400_BAD_REQUEST)

