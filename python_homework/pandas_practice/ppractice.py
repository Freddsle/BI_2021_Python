import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport


def plot_ATCG_hist():
    '''
    Open .csv file as Pandas DataFrame (df).
    df contains information about the number of reads with each of the 4 nucleotides
    at different positions (columns A, T, G, C).
    Plot a histogram of the distribution of these numbers.
    Save it to the .png file.
    '''
    url = "https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv"
    df = pd.read_csv(url)

    plt.rcParams['figure.figsize'] = 15, 10
    df[['pos', 'A', 'T', 'C', 'G']].groupby('pos').sum().plot.bar(stacked=True,
                                                                  ylabel='Reads number',
                                                                  xlabel='Position')

    plt.savefig('./data/task_1_hist.png')


def select_data():
    '''
    Write to the file `train_part.csv` some parts of the `train.csv` (df from prev task):
    1. Strings where matches bigger than matches mean;
    2. Cols 'pos', 'reads_all', 'mismatches', 'deletions', 'insertions'
    '''
    url = "https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv"
    df = pd.read_csv(url)

    columns_to_select = ['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']

    df_selected = df[df['matches'] > df['matches'].mean()][columns_to_select]
    df_selected.to_csv("./data/train_part.csv")

    # other ways to do same selection:
    # df_selected = df[df.matches > df.matches.mean()].filter(columns_to_select)
    # df_selected = df.query('matches > matches.mean()').filter(columns_to_select)


def small_EDA():
    '''
    Data - https://www.kaggle.com/yasserh/wine-quality-dataset.
    Data DataFrame EDA: correlation plot, distribution plots, EDA with pandas_profiling.
    '''
    # open and drop id column
    vine = pd.read_csv('./data/WineQT.csv')
    vine = vine.drop('Id', axis=1)

    # data frame view
    vine.head()

    # vine info
    vine.info()

    # count NAN values
    vine.isnull().sum()

    # simple vine statistics
    vine.describe()

    # correlation plot
    plt.matshow(vine.corr())
    # plt.show()
    plt.savefig("./data/correlation_01.png")
    plt.close()

    # corralation with coefficients
    vine.corr().style.background_gradient(cmap='PRGn')

    # correlation with scatteplots and distribution
    plt.rcParams['figure.figsize'] = 30, 30
    sns.pairplot(vine, hue='quality', corner=True, palette='Set2')
    plt.savefig("./data/correlation_02.png")
    plt.close()

    # scatter plots
    for data in vine.columns[:-2]:
        plt.subplots(1, 1, figsize=(9, 4))
        plt.scatter(y=vine[data],
                    x=vine['quality'])
        plt.grid()
        plt.title(f"{data} - Scatter plot analysis")
        plt.savefig(f"./data/Scatter/{data}_Scatterplot.png")
    plt.close()

    # plot distribution plots
    for data in vine.columns:
        bins = [len(set(vine[data].values)) if len(set(vine[data].values)) < 50 else 50]

        f, ax = plt.subplots(1, 1, figsize=(9, 4))
        plt.hist(vine[data], bins=bins[0], alpha=0.8)

        mean = vine[data].mean()
        median = vine[data].median()
        mode = vine[data].mode().values[0]

        ax.axvline(mean, color='r', linestyle='--', label="Mean")
        ax.axvline(median, color='g', linestyle='-', label="Mean")
        ax.axvline(mode, color='b', linestyle='-', label="Mode")

        ax.legend()
        plt.grid()
        plt.title(f"{data} - Histogram analysis")
        plt.savefig(f"./data/Histograms/{data}_Histogram.png")
    plt.close()

    # plot distribution plots
    for data in vine.columns:
        bins = [len(set(vine[data].values)) if len(set(vine[data].values)) < 50 else 50]

        f, ax = plt.subplots(1, 1, figsize=(6, 4))
        plt.boxplot(vine[data], vert=False)

        plt.grid()
        plt.title(f"{data} - Boxplot analysis")
        plt.savefig(f"./data/Boxplot/{data}_Boxplot.png")
    plt.close()

    # html ProfileReport report saved in data folder
    profile = ProfileReport(vine, title="Pandas Profiling Report", explorative=True)
    profile.to_file("./data/EDA_report.html")


def read_gff(file):
    '''
    Read gff files (input - path to the file) and return Pandas DataFrame.
    Does not works with really large gff files.
    '''
    colnames = ['chromosome', 'source', 'type',
                'start', 'end', 'score',
                'strand', 'phase', 'attributes']

    df_gff = pd.read_csv(file,
                         sep='\t',
                         engine='python',
                         header=None,
                         names=colnames,
                         comment='#')

    return df_gff


def read_bed6(file):
    '''
    Read bed6 files (input - path to the file) and return Pandas DataFrame.
    Does not works with really large bed files.
    '''
    colnames = ['chromosome', 'start', 'end', 'name', 'score', 'strand']
    df_bed6 = pd.read_csv(file,
                          sep='\t',
                          engine='python',
                          header=None,
                          names=colnames)
    return df_bed6


def gff_bed_work():
    '''
    Work with bioinf data:
    rrna_annotation.gff - annotation of ribosomal RNA.
    alignment.bed - file with metagenomic assembly alignment to the same dataset.
    '''
    # read files with functions:
    gff_df = read_gff('./data/rrna_annotation.gff')
    df_bed6 = read_bed6('./data/alignment.bed')

    # Truncate attributes column - leave only info about RNA type (16S, 23S, 5S).
    gff_df['attributes'] = gff_df['attributes'].str.extract("([0-9]{1,2}S)")
    # long version:
    # gff_df['attributes'] = gff_df['attributes'].str.replace(r'(?<=[0-9]S).*', '',
    #                                                         regex=True).replace(r'.*=(?=[0-9]{1,2}S)',
    #                                                                             '', regex=True)

    # Count RNA types for each "chromosome" and plot barplot.
    gff_df.groupby(['chromosome', 'attributes']).agg({'attributes': 'count'})
    # another way - returns series
    # gff_df.groupby('chromosome').attributes.value_counts()
    gff_df.groupby('attributes').chromosome.value_counts().unstack(0).plot.barh()
    plt.savefig("./data/attributes_barhplot.png")
    plt.close()

    # Pandas as bedtools intersect
    # We want to know how much rRNA was successfully assembled during the assembly process.
    # Creates a DataFrame containing initial records about rRNA completely included in the assembly (not a fragment),
    # as well as a record about the contig in which this RNA got.

    bedtools_intersect = gff_df.merge(df_bed6, how='outer', on=['chromosome'])
    bedtools_intersect = bedtools_intersect[(bedtools_intersect.
                                             start_x >= bedtools_intersect.
                                             start_y+1) & (bedtools_intersect.end_x <= bedtools_intersect.end_y+1)]


def main():
    plot_ATCG_hist()
    select_data()
    small_EDA()


if __name__ == '__main__':
    main()
