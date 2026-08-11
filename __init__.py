from .ltx_director import LTXDirector
from .ltx_director_guide import LTXDirectorGuide, LTXDirectorCropGuides
from comfy_api.latest import ComfyExtension, io
from typing_extensions import override
from .latent_slice import CleanLatentSlice
from .ltx_chunk_writer import LTXChunkWriter, LTXChunkAssembler

class PromptRelay(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [
            LTXDirector,
        ]

async def comfy_entrypoint() -> PromptRelay:
    return PromptRelay()

NODE_CLASS_MAPPINGS = {
    "LTXDirectorCS": LTXDirector,
    "LTXDirectorGuideCS": LTXDirectorGuide,
    "LTXDirectorCropGuidesCS": LTXDirectorCropGuides,
    "CleanLatentSliceCS": CleanLatentSlice,
    "LTXChunkWriterCS": LTXChunkWriter,
    "LTXChunkAssemblerCS": LTXChunkAssembler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LTXDirectorCS": "LTX Director CS",
    "LTXDirectorGuideCS": "LTX Director Guide CS",
    "LTXDirectorCropGuidesCS": "LTX Director Crop Guides CS",
    "CleanLatentSliceCS": "Clean Latent Slice CS",
    "LTXChunkWriterCS": "LTX Chunk Writer CS",
    "LTXChunkAssemblerCS": "LTX Chunk Assembler CS",
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
