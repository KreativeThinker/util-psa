# 🧠 util-psa

Spectral chunk-based analysis of rat EEG data during REM and NREM sleep.

## Project Structure

```
util-psa/
├── config.py               # configuration file for the project
├── data/                   # Data folder
│   ├── raw/                # Raw input data from recordings
│   ├── input/              # Cleaned + transposed cFFT files
│   └── output/             # Final analysis results
├── LICENSE
├── main.py
├── pyproject.toml
├── README.md
├── src/                    # Source code for the project
│   └── files/
│       ├── include.py
│       └── __init__.py
└── uv.lock
```

## 🧪 Workflow

1. **Extract `Traces_cFFT.csv`**
   From: `data/raw/{animal}/{baseline|test}/`

2. **Clean files**

   - Remove first 20 lines (metadata)
   - Save to: `data/input/{animal}/{baseline|test}/`

3. **Preprocess**

   - Transpose CSV
   - Sort by 2nd column (R, NR, W)
   - Drop rows with 'W'

4. **Split**

   - Save REM and NREM to:
     `data/output/{animal}/{rem|nrem}/original/{baseline|test}/`

5. **Chunk by time**

   - Save to:
     `data/output/{animal}/{rem|nrem}/chunked/{baseline|test}_{chunk_num}`

6. **Per-chunk analysis**

   - Average frequency across epochs
   - Combine across baseline/test into:
     `data/output/{animal}/{rem|nrem}/chunked/{chunk_num}_raw`

7. **Normalize**

   - Normalize per-frequency
   - Then normalize w.r.t BL1
   - Save to:
     `data/output/{animal}/{rem|nrem}/chunked/{chunk_num}_norm`
