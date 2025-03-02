from flask import Flask, render_template,send_from_directory,request
import logging,requests
app = Flask(__name__)

# Configure logging to append logs to logs.txt
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        return response.json()
    except Exception as e:
        return {"error": f"Could not fetch details: {str(e)}"}
    
@app.route('/')
def home():
    user_ip = request.remote_addr  # Get IP
    user_agent = request.headers.get('User-Agent')  # Get browser info
    referrer = request.referrer  # Get referrer (if available)

    # Fetch extra details from ipinfo.io
    ip_details = get_ip_info(user_ip)

    # Log info to console
    print(f"IP: {user_ip}, User-Agent: {user_agent}, Referrer: {referrer}, Details: {ip_details}")

    # Log info to file
    log_info = f"IP: {user_ip}, User-Agent: {user_agent}, Referrer: {referrer}, Details: {ip_details}"
    logging.info(log_info)

    return render_template('home.html')

@app.route('/image')
def get_image():
    user_ip = request.remote_addr  # Get IP
    user_agent = request.headers.get('User-Agent')  # Get browser info
    referrer = request.referrer  # Get referrer (if available)

    # Fetch extra details from ipinfo.io
    ip_details = get_ip_info(user_ip)

    # Log info to console
    print(f"IP: {user_ip}, User-Agent: {user_agent}, Referrer: {referrer}, Details: {ip_details}")

    # Log info to file
    log_info = f"IP: {user_ip}, User-Agent: {user_agent}, Referrer: {referrer}, Details: {ip_details}"
    logging.info(log_info)

    return send_from_directory('static', 'japan.jpg')

if __name__ == '__main__':
    app.run(debug=True)
