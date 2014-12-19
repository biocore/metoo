from skbio import BiologicalSequence

import metoo.examples as examples
from metoo.types import RawSequences, QualityFilteredSequences, SampleMetadata
import metoo.framework as framework
from metoo import qiime

@qiime.register("Join paired sequences")
@framework.parameter('prime5_sequences', RawSequences, help='')
@framework.parameter('prime3_sequences', RawSequences, help='')
@framework.result('joined_sequences', RawSequences, help='')
@framework.raises(ValueError, when='Shit happens')
@framework.notes('asd')
@framework.see_also(foo, bar)
@framework.example("Do the stuff",
                   prime5_sequences=examples.foo,
                   prime3_sequences=examples.bar,
                   example_result=examples.stuff)
def join_sequences(prime5_sequences, prime3_sequences):
    """UI agnostic description of method

    blah blah blah
    """
    return RawSequences('')


@framework.register("Demultiplex sequences")
@framework.parameter('sequences', RawSequences, help='')
@framework.parameter('barcodes', RawSequences, help='')
@framework.parameter('barcode_map', SampleMetadata, help='')
@framework.result('demultiplexed_sequences', help='')
def demux_sequences(sequences, barcodes, barcode_map):
    yield BiologicalSequence('')


@framework.register("Quality filter sequences")
@framework.parameter('sequences', RawSequences, help='')
@framework.parameter('barcodes', RawSequences, help='')
@framework.result('demultiplexed_sequences', QualityFilteredSequences, help='')
def quality_filter_sequences(sequences, barcodes):
    return BiologicalSequence('')
