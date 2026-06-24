from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import random



app = Flask(__name__)

app.config["SECRET_KEY"]="monster-secret"

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///monster.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False



db=SQLAlchemy(app)


login_manager=LoginManager(app)

login_manager.login_view="login"





# ==========================
# DATABASE
# ==========================


class User(db.Model,UserMixin):

    id=db.Column(
        db.Integer,
        primary_key=True
    )


    username=db.Column(
        db.String(50),
        unique=True
    )


    password=db.Column(
        db.String(200)
    )


    monsters=db.relationship(
        "Monster",
        backref="owner",
        lazy=True
    )


    def set_password(self,p):

        self.password=generate_password_hash(p)



    def check_password(self,p):

        return check_password_hash(
            self.password,
            p
        )






class Monster(db.Model):


    id=db.Column(
        db.Integer,
        primary_key=True
    )


    name=db.Column(
        db.String(50)
    )


    element=db.Column(
        db.String(30)
    )


    hp=db.Column(
        db.Integer
    )


    attack=db.Column(
        db.Integer
    )


    level=db.Column(
        db.Integer,
        default=1
    )


    xp=db.Column(
        db.Integer,
        default=0
    )


    image=db.Column(
        db.String(100)
    )


    user_id=db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )






@login_manager.user_loader
def load_user(id):

    return User.query.get(int(id))






# ==========================
# GAME ENGINE
# ==========================


def create_wild_monster():


    monsters=[

        (
        "Flameling",
        "Fire",
        80,
        20,
        "fire.png"
        ),


        (
        "Aquari",
        "Water",
        100,
        15,
        "water.png"
        ),


        (
        "Terra",
        "Earth",
        90,
        18,
        "earth.png"
        ),


        (
        "Zephyr",
        "Air",
        120,
        25,
        "air.png"
        )

    ]


    m=random.choice(monsters)


    return {

        "name":m[0],

        "element":m[1],

        "hp":m[2],

        "attack":m[3],

        "image":m[4]

    }






wild={}






def catch_chance():

    return random.randint(1,100)>40






def evolve(monster):


    if monster.xp>=100:


        monster.level+=1

        monster.hp+=30

        monster.attack+=10

        monster.xp=0


        monster.name += " ⭐"




# ==========================
# ROUTES
# ==========================



@app.route("/",methods=["GET","POST"])
def register():


    if request.method=="POST":


        user=User(
            username=request.form["username"]
        )


        user.set_password(
            request.form["password"]
        )


        db.session.add(user)

        db.session.commit()


        login_user(user)


        return redirect("/world")



    return render_template(
        "register.html"
    )






@app.route("/login",methods=["GET","POST"])
def login():


    if request.method=="POST":


        user=User.query.filter_by(
            username=request.form["username"]
        ).first()



        if user and user.check_password(
            request.form["password"]
        ):

            login_user(user)

            return redirect("/world")



    return render_template(
        "login.html"
    )







@app.route("/world",methods=["GET","POST"])
@login_required
def world():


    if current_user.id not in wild:


        wild[current_user.id]=create_wild_monster()



    monster=wild[current_user.id]


    message=""



    if request.method=="POST":


        action=request.form["action"]



        if action=="catch":



            if catch_chance():


                new=Monster(

                    name=monster["name"],

                    element=monster["element"],

                    hp=monster["hp"],

                    attack=monster["attack"],

                    image=monster["image"],

                    user_id=current_user.id

                )


                db.session.add(new)

                db.session.commit()


                message="🎉 Monster Captured!"



            else:

                message="😢 Monster escaped!"




            wild[current_user.id]=create_wild_monster()




        elif action=="search":


            wild[current_user.id]=create_wild_monster()



    return render_template(
        "world.html",
        monster=monster,
        message=message
    )






@app.route("/team")
@login_required
def team():


    monsters=Monster.query.filter_by(
        user_id=current_user.id
    ).all()



    return render_template(
        "team.html",
        monsters=monsters
    )






@app.route("/train/<int:id>")
@login_required
def train(id):


    monster=Monster.query.get(id)


    monster.xp+=50


    evolve(monster)


    db.session.commit()



    return redirect("/team")







@app.route("/battle/<int:id>")
@login_required
def battle(id):


    player=Monster.query.get(id)


    enemy=create_wild_monster()



    winner=""



    if player.attack >= enemy["attack"]:

        player.xp+=40

        evolve(player)

        winner="🏆 You won!"


    else:

        winner="💀 You lost"



    db.session.commit()



    return render_template(
        "battle.html",
        player=player,
        enemy=enemy,
        winner=winner
    )






@app.route("/logout")
def logout():

    logout_user()

    return redirect("/")






with app.app_context():

    db.create_all()





if __name__=="__main__":

    app.run(debug=True)