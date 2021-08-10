
import re
import os
import glob
from pprint import pprint
import matplotlib
matplotlib.use('Agg')

analyze_pattern = re.compile('.*.analyze.log')
explain = re.compile('.*.explainonly.log')


def parse_analyze_log(logfile):
    content = None
    with open(logfile) as r:
        content = r.read()
    return {
        'planningTime': re.findall('Planning Time: (\d+.\d+) ms', content),
        'executionTime': re.findall('Execution Time: (\d+.\d+) ms', content)
    }


def parse_all_analyze():
    import matplotlib.pyplot as plt
    res = {}
    for logfile in glob.glob('logs/*.analyze.log'):
        sqlname = re.findall('logs/(.*).analyze.log', logfile)[0]
        res[sqlname] = parse_analyze_log(logfile)

    # draw png
    for sqlname in res:
        data = res[sqlname]['executionTime']
        plt.bar(range(len(data)), data)
        pngname = 'png/%s.png' % sqlname
        print('save executionTime for %s' % sqlname)
        plt.savefig(pngname)


parse_all_analyze()
