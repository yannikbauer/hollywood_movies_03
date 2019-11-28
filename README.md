## Info / README

### General movie stimulus info
This is version 3 of the Hollywood movie stimulus, a sequence of randomly selected short 5 s-scene snippets from various movies, to be presented in experiments in the Busse Lab involving in vivo extracellular ephys of awake, head-fixed, behaving mice. Version 1 (for details, see hollywood_movies_01) used the exact same 64x64 pixel frames as in previous retina recordings in the Euler Lab, but at 4 pix/deg, it was found to be to small, covering only 16 deg visual angle. Version 2 was building on that but using the original source files from the Tolias Lab, Houston, for stimulus generation, to contain both high-res 424x264 and low-res 212x132 rectangular frames that can cover the entire stimulus screen and match the original Tübingen frames in terms of spatial frequency content. Version 3 now got rid of the histogram equalization step used in both version 1 and 2, and uses only high-res 424x264 frames that are presented without gamma linearization, at both full-screen and half-screen. Details below.

The source high-res Hollywood movies came from the Tolias Lab, Baylor College of Medicine, Houston, Texas (by Emmanouil Froudarakis, made available by Alex Ecker).

### Details on image frames in Houston, Tübingen and Munich
- Original High-res movies from Houston
  - 8 source movies: Mad Max, The Matrix 1-3, Star Wars 9, Naqoyqatsi, Koyaanisqatsi, Powaqqatsi
    - converted into BW
    - cut into a random sub-selection of scenes of 1 min length
    - 448x252 frames 
    - 30 fps
    - saved as .mov files
- Houston database movies
  - presented to monkeys during V1 recordings
  - downsampled the original high-res 448x252 to 256x144 frames while maintaining the same image content
  - histogram equalized
  - presented at 2 pix/deg (approx. at screen center) on 55x31 cm screen at 15 cm distance -> ca. 120x90º
  - 30 fps
- Tübingen movies
  - presented to mouse retinae during 2P imaging of retinal cells
  - cropped the downsampled 256x144 Houston database movies to 64x64
  - presented at 4 pix/deg -> ca. 16x16º
  - recording field size: 64x64 pixel
  - recording field magnification factor: 0.65
  - 30 fps
  - histogram equalized
  - saved as .tiff and .png files
- Munich movies
  - presented to mouse during dLGN and V1 recordings
  - using a 47x29 cm LCD screen at 25 cm distance
  - Version 1 (older version)
    - used same 64x64 retina movie crops
    - presented at 4 pix/deg on 47x29 cm screen at 25 cm distance -> ca. 16x16º
    - 30 fps
    - histogram equalized
    - saved as .tiff and .avi files
  - Version 2 (older version)
    - 30 fps
    - histogram equalized    
    - used 448x252 high-res frames from Houston and created two stimulus versions to be tested:
      1. low-res 212x132 frames
        - created by downsampling 448x252 high-res frames into 256x144 frames, preserving image content, like in Houston, and cropping to 212x132 to match the dimensions of the 47x29 cm monitor at 25 cm distance
        - if presented @ 2 pix/deg = 106x66º (full-screen): same spatial frequency content & spatial resolution as Houston
        - if presented @ 4 pix/deg = 53x33º (half-screen): same spatial frequency content & spatial resolution as Tuebingen
      2. high-res 424x264
        - created by upsampling 448x252 high-res frames into 512x288 frames, which is twice the size of the downsampled frames in Houston, so that we can use twice the spatial resolution to present the same image content at the same size as in Houston or Tübingen
        - cropped to 424x264 to match the dimensions of the 47x29 cm monitor at 25 cm distance
        - if presented @ 4 pix/deg = 106x66º (full-screen): same spatial frequency content but twice spatial resolution of Houston
        - if presented @ 8 pix/deg = 53x33º (half-screen): same spatial frequency content but twice spatial resolution of Tuebingen
    - In Expo, the degree numbers for the 47x29 cm screen at 25 cm distance are determined not by standard trig assuming a flat screen, but by small-angle approximation      
      - this means that the 106x66º indicated in Expo on a 47x29 cm screen at 25 cm distance would be 86x60º by standard trigonometry
      - this discrepancy is currently accepted because the small angle approximation preserves pixel sizes in the screen center better than standard trig and we decided that we care most about the central pixels, because this is how the pix/deg were calculated in Houston and because this is presumably also closest to the pix/deg-calculation in Tübingen
    - In Expo, we tested both corrected (linearized) and uncorrected (non-linearized) gamma calibration
  - Version 3 (this version)
    - 30 fps
    - NOT histogram equalized    
    - used 448x252 high-res frames from Houston and created one stimulus versions to be tested:
      1. high-res 424x264
        - created by upsampling 448x252 high-res frames into 512x288 frames, which is twice the size of the downsampled frames in Houston, so that we can use twice the spatial resolution to present the same image content at the same size as in Houston or Tübingen
        - cropped to 424x264 to match the dimensions of the 47x29 cm monitor at 25 cm distance
        - if presented @ 4 pix/deg = 106x66º (full-screen): same spatial frequency content but twice spatial resolution of Houston
        - if presented @ 8 pix/deg = 53x33º (half-screen): same spatial frequency content but twice spatial resolution of Tuebingen
    - In Expo, the degree numbers for the 47x29 cm screen at 25 cm distance are determined not by standard trig assuming a flat screen, but by small-angle approximation      
      - this means that the 106x66º indicated in Expo on a 47x29 cm screen at 25 cm distance would be 86x60º by standard trigonometry
      - this discrepancy is currently accepted because the small angle approximation preserves pixel sizes in the screen center better than standard trig and we decided that we care most about the central pixels, because this is how the pix/deg were calculated in Houston and because this is presumably also closest to the pix/deg-calculation in Tübingen
    - In Expo, we do not correct (linearize) gamma, unlike our artificial stimuli, but use uncorrected (non-linearized). Details below in section 'Munich stimulus presentation'.

