# write-html.py
import mmap

#write html
def write_html_from_file(report_path, fpath='report.html', debug= True):
	mmap = read_txt(report_path)

	if mmap:
		f = open(fpath,'w')
		message = """<html><head></head><body>"""

		print_title_flag = False
		for line in iter(mmap.readline, b""):
			if not print_title_flag:
				message += "<h1> "+ line +" </h1>"
				print_title_flag = True
				continue			
			if line[0] == '=':
				message += "<h2> "+ line +" </h2>"
			else:
				message += "<p>"+ line +"</p>"

		#Hello World!
		message += "</body></html>"""

		f.write(message)
		f.close()
	else:
		print("Something went terrably wrong on the report creation")

#read txt
def read_txt(txt_path='../report_migration.txt'):
	mmap = read_module_to_mmap(txt_path)
	return mmap

#read file to mmap - FROM CORE import is not working::
def read_module_to_mmap(fname, debug = False):
    if debug:
        print fname
    try:
    	with open(fname) as f:
    	    file_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    	return file_mmap
    except IOError:
        print("Report not generated yet")
    except ValueError:
        print("Oops!  Report is empty")


#write_html_from_file()        