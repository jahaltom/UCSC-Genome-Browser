import pandas as pd
import csv






md = pd.read_csv("Transcript_level_metadata.tsv",sep='\t')

covid = pd.read_csv("CovidEBs.txt",sep='\t',header=None)
covid.columns =['Gene_stable_ID']
non = pd.read_csv("NonCovidEBs.txt",sep='\t',header=None)
non.columns =['Gene_stable_ID']


#Get useful attributes for gtf
md['attributes']= "gene_id \"" + md['Gene_stable_ID'] + "\"; "  +"transcript_id \"" + md['TranscriptID'] + "\"; "  + "ORF_length \"" + md['ORF_length'].astype(str) + "\"; "  + "cdna_length \"" + md['cdna_length'].astype(str) +"\"; "  + "final_strata \"" + md['final_strata'].fillna('').astype('string') + "\"; "   



non["source"]="EB"
covid["source"]="COVID-19 expressed EB"

_54k=md[md["is54K_EB"]==True]
_54k["source"]="EB"
_54k=_54k[["Gene_stable_ID","source"]]

ebs = pd.concat([covid,non,_54k],ignore_index=True)
ebs=ebs.drop_duplicates(subset=['Gene_stable_ID'], keep='first').reset_index()

ebs=pd.merge(ebs,md,on=["Gene_stable_ID"])
ebs["feature"]="CDS"
ebs["score"]="."
ebs["frame"]="."

gtf=ebs[["chr","source","feature","start","end","score","strand","frame","attributes"]]


gtf.to_csv("EBs.gtf",sep='\t',index=False,mode='w',quoting=csv.QUOTE_NONE)  

      
###Adding to current metadata files.
  
txmd = pd.read_csv("Transcript_level_metadata.tsv",sep='\t')
genemd = pd.read_csv("Gene_level_metadata.tsv",sep='\t')

ebs=ebs[["Gene_stable_ID","source"]]
ebs=ebs.drop_duplicates(subset=['Gene_stable_ID'], keep='first').reset_index()



txmd=pd.merge(txmd,ebs,on=["Gene_stable_ID"],how='left')
genemd=pd.merge(genemd,ebs,on=["Gene_stable_ID"],how='left')



txmd=txmd.drop(['EB_type'], axis=1)
txmd=txmd.drop(['index'], axis=1)
genemd=genemd.drop(['EB_type'], axis=1)
genemd=genemd.drop(['index_x'], axis=1)
genemd=genemd.drop(['index_y'], axis=1)
txmd = txmd.rename(columns={'source': 'EB_type'})
genemd = genemd.rename(columns={'source': 'EB_type'})


txmd=txmd[['Gene_stable_ID', 'EB_type', 'TranscriptID', 'Gene_name',
       'Gene_description', 'type', 'Gene_type', 'tx_name', 'tx_type', 'chr',
       'start', 'end', 'strand', 'status', 'ref_tid', 'ref_gene', 'ccode',
       'gid', 'ref_num_exons', 'cdna_length', 'ORF_length', 'exon_num', 'mrca',
       'ps', 'mrca_name', 'Liftoff_matches', 'final_strata', 'Gorilla_gorilla',
       'Macaca_mulatta', 'Nomascus_leucogenys', 'Pongo_abelii',
       'Pan_troglodytes', 'mouse', 'is_complete', 'is54K_EB', 'seq']]

genemd=genemd[['Gene_stable_ID', 'EB_type', 'Gene_name', 'Gene_description',
       'final_strata', 'mrca_name', 'ps', 'Gorilla_gorilla', 'Macaca_mulatta',
       'Nomascus_leucogenys', 'Pongo_abelii', 'Pan_troglodytes', 'mouse',
       'is_complete', 'is54K_EB', 'chr', 'Gene_type', 'Longest_ORF_length',
       'cdna_length', 'strand', 'status', 'ccode', 'exon_num', 'Gene_ID_ver',
       'TX_names', 'TX_type', 'Tx_ids', 'ref_tid', 'ref_gene',
       'ref_num_exons']]


txmd.to_csv("Transcript_level_metadata.2.tsv",sep='\t',index=False,mode='w',quoting=csv.QUOTE_NONE)
genemd.to_csv("Gene_level_metadata.2.tsv",sep='\t',index=False,mode='w',quoting=csv.QUOTE_NONE)


