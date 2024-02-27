from scapy.all import *
import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

logs = []

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = {
            "timestamp": timestamp,
            "src_ip": src_ip,
            "dst_ip": dst_ip,
        }

        logs.append(log_entry)
        socketio.emit('log_entry', log_entry)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    sniff(prn=packet_callback, store=0)
    # Use socketio.run instead of app.run for real-time updates
    socketio.run(app, debug=True)
