from .models import RequestJournal


class RequestLog:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        # Действие с запросом
        journal_record = RequestJournal.objects.create(
            request_method=request.method,
            request=request.path,
        )
        response = self._get_response(request)  # Получение ответа
        # Действие с ответом
        journal_record.response_code = response.status_code
        journal_record.save()
        return response
