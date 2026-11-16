import os

# 🔹 Set your target folder where you want to save files
target_dir = "../usr/local/envs/internimage2/lib/python3.7/site-packages/mmseg/datasets"

# Make sure the folder exists
# os.makedirs(target_dir, exist_ok=True)

# Define contents for each file
files_content = {
    "All_Disease.py": """# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp
import mmcv
import numpy as np
from mmcv.utils import print_log
from PIL import Image
from .builder import DATASETS
from .custom import CustomDataset

@DATASETS.register_module()
class All_DiseaseDataset(CustomDataset):

    CLASSES = (
        'Background','rust','rot','mosaic','scab','spot','downy_mildew',
        'blight','anthracnose','mold','powdery_mildew','blotch','smut',
        'leaf_streak','leaf_curl','scorch','bacterial_wilt','blast',
        "pocket_disease","leafroll","blueberry_mummy"
    )

    PALETTE = [
        [0, 0, 0],[128, 0, 0],[0, 128, 0],[128, 128, 0],[0, 0, 128],
        [128, 0, 128],[0, 128, 128],[128, 128, 128],[255, 0, 0],[0, 255, 0],
        [0, 0, 255],[255, 255, 0],[255, 0, 255],[0, 255, 255],
        [192, 128, 0],[0, 64, 128],[128, 64, 0],[64, 0, 128],
        [60, 120, 180],[180, 60, 120],[120, 180, 60]
    ]

    def __init__(self,img_suffix='.jpg',seg_map_suffix='.png',**kwargs):
        super().__init__(img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",

    "RiceDisease.py": """# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp
import mmcv
import numpy as np
from mmcv.utils import print_log
from PIL import Image
from .builder import DATASETS
from .custom import CustomDataset

@DATASETS.register_module()
class RiceDiseaseDataset(CustomDataset):

    CLASSES = ("Background","rice_blast","rice_blight","rice_brownspot")

    PALETTE = [
        [0, 0, 0],[255, 0, 0],[0, 255, 0],[0, 0, 255]
    ]

    def __init__(self,img_suffix='.jpg',seg_map_suffix='.png',**kwargs):
        super().__init__(img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",

    "SoybeanDisease.py": """# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp
import mmcv
import numpy as np
from mmcv.utils import print_log
from PIL import Image
from .builder import DATASETS
from .custom import CustomDataset

@DATASETS.register_module()
class SoybeanDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background","soybean_bacterial_blight","soybean_brown_spot",
        "soybean_downy_mildew","soybean_frog_eye_leaf_spot",
        "soybean_mosaic","soybean_rust"
    )

    PALETTE = [
        [0, 0, 0],[255, 0, 0],[0, 255, 0],[0, 0, 255],
        [255, 255, 0],[255, 0, 255],[0, 255, 255]
    ]

    def __init__(self,img_suffix='.jpg',seg_map_suffix='.png',**kwargs):
        super().__init__(img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "CornDisease.py": """
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
class CornDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "corn_gray_leaf_spot",
        "corn_northern_leaf_blight",
        "corn_rust",
        "corn_smut"
    )


    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [255, 255, 0]
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "BananaDisease.py":  """# Copyright (c) OpenMMLab. All rights reserved.
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
class BananaDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "banana_anthracnose",
        "banana_black_leaf_streak",
        "banana_bunchy_top",
        "banana_cigar_end_rot",
        "banana_cordana_leaf_spot",
        "banana_panama_disease",
    )


    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [255, 255, 0],
        [255, 0, 255],
        [0, 255, 255]
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "PotatoDisease.py": """
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
class PotatoDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "potato_early_blight",
        "potato_late_blight"
    )


    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],
        [0, 255, 0]

    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "AppleDisease.py": """
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
class AppleDiseaseDataset(CustomDataset):

    CLASSES = (
        'Background',
        'apple_black_rot',
        'apple_mosaic_virus',
        'apple_rust',
        'apple_scab'
    )

    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],      # apple_black_rot
        [0, 255, 0],      # apple_mosaic_virus
        [0, 0, 255],      # apple_rust
        [255, 255, 0]     # apple_scab
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "GrapesDisease.py": """
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
class GrapesDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "grape_black_rot",
        "grape_downy_mildew",
        "grape_leaf_spot",
        "grapevine_leafroll_disease"
    )

    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],      # apple_black_rot
        [0, 255, 0],      # apple_mosaic_virus
        [0, 0, 255],      # apple_rust
        [255, 255, 0]     # apple_scab
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "WheatDisease.py": """
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
class WheatDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "wheat_bacterial_leaf_streak_(black_chaff)", "wheat_head_scab",
        "wheat_leaf_rust",
        "wheat_loose_smut",
        "wheat_powdery_mildew",
        "wheat_septoria_blotch",
        "wheat_stem_rust",
        "wheat_stripe_rust"
    )


    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [255, 255, 0],
        [255, 0, 255],
        [0, 255, 255],
        [180, 200, 120],
        [120, 200, 180]
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "TomatoDisease.py": """
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
class TomatoDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "tomato_bacterial_leaf_spot",
        "tomato_early_blight",
        "tomato_late_blight",
        "tomato_leaf_mold",
        "tomato_mosaic_virus",
        "tomato_septoria_leaf_spot",
        "tomato_yellow_leaf_curl_virus",
    )


    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [255, 255, 0],
        [255, 0, 255],
        [0, 255, 255],
        [180, 200, 120],
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "CabbageDisease.py": """
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
class CabbageDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "cabbage_alternaria_leaf_spot",
        "cabbage_black_rot",
        "cabbage_downy_mildew"
    )

    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],      # apple_black_rot
        [0, 255, 0],      # apple_mosaic_virus
        [0, 0, 255]      # apple_rust
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "BeanDisease.py": """
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
class BeanDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "bean_halo_blight",
        "bean_mosaic_virus",
        "bean_rust"

    )

    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],      # apple_black_rot
        [0, 255, 0],      # apple_mosaic_virus
        [0, 0, 255]      # apple_rust
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
""",
      "CucumberDisease.py": """
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
class CucumberDiseaseDataset(CustomDataset):

    CLASSES = (
        "Background",
        "cucumber_angular_leaf_spot",
        "cucumber_bacterial_wilt",
        "cucumber_powdery_mildew"

    )

    PALETTE = [
        [0, 0, 0],        # Background
        [255, 0, 0],      # apple_black_rot
        [0, 255, 0],      # apple_mosaic_virus
        [0, 0, 255]      # apple_rust
    ]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
"""
}


# 🔹 Write files
for filename, content in files_content.items():
    file_path = os.path.join(target_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)
    print(f"✅ Created: {file_path}")
