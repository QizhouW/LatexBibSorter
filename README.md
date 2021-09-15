# bibtexSorter
To sort and filter irrelavant entries in the bibtex.

**Environmet** 
python 3.x

### To use
1. Download your article tex file and reference bibtex file. 
   
2. <pre><code>python sortbib.py -bibname YOUR_BIB_FIlENAME -texname YOUR_TEX_FILENAME </code></pre> 
   or by default (bibname='ref.bib',texname='article.tex')
   <pre><code>python sortbib.py</code></pre> 
   
3. The script scan and record all present citations in the article file and sort the entries in bibtex with this order.
   
4. Original bib file will be backuped as 'ref_old.bib'

### Example
<pre><code>python sortbib.py -bibname ref.bib -texname article.tex
Total number of bib entries:  165
Total number of cite positions:  124
Total number of references:  139 , irrelevant entries removed
</code></pre>
