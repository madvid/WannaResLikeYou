1. Traditional Interpolation Methods

    Nearest Neighbor Interpolation:
        Simplest form of interpolation that assigns the nearest pixel value to the new pixel.
        Fast but can lead to blocky images, especially at higher scaling factors.
    Bilinear Interpolation:
        Considers the closest 2x2 neighborhood of known pixel values surrounding the unknown pixel.
        Averages the four nearest pixels, resulting in smoother images than nearest neighbor but can still blur edges.
    Bicubic Interpolation:
        Considers the closest 4x4 neighborhood of known pixel values.
        Produces smoother and sharper images than bilinear, with better edge preservation, but at a higher computational cost.
    Spline Interpolation:
        Uses polynomial functions to interpolate between pixels, resulting in smooth curves.
        Can preserve more detail and sharpness but can be computationally expensive.

2. Edge-Directed Interpolation

    New Edge-Directed Interpolation (NEDI):
        Aims to preserve edges by adjusting the interpolation process based on local edge directions.
        Improves image sharpness, especially along edges, but can be more complex to implement.
    Iterative Back Projection (IBP):
        Iteratively refines an image by comparing the downsampled image with the original lower-resolution image, focusing on maintaining edge detail.
        This iterative process can produce high-quality images but is computationally intensive.


# Image Interpolation Feature
## Overview

The `interpolate` feature allows users to apply different interpolation methods to images using OpenCV. This feature supports four interpolation methods: **linear**, **nearest**, **cubic**, and **lanczos4**. It can be used to scale images by specific x and y factors.

This feature can be accessed via the `interpolate` entry point, which accepts an input image, a configuration file specifying the interpolation method and scaling factors, and generates an output image.

## Supported Interpolation Methods

**Linear interpolation**: Suitable for simple resizing tasks with minimal image distortion.
**Nearest-neighbor interpolation**: Fastest method, best for categorical images but can result in pixelated edges.
**Cubic interpolation**: Produces smoother images with better quality when upscaling.
**Lanczos interpolation**: A high-quality downsampling and upscaling method that preserves fine details in the image.

---

## Usage

The entry point for using this feature is `interpolate.py`. Below is the detailed usage information:

```bash
usage: interpolate.py [-h] --input INPUT --output OUTPUT [--overwrite OVERWRITE] --config CONFIG

options:
  -h, --help            Show this help message and exit.
  --input INPUT, -i INPUT
                        Path to the input image.
  --output OUTPUT, -o OUTPUT
                        Path to the output image.
  --overwrite OVERWRITE, -f OVERWRITE
                        Flag to allow overwriting the output file.
  --config CONFIG, -c CONFIG
                        Path to the configuration file specifying interpolation parameters.
```

## Example

```bash
python interpolate.py --input image.jpg --output resized_image.png --config config.json
```

In this example:

* `--input` is the path to the source image to be interpolated.
* `--output` is the path where the resized image will be saved.
* `--config` points to a configuration file specifying the interpolation method and scaling factors (described below).


### Input image example
![](../../../examples/sources/origines_du_lindy_hop.jpeg)


### Output image example
![](../../../examples/sources/origines_du_lindy_hop.jpeg)