import sys
import filecmp
import difflib

from os import listdir, path, remove
from hashlib import md5

def main():
	if len(sys.argv) < 2:
		print "Usage: verify <Path>"
		sys.exit(0)

	dir = sys.argv[1].strip("\\")
	HASH_FILE = ".\__{}.hashes".format(dir.strip("C:").replace("\\", "_"))
	if path.exists(HASH_FILE):
		newfile = "{}.new".format(HASH_FILE)
		if path.exists(newfile):
			remove(newfile)
		generateHash("{}.new".format(HASH_FILE), dir)
		if not filecmp.cmp(HASH_FILE, newfile):
			print "WARNING: FILE HASHES DIFFER!"
			with open(HASH_FILE, 'r') as original_hashes:
				with open(newfile, 'r') as new_hashes:
					diff = difflib.context_diff(original_hashes.readlines(), new_hashes.readlines())
					print ''.join(diff)
	else:
		generateHash(HASH_FILE, dir)

def get_md5(fpath):
	md5hash = md5()
	with open(fpath, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			md5hash.update(chunk)
	return "{}:{}\n".format(fpath,md5hash.hexdigest())

def generateHash(outFile, dir):
	for f in listdir(dir):
		fpath = "{}\\{}".format(dir, f)
		if path.isdir(fpath):
			generateHash(outFile, fpath)
		else:
			with open(outFile, "a+") as hash_file:
				hash_file.write(get_md5(fpath))

if __name__ == "__main__":
	main()