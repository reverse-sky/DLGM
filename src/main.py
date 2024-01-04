import os
import torch
import warnings
import torch
torch.cuda.empty_cache()
import hydra
from omegaconf import DictConfig
# from pytorch_lightning import Trainer
# from pytorch_lightning.callbacks import ModelCheckpoint
# from pytorch_lightning.utilities.warnings import PossibleUserWarning

# from src import utils
# from metrics.abstract_metrics import TrainAbstractMetricsDiscrete, TrainAbstractMetrics

# from diffusion_model import LiftedDenoisingDiffusion
# from diffusion_model_discrete import DiscreteDenoisingDiffusion
# from diffusion.extra_features import DummyExtraFeatures, ExtraFeatures

#DictConfig를 사용하면 cfg에 직접 접근할 수 있음 
@hydra.main(version_base='1.3', config_path='../configs', config_name='config')
def main(cfg:DictConfig):
