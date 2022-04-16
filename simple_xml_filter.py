import sys
import html

def filter_xml (infile, outfile):
	import re
	out_string = ''
	xmlstring = ''
	with open(infile) as instream:
		instring = instream.read()
		html_pattern = re.compile('(<style>)((\s)|(\S))*(<\/style>)')
		xmlstring = html_pattern.sub('', instring)
		xml_pattern = re.compile('<[^>]*>')
		out_string = xml_pattern.sub('',xmlstring)
		out_string = out_string.replace('&nbsp;', ' ')
		out_string = out_string.replace('&lt;', '<')
		out_string = out_string.replace('&gt;', '<')
		out_string = out_string.replace('&amp;', '&')
		out_string = out_string.replace('&quot;', '"')
		out_string = out_string.replace('&apos;', '\'')
		out_string = out_string.replace('&ndash;', '-') 
	with open(outfile,'w') as outstream:
		outstream.write(out_string)
def main(args):
	infile = args[1]
	split_point = infile.rindex('.')
	outfile = infile[:split_point]+'.txt'
	filter_xml(infile,outfile)

sys.exit(main(sys.argv))
