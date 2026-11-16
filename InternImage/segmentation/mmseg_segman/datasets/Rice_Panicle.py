# Copyright (c) OpenMMLab. All rights reserved.
# from mmseg.registry import DATASETS
# from .basesegdataset import BaseSegDataset
import os.path as osp

import mmcv
import numpy as np
from mmcv.utils import print_log
from PIL import Image

from .builder import DATASETS
from .custom import CustomDataset

@DATASETS.register_module()
class Rice_PanicleDataset(CustomDataset):

# 0: (0, 0, 0),       # Background (Black)
# 1: (255, 255, 255),     # Panicle (White)



    CLASSES =('Background', 'Panicle')

    PALETTE=[[0, 0, 0], [255, 255, 255]]

    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)

