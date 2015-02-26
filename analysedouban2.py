from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordFreqCount(MRJob):

    def mapper (self, _, line):
        l = line.strip('\n').split()
        yield '%010d'%int(l[1]), l[0]

    def reducer(self, key, values):
        yield int(key),int(list(values)[0])


if __name__ == '__main__':
    MRWordFreqCount.run()