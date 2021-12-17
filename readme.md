<img src="https://github.com/varungupta31/AutoVision/blob/main/graphics/CoverPage.png" height='auto' width='auto'/>

The following Project is Divided into the following Modules:
<ol>
  <li><b>Driver Side Detection</b></li>
  <ul>
    <li>Distraction Detection Using YOLOv4 Tiny</li>
    <li>Drowsiness Detection Using Histrogram of Orient Gradients, Facial Landmarks and Eye Aspect Ratio</li>
    </ul>
  <li><b>Road Side Detections</b></li>
      <ul>
    <li>Pedestrian Detection YOLOv4</li>
    <li>Traffic Sign Detection Using YOLOv4</li>
    </ul>
  </ol>
  
  ## Distraction Detection Using YOLOv4 Tiny
  
  
<img src="https://github.com/varungupta31/AutoVision/blob/main/DistractedDriverDetection/graphics/FINALGIF.gif" height='auto' width='auto'/>

The GPU Configurations for the model training were as follows:
<img src="https://github.com/varungupta31/AutoVision/blob/main/DistractedDriverDetection/graphics/training_GPU.png" height='auto' width='auto'/>

The data of human hands, in the form of images, was acquired from the <em>Open Images Dataset </em> Version 6, by Google Open Source.

The performance metrics of the trained model were as follows:

<img src="https://github.com/varungupta31/AutoVision/blob/main/DistractedDriverDetection/graphics/Screenshot%202021-12-17%20163304.png?raw=true" height='auto' width='auto'/>

<img src="https://github.com/varungupta31/AutoVision/blob/main/DistractedDriverDetection/graphics/Picture1.png" height='auto' width='auto'/>

  ## Drowsiness Detection with HOG and EAR  
  
  The implementation workflow was as follows:
  
  
  <img src="https://github.com/varungupta31/AutoVision/blob/main/Driver_Drowsiness_Detection/graphics/workflow.jpg" height='auto' width='auto'/>
  
  The Eye Aspect Ratio (EAR) was calculated as follows:
  
  <img src="https://github.com/varungupta31/AutoVision/blob/main/Driver_Drowsiness_Detection/graphics/eyeAspectRatio.png" height='auto' width='auto'/>
  

https://user-images.githubusercontent.com/51288316/146536687-68fdd8c9-e837-4afe-8e50-70375d238919.mp4

## Pedestrian Detection

The dataset chosen for this was the [PENN FUDAN Pedestrian Dataset](https://www.cis.upenn.edu/~jshi/ped_html/). Pedestrians' data containing around 400 images with an average of 6 pedestrians per image was downloaded (approx. 2400 annotations). Several images (around 200) were also sourced from Google Images.

<img src="https://github.com/varungupta31/AutoVision/blob/main/Pedestrian_Detection_YOLOv4/graphics/WalkVideo1.gif" height='auto' width='auto'/>

The trained model had the following metrics:

<img src="https://github.com/varungupta31/AutoVision/blob/main/Pedestrian_Detection_YOLOv4/graphics/metrics.png" height='auto' width='auto'/>

<img src="https://github.com/varungupta31/AutoVision/blob/main/Pedestrian_Detection_YOLOv4/graphics/pedestriansDetect.png" height='auto' width='auto'/>

<b><h4> The model generalized well even in low-light conditions </h4></b>

<img src="https://github.com/varungupta31/AutoVision/blob/main/Pedestrian_Detection_YOLOv4/graphics/WalkVideoNight.gif" height='auto' width='auto'/>

## Traffic Sign Detection

Indian traffic-sign datasets are limited. Available ones are private with restricted access. For this task, the [GTSRB (German Traffic Sign Detection Benchmark) dataset](https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) containing 800 distinct images was used. Traffic signs were classified into 4 categories: Prohibitory, Danger, Mandatory and Other




