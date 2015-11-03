import logging
logger = logging.getLogger('testlogger')
hdlr = logging.FileHandler('/Users/cmanning/Documents/workspace/SBv3_Py_Framework/src/Test/testlogs.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)