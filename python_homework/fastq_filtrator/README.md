## FASTQ filtrator

It's a simple fastq filter tool.

Tool is able to:
1. Filter reads by GC composition - by <--gc-bounds> flag. The GC interval for filtering default is 0-100%.
2. Filter reads by quality - by <--quality-threshold> flag. Default is 0. [Quality Score Encoding](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm)
3. Filter reads by length - by <--length-bounds> flag. The lenght interval for filtering default is 0-2**32.
4. Save results to file:
    - if <--save-filtered> == Fasle - save only passed filter reads.
    - if <--save-filtered> == True - save passed and failed filter reads to two different files.