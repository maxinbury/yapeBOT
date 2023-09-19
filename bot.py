import requests
from botbuilder.core import ActivityHandler, TurnContext

class MyBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text.lower()

        # Obtener la pregunta del usuario
        user_question = user_message

        # Crear el cuerpo de la solicitud JSON con la pregunta del usuario
        request_body = {"question": user_question}

        # Realiza la llamada a tu API aquí
        api_url = "https://secureapiyape.azurewebsites.net/api/messages"  # Reemplaza con la URL de tu API

        response = requests.post(api_url, json=request_body)

        if response.status_code == 200:
            api_response = response.json()
            result_from_api = api_response.get("result", "No se encontró resultado")
            await turn_context.send_activity(f"Respuesta de la API: {result_from_api}")
        else:
            await turn_context.send_activity("Hubo un problema al llamar a la API.")
