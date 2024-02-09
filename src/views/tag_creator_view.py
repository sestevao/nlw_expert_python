from src.controllers.tag_creator_controller import TagCreateController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
  '''
  responsability for interacting with HTTP
  '''
  
  def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
    tag_creator_controller = TagCreateController()
    
    body = http_request.body
    
    if not body or body["product_code"]:
      return HttpResponse(status_code=400, body={"message": "Body not found!"})
    
    product_code = body["product_code"] 
    
    # logica de regra de negocio
    formatted_response = tag_creator_controller.create(product_code)
    
    # retorno http   
    return HttpResponse(status_code=200, body=formatted_response)