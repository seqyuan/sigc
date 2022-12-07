# sigc

# install
`pip install -i https://pypi.org/simple sigc==0.1.15`

# usage
```
import sigc
import scanpy as sc
import anndata as ad
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

kegg_metabolism = sigc.metabolism_sigs(resources='KEGG')
display(kegg_metabolism.head(5))


adata = ad.read_h5ad("/data/THU/srt.h5ad")
df = adata.to_df()
print(df.shape)

sig_mtx = sigc.sigc_score(df, kegg_metabolism, method="AUCell")

adata.obsm["umap"] = adata.obsm["X_umap_harmony"]
sig_adata = ad.AnnData(sig_mtx, obs=adata.obs, obsm=adata.obsm)

sc.pl.umap(sig_adata, color='Glycolysis / Gluconeogenesis')
```

