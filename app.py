from flask import Flask, request, render_template, flash
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()
app = Flask(__name__)

#class HexData(object):
    #msgtype = {0: "emergency", 1: "requested", 2: "emergency requested"}

#   def __init__(self, input):
#    decoded = bytearray.fromhex(input).decode()
#        self.msglen = decoded[:2]
#        self.msgID = decoded[2:5]
#        self.timestamp = decoded[5:11]
#        try:
#            self.msgtype = HexData.msgtype[int(decoded[11])]
#        except:
#            self.msgtype = decoded[11]
#        self.devreg = decoded[12:20]
#        self.gpspos = decoded[20:28]
#        self.gpssignal = decoded[28]
#        self.unstructlen = decoded[29]
#        self.unstruct = decoded[30: -1]
#        self.crc = decoded[-1]
#        a = []
#        a.append("Message length: {}{}".format((" "*6), self.msglen))
#        a.append("Message ID: {}{}".format((" "*10),self.msgID))
#        a.append("Timestamp: {}{}".format((" "*11),self.timestamp))
#        a.append("Message Type: {}{}".format((" "*8),self.msgtype))
#        a.append("Device Reg: {}{}".format((" "*10),self.devreg))
#        a.append("GPS Position: {}{}".format((" "*8),self.gpspos))
#        a.append("GPS signal strength: {}{}".format(" ",self.gpssignal))
#        a.append("Unstructured length: {}{}".format((" "),self.unstructlen))
#        a.append("Unstructured: {}{}".fordat((" "*8),self.unstruct))
#        a.append("CRC: {}{}".format((" "*17),self.crc))
#        self.a = a

@app.route('/')
def index():
    return render_template("index.html", test=False)


@app.route("/", methods=["POST"])
def submit():
    #try:
    m1 = HexData(request.form['text'])
    return m1.decoded
    #return "\n".join(m1.a)
    #return "<br>".join(m1.a)
    #except:
    #    return index()

@app.route("/", methods=["POST"])
def submit_request():
    flash("Request sent")
    return index()

@app.route("/", methods=["POST"])
def close():
    message = None
    return index()

app.secret_key = "secret"
nav.init_app(app)
