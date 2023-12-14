from flask import Flask, render_template, request
app = Flask(__name__)
 
from python_loovpay import LoovPay

@app.route('/', methods=['GET', 'POST'])
def testApp():
 # If method is POST, get the ref entered by user
    if request.method == 'POST':
        if(request.form['ref'] == ''):
            return "<html><body> <h1>Invalid Reference</h1></body></html>"
        else:
            reference = request.form['ref']

            loov_pay = LoovPay()
            loov_pay.set_keys('APPKEY', 'MERCKANTKEY')
            # reference = 'MOMAVzvTY7DLyiRCR38'
            response = loov_pay.check_status(reference)
            print(response)
            return render_template('answer.html', response=response, ref=reference)
    # If the method is GET,render the HTML page to the user
    if request.method == 'GET':
        return render_template("index.html")

 
# Start with flask web app with debug as True only 
# if this is the starting page
if(__name__ == "__main__"):
    app.run(debug=True)