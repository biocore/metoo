@qiime.register_method("Build tree")
def build_tree(alignment: Alignment("the multiple sequence alignment") or None,
               dm: DistanceMatrix("the distance matrix") or None,
               method: ChooseOne("the method to use for phylogenetic reconstruction",
                                 String,
                                 ['neighbor-join', 'FastTree']) = 'FastTree')
    raise NotImplementedError

@qiime.register("De novo sequence clustering")
@framework.parameter('sequences', DemultiplexedSequences, help='')
@framework.parameter('method', ClusteringMethod, help='')
@framework.parameter('similarly', Float, help='')
@framework.result('otu_map', OtuMap, help='')
def de_novo_cluster_sequences(sequences, method, similarity):
    return OtuMap

@qiime.register("Closed-reference sequence clustering")
@framework.parameter('sequences', DemultiplexedSequences, help='')
@framework.parameter('reference_sequences', DemultiplexedSequences, help='')
@framework.parameter('method', ClusteringMethod, help='')
@framework.parameter('similarly', Float, help='')
@framework.result('otu_map', OtuMap, help='')
@framework.result('failures', DemultiplexedSequences,
                  help='Sequences that failed to hit the reference')
def closed_reference_cluster_sequences(sequences, reference_sequences, method, similarity):
    return OtuMap, DemultiplexedSequences

@qiime.register("open-reference sequence clustering")
@framework.parameter('sequences', DemultiplexedSequences, help='')
@framework.parameter('reference_sequences', DemultiplexedSequences, help='')
@framework.parameter('method', ClusteringMethod, help='')
@framework.parameter('similarly', Float, help='')
@framework.result('otu_map', OtuMap, help='')
help='Sequences that failed to hit the reference')
def open_reference_cluster_sequences(sequences, reference_sequences, method, similarity):
    closed_reference_otu_map, closed_reference_failures = \
        closed_reference_cluster_sequences(sequences, reference_sequences, method, similarity)
    open_reference_otu_map = de_novo_cluster_sequences(
     closed_reference_failures, method, similarity)
    result = _merge_otu_maps([closed_reference_otu_map, open_reference_otu_map])
    return result


@framework.result('otu_map', OtuMap, help='')
def _merge_otu_maps(otu_maps):
    return OtuMap
