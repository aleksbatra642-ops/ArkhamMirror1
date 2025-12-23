import os
import sys

# =============================================================================
# WINDOWS CONSOLE FIX FOR REFLEX BACKEND
# =============================================================================
# When running under Reflex's backend context on Windows, stderr/stdout may be
# redirected in ways that cause "OSError: [Errno 22] Invalid argument" when
# libraries try to write progress bars or use tqdm.
#
# This comprehensive fix disables all progress bars and advisory warnings
# BEFORE any HuggingFace/transformers imports occur.
# =============================================================================

# Disable all HuggingFace progress indicators
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Disable tqdm globally for any library that uses it
os.environ["TQDM_DISABLE"] = "1"

# Now safe to import torch and FlagEmbedding
import torch
from FlagEmbedding import BGEM3FlagModel
from .base import EmbeddingProvider


class BGEM3Provider(EmbeddingProvider):
    """
    Provider for BAAI/bge-m3 model.
    Supports multilingual dense embeddings (1024 dim) and native sparse lexical weights.
    """

    def __init__(self, model_name: str = "BAAI/bge-m3", device: str = None):
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        print(f"Loading BGE-M3 Model ({model_name}) on {self.device}...")
        self.model = BGEM3FlagModel(
            model_name, use_fp16=(self.device == "cuda"), device=self.device
        )

    @property
    def dense_dimension(self) -> int:
        return 1024

    def encode(self, text: str) -> dict:
        output = self.model.encode(text, return_dense=True, return_sparse=True)
        return {
            "dense": output["dense_vecs"].tolist(),
            "sparse": output["lexical_weights"],
        }
