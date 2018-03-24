from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quit", action="store_false", dest="verbose", default=True, help="dont't print status message to stdout")

(options, args) = parser.parse_args()