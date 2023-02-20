import pandas as pd
import csv






md = pd.read_csv("Transcript_level_metadata.tsv",sep='\t')

covid = pd.read_csv("CovidEBs.txt",sep='\t',header=None)
covid.columns =['Gene_stable_ID']
non = pd.read_csv("NonCovidEBs.txt",sep='\t',header=None)
non.columns =['Gene_stable_ID']


#Get useful attributes for gtf
md['attributes']= "gene_id \"" + md['Gene_stable_ID'] + "\"; "  +"transcript_id \"" + md['TranscriptID'] + "\"; "  + "ORF_length \"" + md['ORF_length'].astype(str) + "\"; "  + "cdna_length \"" + md['cdna_length'].astype(str) +"\"; "  + "final_strata \"" + md['final_strata'].fillna('').astype('string') + "\"; "   



       



non=pd.merge(non,md,on=["Gene_stable_ID"])
non["source"]="EB"
non["feature"]="CDS"
non["score"]="."
non["frame"]="."
non=non[["chr","source","feature","start","end","score","strand","frame","attributes"]]



covid=pd.merge(covid,md,on=["Gene_stable_ID"])
covid["source"]="COVID-19 expressed EB"
covid["feature"]="CDS"
covid["score"]="."
covid["frame"]="."
covid=covid[["chr","source","feature","start","end","score","strand","frame","attributes"]]




gtf = pd.concat([covid,non],ignore_index=True)
gtf.to_csv("EBs.gtf",sep='\t',index=False,mode='w',quoting=csv.QUOTE_NONE)
