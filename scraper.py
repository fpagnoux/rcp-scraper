import sys, os
args = sys.argv

if (len(args) <= 1):
	print("ERROR: Please provide source url")
	print("Example : python scraper.py url output.csv")
else:
	url = args[1]
	if (len(args) == 2):
		filename = url.split('/')[-1].split('.')[0]
		output = filename + ".csv"
		print("No output file specified : using " + output)
	else:
		output = sys.argv[2]
		if not output.endswith(".csv"):
			output = output + ".csv"
	if os.path.isfile(output):
		os.remove(output)
	os.system("scrapy crawl realclearpoliticsSpider -a url="+url+" -o "+output)

