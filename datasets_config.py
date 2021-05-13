small_sizes = [200, 100, 50, 10, 1]

# Root of tudocomp provided mirrors of datasets
TDC_URL = "dolomit.cs.uni-dortmund.de/tudocomp"

# TODO: This server went offline
# Only he-graph has an existing 200mb prefix on loebels system
# TODO: Need to upload to our server
# HashTag Datasets, see http://acube.di.unipi.it/datasets/
#ACUBE_URL = "http://acube.di.unipi.it/repo/he-graph"
#download_and_extract("hashtag", small_sizes, [
#    ACUBE_URL + "/graph/he-graph.txt.gz",
#    ACUBE_URL + "/relatedness/pairs.tsv",
#    ACUBE_URL + "/classification/crowdflower.tsv",
#])

# ASCII-only, no inner null commoncrawl.org extract
download_and_extract("cc", small_sizes, [
    TDC_URL + "/commoncrawl.ascii.xz"
])

download_and_extract("chr19", small_sizes, [
    TDC_URL + "/chr19.10.fa.xz"
])

# Pizza&Chili Corpus text collection
PC_URL = "http://pizzachili.dcc.uchile.cl"

download_and_extract("pc", small_sizes, [
    TDC_URL + "/pc/sources.xz",
    TDC_URL + "/pc/pitches.xz",
    TDC_URL + "/pc/proteins.xz",
    TDC_URL + "/pc/dna.xz",
    TDC_URL + "/pc/english.xz",
    TDC_URL + "/pc/dblp.xml.xz",
])
download_and_extract("pcr", small_sizes, [
    TDC_URL + "/pc-pseudo-real/english.001.2.xz",
    TDC_URL + "/pc-pseudo-real/dblp.xml.00001.1.xz",
    TDC_URL + "/pc-pseudo-real/dblp.xml.00001.2.xz",
    TDC_URL + "/pc-pseudo-real/dblp.xml.0001.1.xz",
    TDC_URL + "/pc-pseudo-real/dblp.xml.0001.2.xz",
    TDC_URL + "/pc-pseudo-real/dna.001.1.xz",
    TDC_URL + "/pc-pseudo-real/english.001.2.xz",
    TDC_URL + "/pc-pseudo-real/proteins.001.1.xz",
    TDC_URL + "/pc-pseudo-real/sources.001.2.xz",
    TDC_URL + "/pc-real/cere.xz",
    TDC_URL + "/pc-real/coreutils.xz",
    TDC_URL + "/pc-real/einstein.de.txt.xz",
    TDC_URL + "/pc-real/einstein.en.txt.xz",
    TDC_URL + "/pc-real/Escherichia_Coli.xz",
    TDC_URL + "/pc-real/influenza.xz",
    TDC_URL + "/pc-real/kernel.xz",
    TDC_URL + "/pc-real/para.xz",
    TDC_URL + "/pc-real/world_leaders.xz",
    TDC_URL + "/pc-artificial/fib41.xz",
    TDC_URL + "/pc-artificial/rs.13.xz",
    TDC_URL + "/pc-artificial/tm29.xz",
])

# # TAGME Datasets, see http://acube.di.unipi.it/datasets/
# download_and_extract("tagme", small_sizes, [
#     TDC_URL + "/wiki-annot30.gz",
#     TDC_URL + "/wiki-disamb30.gz",
# ])
#
# # TagMyNews Datasets, see http://acube.di.unipi.it/datasets/
# download_and_extract("tagmynews", small_sizes, [
#     TDC_URL + "/news.gz",
#     TDC_URL + "/data-web-snippets.tar.gz",
# ])

# ASCII-only Wikipedia excerpt from the "10.000 most vital articles" project
download_and_extract("wiki", small_sizes, [
    TDC_URL + "/all_vital.txt.xz",
])
