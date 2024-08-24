

# Virtual Piano Project

## Overview

This project involves creating a virtual piano that allows users to play notes using hand gestures tracked by a webcam. The system integrates computer vision, sound synthesis, and real-time interaction to provide an engaging musical experience. Users can see a live video feed with hand tracking and hear piano notes corresponding to their hand positions.

## Key Features

1. **Hand Tracking:** Utilizes a webcam to detect hand positions and gestures, enabling users to interact with the virtual piano.
2. **Sound Synthesis:** Generates piano-like sounds using custom waveform synthesis.
3. **Real-Time Interaction:** Provides immediate feedback with visual and auditory responses as users play.

## Components

1. **Hand Tracking:** 
   - **Method:** A hand detection algorithm identifies and tracks hand positions in real-time.
   - **Libraries:** OpenCV and a custom hand detection module are used.

2. **Sound Synthesis:**
   - **Waveform Generation:** Custom waveforms are created to simulate piano sounds. The process involves summing harmonic sine waves, modulating the amplitude with an envelope, normalizing the waveform, filtering out noise, and creating a stereo signal.
   - **Mathematics:**
     - **Fundamental Frequency and Harmonics:** The waveform is defined by a fundamental frequency \( f_0 \) and its harmonics. The overall waveform \( y(t) \) is given by:

       \[
       y(t) = \sum_{n=1}^{N} A_n \sin(2\pi n f_0 t)
       \]

       where \( A_n \) represents the amplitude of the \( n \)-th harmonic.
     - **Amplitude Modulation with Envelope:** An envelope function \( e(t) \) modulates the waveform:

       \[
       y(t) = e(t) \times \sum_{n=1}^{N} A_n \sin(2\pi n f_0 t)
       \]

     - **Normalization:** The waveform is normalized to prevent distortion:

       \[
       y(t) = \frac{y(t)}{\max(|y(t)|)}
       \]

     - **High-Pass Filtering:** Low-frequency noise is removed using a high-pass filter:

       \[
       y_{\text{filtered}}(t) = y(t) * h(t)
       \]

       where \( h(t) \) is the filter's impulse response.
     - **Stereo Signal Creation:** The mono waveform is converted to stereo:

       \[
       \text{stereo\_waveform} = [y(t), y(t)]
       \]

3. **Integration:**
   - **Real-Time Playback:** As hand gestures are detected, corresponding piano notes are played through a sound synthesis engine.
   - **Visual Feedback:** The video feed is updated with hand positions and FPS information.

## Setup Instructions

1. **Install Dependencies:**
   - Ensure you have Python installed.
   - Install required libraries using pip:
     ```bash
     pip install opencv-python pygame numpy scipy
     ```

2. **Run the Project:**
   - Start the virtual piano by running the main script:
     ```bash
     python main.py
     ```
   - Ensure your webcam is connected and positioned correctly.

## Image

![Virtual Piano Interface](images/virtual_piano_interface.png)


## Future Enhancements

1. **Advanced Sound Synthesis:** Explore more sophisticated sound synthesis techniques for richer sound quality.
2. **User Interface Improvements:** Enhance the visual feedback and controls for a more intuitive user experience.
3. **Additional Features:** Integrate features such as recording and playback, or expand to support more musical instruments.

## Conclusion

This virtual piano project combines computer vision and sound synthesis to create an interactive musical experience. By tracking hand gestures and generating realistic piano sounds, it offers a unique way to play music using just a webcam.

For more details, contact [Your Name] at [Your Email].
