@qiime.register_method("Build tree")
def build_tree(alignment: Alignment("the multiple sequence alignment") or None,
               dm: DistanceMatrix("the distance matrix") or None,
               method: ChooseOne("the method to use for phylogenetic reconstruction",
                                 String,
                                 ['neighbor-join', 'FastTree']) = 'FastTree')
    raise NotImplementedError
