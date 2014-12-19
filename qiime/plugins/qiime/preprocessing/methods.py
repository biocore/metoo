from skbio import BiologicalSequence

import metoo.examples as examples
from metoo.types import RawSequences, QualityFilteredSequences, SampleMetadata
import metoo.framework as method
from metoo import qiime

@qiime.method
@method.deprecated("2.1.0",
                   "This will be replaced with skbio.join_sequences.")
@method.parameter('prime5_sequences', RawSequences, help='')
@method.parameter('prime3_sequences', RawSequences, help='')
@method.result('joined_sequences', RawSequences, help='')
@method.raises(ValueError, "IDs aren't consistent between the files")
@method.note('Joining paired ends can improve the specificity of taxonomic '
             'assignment and OTU definition.')
@method.reference('https://code.google.com/p/ea-utils/wiki/FastqJoin')
@method.see_also('demux_sequences')
@method.see_also('quality_filter_sequences')
@method.example("Join five and three prime reads.",
                prime5_sequences=examples.foo,
                prime3_sequences=examples.bar,
                example_result=examples.stuff)
def join_sequences(prime5_sequences, prime3_sequences):
    """Join paired sequences

    This allows users to join paired end reads, as is often generated on the
    Illumina instruments.
    """
    return RawSequences('')


@qiime.method
@method.parameter('sequences', RawSequences, help='')
@method.parameter('barcodes', RawSequences, help='')
@method.parameter('barcode_map', SampleMetadata, help='')
@method.result('result', DemultiplexResult, help='')
def demux_sequences(sequences, barcodes, barcode_map):
    """Demultiplex sequences
    """
    result = DemultiplexResult()
    for sequence, barcode in zip(sequences, barcodes):
        try:
            sample_id = _dumux_sequence(barcode, barcode_map)
            result.successes[sample_id].add(sequence)
        except KeyError:
            bad_barcode_count += 1
            result.failures.add(sequence)
            result.bad_barcode_count += 1
    return result
#
#
# @method.parameter('barcode', RawSequence, help='')
# @method.parameter('barcode_map', SampleMetadata, help='')
# @method.raises(KeyError, "barcode is not in barcode_map")
# def _dumux_sequence(barcode, barcode_map):
#     """Demultiplex sequence
#     """
#     return barcode_map[barcode]
#
#
#
#     @method.parameter('max_bad_run_length', Range(Integer, 0, None),
#     help='max number of consecutive low quality base calls '
#     'allowed before truncating a read', default=3)
#     @method.parameter('min_per_read_length_fraction', Range(Float, 0.0, 1.0),
#     help='min number of consecutive high quality base calls to '
#     'include a read (per single end read) as a fraction of '
#     'the input read length', default=0.75)
#     @method.parameter('sequence_max_n', Range(Integer, 0, None),
#     help='maximum number of N characters allowed in a sequence '
#     'to retain it -- this is applied after quality '
#     'trimming, and is total over combined paired end reads '
#     'if applicable', default=0)
#     @method.parameter('start_seq_id', Range(Integer, 0, None),
#     help='start seq_ids as ascending integers beginning with '
#     'start_seq_id', default=0)
#
#
#
# @method.register("Quality filter sequences")
# @method.parameter('sequences', RawSequences, help='')
# @method.parameter('barcodes', RawSequences, help='')
# @method.result('demultiplexed_sequences', QualityFilteredSequences, help='')
# def quality_filter_sequences(sequences, barcodes):
#     return BiologicalSequence('')
