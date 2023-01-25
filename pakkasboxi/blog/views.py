from flask import Blueprint, render_template

blueprint = Blueprint("blog", __name__)

@blueprint.route("/")
def load_index_page():
    return load_blog_page()

@blueprint.route("/blog")
def load_blog_page():
    return render_template("blog.html")

@blueprint.route("/dadjoke")
def tell_dadjoke():
    return "<p>Tiesittekö että Pakkanen voi tehdä teistä liukkaita yön aikana?</p>"

@blueprint.route("/my-gm-journey")
def tell_dadjoke():
    return "<p>Tiesittekö että Pakkanen voi tehdä teistä liukkaita yön aikana?</p>"
