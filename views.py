from flask import render_template, request, redirect
from models import Video, Theme


def home():
    display_message = None
    if request.method == 'POST':
        theme_name = request.form['theme_name']
        video_title = request.form['video_title']

        if theme_name and video_title:
            if Theme.objects(name=theme_name).count() > 0:
                theme = Theme.objects(name=theme_name).first()
            else:
                theme = Theme(name=theme_name)
                theme.save()
            
            Video(title=video_title, theme=theme).save()

            display_message = 'Video added successfully!'
        else:
            display_message = 'An error occurred while adding a video!'
        
    
    return render_template('homepage.html', videos=Video.objects(), message=display_message)

def themes():
    return render_template('themes.html', themes=Theme.objects().order_by('-score'))

def vote_thumbs_up(video_id):
    video = Video.objects.get(id=video_id)
    video.add_thumbs_up()
    return redirect('/')

def vote_thumbs_down(video_id):
    video = Video.objects.get(id=video_id)
    video.add_thumbs_down()
    return redirect('/')
