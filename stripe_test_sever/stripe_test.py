import logging

from time import time

from flask import request, render_template, jsonify
from stripe_test_sever import app

logging.basicConfig(filename='app.log', level=logging.INFO)


@app.route('/', methods=['GET'])
def page_1():
    return render_template('page_1.html')


test_list = []
testname = ['SnxRTC', 'SnxEthernet', 'SnxTemp', 'SnxMemory']
testsuccessresult = [0, 0, 0, 0]
testfailresult = [0, 0, 0, 0]

count = 0

"""@socketio.on('connect')
def connect():
    global count
    if current_user.is_authenticated:
        count += 1
    emit('status', {'count': count}, broadcast=True)


@socketio.on('disconnect')
def disconnect():
    global count
    if current_user.is_authenticated:
        count -= 1
    emit('status', {'count': count}, broadcast=True)
"""


@app.route("/2", methods=['GET', 'POST'])
def page_2():
    global test_list
    if request.method == 'POST':
        test_list = request.form.getlist('test')
        if len(test_list) > 0:
            logging.info(f"LOG @ {time} | {test_list}")

            render_template('page_2.html', length=len(test_list), test_list=test_list,
                            testsuccessresult=testsuccessresult,
                            testfailresult=testfailresult)

        else:
            return render_template('page_1.html')
    return render_template('page_2.html', length=len(test_list), test_list=test_list,
                           testsuccessresult=testsuccessresult,
                           testfailresult=testfailresult)


@app.route("/api/v1/test_mode", methods=['GET'])
def test_modes():
    stt = ''
    data = [0, 0, 0, 0]
    for i in test_list:
        data[testname.index(i)] = 1 if i in testname else 0

    logging.info(data)
    if len(test_list) > 0:
        for x in data:
            stt = stt + str(x) + ','
        logging.info(f"LOG @ {time} | Test Mode Selected: {stt}")
        stt = stt[0:len(stt) - 1]
        return stt
    else:
        logging.info(f"LOG @ {time} | No Test Mode Selected")
        return '999'


@app.route("/api/v1/test_response/<test_name>/<test_result>", methods=['PUT'])
def test_results(test_name, test_result):
    if test_result == '1':
        if test_name in testname:
            testsuccessresult[testname.index(test_name)] = testsuccessresult[testname.index(test_name)] + 1
    elif test_result == '0':
        if test_name in testname:
            testfailresult[testname.index(test_name)] = testfailresult[testname.index(test_name)] + 1

    logging.info(f"LOG @ {time} | Success: {testsuccessresult} Failure: {testfailresult}")
    return jsonify({"success": testsuccessresult, "fail": testfailresult})


@app.route("/000000_s@v^server_shutdown", methods=['GET'])
def shutdowm():
    if request.form.get('stop') == 'stop':
        print("down")
        request.environ.get('werkzeug.server.shutdown')
    if request.form.get('save') == 'save':
        print("save")
    return 'Server shutting down...'


"""def main():
    ip = gethostbyname_ex(gethostname())
    ip = ip[-1][-1]
    port = 8000
    app.run(debug=True, use_reloader=True, host=ip, port=port)
    sys.exit()


if __name__ == '__main__':
    main()
"""