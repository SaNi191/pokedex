# modules
import json
import numpy as np
from website import init_app

if __name__ == '__main__':
    web_app = init_app()
    web_app.run(debug=True)

for i in range(10):
    print(i)
