import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from reportserver.auth import login_required
from reportserver.db import get_db

bp = Blueprint('report', __name__)

@bp.route('/')
@login_required
def index():
    db = get_db()
    reports = db.execute(
        'SELECT participant, completedTimeStamp, completedDate, clientMD5 FROM report ORDER BY completedTimeStamp DESC'
    ).fetchall()
    return render_template('report/index.html', reports=reports)


@bp.route('/create', methods=['POST'])
def create():
    submitted_report = json.loads(request.get_json())
    db = get_db()
    report = db.execute(
        'SELECT participant, completedTimeStamp, completedDate, clientMD5 FROM report WHERE participant = ?', (submitted_report['participant'],)
    ).fetchone()
    if report is None:
        create = db.execute(
            'INSERT INTO report (participant, completedTimeStamp, completedDate, clientMD5) VALUES (?, ?, ?, ?)', (
                submitted_report['participant'],
                submitted_report['completedTimeStamp'],
                submitted_report['completedDate'],
                submitted_report['clientMD5']
            )
        )
        db.commit()
        submitted_report['status'] = 'created'
    else:
        submitted_report['status'] = 'existing'
    return jsonify(submitted_report)
