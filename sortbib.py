import argparse
import re
import os
parser=argparse.ArgumentParser(description='bibtex sorter')
parser.add_argument('-bibname', type=str, default='ref.bib', help='bibtex file name')
parser.add_argument('-texname', type=str, default='article.tex', help='tex file name')
args=parser.parse_args()
bibname=args.bibname
texname=args.texname

with open(bibname, 'r') as fo:
    bib=fo.read()
pattern=re.compile(r'@.*?\n}\n',re.DOTALL)
biblist=re.findall(pattern,bib)
print('Total number of bib entries: ', len(biblist))


with open(texname, 'r') as fo:
    tex=fo.read()
p=re.compile(r'(?<!\\)%.*?\n')
tex=re.sub(p,'\n',tex)

pattern=re.compile(r'(?<=cite{).*?(?=})',re.DOTALL)
citelist=re.findall(pattern,tex)
print('Total number of cite positions: ', len(citelist))


def find_bib(abbr):
    for entry in biblist:
        if re.search(abbr,entry) is not None:
            return entry
    raise ValueError('abbreviation:'+abbr+' not found in bib file')


entries_found=[]
sorted_list=[]
for abbrs in citelist:
    abbrs=re.split(',',abbrs)
    if len(abbrs)==1:
        abbr=abbrs[0].strip()
        if abbr not in entries_found:
            sorted_list.append(find_bib(abbr))
            entries_found.append(abbr)
    else:
        for abbr in abbrs:
            abbr=abbr.strip()
            if abbr not in entries_found:
                sorted_list.append(find_bib(abbr))
                entries_found.append(abbr)
        #temp=[find_bib(abbr.strip()) for abbr in abbrs]
        #sorted_list=sorted_list+temp
if len(sorted_list)!=len(biblist):
    print('Total number of references: ', len(sorted_list),', irrelevant entries removed')
else:
    print('Total number of references: ', len(sorted_list),', all entries complete')

new_bib=''
for item in sorted_list:
    new_bib=new_bib+item

os.rename(bibname,'ref_old.bib')

with open(bibname,'w') as fo:
    fo.write(new_bib)

