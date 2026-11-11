
import os
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
reference_wav = sys.argv[2] if len(sys.argv) > 2 else ("test.wav" if os.path.exists("test.wav") else None)

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

sections = [s.strip() for s in content.split("----") if s.strip()]

for i, text in enumerate(sections):
    torch.manual_seed(42)
    audio = model.generate(
        text=text,
        reference_wav_path=reference_wav,
        cfg_value=2.0,
        inference_timesteps=10,
    )
    out = f"output_{i + 1}.wav"
    sf.write(out, audio, model.tts_model.sample_rate)
    if reference_wav is None:
        reference_wav = out
    print(f"Saved {out} (reference_wav={reference_wav})")

