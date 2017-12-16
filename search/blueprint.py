from flask import Blueprint
from flask_security import login_required

from flask_security import current_user
from flask import render_template, request

from models import *
from app import db

import datetime
import yapi


search = Blueprint('search', __name__, template_folder='templates')
api = yapi.YoutubeAPI('AIzaSyCI9Tz7b_kqNCLCv0F12_jUEZQxEoMEk_8')

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

        i = 0
        while True:
            try:
                if results.items[i].id.kind == "youtube#video":
                    videos_id_list.append(results.items[i].id.videoId)
                    i += 1
                else:
                    i += 1
            except IndexError:
                break
        return render_template('search/search.html', videos_id=videos_id_list)
    else:
        pass

    return render_template('search/search.html')

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