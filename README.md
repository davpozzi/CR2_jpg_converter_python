# CR2 to JPG Converter

A very basic Python converter for **Canon `.CR2` RAW files to `.JPG`**.

The script takes a folder containing `.CR2` files, converts them to JPEG, and saves the converted images in a separate `converted_in_jpg` folder.

No advanced controls, no color-space management, no exposure adjustments — just a simple CR2 → JPG conversion.

## Features

* Converts Canon `.CR2` RAW files to `.JPG`
* Processes all CR2 files in a selected folder
* Keeps the original CR2 files untouched
* Automatically creates a `converted_in_jpg` folder
* Uses the camera's white balance
* Saves JPGs at quality `95`
* Can be run directly from the command line

## Requirements

* Python 3
* [rawpy](https://pypi.org/project/rawpy/)
* [Pillow](https://pypi.org/project/Pillow/)

Install the dependencies with:

```bash
pip install rawpy Pillow
```

## Usage

Run the script from the terminal and pass the path to the folder containing the CR2 files:

```bash
python script.py "/path/to/your/photos"
```

### Windows

```bash
python script.py "C:\Users\YourName\Pictures\Photos"
```

### macOS / Linux

```bash
python3 script.py "/home/yourname/Pictures/Photos"
```

## Example

Before conversion:

```text
photos/
├── IMG_0001.CR2
├── IMG_0002.CR2
├── IMG_0003.CR2
└── IMG_0004.CR2
```

After running the converter:

```text
photos/
├── IMG_0001.CR2
├── IMG_0002.CR2
├── IMG_0003.CR2
├── IMG_0004.CR2
└── converted_in_jpg/
    ├── IMG_0001.jpg
    ├── IMG_0002.jpg
    ├── IMG_0003.jpg
    └── IMG_0004.jpg
```

The original `.CR2` files are not modified or deleted.

## How It Works

The script uses [`rawpy`](https://github.com/letmaik/rawpy) to read and process the Canon RAW files.

The RAW data is processed using the camera's white balance:

```python
raw.postprocess(use_camera_wb=True)
```

The resulting image is then converted to a Pillow image and saved as JPEG with quality `95`.

## Limitations

This is intentionally a **very simple converter**.

It does **not** provide controls for:

* Color space
* Exposure
* Contrast
* Saturation
* Sharpness
* White balance adjustments
* Tone curves
* Highlight/shadow recovery
* RAW development settings
* Output resolution
* JPEG quality from the command line

The goal is simply to provide a quick and straightforward way to turn Canon CR2 files into usable JPG files.

## License

Feel free to use, modify, and adapt this script for your own needs.
