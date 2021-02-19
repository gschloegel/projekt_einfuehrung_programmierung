# PYTHON_FINAL
information provided by eggNOG is used to explore highly conserved genes in the three domains of life, Bacteria, Archaea and Eukaryota.
  
5 required gzipped files are downloaded (2_members.tsv.gz, 2157_members.tsv.gz, 2759_members.tsv.gz, 2157_annotations.tsv.gz eggnog4.functional_categories.txt)\
7 textfiles are created (cogs_bacteria_o99.txt, cogs_archaea_o99.txt, cogs_eukaryota_o99.txt, cogs_bacteria_o50_u99.txt, cogs_bacteria_o99_u99.txt, cogs_archaea_os97.txt, functional_categories.txt)\
other results are printed to stdout

## Scripts
run.sh and 2 other pythonscripts (read_members_file.py and annotate_cogs.py)

## Usage
execute the Bash script (run.sh)

## Autors
Schlögel Guido, Tockner Sonja, Hennebichler Bernhard, Gebhart Verena


## Questions

### Which genes are universally required for an organism to survive? More precisely: Which genes (OGs) occur in at least 99% of all genomes in the eggNOG5 database in each domain of life, respectively?
How many such genes did you identify in each domain? Bacteria 123, Archaea 175, Eukaryota 273 \
Provide the results as three files (one for each domain) listing the OGs in sorted order (by name). see cogs_bacteria_o99.txt, cogs_archaea_o99.txt and cogs_eukaryota_o99.txt

### Which common bacterial genes occur almost exclusively as single-copy genes?More precisely: Which OGs occur in at least 50% of all bacterial genomes, and in at least 99% thereof as single-copy?
Provide the results as a sorted text file. see cogs_bacteria_o50_u99.txtn \
How many of these OGs were also identified as universal bacterial OGs (previous question)? 40, see cogs_bacteria_o99_u99.txt 

### Identify all OGs that occur as single-copy in at least 97% of all Archaea.
How many such OGs did you identify? Provide the result as a sorted text file. 121, see cogs_archaea_os97.txt \
Are there Archaea which lack 4 or more of these universal OGs? yes 6 archaeal genomes \
Which organism (scientific name) lacks most? Taxonomy ID: 70601, Pyrococcus horikoshii OT3, with 7 lacks. \
What is its preferred growing temperature/environment? 98 °C

### Compile an overview of the functional categories of these 121 archaeal OGs.
Provide the result as a text file sorted by the number of the functional categories. see functional_categories.txt
