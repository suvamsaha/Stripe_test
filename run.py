import sys
from socket import gethostbyname_ex, gethostname

from stripe_test_sever import app

if __name__ == "__main__":
    ip = gethostbyname_ex(gethostname())
    ip = ip[-1][-1]
    port = 8000
    app.run(debug=True, use_reloader=True, host=ip, port=port)
    sys.exit()
