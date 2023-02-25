
**UniqueList:** Takes in nonCovidEBs.txt and covidEBs.txt (these are a list of EB gene IDs) from NewEBs.py (Mason data and SRA) and combines them. EBs common between nonCovidEBs and covidEBs were classafied as nonCovidEBs. These contain some EBs from Urmis54K and new ones I found. All unique. 


**UCSCGbrowsTrackGenerator.py:** Takes in NonCovidEBs.txt and CovidEBs.txt from UniqueList and generated UCSC bed detaile formated tracks for each chromosome. 

bed detail format: https://genome.ucsc.edu/FAQ/FAQformat.html#format1

see track lines: https://genome.ucsc.edu/goldenPath/help/customTrack.html#TRACK

see track grouping: https://genome.ucsc.edu/goldenPath/help/trackDb/trackDbHub.html#superTrack

## UCSC Genome Browser##
After making the track files, make a UCSC accout to enable track sharing. Then upload your bed detail files https://genome.ucsc.edu/cgi-bin/hgCustom.



![alt text](https://github.com/jahaltom/UCSC-Genome-Browser/blob/main/UCSCGenomeBrowserSession.png?raw=true)
