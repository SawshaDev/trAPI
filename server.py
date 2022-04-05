
import praw
import random
import os
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
reddit = praw.Reddit(client_id='pua14mlzkyv5_ZfQ2WmqpQ',
                     client_secret='T5loHbaVD7m-RNMpFf0z24iOJsInwg',
                     user_agent='Oxygen',
                     check_for_async= False)



@app.route("/favicon.png")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.png',mimetype='favicon.png')


    
@app.route("/", methods=['GET'])
def home():
    
    subreddits = ['FemboysAndHentai', 'hentai', 'rule34', 'nsfw']
    choices = random.choice(subreddits)
    nsfw_submission = reddit.subreddit(choices).new(limit=15)
    post_to_pick = random.randint(1,15)
    for i in range(0, post_to_pick):
            submission = next(x for x in nsfw_submission if not x.stickied)

    
    title = submission.title
    link = submission.permalink
    url = submission.url

    upvotes = submission.score
    upvote_ratio = submission.upvote_ratio
    author = submission.author
    
    print(link)


    return render_template("home.html", title=title, url=url, upvotes=upvotes, author=author, upvote_ratio=upvote_ratio, link=link)

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
        if random_sub.is_reddit_media_domain and not random_sub.is_video:
        	submission = next(x for x in nsfw_submission if not x.stickied)

    title = submission.title

    return {'status':200, 'title':title, 'link':submission.url}




if __name__ == "__main__":
    app.run(debug=True, port=2323)
