# Run Parser
Parses NovaSeq Sequencer run files from a list of file locations.

# Requirements
* Python 2.7.whatever..
* Pip

# To Use
* git clone the project
```
git clone https://github.com/graffam/run_parser.git
```
* Install python dependencies with pip:
```
pip install -r requirements.txt
```
* add xml paths to the file_paths.txt
* run it!
```
python app.py file_paths.txt output.csv
```

# Arguments:
command line arguments application takes:
the paths to the files to parse, line seperated in a text file, and the output
file you would like to store the results in.
