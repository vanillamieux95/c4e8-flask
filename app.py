from flask import *
from datetime import *

app = Flask(__name__)

pistols = [
{
    "src"   : "http://assets.academy.com/mgen/85/10106785.jpg",
    "title" : "Beretta U22 Neos .22 LR Semiautomatic Single-Action Pistol",
    "pricetag"  : "$278.00"
    },

{
    "src"   : "http://assets.academy.com/mgen/60/10115060.jpg",
    "title" : "Bersa Thunder .380 ACP Pistol",
    "pricetag"  : "$289.99"
    },

{
    "src"   : "http://assets.academy.com/mgen/94/10106794.jpg",
    "title" : "GLOCK 17 9mm Safe-Action Pistol",
    "pricetag"  : "$499.99"
    },

{
    "src"   : "http://assets.academy.com/mgen/74/10108274.jpg",
    "title" : "Beretta 92FS 9 mm Semiautomatic Pistol",
    "pricetag"  : "$598.00"
    },

]

revolvers = [
{
    "src"   : "http://assets.academy.com/mgen/14/10050414.jpg",
    "title" : "Ruger® LCR™ .38 Special Double-Action Revolver",
    "pricetag"  : "$429.99"
    },

{
    "src"   : "http://assets.academy.com/mgen/72/10115572.jpg",
    "title" : "Smith & Wesson Model 637 .38 Special +P Revolver",
    "pricetag"  : "$429.99"
    },

{
    "src"   : "http://assets.academy.com/mgen/27/10104127.jpg",
    "title" : "Smith & Wesson Model 642 .38 Special +P Revolver",
    "pricetag"  : "$429.99"
    },

{
    "src"   : "http://assets.academy.com/mgen/81/10194781.jpg",
    "title" : "Taurus Judge® Model 4510 .45/.410 DA/SA Revolver",
    "pricetag"  : "$479.99"
    },

]

phanh = [{
    "avatar"    : "http://static.appstore.vn/a/uploads/thumbnails/092016/deemo_icon.png",
    "fullname"  : "Phuong Anh, NGUYEN PHAM",
    "quote" : "- 不愉快です！-",
    "dob"   : "23.11.1995",
    "phone" : "0122.385.5472",
    "email" : "ph.anh.nguyenpham.l1221@gmail.com",
    "location"  : "Hanoi, Vietnam",
    "gradyear"  : ["01-06","06-10","10-13","13-17"],
    "education" : ["Doan Thi Diem Primary School",
                   "Lomonosov Middle School",
                   "Yen Hoa High School",
                   "BA in French and International Business"],
    "workexp"   : ["volunteering", "translating", "playing games", "staying home"]
}]


@app.route('/')
def hello_world():
    return redirect(url_for("firearms"))


number_of_visitor = 0


@app.route('/login')
def login():
    global number_of_visitor
    number_of_visitor += 1
    current_time_on_ser = str(datetime.now())
    return render_template(
        "login.html",
        current_time=current_time_on_ser,
        number_of_visitor=number_of_visitor * 100
    )


@app.route('/guns')
def guns():
    return render_template("guns.html", pistols_list = pistols)


@app.route('/contact')
def gun():
    return render_template("contact.html", person = phanh)


@app.route('/cssdemo')
def css_demo():
    return render_template("cssdemo.html")


@app.route('/w3cssdemo')
def w3_cssdemo():
    return render_template("w3cssdemo.html")


@app.route('/howly')
def firearms():
    return render_template("firearms.html", pistols_list = pistols, revolvers_list = revolvers)


if __name__ == '__main__':
    app.run()
