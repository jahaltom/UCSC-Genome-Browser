import pandas as pd
import csv




##Makes bed detailed tracks. By chr. 

md = pd.read_csv("Transcript_level_metadata.tsv",sep='\t')

covid = pd.read_csv("CovidEBs.txt",sep='\t',header=None)
covid.columns =['TranscriptID']
non = pd.read_csv("NonCovidEBs.txt",sep='\t',header=None)
non.columns =['TranscriptID']


#Get useful attributes for gtf
md['attributes']= "Gene ID: " + md['Gene_stable_ID'] + "    Transcript ID: " + md['TranscriptID'] + "    ORF length: " + md['ORF_length'].astype(str) + "    cDNA length: " + md['cdna_length'].astype(str) +"    Final Strata: " + md['final_strata'].fillna('').astype('string')   



non["source"]="EB"
covid["source"]="COVID-19 expressed EB"

_54k=md[md["is54K_EB"]==True]
_54k["source"]="EB"
_54k=_54k[["TranscriptID","source"]]

ebs = pd.concat([covid,non,_54k],ignore_index=True)
ebs=ebs.drop_duplicates(subset=['TranscriptID'], keep='first').reset_index()

ebs=pd.merge(ebs,md,on=["TranscriptID"])
ebs["ID"]="."
ebs["score"]="0"

bedDet=ebs[["chr", "start","end","TranscriptID","score","strand","source","attributes"]]

#Make start 0-based
bedDet["start"]=bedDet["start"].astype(int)-1
bedDet["end"]=bedDet["end"].astype(int)



bed=open("UCSC_EB.bed", "w")
bed.write('browser position chr1')
bed.write('\n')   
bed.write("track name=\"COVID-19 expressed\" type=bedDetail color=255,0,0 description=\"COVID-19 expressed evidence based\" visibility=1")
bed.write('\n')
bed.write(bedDet[(bedDet['source'] == 'COVID-19 expressed EB') ].to_csv(index=False, header=False, sep='\t'))
   
bed.write('\n')
bed.write("track name=\"Evidence based\" type=bedDetail color=0,0,255 description=\"Evidence based\" visibility=1")
bed.write('\n')
bed.write(bedDet[(bedDet['source'] == 'EB') ].to_csv(index=False, header=False, sep='\t'))
bed.close()
