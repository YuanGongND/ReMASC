# ReMASC: Realistic Replay Attack Corpus for Voice Controlled Systems

We introduce a new database of voice recordings with the goal of supporting research on vulnerabilities and protection of voice-controlled systems. In contrast to prior efforts, the proposed database contains genuine and replayed recordings of voice commands obtained in realistic usage scenarios and using state-of-the-art voice assistant development kits. Specifically, the database contains recordings from four systems (each with a different microphone array) in a variety of environmental conditions with different forms of background noise and relative positions between speaker and device. To the best of our knowledge, this is the first database that has been specifically designed for the protection of voice controlled systems (**VCS**) against various forms of replay attacks.

## Updates
June, 30, 2020:
- We now release the complete set.
- We now host the data on **[IEEE DataPort](https://ieee-dataport.org/open-access/remasc-realistic-replay-attack-corpus-voice-controlled-systems)**, which offers a high-speed download (you will need an [IEEE account](https://ieee-dataport.org/faq/how-do-i-access-dataset-ieee-dataport) to download, which is also free).
- The ReMASC corpus remains **free for academic and commercial use**, and we no longer require a verification process, you can download the data immediately. Nevertheless, it is highly recommended to sign up to our mailing list to get the latest news about the dataset.

## Downloads
**Sample Set** (~10MB)

A mini set consists of 16 samples for initial evaluation. You can download it **\[[here](https://drive.google.com/open?id=1RYHaaHnwuTb7Mx-jlVynQBaIJ-qQ80my)]**.

**Complete Set** (92.3GB)

All data we've collected and processed. Please download it from **\[[IEEE DataPort](https://ieee-dataport.org/open-access/remasc-realistic-replay-attack-corpus-voice-controlled-systems)]**,  it is free. You will need an [IEEE account](https://ieee-dataport.org/faq/how-do-i-access-dataset-ieee-dataport) to download, which is also free.

The complete set consists of two disjoint set:

- **Core Set**: the suggest training and development set.
- **Evaluation Set**: the suggest evaluation set. 

We also include an unsplited complete set in the .zip package in case you want to customerize the data split. It is just a simple union of the core set and the evaluation set. 


## Cite Us:  
If you use the data, please cite the following paper:

Yuan Gong, Jian Yang, Jacob Huber, Mitchell MacKnight, Christian Poellabauer, ["ReMASC: Realistic Replay Attack Corpus for Voice Controlled Systems"](https://www.isca-speech.org/archive/Interspeech_2019/abstracts/1541.html), Interspeech 2019.

If you use our neural network example, please cite the following paper:

Yuan Gong, Jian Yang, Christian Poellabauer, ["Detecting Replay Attacks Using Multi-Channel Audio: A Neural Network-Based Method"](https://arxiv.org/abs/2003.08225)  IEEE Signal Processing Letters, 2020.

## Examples:
- The Python neural network baseline, PyTorch implementation, and the dataloader can be found in the example directory.
- The MATLAB CQCC-GMM baseline can be found \[[here](https://github.com/jlinear/ReMASC_Exp)].



## Definitions and Data Collection Strategy

![enter image description here](https://yuangongorg.files.wordpress.com/2018/11/figure12.png?w=400)

**Figure 1**. An illustration of legitimate usage of a VCS (upper figure) and a replay attack (lower figure).

![enter image description here](https://yuangongorg.files.wordpress.com/2018/11/figure22.png?w=400)

**Figure 2**. The recording environments and conditions.

A typical VCS replay attack is illustrated in the lower part of Figure 1. An attacker first needs to prepare a **replay source recording** (i.e., circled 2 in Figure 1), which can be done by either recording a speaker (using a source recorder) or by performing speech synthesis. The attacker can then replay it using a replay device and the **replayed recording** (i.e., circled 3 in Figure 1) is captured by the VCS device. In contrast, a legitimate usage scenario is illustrated in the upper part of Figure 1, where a **genuine recording** (i.e., circled 1 in Figure 1) is directly captured by the VCS device. A defense task is then to build a model that is able to **distinguish genuine recordings from replayed recordings**. 

As shown in Figure 2, in our data collection, we ask the subject to hold the source recorder at a short distance when speaking into the microphone arrays (which emulates the VCS device). When the subject speaks the voice command, both the source recorder and the microphone array record simultaneously. We define the recording captured by the microphone array as the **genuine recording**, and the recording captured by the source recorder as the **replay source recording**. Then, we play the replay source recording multiple times in different settings into the microphone array again, and refer to the recording captured by the microphone array as the **replayed recording**. The ReMASC data set provides all three types of recording. We also emulate  situations where the attacker uses speech synthesis to generate replay source recordings (i.e., there is no genuine recording).  

## Text Materials and Recording Subjects

A total of 132 voice commands are used as the recording text material. Among them, 31 commands are security sensitive and 49 commands are used in the vehicle. The command list contains 273 unique words, which provides reasonable phonetic diversity. Further, we recruited 50 subjects (22 female and 28 male), where 36 subjects are English native speakers, 12 subjects are Chinese native speakers, and the remaining 2 subjects are Indian native speakers. The subjects’ ages range from 18 to 36. Three subjects participated more than once, leading to a total of 55 data sets (i.e., 47 subjects with one set of recordings and 3 with several sets of recordings).

## Microphone Array Based Recorder
![enter image description here](https://yuangongorg.files.wordpress.com/2018/11/figure32.png?w=400)

**Figure 3**. Microphone arrays used in the data collection (microphones are shown with the rectangles and a white arrow indicates the direction of the microphone array during data collection).

![enter image description here](https://yuangongorg.files.wordpress.com/2018/11/table12.png?w=400)

**Table 1**. Microphone array settings.

Due to privacy concerns, off-the-shelf VCS products such as Amazon Echo or Google Home do not allow developers toaccess the raw audio.  Therefore, we use the following VCS development kits in our work:  A) Amlogic A113X1 (4-mic triangle or 6-mic circular array);  B) Respeaker 4-mic lineararray; C) Respeaker Core V2 (6-mic circular array); and D) Google AIY Voice Kit (2-mic linear array).  As illustrated in Figure 3, in all experiments, we mount the four microphonearrays on a stand and for all recording devices,  we use theAdvanced Linux Sound Architecture (ALSA) to collect multi-channel waveform files.  We use the highest possible record-ing quality for each kit (summarized in Table 1).   Practical VCSs might use lower sampling rates and bit depths to lowerthe computational and network transmission overheads.

## Source Recorder and Playback Devices
![enter image description here](https://yuangongorg.files.wordpress.com/2018/11/figure52.png?w=400)

**Figure 4**. Playback device (left figure) and source recorder (right figure) used in the data collection.

To study if the source recorder affects the replay attack detection, we use a low-cost recorder, i.e., an iPod Touch (Gen5), and a professional recorder, i.e., a Tascam DR-05, together as the source recorder. As shown in Figure 4, we tape the two recorders together and ask the subject to hold it at a close distance when they speak into the VCS (microphone array). The captured recording is then used as the replay source recording. Although the Tascam DR-05 is a professional high fidelity device, channel and background noise are still inevitable. Therefore, we also use Google Text-to-speech (TTS) to synthesize the voice commands as additional replay source recordings, which can then be considered as completely channel and background noise free. For diversity considerations, we use 26 different voice settings (13 male and 13 female) with two different synthesis technologies (standard and WaveNet) and three dialect settings (Australia, UK, and U.S.). As shown in Figure 4, we use four common representative playback devices: A) Sony SRSX5, B) Sony SRSX11, C) Audio Technica ATH-AD700X headphone, and D) iPod Touch. Further, in the vehicle environment, we use the vehicular audio system as an additional playback device.

## Recording Environment
![enter image description here](https://yuangongorg.files.wordpress.com/2018/11/figure43.png?w=400)

**Figure 5**. Illustration of device and speaker position settings. In indoor environment 1, each hollow symbol represents a microphone array placement and the direction it faces is indicated by an arrow. The corresponding solid symbols of the same shape represent a speaker position (for a total of 18 device placement - speaker position combinations, can be generalized to more combinations since array is symmetric). In indoor environment 2, the hollow circle represents the microphone array, the square represents the speaker playing the background sound, and the solid circle represents the speaker. 

We performed the data collections in four environments:

**(A) Outdoor environment**: To emulate uncontrolled noise in an outdoor environment, we collect data at a student plaza with various background noises such as chatting, traffic, and wind. The speaker-recorder distance ranges from 0.5 to 1.5m.

**B) Indoor environment 1**: Modern VCSs usually allow flexible device placement and speaker positions. To emulate this, we perform data collection in a quiet study room using three device placement settings: room corner, against the wall, and center of the room. For each device placement, the speaker speaks in six locations, forming 18 different position combinations (illustrated in Figure 5).

**C) Indoor environment 2**: In realistic scenarios, VCSs will receive voice commands while some background sounds might be playing. In such situations, although there is an electronic device playing sounds, the VCS should not reject the user’s voice command. This requires a defense model that is able to precisely detect the sound source of the voice command rather than that of the entire received audio. To emulatethis situation, we collected data in a lounge with music and TV sounds in the background (illustrated in Figure 5). Device placement and speaker position are fixed.

**D) Vehicle environment**: To emulate a vehicle-based VCS, we collected data in a moving vehicle (Dodge Grand Caravan). As shown in Figure 5, the microphone array is placed at the center console and the subjects speak while sitting in different seats (except the driver’s seat). It is very common that the driver will make voice commands; therefore, about half of the data is collected from position 1 in Figure 5. Each subject is asked to say 49 vehicle-related voice commands twice, once in a silent environment (parking lot when the engine is off) and once when the car is moving. The source recording obtained from a silent environment is then used for replay. We collected the data in various environments (e.g., highway, urban area), with speeds ranging from 3 to 40 mph.


## Replay Settings

For each replay source recording collected by each source recorder, we replay it multiple times with different playback devices. In indoor environment 2 and the vehicle environment, the position of the playback device is identical to the subject’s position. In the outdoor environment and indoor environment 1, we also replay it in different positions. To keep the data collection effort reasonable, each replay source recording is replayed in 1 to 3 randomly selected replay settings, while the replay settings are normally distributed. All replay recordings and genuine recordings are collected in the same environments with similar volume. Further, for each recording environment, we did our best to make everything in the environment identical for both genuine recordings and replay recordings.

## Questions

If you have a question on how to use the dataset, you can rasie an issue in this Github reporsity. You can also contact Yuan Gong (ygong1@nd.edu).
