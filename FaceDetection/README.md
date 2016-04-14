#How Face Detection Works

The algorithm uses the Viola Jones method of calculating the integral image and then performing some calculations on all the areas defined by the black and white rectangles to analyze the differences between the dark and light regions of a face. The sub-window (in red) is scanned across the image at various scales to detect if there is a potential face within the window. If not, it continues scanning. If it passes all stages in the cascade file, it is marked with a red rectangle. But this does not yet confirm a face. In the post-processing stage all the potential faces are checked for overlaps. Typically, 2 or 3 overlapping rectangles are required to confirm a face. Loner rectangles are rejected as false-positives.

