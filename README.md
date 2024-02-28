# mDELTA_prepro: Preprocess real data for quantitative and qualitative file options in mdelta input

<a href="https://github.com/Chenjy0212/mdelta_full/blob/main/image/mDELTA.png"><img src="prepro.png" height="500" align="right" /></a>

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/DecryptLogin?logo=python&labelColor=white)](https://pypi.org/project/mdelta/)
[![Jupyter](https://img.shields.io/badge/-Jupyter-ffffff?logo=jupyter)](https://jupyter.org/)
[![r](https://img.shields.io/badge/-Rcript-blue?logo=R)](https://www.r-project.org/)

- **`mDELTA`** is an algorithm for **m**ultifuricating **D**evelopmental c**E**ll **L**ineage **T**ree **A**lignment. In essence, it compares two rooted, unordered, tip-labeled trees, and finds the best global ｜ local correspondence between the nodes. The **mDELTA** program is designed for analyzing developmental cell lineage trees
  reconstructed through single-cell DNA barcoding (such as done by
  **`scGESTALT`** or **`SMALT`**, while greater cellular coverage is expected to
  yield more meaningful **mDELTA** alignments).

- Except for dealing with cell lineage trees instead of biological
  sequences, **mDELTA** is conceptually similar to sequence alignment.
  It helps quantify similarity among different lineage trees,
  disentangle the consensus and variation, find recurrent motifs, and
  facilitate comparative/evolutionary analyses.

- Also included in this repository are Python/R scripts for
  statistical analyses and visualization of **mDELTA** results, which
  facilitates their biological interpretation.

- **mDELTA** was developed by Jingyu Chen (EeWhile) under the supervision of
  Professor Jian-Rong Yang at the Zhongshan School of Medicine of Sun
  Yat-Sen University in China.

For more details, please visit

> - You can try to learn about the latest examples of dynamic mDELTA running results, which will help you better understand the purpose of mDERTA ⚙️
>   <http://eewhile.cn/mdelta_ui>
>
> ![mdelta_ui](./image/mdelta_ui.png)
>
> - You can obtain a separate Python package for mDELTA for further development
>   <https://github.com/Chenjy0212/mdelta>

If you have any questions, please contact me. My contact information is located at the bottom

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Chenjy0212&repo=mdelta_full)](https://github.com/Chenjy0212/mdelta_full)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Chenjy0212&repo=mdelta)](https://github.com/Chenjy0212/mdelta)

# Before you begin ⚠️

1. It's best to use **jupyter** as your menu display tool, or you can install the corresponding plugin in **vscode** to use it.
2. You can install the required packages automatically by running **`mdelta_menu.ipynb`**, or you can manually run the **`package_manger.py`** to install the required packages.
   > **Tips** : The first download time may be relatively long. If any installation package fails, please go ahead and install a package that is suitable for your current running environment (Python and R)
3. You should first install stable versions of **`Python`** and **`R`** language to facilitate subsequent operations
