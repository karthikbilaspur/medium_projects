from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Video
from app.forms import VideoForm

video_routes = Blueprint('video_routes', __name__)

@video_routes.route('/upload', methods=['GET', 'POST'])
def upload():
    form = VideoForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        video = Video(title=form.title.data, filename=filename)
        db.session.add(video)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)

@video_routes.route('/play/<int:video_id>')
def play(video_id):
    video = Video.query.get(video_id)
    return render_template('video_player.html', video=video)

@video_routes.route('/download/<int:video_id>')
def download(video_id):
    video = Video.query.get(video_id)
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], video.filename), as_attachment=True)