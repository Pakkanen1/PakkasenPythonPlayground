from flask import Blueprint, render_template

blueprint = Blueprint("blog", __name__)

@blueprint.route("/")
def load_index_page():
    return render_template("index.html")

@blueprint.route("/blog")
def load_blog_page():
    return render_template("blog.html")

@blueprint.route("/dadjoke")
def tell_dadjoke():
    return "<p>Tiesittekö että Pakkanen voi tehdä teistä liukkaita yön aikana?</p>"

@blueprint.route("/my-gm-journey")
def load_gm_journey_page():
    return render_template("gmjourney.html")
