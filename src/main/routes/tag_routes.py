from flask import Blueprint, jsonify, request

from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tags_routs_bp = Blueprint('tags_routes', __name__)

@tags_routs_bp.route('/create_tag', methods=["POST"])
def create_tag():
  '''
    create tag routes (localhost/create_tag)
  '''
  tag_creator_view = TagCreatorView()
  
  http_request = HttpRequest(body=request.json)
  response = tag_creator_view.validate_and_create(http_request)
  
  return jsonify(response.body), response.status_code