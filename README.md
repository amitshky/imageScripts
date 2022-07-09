# imageScripts
Python scripts for executing [imagemagick](https://imagemagick.org/) commands in all files of the directory.

### Prerequisites
* [Python](https://www.python.org/downloads/) v3.6 or higher
* Download and set up [imagemagic](https://imagemagick.org/script/download.php)
* [Pillow](https://pypi.org/project/Pillow/)

## Example
```
python src/imageQuality.py -q 80 -w 1500 -ih 1200
```

* Use `-h` or `--help` to see all the possible command line arguments