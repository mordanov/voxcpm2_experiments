# VoxCPM2 Text-to-Speech

Converts a text file into multiple WAV files using [VoxCPM2](https://huggingface.co/openbmb/VoxCPM2). Each section separated by `----` becomes a separate file.

## Requirements

- Python 3.12
- Apple Silicon Mac (MPS)

## Setup

### 1. Hugging Face token

VoxCPM2 is a gated model. Request access at https://huggingface.co/openbmb/VoxCPM2, then set your token:

```bash
export HF_TOKEN=hf_...
```

Or log in once:

```bash
huggingface-cli login
```

### 2. Install dependencies

```bash
python -m venv voxpy13
source voxpy13/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python text_voxcpm.py input.txt
```

Produces `output_1.wav`, `output_2.wav`, etc. in the current directory.

## Input format

```
First section text here.
----
Second section text here.
----
Third section text here.
```