### Tübingen movie stimulus structure & presentation

The movies have been preprocessed using the JNB 'image_luminance_preprocessing' for histogram equalization.

The movie frame rate is 30 Hz and each scene is 5 s long, resulting in 150 frames per scene.

There is 1 test sequence with 5 test scenes (5 seconds each). Katrin: "The test sequences are always the same. I think we decided to do it like that in order to check the response variance for the same scenes (to test the fraction of explainable variance explained), and because we always wanted to have the same test sequences to compare recordings across batches and animals." The training sequence contains 108 training scenes (5 seconds each) that we play in randomized order. For that, we use 20 random sequences (see file 'RandomSequences.txt') and pick a different one every time we play the movie. 

We play the test scence 3 times, in the beginning, in the middle and at the end. Between those, we play the training sequence. At the beginning and at the end, we have 1 min each of spontaneous activity (to grey screen) with optogenetic pulses, to test for spontaneous opto effects. This results in the following movie stimulus:<br>
**spontaneous opto > test > training part 1 > test > training part 2 > test > spontaneous opto<br>
=> total duration = 60 + 25 + 270 + 25 + 270 + 25 + 60 = 735 s = 12 min 15 s**<br>

In Tübingen, we use QDSpy for stimulus presentation. The input file there is a .png matrix of all the frames, which has been generated from the source .tiff sequence. QDSpy selects the appropriate frames to show from the .png file. For the test .png file, we just follow the whole sequence. For the training .png file, we use one of the random sequences (by re-compiling the stimulus and generating one random number between 1-20 to pick one column from 'RandomSequences.txt'), which QDSpy then presents in the appropriate random order.

### Munich movie stimulus structure

The Munich movies are based directly on the high-res movies from Houston. The movie frame rate is 30 Hz and each scene is 5 s long, resulting in 150 frames per scene. Unlike in Houston and Tübingen, the image frames are NOT preprocessed via histogram equalization anymore in version 3.

Some basic parameters: 
- do_resize = True # resize source images or not
- frame_shape_res = [512, 288] #[256, 144]# shape of resized frame, used only if resizing frames
- frame_shape = [424, 264] # shape of output frames (may be crops from resampled frame, but not larger)
- pix_per_deg = 8 # pixels per degree: 8 in retina experiments; 4 in Houston
- total_dur = 30 # desired total movie sequence duration (min)
- scene_dur = 5 # scene duration (s)
- fps = 30 # framerate of original and output movies (frames per second) -> 150 fpscene
- percent_train = 0.8 # train-test split: 80% training
- percent_test = 0.2 # train-test split: 20% test

- The 30 min movie will be split into 80% training and 20% test scenes, to train an evaluate a convolutional neural network on neural responses.
- The training sequence will contain 288 unique scenes (5 s each), split into 8 parts (each containing 36 scenes à 5 s -> 180 s per training part)
  - the same set of training sequences will be permuted in pseudo-random order in different experimental runs, to avoid order effects. For that, we create 10 different training sequences (see file 'RandomSequences.txt') and pick a different one every time we play the movie.
- The test sequence will contain 8 scenes à 5 s (-> 40 s per test sequence), and the same test sequence will be repeated 9 times, played once before and after the training sequence parts.
  - test scenes are repeated in order to check the response variance for the same scenes (to test the fraction of explainable variance explained), and because we always wanted to have the same test sequences to compare recordings across batches and animals.
- Lastly, for optogenetics experiments, there will be a 1 min period of spontaneous activity (to grey screen) at the beginning and at the end of the experiment, to test for opto effects on spontaneous neural activity.

This results in the following movie stimulus sequence: <br>
**spont opto > te1 > tr1 > te2 > tr2 > ... te8 > tr8 > te9 > spont opto** <br>
**=> total duration = 60 + 9*40 + 8*180 + 60 = 1920 s = 32 min**

See code sections below for calculations for number of scenes, durations and partitions.

