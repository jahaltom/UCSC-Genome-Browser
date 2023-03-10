import pandas as pd
import csv




##Makes bed detailed tracks. By chr. 

md = pd.read_csv("Transcript_level_metadata.tsv",sep='\t')

covid = pd.read_csv("CovidEBs.txt",sep='\t',header=None)
covid.columns =['Gene_stable_ID']
non = pd.read_csv("NonCovidEBs.txt",sep='\t',header=None)
non.columns =['Gene_stable_ID']


#Get useful attributes for gtf
md['attributes']= "Gene ID: " + md['Gene_stable_ID'] + "    Transcript ID: " + md['TranscriptID'] + "    ORF length: " + md['ORF_length'].astype(str) + "    cDNA length: " + md['cdna_length'].astype(str) +"    Final Strata: " + md['final_strata'].fillna('').astype('string')   



non["source"]="EB"
covid["source"]="COVID-19 expressed EB"

_54k=md[md["is54K_EB"]==True]
_54k["source"]="EB"
_54k=_54k[["Gene_stable_ID","source"]]

ebs = pd.concat([covid,non,_54k],ignore_index=True)
ebs=ebs.drop_duplicates(subset=['Gene_stable_ID'], keep='first').reset_index()

ebs=pd.merge(ebs,md,on=["Gene_stable_ID"])
ebs["ID"]="."
ebs["score"]="0"

bedDet=ebs[["chr", "start","end","TranscriptID","score","strand","source","attributes"]]

bedDet["start"]=bedDet["start"].astype(int)
bedDet["end"]=bedDet["end"].astype(int)

chrs=bedDet["chr"].drop_duplicates().to_list()

bed=open("UCSC_EB.bed", "w")
for i in chrs:
    df=bedDet[(bedDet['chr'] == i) ]
    if len(df[(df['source'] == 'COVID-19 expressed EB') ])>0:
        bed.write("track name=\""+i+" COVID-19 expressed evidence based\" type=bedDetail color=255,0,0 description=\"COVID-19 expressed evidence based\"")
        bed.write('\n')
        bed.write(df[(df['source'] == 'COVID-19 expressed EB') ].to_csv(index=False, header=False, sep='\t'))
    if len(df[(df['source'] == 'EB') ])>0:
        bed.write('\n')
        bed.write("track name=\""+i+" Evidence based\" type=bedDetail color=0,0,255 description=\"Evidence based\"")
        bed.write('\n')
        bed.write(df[(df['source'] == 'EB') ].to_csv(index=False, header=False, sep='\t'))
bed.close()
    
