
**UniqueList:** Takes in nonCovidEBs.txt and covidEBs.txt (these are a list of EB Gene_stable_IDs)) from NewEBs.py (Mason data and SRA) and combines them. EBs common between nonCovidEBs and covidEBs were classafied as nonCovidEBs. These contain some EBs from Urmis54K and new ones I found. All unique. 


**UCSCGbrowsTrackGenerator.py:** Takes in NonCovidEBs.txt and CovidEBs.txt ( Gene_stable_IDs) from UniqueList and generated UCSC bed detaile formated track for the whole genome. Contains all covid/non-covid EBs I found in my analysis some are new some are Urmi’s 54K (covid marked “COVID-19 expressed EB”, non-covid marked “EB”). The remaining EBs from Urmi’s 54K are also included marked as “EB”.  Each Gene_stable_ID  is merged with Transcript_level_metadata.tsv which results in some Gene_stable_ID being associated with multiple transcripts. 

bed detail format: https://genome.ucsc.edu/FAQ/FAQformat.html#format1

see track lines: https://genome.ucsc.edu/goldenPath/help/customTrack.html#TRACK

see track grouping: https://genome.ucsc.edu/goldenPath/help/trackDb/trackDbHub.html#superTrack

## UCSC Genome Browser
After making the track file, make a UCSC accout to enable track sharing. Then upload your bed detail file https://genome.ucsc.edu/cgi-bin/hgCustom. USe GRCh38/hg38.
Use EB.html for "Optional track documentation:"


Gbrows link: https://genome.ucsc.edu/s/jahaltom/EB%20Genes

![alt text](https://github.com/jahaltom/UCSC-Genome-Browser/blob/main/UCSCGenomeBrowserSession.png?raw=true)