### Munich stimulus presentation

The Busse Lab in Munich uses Expo for stimulus presentation (in 2019), and needed to adapt the stimulus accordingly. Instead of creating a .png matrix from the .tiff sequence (as in the Euler Lab, Tuebingen), we present .avi movie files. One .avi is created for the test sequence, but for the training sequences, we generate 10 random sequences of the 288 training scenes, which are split into 8 .avi files around which the test sequence is repeated 9 times. Currently, in each experiment, we manually pick which one of the 10 random sequences to play on expo.
We have now settled on testing only the high-res frames.

The movies are presented on a 47x29 cm Samsung SynMaster 2233. For details on image frames, see above. The gamma calibration on our screen is usually corrected (linearized) for other stimuli. Since movie images are typically recorded with inverse gamma by the camera, we are using the standard uncorrected (non-linearized) gamma calibration of the screen pixel intensities.

### Data & code structure

- Original data:
  - please get the source .mov files by manually downloading (see sources link below) and saving them in "../data/original/"

- "01_convert_mov_to_tiff.ipynb":
  - selects random list from source files and puts them into a test and a training sequence
  - saves image stacks as "../data/processed/hmovTest.tiff" and "../data/processed/hmovTrain.tiff"
  - for reproducibility, the meta data for each scene (source file name, start frame, frame x/y-pos, and first/last index in the .tiff stacks) are saveed in "..data/processed/test_meta.json" and "..data/processed/training_meta.json"

- "02_make_rnd_avi_sequences.ipynb":
  - Converts original .tiff sequence into one test and 10 pseudo-randomized .avi scene sequences.
  - test sequence:
    - saves .tiff stack simply as "../data/processed/hmov_test.avi"
  - training sequence:
    - makes 10 pseudo-random training sequences from the 288 training scenes
      - scene order array (288x10) saved in "..data/processed/RandomSequences.txt"
    - splits each random sequence into 8 parts and save as each part as "../data/processed/hmov_train_[seq#]_[part#].avi"

- utils.py
  - contains functions used in "02_preprocess_image_contrast.ipynb" and "03_make_rnd_avi_sequences.ipynb"

- 'hollymov_opto_03.exxp'
  - file programming details
    - gamma calibration: uncorrected: set Monitor -> calibrate -> linear formula
    - show in 30 Hz: set synchronisation to 'Free Run'
    - expo source file name character limit: 18
  - states
    - spontOpto: presents grey screen for 60 s with 1 s opto pulses (p=0.5) to test opto-effect on spontaneous activity, both at the beginning and the end of the experiment
    - test_opto: presents test movie sequence for 40 s with 1 s opto pulses (p=0.5) to test opto-effect on stimulus-evoked activity; gets repeated 9x, in between training parts
    - train_opto_[0-8]: presents random training movie sequence for 180 s with 1 s opto pulses (p=0.5) to test opto-effect on stimulus-evoked activity; there are 8 parts, each of which gets presented 1x
  - parameters: 
    - size: size of the stimulus frame, automatically retrieved depending on source file
      - 424 for 424x264 movies
    - diaDeg: diameter in degrees of stimulus presentation. Since we present the 424x264 at either full- or half-screen (= 4 or 8 pix/deg), this can be either 106x66º (full) or 53x33º (half). Note that expo only saves either 106 or 53.
    - xPix, yPix: x- and y-position (in pixels) of the stimulus center. Typically 0,0 for now.
  - random sequence number:
    - this unfortunately does not get saved as a parameter, and the appropriate source files need to be manually selected before each experiment
    - for analysis, the sequence number can be retrieved from the name of the source file name "hmov_train_[seq#]_[part#].avi"
  - monitor parameters
    - distance = 25 cm
    - width = 47 cm
    - height = 29 cm
    - gamma calibration = non-linearized (i.e. using linear translation formula rather than inverse gamma parameters for linearization)
  - metadata storage
    - all relevant metadata should be accessible and database readable from the expo .xml file but can also be found in the excel log file in the "notes" column.

### Sources
- source hi-res hollywood movies from Tolias Lab, Baylor College of Medicine, Houston, Texas:
https://bcm.app.box.com/s/n5jb0w4nn1ilu5kw8f824zjknjd0u71s/folder/49369943735
- Dropbox with retinal movie .tiff stacks and code: https://www.dropbox.com/sh/q2rcv8eha86s8qv/AADNUSoQV56fGBil_QHy3K_ca?dl=0

### Regarding copyrights
Use of copyrighted material for research is fine in the US and many other countries under Fair Use (https://en.wikipedia.org/wiki/Fair_use). It can create issues if you try to use images in publications (in which case they should be replaced by public domain pictures) or when you want to provide the data for download. For this reason, ImageNet is not simply available as a big archive containing all the images, but you first have to register before you can download it. We’d probably have to use a similar solution for sharing the original inputs used to train the models. Not ideal, but short of having lots of public domain video footage there is no simple workaround.