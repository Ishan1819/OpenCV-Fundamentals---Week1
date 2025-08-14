Setup

Create venv (optional):

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate


Install deps:

pip install -r requirements.txt

Run the code by:

python exercises/hist_plot.py

# blur and sharpen example
python exercises/blur_sharpen.py

# resize / scale
python exercises/resize_transform.py

# bitwise AND/OR/XOR/NOT
python exercises/bitwise_ops.py

# face detection on one image
python exercises/face_detect_image.py --image input.jpg

# multi-cascade detection on an image (face/eyes/car/etc., labels not hardcoded)
python exercises/multi_cascade_image.py --image street.jpg

# YOLO object detection on image
python exercises/yolo_detect_image.py --image scene.jpg

# OCR (print all text to terminal)
python exercises/ocr_easyocr_print.py --image doc.png

# panorama stitch (saves output even if no GUI)
python exercises/image_stitch_basic.py --images img1.jpg img2.jpg

# DeepLabV3 segmentation
python exercises/segmentation_deeplabv3.py --image person.jpg

# MediaPipe hand gestures (webcam)
python exercises/mediapipe_hand_gestures.py

✅ Topics Covered (short notes)
1) Introduction to OpenCV

Sources: OpenCV docs (overview), freeCodeCamp video.

Learned: OpenCV started at Intel (2000), now open-source. Works on Windows/Linux/Mac. Used in C++ or Python. Install in Python via pip install opencv-python.

Key: read/show/save images, handle photos and video, many modules for filters, detection, etc.

2) Core Module (core)

Sources: OpenCV core docs, playlist section.

Learned: base data structures and math ops (Mat / NumPy arrays). Other modules depend on it.

Key: image arrays, basic math, RNG, file I/O helpers.

3) Image Processing (imgproc)

Sources: imgproc docs, blogs on blur/edges.

Learned: filters (blur/sharpen), edges, color spaces (BGR, Gray, HSV), transforms (rotate, resize, warp).

Code: blurring background, changing contrast/brightness, histograms.

4) Application Utils (highgui, imgcodecs, videoio)

Sources: module docs, small YT examples.

Learned: open windows, read/write images, read webcam/video.

Key APIs: imread, imwrite, imshow, VideoCapture, waitKey.

5) Camera Calibration & 3D (calib3d)

Sources: calibration tutorial, chessboard example.

Learned: fix lens distortion, get camera intrinsics/extrinsics, stereo depth via disparity.

Key: remove fisheye, estimate pose, measure 3D distances.

6) Object Detection (objdetect)

Sources: objdetect docs, Haar cascade samples.

Learned: fast classical detectors (Haar/LBP). Works for faces, eyes, cars; needs XML files. Good for simple tasks.

Note: deep models (YOLO/SSD) are more accurate but heavier.

7) 2D Features (feature2d)

Sources: docs on SIFT/ORB, FLANN blog.

Learned: keypoint detection, description, matching. Use for stitching, recognition, tracking.

Names: SIFT, SURF, ORB, FAST; matching with BF/FLANN.

8) Deep Neural Networks (dnn)

Sources: dnn docs, PyImageSearch loading examples.

Learned: load run pre-trained models from TensorFlow, Caffe, ONNX. Do detection, segmentation, etc. CPU works; GPU better.

Files: .pb, .onnx, .caffemodel + config.

9) Graph API (G-API)

Sources: G-API docs, one sample repo.

Learned: build pipelines (like flow chart). OpenCV can optimize backend. Useful when same steps repeat a lot.

10) Other Tutorials (ml, photo, stitching, video)

ml: classic ML models (SVM, KNN) for simple tasks.

photo: denoise, inpaint (repair photos).

stitching: join overlapping images to panorama.

video: motion analysis, trackers.

11) Theory (pixels, color, convolution, edges, Fourier)

Sources: college notes + OpenCV theory pages.

Learned: pixel = smallest unit. color spaces = RGB/HSV/Gray. convolution = filter apply. edges = borders of objects. Fourier = frequency view of image.

🔬 Research (Misc)
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

Sports: player and ball tracking.

Windows vs Linux – OpenCV Windows

On Windows, GUI (imshow) should run in main thread. Else windows may freeze.

On Linux, a bit more forgiving, still better to keep GUI on main thread.

waitKey() is important to keep window responsive.

If GUI is missing, save images to file or use Matplotlib to display.

🖼️ Screenshots / Results

Add your own outputs here, e.g.:

screenshots/hist_example.png

screenshots/faces_detected.png

screenshots/stitched_output.jpg

screenshots/segmentation_mask.png

(Screenshots help in the PDF report.)

📘 References

OpenCV Docs (4.x): https://docs.opencv.org/4.x/d9/df8/tutorial_root.html

YouTube playlist (study): https://www.youtube.com/playlist?list=PLjMXczUzEYcHvw5YYSU92WrY8IwhTuq7p

Extra reads: pjreddie GitHub exercises (for practice ideas)

(Also include any blogs/videos you actually used in research/references.md.)

🧾 Report (PDF)

File: report.pdf in repo root.

It includes:

sources per topic,

key learnings + insights,

screenshots,

small notes on issues faced (e.g., cv2.imshow GUI on Windows),

summary of code work and results.

(You can export your .docx notes to PDF, or combine them into one PDF as per manager.)

✅ Deliverables Checklist

 11 topics covered (notes per topic)

 Codes added under exercises/ (clean, commented)

 requirements.txt present

 Screenshots of results added

 README.md (this file)

 report.pdf (comprehensive report)

🗒️ Notes / Common Issues

If cv2.imshow fails on some Windows setups, save output to file or use Matplotlib to show.

Haar cascades are fast but may miss cases; deep models are better for accuracy.

When stitching fails, ensure 30–50% overlap and good texture.

OCR works better after grayscale + slight blur or threshold.
