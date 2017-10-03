import sys
import csv
from bs4 import BeautifulSoup

# Scrapes RfidInfo from XML tags on run data

if len(sys.argv) != 3:
    print "Usage: python app.py file_paths.txt output.csv"
else:
    file_paths = []
    with open(sys.argv[1]) as f:
        for line in f:
            file_paths.append(line.rstrip())
    with open(sys.argv[2],'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        # Location of xml files on the network
        writer.writerow(['folder_name', 'SbsLotNumber', 'ClusterLotNumber', 'BufferLotNumber', 'FlowCellSerialBarcode',
                         'ExperimentName'])
        for i in range(0, len(file_paths)):
            infile = open(file_paths[i] + '\\RunParameters.xml', "r")
            contents = infile.read()
            obj = BeautifulSoup(contents, 'xml')
            sbs = ""
            buffer = ""
            cluster = ""
            flow = ""
            experiment_name = ""
            if obj.RunParameters.RfidsInfo:
                if obj.RunParameters.RfidsInfo.SbsLotNumber:
                    sbs = obj.RunParameters.RfidsInfo.SbsLotNumber.string
                if obj.RunParameters.RfidsInfo.ClusterLotNumber:
                    cluster = obj.RunParameters.RfidsInfo.ClusterLotNumber.string
                if obj.RunParameters.RfidsInfo.BufferLotNumber:
                    buffer = obj.RunParameters.RfidsInfo.BufferLotNumber.string
                if obj.RunParameters.RfidsInfo.FlowCellSerialBarcode:
                    flow = obj.RunParameters.RfidsInfo.FlowCellSerialBarcode.string
            if obj.RunParameters.ExperimentName:
                    experiment_name = obj.RunParameters.ExperimentName.string
            writer.writerow([file_paths[i], sbs, cluster, buffer, flow, experiment_name])
