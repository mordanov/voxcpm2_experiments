
import sys
import torch
import soundfile as sf
from voxcpm import VoxCPM

print("MPS available:", torch.backends.mps.is_available())

model = VoxCPM.from_pretrained(
    "openbmb/VoxCPM2",
    device="mps",
    load_denoiser=False,
    optimize=False,
)

input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(input_file, "r") as f:
    content = f.read()

sections = [s.strip() for s in content.split("----") if s.strip()]

for i, text in enumerate(sections):
    audio = model.generate(
        text=text,
        cfg_value=2.0,
        inference_timesteps=10,
    )
    out = f"output_{i + 1}.wav"
    sf.write(out, audio, model.tts_model.sample_rate)
    print(f"Saved {out}")

