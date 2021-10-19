# Simple fastq filtrator
# run the .py file with flag -h in terminal for help

import argparse


def bound_check(bound):
    """
    Check type and number of elements in bounds.
    """

    if 2 < len(bound):
        print('Error. Added more than two number to bounds.')
        return

    try:
        normalized_bound = [float(value) for value in bound]
        return normalized_bound

    except ValueError:
        print('Error. Not a number in bounds.')
        return


def len_bounds_maker(length_bounds):    
    '''
    Check types, number of values in length_bounds. 
    Transform it to [float, float].
    '''

    normalized_length_bound = bound_check(length_bounds)

    if not normalized_length_bound:
        return

    # add lower bound to normalized_length_bounds
    if len(normalized_length_bound) == 1:
        return [0, normalized_length_bound[0]]

    return normalized_length_bound


def gc_bounds_maker(gc_bounds):
    '''
    Check types, number of values in gc_bonus. 
    Transform it to [float, float].
    '''

    normalized_gc_bound = bound_check(gc_bounds)

    if not normalized_gc_bound:
        return

    # add lower bound to normalized_gc_bounds
    if len(normalized_gc_bound) == 1:
        return [0, normalized_gc_bound[0]]

    return normalized_gc_bound


def gc_filter(lines, gc_bounds):
    '''
    Filter the read by GC content (in percent)
    '''
    read_len = len(lines[1].removesuffix('\n'))
    gc_number = lines[1].count('C') + lines[1].count('G')
    gc_content = 100 * gc_number // read_len

    if gc_content < gc_bounds[0] or gc_content > gc_bounds[1]:
        return 'failed'

    return 'passed'


def length_filter(lines, length_bounds):
    '''
    Filter the read by length.
    '''
    read_len = len(lines[1].removesuffix('\n'))

    if read_len < length_bounds[0] or read_len > length_bounds[1]:
        return 'failed'

    return 'passed'


def quality_filter(lines, quality_threshold):
    '''
    Filter the read by quality
    '''
    quality = 0
    read_len = len(lines[1].removesuffix('\n'))
    quality_line = lines[3].removesuffix('\n')

    for character in quality_line:
        quality += (ord(character) - 33)

    average_quality = quality // read_len

    if average_quality < quality_threshold:
        return 'failed'

    return 'passed'


def filter_fastq(lines, gc_bounds, length_bounds, quality_threshold):
    '''
    Check the quality for each read in fastq file.
    If passed - return True, else - False.
    '''

    filter_tests = []

    # filter the read by GC content
    if gc_bounds != [0, 100]:
        filter_tests.append(gc_filter(lines, gc_bounds))
    else: filter_tests.append('passed')

    # filter the read by length
    filter_tests.append(length_filter(lines, length_bounds))

    # filter the read by quality
    if quality_threshold != 0:
        filter_tests.append(quality_filter(lines, quality_threshold))
    else: filter_tests.append('passed')

    # write passed lines to one fite, 
    if 'failed' in filter_tests:
        return False

    return True

def create_out_fastq(output_file_prefix, save_filtered):
    '''
    Create empty output fastq file or files
    '''

    f_passed = open(output_file_prefix+'_passed.fastq', 'w')
    f_passed.close()

    if save_filtered:
        f_failed = open(output_file_prefix+'_failed.fastq', 'w')
        f_failed.close()


def write_filtered_fastq(lines, quality_result, output_file_prefix, save_filtered):
    '''
    Write (to the end of file) each read to the passed or (if needed) failed file.
    '''

    if quality_result:
        with open(output_file_prefix+'_passed.fastq', 'a') as fastq_out:
            fastq_out.writelines(lines)

    else:
        if save_filtered:
            with open(output_file_prefix+'_failed.fastq', 'a') as fastq_out:
                fastq_out.writelines(lines)


def read_fatsq_for_filter(input_fastq, gc_bounds, length_bounds, quality_threshold, 
                          output_file_prefix, save_filtered):
    """
    Reads four lines from a fastq file and passes them to filtering function.
    """

    with open(input_fastq, 'r') as fastq:
        # Create an empty out file or files
        create_out_fastq(output_file_prefix, save_filtered)

        while True:
            try:
                lines = [next(fastq) for x in range(4)]
                quality_result = filter_fastq(lines, gc_bounds, length_bounds, quality_threshold)

                # Write out fastq file after filter
                write_filtered_fastq(lines, quality_result, output_file_prefix, save_filtered)

            except StopIteration:
                return 


def main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered):

    # Check bounds and update it
    gc_bounds_cheked = gc_bounds_maker(gc_bounds)
    length_bounds_cheked = len_bounds_maker(length_bounds)

    # End programm if something wrong with bonds or quality
    if not gc_bounds_cheked or not length_bounds_cheked:
        return

    # Start reading input file and filtering it
    read_fatsq_for_filter(input_fastq, gc_bounds_cheked, length_bounds_cheked, quality_threshold, 
               output_file_prefix, save_filtered)


if __name__ == '__main__':
    """
    Show help message: -h, -- help
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input_fastq", help="path to fastq file for filter")
    parser.add_argument("-o", "--outpref", help="path prefix of file to which the result will be written")

    parser.add_argument("-g", "--gc_bounds", nargs='*', default=[0, 100], 
                        help="the GC interval of the composition (in percents) for filtering (default is (0, 100) - all reads are saved)")
    parser.add_argument("-l", "--length_bounds", nargs='*', default=[0, 2**32], 
                        help="filtering length interval. Default is (0, 2**32)")

    parser.add_argument("-q", "--quality_threshold", default=0, type=int,
                        help="threshold value of average read quality for filtering. Default is 0 (phred33 scale)")
    parser.add_argument("-s", "--save_filtered", default=False, type=bool,
                        help="whether to save filtered reads. Default - False")

    args = parser.parse_args()

    main(input_fastq=args.input_fastq, output_file_prefix=args.outpref, 
         gc_bounds=args.gc_bounds, length_bounds=args.length_bounds, 
         quality_threshold=args.quality_threshold, 
         save_filtered=args.save_filtered)
