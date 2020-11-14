# coding=utf-8
# -*- codeing = utf-8 -*-
# @Time:2020/9/12 14:17
# @Author:邵东延
# @File:fasta_stats.py
# @software:PyCharm
# coding=utf-8
import os
import re
import glob
import pandas as pd

n = 0
import numpy as np

df_data = pd.DataFrame(columns=(
"names", "Total scaffolds", "Total base (bp)", "Total N (bp)", "Average length (bp)", "Longest scaffold (bp)",
"Shortest scaffold (bp)", "L50", "N50", "L75", "N75", "L90", "N90", "GC (%)", "Total scaffolds (>= 1000000 bp)",
"Total scaffolds (>= 100000 bp)", "Total scaffolds (>= 10000 bp)", "Total scaffolds (>= 1000 bp)",
"Total length (>= 1000000 bp)", "Total length (>= 100000 bp)", "Total length (>= 10000 bp)",
"Total length (>= 1000 bp)"))

output = 'fasta.stat.txt'
#liebiao = ['09b17.fasta', '09b19.fasta', '09b21.fasta', '09b23.fasta', '09b25-2.fasta', '09b28.fasta', '09b31.fasta',
           #'10.fasta', '11b11.fasta', '11b12.fasta', '11B206.fasta', '11B220.fasta', '11B234.fasta', '11B247.fasta',
           #'11b4.fasta', '11b7.fasta', '11C126.fasta', '11d8.fasta', '11HE3.fasta', '11J212.fasta', '2_HS-C.fasta',
           #'5.fasta', '5CRE51.fasta', '7-1.fasta', '7.fasta', '9.fasta']
liebiao=glob.glob("*.fasta")
for i in liebiao:
    input = i
    dict = {};
    dict_refer = {}
    seqs_sum = 0
    base_sum = 0
    GC_sum = 0
    N_sum = 0
    H_sum = 0
    Ln = 0;
    base_sum_n = 0
    N50 = 0;
    N75 = 0;
    N90 = 0
    n1000000 = 0;
    n1000000_len = 0
    n100000 = 0;
    n100000_len = 0
    n10000 = 0;
    n10000_len = 0
    n1000 = 0;
    n1000_len = 0
    n += 1
    # 读入 fasta 文件，统计 scaffolds（每条 + 所有）总数、长度、GC 含量等基本信息
    with open(input, 'r') as read_fas:
        for line in read_fas:
            if line[0] == '>':
                key = line.strip('[ >\n]')
                dict[key] = 0
                seqs_sum += 1
            else:
                value = line.strip()
                seqs_len = len(value)
                base_sum += seqs_len
                dict[key] += seqs_len
                GC_sum += len(re.findall('[gcGC]', value))
                N_sum += len(re.findall('[nN]', value))
                H_sum += len(re.findall('[vV]', value))

    read_fas.close()
    # 统计 N50、N75、N90 以及各长度区间 scaffolds 数量及长度
    dict_sort = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    base_sum_n50 = 5 * base_sum / 10
    base_sum_n75 = 7.5 * base_sum / 10
    base_sum_n90 = 9 * base_sum / 10
    for value in dict_sort:
        base_sum_n += value[1]
        Ln += 1
        if N50:
            if N75:
                if base_sum_n >= base_sum_n90:
                    N90 = value[1]
                    L90 = Ln
                    break
            else:
                if base_sum_n >= base_sum_n75:
                    N75 = value[1]
                    L75 = Ln
        else:
            if base_sum_n >= base_sum_n50:
                N50 = value[1]
                L50 = Ln
    for value in dict_sort:
        if value[1] >= 1000000:
            n1000000 += 1
            n1000000_len += value[1]
        if value[1] >= 100000:
            n100000 += 1
            n100000_len += value[1]
        if value[1] >= 10000:
            n10000 += 1
            n10000_len += value[1]
        if value[1] >= 1000:
            n1000 += 1
            n1000_len += value[1]
        if value[1] < 1000:
            break
    # 统计总览，并输出结果
    aver = int(base_sum / seqs_sum)
    longest = dict_sort[0][1]
    shortest = dict_sort[-1][1]
    gc = round(100 * GC_sum / base_sum, 2)
    df_data.loc[len(df_data)]= [i, seqs_sum, base_sum, N_sum, aver, longest, shortest, L50, N50, L75, N75, L90, N90, gc, n1000000,
                          n100000, n10000, n1000, n1000000_len, n100000_len, n10000_len,n1000_len]
    #df_data.append(pd.Series(new_row,index=df_data.columns[:len(df_data)]),ignore_index=True)
    basic_stat = open(output, 'w')
    print(f'Total scaffolds\t{seqs_sum}', file=basic_stat)
    print(f'Total base (bp)\t{base_sum}', file=basic_stat)
    print(f'Total N (bp)\t{N_sum}', file=basic_stat)
    print(f'Average length (bp)\t{int(base_sum / seqs_sum)}', file=basic_stat)
    print(f'Longest scaffold (bp)\t{dict_sort[0][1]}', file=basic_stat)
    print(f'Shortest scaffold (bp)\t{dict_sort[-1][1]}', file=basic_stat)
    print(f'L50\t{L50}', file=basic_stat)
    print(f'N50\t{N50}', file=basic_stat)
    print(f'L75\t{L75}', file=basic_stat)
    print(f'N75\t{N75}', file=basic_stat)
    print(f'L90\t{L90}', file=basic_stat)
    print(f'N90\t{N90}', file=basic_stat)
    print(f'GC (%)\t{round(100 * GC_sum / base_sum, 2)}', file=basic_stat)
    print(f'Total scaffolds (>= 1000000 bp)\t{n1000000}', file=basic_stat)
    print(f'Total scaffolds (>= 100000 bp)\t{n100000}', file=basic_stat)
    print(f'Total scaffolds (>= 10000 bp)\t{n10000}', file=basic_stat)
    print(f'Total scaffolds (>= 1000 bp)\t{n1000}', file=basic_stat)
    print(f'Total length (>= 1000000 bp)\t{n1000000_len}', file=basic_stat)
    print(f'Total length (>= 100000 bp)\t{n100000_len}', file=basic_stat)
    print(f'Total length (>= 10000 bp)\t{n10000_len}', file=basic_stat)
    print(f'Total length (>= 1000 bp)\t{n1000_len}', file=basic_stat)
    basic_stat.close()
print(df_data)
df_data.to_csv("stat.csv", sep=",", index=False)

