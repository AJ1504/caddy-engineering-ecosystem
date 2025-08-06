from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/image-to-cad/")
async def image_to_cad(file: UploadFile = File(...)):
    # TODO: Integrate ControlNet/MiDaS to generate primitives from image
    # For now, return mocked JSON schema example
    return {
        "object_analysis": "Mocked primitive shapes from uploaded image",
        "components": [
            {
                "name": "box1",
                "type": "box",
                "material": "plastic",
                "dimensions": {"width": 30, "height": 20, "depth": 15},
                "position": {"x": 0, "y": 10, "z": 0},
                "rotation": {"x": 0, "y": 0, "z": 0},
            }
        ],
    }
