# Setup

git clone https://github.com/Ishan1819/OpenCV-Fundamentals---Week1.git

Create venv (optional):

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate


# Install deps:

pip install -r requirements.txt

# Run the code by:

cd <go inside the directory whose code to be run>
python <filename.py>

# Topics Covered (short notes)

1) Introduction to OpenCV

2) Core Module (core)

3) Image Processing (imgproc)

4) Application Utils (highgui, imgcodecs, videoio)

5) Camera Calibration & 3D (calib3d)

6) Object Detection (objdetect)

7) 2D Features (feature2d)

8) Deep Neural Networks (dnn)

9) Graph API (G-API)

10) Other Tutorials (ml, photo, stitching, video)

11) Theory (pixels, color, convolution, edges, Fourier)

# Research (Misc)

Image Processing Concepts – quick take

Filtering: smooth noise or sharpen details.

Thresholding: separate foreground/background.

Transforms: rotate, scale, warp for alignment and effects.

Use cases: face blur in news, cleaning medical scans, document cleanup.

OpenCV Applications – examples

Robotics: obstacle detection, path following.

Medical: MRI/X-ray analysis.

Autonomous: lane/pedestrian/car detection.

Surveillance: motion/people detection.

AR: overlay graphics on real world.

Inspection: defect detection on assembly line.

Docs: scan + crop + OCR.

Face ID: attendance, door access.

Gestures: control with hand signs.

Windows vs Linux – OpenCV Windows

On Windows, GUI (imshow) should run in main thread. Else windows may freeze.

On Linux, a bit more forgiving, still better to keep GUI on main thread.

waitKey() is important to keep window responsive.

If GUI is missing, save images to file or use Matplotlib to display.

# References

OpenCV Docs (4.x): https://docs.opencv.org/4.x/d9/df8/tutorial_root.html

YouTube playlist (study): https://www.youtube.com/playlist?list=PLjMXczUzEYcHvw5YYSU92WrY8IwhTuq7p

Extra reads: pjreddie GitHub exercises (for practice ideas), ChatGPT references.

# Report (PDF)

File: OpenCV Fundamentals - Week1 (1).pdf in repo root.

It includes:

sources per topic,

key learnings + insights,

summary of code work and results.

(You can export your .docx notes to PDF, or combine them into one PDF as per manager.)

# Notes

If cv2.imshow fails on some Windows setups, save output to file or use Matplotlib to show.

Haar cascades are fast but may miss cases; deep models are better for accuracy.

When stitching fails, ensure 30–50% overlap and good texture.

OCR works better after grayscale + slight blur or threshold.
