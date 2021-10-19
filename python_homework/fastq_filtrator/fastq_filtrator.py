# Simple fastq filtrator
# run the .py file with flag -h in terminal for help

import argparse


def check_bound(bound):
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


def make_len_bounds(length_bounds):
    '''
    Check types, number of values in length_bounds.
    Transform it to [float, float].
    '''

    normalized_length_bound = check_bound(length_bounds)

    if not normalized_length_bound:
        return

    # add lower bound to normalized_length_bounds
    if len(normalized_length_bound) == 1:
        return [0, normalized_length_bound[0]]

    return normalized_length_bound


def make_gc_bounds(gc_bounds):
    '''
    Check types, number of values in gc_bonus.
    Transform it to [float, float].
    '''

    normalized_gc_bound = check_bound(gc_bounds)

    if not normalized_gc_bound:
        return

    # add lower bound to normalized_gc_bounds
    if len(normalized_gc_bound) == 1:
        return [0, normalized_gc_bound[0]]

    return normalized_gc_bound


def filter_gc(seq_line, read_len, gc_bounds):
    '''
    Filter the read by GC content (in percent)
    '''
    gc_number = seq_line.count('C') + seq_line.count('G')
    gc_content = 100 * gc_number / read_len

    if gc_content < gc_bounds[0] or gc_content > gc_bounds[1]:
        return False

    return True


def filter_length(read_len, length_bounds):
    '''
    Filter the read by length.
    '''
    if read_len < length_bounds[0] or read_len > length_bounds[1]:
        return False

    return True


def filter_quality(read_len, quality_line, quality_threshold):
    '''
    Filter the read by quality
    '''
    quality = 0

    for character in quality_line:
        quality += (ord(character) - 33)

    average_quality = quality / read_len

    if average_quality < quality_threshold:
        return False

    return True


def filter_fastq(lines, gc_bounds, length_bounds, quality_threshold):
    '''
    Check the quality for each read in fastq file.
    If passed - return True, else - False.
    '''
    seq_line = lines[1][::-2]
    quality_line = lines[3][::-2]
    read_len = len(seq_line)

    # filter the read by GC content
    if gc_bounds != [0, 100]:
        if not filter_gc(seq_line, read_len, gc_bounds):
            return False

    # filter the read by length
    if not filter_length(read_len, length_bounds):
        return False

    # filter the read by quality
    if quality_threshold != 0:
        if not filter_quality(read_len, quality_line, quality_threshold):
            return False

    # True if the read passed filtration
    return True


def write_filtered_fastq(lines, quality_result, save_filtered, wons, wonf):
    '''
    Write (to the end of file) each read to the passed or (if needed) failed file.
    '''
    if quality_result:
        wons.writelines(lines)

    else:
        if save_filtered:
            wonf.writelines(lines)


def read_fatsq_for_filter(input_fastq, gc_bounds, length_bounds, quality_threshold,
                          output_file_prefix, save_filtered, read_len=4):
    """
    Reads four lines from a fastq file and passes them to filter and write function.
    """
    read_from = open(input_fastq, 'r')
    write_on_success_to = open(output_file_prefix + '_passed.fastq', 'w')
    write_on_fail_to = None

    if save_filtered:
        write_on_fail_to = open(output_file_prefix + '_failed.fastq', 'w')

    try:
        while True:

            try:
                lines = [next(read_from) for x in range(read_len)]
                quality_result = filter_fastq(lines, gc_bounds, length_bounds, quality_threshold)

                # Write out fastq file after filter
                write_filtered_fastq(lines,
                                     quality_result,
                                     save_filtered,
                                     wons=write_on_success_to,
                                     wonf=write_on_fail_to)

            except StopIteration:
                return

    finally:
        read_from.close()
        write_on_success_to.close()
        
        if write_on_fail_to:
            write_on_fail_to.close()


def main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered):

    # Check bounds and update it
    gc_bounds_cheked = make_gc_bounds(gc_bounds)
    length_bounds_cheked = make_len_bounds(length_bounds)

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

    parser.add_argument("-i", "--input-fastq", help="path to fastq file for filter")
    parser.add_argument("-o", "--outpref", help="path prefix of file to which the result will be written")

    parser.add_argument("-g", "--gc-bounds", nargs='*', default=[0, 100],
                        help="the GC interval (in percents) for filtering (default (0, 100))")
    parser.add_argument("-l", "--length-bounds", nargs='*', default=[0, 2**32],
                        help="filtering length interval. Default is (0, 2**32)")

    parser.add_argument("-q", "--quality-threshold", default=0, type=int,
                        help="threshold value of average read quality for filtering. Default is 0 (phred33 scale)")
    parser.add_argument("-s", "--save-filtered", default=False, type=bool,
                        help="whether to save filtered reads. Default - False")

    args = parser.parse_args()

    main(input_fastq=args.input_fastq,
         output_file_prefix=args.outpref,
         gc_bounds=args.gc_bounds,
         length_bounds=args.length_bounds,
         quality_threshold=args.quality_threshold,
         save_filtered=args.save_filtered)
