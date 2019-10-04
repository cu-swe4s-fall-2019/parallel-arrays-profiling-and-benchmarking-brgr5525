test -e ssshtest || curl https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest -o ssshtest

source ssshtest


rm -f ACTA2.png
run sample_input python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file ACTA2.png
assert_exit_code 0


run group_type_wrong python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type NoGroup \
--output_file test.png
assert_exit_code 1
assert_in_stdout '--group_type must be either SMTS or SMTSD'


run sample_attributes_not_found python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes no_file.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file test.png
assert_exit_code 1
assert_in_stdout '--sample_attributes could not be found'


> empty_file.txt

run sample_attributes_empty python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes empty_file.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file test.png
assert_exit_code 1
assert_in_stdout '--sample_attributes is not formatted properly, check that it is not empty'


run gene_reads_not_gzip python plot_gtex.py \
--gene_reads not_gzip_file.py \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file test.png
assert_exit_code 1
assert_in_stdout '--gene_reads must be a gzipped file'


run gene_does_not_exist python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene NotAGene \
--group_type SMTS \
--output_file test.png
assert_exit_code 1
assert_in_stdout 'Gene could not be found in given data'


run out_file_already_exists python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file ACTA2.png
assert_exit_code 1
assert_in_stdout '--output_file already exists, please choose a different name'


run out_file_bad_extension python plot_gtex.py \
--gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file ACTA2.py
assert_exit_code 1
assert_in_stdout '--output_file is of unsupported type, try a .png'
