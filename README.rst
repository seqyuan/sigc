sigc

install
=======

.. code-block:: bash

    pip install sigc

core usage
===========

.. code-block:: python

	import sigc

	kegg_metabolism = sigc.metabolism_sigs(resources='KEGG')
	# other custom also support

	df = pd.read_table("cells_X_genes.mat", header=0, index_col=0)

	sig_mtx = sigc.sigc_score(df, kegg_metabolism, method="AUCell")
	# sig_mtx: cells_X_signatures

signature example
==================

=== =========== ============ =======
    name        description  member
=== =========== ============ =======
0   Glycolysis  00010        HK3
1   Glycolysis  00010        HK1
2   Glycolysis2 describ2     geneX 
=== =========== ============ =======

