from flask import Flask, render_template, send_from_directory ,jsonify, request

import praw
import random
import os


app = Flask(__name__)
reddit = praw.Reddit(client_id='client_id here',
                     client_secret='client_secret herre',
                     user_agent='just put the app name',
                     check_for_async= False)



@app.route("/favicon.png")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.png',mimetype='favicon.png')


    
@app.route("/", methods=['GET'])
def home():
    

    nsfw_submission = reddit.subreddit('femboysandhentai').hot()
    post_to_pick = random.randint(1,30)
    for i in range(0, post_to_pick):
            submission = next(x for x in nsfw_submission if not x.stickied)
    
    title = submission.title

    url = submission.url

    upvotes = submission.score
    upvote_ratio = submission.upvote_ratio
    author = submission.author


    return render_template("index.html", title=title, url=url, upvotes=upvotes, author=author, upvote_ratio=upvote_ratio)

@app.route("/endpoint")
def endpoints():

    pass



@app.route("/api/v1/femboy")
def femboy():
    nsfw_submission = reddit.subreddit('FemboysAndHentai').hot()
    post_to_pick = random.randint(1,30)
    for i in range(0, post_to_pick):
            submission = next(x for x in nsfw_submission if not x.stickied)
    
    title = submission.title


    return {'status': 200, 'title':title,'link': submission.url}


@app.route("/api/v1/nsfw")
def nsfw():
    nsfw_submission = reddit.subreddit('nsfw').hot()
    post_to_pick = random.randint(1,30)
    for i in range(0, post_to_pick):
        submission = next(x for x in nsfw_submission if not x.stickied)

    title = submission.title

    return {'status':200, 'title':title, 'link':submission.url}




if __name__ == "__main__":
    app.run(debug=True, port=2323)
