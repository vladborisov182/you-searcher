import datetime

import yapi
from flask import Blueprint, render_template, request
from flask_security import current_user, login_required

from app import db
from config import api_key
from models import Inquiry, User

search = Blueprint('search', __name__, template_folder='templates')
api = yapi.YoutubeAPI(api_key)

@search.route("/")
@login_required
def search_videos():

    q = request.args.get('q')

    if q:
        user = current_user
        inquiry = Inquiry(body=q, timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), user_id=user.id)

        db.session.add(inquiry)
        db.session.commit()

        results = api.general_search(q, max_results=10)

        videos_id_list = []

        return render_template('search/search.html', videos_id=videos_id_list)

@search.route("/history")
@login_required
def query_history():

    queries = Inquiry.query.filter(Inquiry.user_id == current_user.id)

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pages = queries.paginate(page=page, per_page=10)

    return render_template('search/history.html', queries=queries, pages=pages)