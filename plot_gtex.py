import gzip
import sys
import data_viz
import argparse


def linear_search(key, L):
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1


def binary_search(key, L):
    lo = -1
    hi = len(L)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == L[mid][0]:
            return L[mid][1]

        if (key < L[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1


def main():

    # data_file_name='GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
    data_file_name = args.gene_reads
    # sample_info_file_name='GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
    sample_info_file_name = args.sample_attributes

    # group_col_name = 'SMTS'
    group_col_name = args.group_type
    if (group_col_name != 'SMTS') and (group_col_name != 'SMTSD'):
        print('--group_type must be either SMTS or SMTSD')
        sys.exit(1)

    sample_id_col_name = 'SAMPID'

    # gene_name = 'ACTA2'
    gene_name = args.gene

    samples = []
    sample_info_header = None

    try:
        for l in open(sample_info_file_name):
            if sample_info_header is None:
                sample_info_header = l.rstrip().split('\t')
            else:
                samples.append(l.rstrip().split('\t'))
    except FileNotFoundError:
        print('--sample_attributes could not be found')
        sys.exit(1)

    try:
        group_col_idx = linear_search(group_col_name, sample_info_header)
        sample_id_col_idx = linear_search(sample_id_col_name,
                                          sample_info_header)
    except TypeError:
        print('--sample_attributes is not formatted properly,' +
              ' check that it is not empty')
        sys.exit(1)

    groups = []
    members = []
    names = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]
        names.append(curr_group)

        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)

    names = list(dict.fromkeys(names))

    version = None
    dim = None
    data_header = None

    gene_name_col = 1

    group_counts = [[] for i in range(len(groups))]

    gene_hits = 0

    try:
        for l in gzip.open(data_file_name, 'rt'):
            if version is None:
                version = l
                continue

            if dim is None:
                dim = [int(x) for x in l.rstrip().split()]
                continue

            if data_header is None:
                data_header = []
                i = 0
                for field in l.rstrip().split('\t'):
                    data_header.append([field, i])
                    i += 1
                data_header.sort(key=lambda tup: tup[0])

                continue

            A = l.rstrip().split('\t')

            if A[gene_name_col] == gene_name:
                gene_hits += 1
                for group_idx in range(len(groups)):
                    for member in members[group_idx]:
                        member_idx = binary_search(member, data_header)
                        if member_idx != -1:
                            group_counts[group_idx].append(int(A[member_idx]))
                break
    except OSError:
        print('--gene_reads must be a gzipped file')
        sys.exit(1)
    except Exception:
        print('There was a problem with --gene_reads')
        sys.exit(1)
    if gene_hits == 0:
        print('Gene could not be found in given data')
        sys.exit(1)
    try:
        data_viz.boxplot(group_counts, args.output_file, gene_name,
                         group_col_name, 'Gene read counts', names)
    except SystemExit:
        print('--output_file already exists, please choose a different name')
        sys.exit(1)
    except ValueError:
        print('--output_file is of unsupported type, try a .png')
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description='Input gene and attribute files, gene name, ' +
                'group type, and output file name',
                prog='plot_gtex')

    parser.add_argument('--gene_reads',
                        type=str,
                        help='Name of file containing the gene information',
                        required=True)
    parser.add_argument('--sample_attributes',
                        type=str,
                        help='Name of file containing the sample information',
                        required=True)
    parser.add_argument('--gene',
                        type=str,
                        help='Name of desired gene',
                        required=True)
    parser.add_argument('--group_type',
                        type=str,
                        help='Name of the group type',
                        required=True)
    parser.add_argument('--output_file',
                        type=str,
                        help='Name of file for desired output',
                        required=True)

    args = parser.parse_args()

    main()
