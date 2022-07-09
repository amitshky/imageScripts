import os
import argparse
from pathlib import Path
from PIL import Image


def main():
	parser = argparse.ArgumentParser(description='Change quality of all images (JPEG) in a directory and its sub-directory.')
	parser.add_argument('-q',  '--quality',  type=int, default=80,  metavar='', help='Quality of the output image')
	parser.add_argument('-w',  '--width',    type=int, default=-1,  metavar='', help='Width of the output image')
	parser.add_argument('-H',  '--height',   type=int, default=-1,  metavar='', help='Height of the output image')
	parser.add_argument('-ih', '--inHeight', type=int, default=500, metavar='', help='Height threshold of the input image')
	args = parser.parse_args()

	pathList = list(Path('.').glob('**/*.jpg'))

	outDir = './out'
	if not os.path.exists(outDir):
		os.makedirs(outDir)

		for path in pathList:
			pathStr = str(path)
			filename = os.path.basename(pathStr)
			foldername = pathStr.replace(filename, '')

			img = Image.open(pathStr)
			if (img.size[1] > args.inHeight):
				outDir = './out/' + foldername
				if not os.path.exists(outDir):
					os.makedirs(outDir)

				command = f'magick "{pathStr}" -quality {args.quality} -resize {args.width}x{args.height} "out/{pathStr}"'
				print(command)
				os.system(command)
	
	else:
		print('"out" directory already exists. Rename the output directory or move the contents of the existing "out" directory.')


if __name__ == '__main__':
	main()