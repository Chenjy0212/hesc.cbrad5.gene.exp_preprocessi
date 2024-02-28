# -- coding: utf-8 --
import ipywidgets as widgets
from ipywidgets import *
from IPython.display import display
from multiprocessing import cpu_count

img1 = open("prepro.png", "rb")
logoimage = img1.read()
logo = widgets.Image(
    value= logoimage,
    format='png',
    width='50%',
    height='auto',
)
display(logo)

def get_default():
    import ipywidgets as widgets

    label = widgets.Label(value="表达量文件：")
    display(label)
    # 创建多选框选项
    # /mnt/data4/disk/zhxyu8/lung_progenitor_diff_lineage/result/fig5/modelta/   xxx   .csv
    # options = ["hesc.cbrad5.gene.exp",
    #            "hesc.cbrad5.gene.exp.PC1.PC2",
    #            "hesc.cbrad5.gene.exp.hvgs",
    #            "hesc.cbrad5.gene.exp.pathway"]
    # # 创建Checkbox组件
    # checkboxes = [widgets.Checkbox(description=option) for option in options]
    # mycheckboxes = widgets.VBox(checkboxes)
    # # 或者显示复选框
    
    # layout = widgets.Layout(width='50%')
    # mytextarea = widgets.Textarea(
    #     # value='Hello World',
    #     placeholder='输入文件相对或者绝对路径，用“,”隔开，可输入多个文件',
    #     description='Files:',
    #     disabled=False,
    #     layout=layout
    # )
    # display(mycheckboxes, mytextarea)
    mycheckboxes = widgets.RadioButtons(
        options = ["hesc.cbrad5.gene.exp",
               "hesc.cbrad5.gene.exp.PC1.PC2",
               "hesc.cbrad5.gene.exp.hvgs",
               "hesc.cbrad5.gene.exp.pathway"],
        value="hesc.cbrad5.gene.exp",
        disabled=False,
        # indent=False
    )
    
    layout = widgets.Layout(width='50%')
    mytext2 = widgets.Text(
        # value='Hello World',
        placeholder='输入文件相对或者绝对路径',
        description='File:',
        layout=layout 
    )
    display(mycheckboxes, mytext2)

    
    label2 = widgets.Label(value="Celltype 文件：")
    display(label2)
    # 创建Checkbox组件
    mycheckbox = widgets.Checkbox(
        value=True,
        layout={'width': 'max-content'},
        description="/mnt/data4/disk/zhxyu8/lung_progenitor_diff_lineage/result/fig2/PERMANOVA/all_tree_info_renameCelltype.Rds",
        disabled=False,
        # indent=False
    )
    
    mytext = widgets.Text(
        # value='Hello World',
        placeholder='输入文件相对或者绝对路径',
        description='File:',
        layout=layout 
    )
    display(mycheckbox, mytext)

    cutoff = widgets.FloatRangeSlider(
        value=[15, 85],
        min=0,
        max=100.0,
        step=0.1,
        description='Cutoff (%, 左边为剪枝比例,中间为错配罚分比例,右边为匹配得分比例) :',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
        layout=widgets.Layout(width='80%')
    )
    P1 = widgets.IntSlider(description='放大倍数', min = 0, max= 1000, layout=Layout(width='auto', height='auto'))
    P2 = widgets.IntText(layout=Layout(width='auto', height='auto'))
    P1.value = 1
    jslink((P1, 'value'), (P2, 'value'))
    #合在一起
    P = widgets.VBox([P1, P2])
    
    display(cutoff,P)
        
    label = widgets.Label(value="配对类型：")
    display(label)
    # 创建多选框选项
    # /mnt/data4/disk/zhxyu8/lung_progenitor_diff_lineage/result/fig5/modelta/   xxx   .csv
    optionsw = ["A1-A1",
               "A1-G2",
               "A1-G11",
               "A1-GS",
                "G2-G2",
               "G2-G11",
               "G2-GS",
               "G11-G11",
                "G11-GS",
               "GS-GS",
              ]
    # 创建Checkbox组件
    cc= [widgets.Checkbox(description=optionw) for optionw in optionsw]
    cc[0].value = True
    ccc = widgets.VBox(cc)
    # 或者显示复选框
    
    # 显示SelectMultiple组件
    display(ccc)
        
    return {'checkboxes': mycheckboxes, 
            'text2': mytext2, 
            'checkbox':mycheckbox, 
            'text':mytext,
            'cutoff':cutoff,
            'P':P,
            'ccc':ccc
            }