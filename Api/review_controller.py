from datetime import datetime
from flask import Blueprint, jsonify, request

from Model.review import Reviews
from Repository.review_repository import ReviewRepository


review_controller = Blueprint('review_controller', __name__)

user_manager = ReviewRepository()


