# Wanna Res' Like You

## Introduction

!!! quote ""
    !!! quote ":simple-openai:"
        Welcome to *Wanna Res Like You* a Python-based super resolution tool designed to bring vintage photos into the high-definition domain.
        Advanced image processing techniques are used to enhances the quality and clarity of historical black-and-white and coloured images, making them vividly sharp and detailed.
        Perfect for reviving classic swing dance photos and other retro snapshots, *Wanna Res Like You* combines the charm of yesteryears with modern image resolution technology. Whether you're a swing dance enthusiast, a history buff, or simply a fan of old-time photography, this tool helps transform nostalgic moments into stunning, high-resolution visuals. Dive in and watch history come to life with unparalleled detail!
    
    !!! quote inline end ":fontawesome-regular-user:"
        thank you chatGPT <3

??? note "Objectives" 
    The objectives of this project are:

    - Manipulating super resolution methods,
    - Learning to build an app in Python,
    - Deploy this app.

??? note "Tech Specs"
    The technical specifications are:

    - Create a CLI,
    - Create an app,
    - Create a tool to easily deploy the app.


## Features
### Interpolation entrypoint

The interpolate feature allows users to apply different interpolation methods to images using OpenCV. This feature supports four interpolation methods: linear, nearest, cubic, and lanczos4. It can be used to scale images by specific x and y factors.

This feature can be accessed via the interpolate entry point, which accepts an input image, a configuration file specifying the interpolation method and scaling factors, and generates an output image.
Supported Interpolation Methods

* **Linear interpolation**: Suitable for simple resizing tasks with minimal image distortion.
* **Nearest-neighbor interpolation**: Fastest method, best for categorical images but can result in pixelated edges.
* **Cubic interpolation**: Produces smoother images with better quality when upscaling.
* **Lanczos interpolation**: A high-quality downsampling and upscaling method that preserves fine details in the image.

See specific documentation for more detailled [Interpolation feature](Users/methods/interpolations.md)


## Installation
### Prerequisites
Lorem ipsum

### Install Instructions
Lorem ipsum

### Setup
Lorem ipsum


## Usage
#### Basic Usage
Lorem ipsum

#### Advanced Usage
Lorem ipsum


## Contributing
Guidelines on how to contribute


## License
Details of the project license


## Acknowledgements
Thanks to contributors and linked resources


## Contact Information
How to get in touch or report issues

## FAQ
- Question 1: Answer
- Question 2: Answer