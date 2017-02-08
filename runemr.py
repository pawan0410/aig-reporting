""" File to Start EMR App
"""

from emr.application import emr_app

emr = emr_app('development')

if __name__ == '__main__':
    emr.run()

