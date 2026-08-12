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
    "LTXDirectorCS25": LTXDirector,
    "LTXDirectorGuideCS25": LTXDirectorGuide,
    "LTXDirectorCropGuidesCS25": LTXDirectorCropGuides,
    "CleanLatentSliceCS25": CleanLatentSlice,
    "LTXChunkWriterCS25": LTXChunkWriter,
    "LTXChunkAssemblerCS25": LTXChunkAssembler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LTXDirectorCS25": "LTX Director CS (2.5)",
    "LTXDirectorGuideCS25": "LTX Director Guide CS (2.5)",
    "LTXDirectorCropGuidesCS25": "LTX Director Crop Guides CS (2.5)",
    "CleanLatentSliceCS25": "Clean Latent Slice CS (2.5)",
    "LTXChunkWriterCS25": "LTX Chunk Writer CS (2.5)",
    "LTXChunkAssemblerCS25": "LTX Chunk Assembler CS (2.5)",
}

WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
