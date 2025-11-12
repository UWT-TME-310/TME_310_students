# Project Part 3 - enhanced pile-driving app

Assignment repo: [project_03]()

## Purpose

Demonstrate the coding skills learned in the course to develop a notebook that could be **useful for engineering professionals** working on pile-driving projects.

## Instructions

Your goal for Part 3 of the course project is to enhance the a basic pile-driving app you developed in Part 2 (you are also allowed to use the Part 2 example submission as a starting point for Part 3).

There are several ways that the basic pile-driving app could be enhanced.
Descriptions of suggested enhancements are listed below.
Your project group should choose one of the enhancements listed below OR propose an enhancement to your instructor.

### Enhancement Options

1. **Audio-video saximeter**
   
   A Saximeter is an instrument that uses sound to determine the timing of hammer blows during pile-driving. 
   Traditionally, a field engineer uses a saximeter to record blows per minute (BPM) while watching for the pile to have been driven a certain length (usually one foot). 
   By manually pressing a button on the saximeter, the field engineer records the time between 1-foot driving intervals, which the saximeter uses (in combination with its audio-based record of blows) to calculate blows per foot (BPF).

   The *Audio-video saximeter* enhancement will involve using a video of a pile-driving installation to create the same data as are traditionally captured by the field engineer and saximeter.
   The data interpreted from the video, will produce a pile-driving log and the associated plots from Part 2.

   The focus of this option is the audio/video analysis.

2. **Diesel hammer combustion**

   Open-ended diesel hammers consist of a single cylinder containing a heavy piston called a ram. 
   During operation, fuel ignition launches the  ram up into the air. 
   When the ram falls back down, it compresses and heats an air/fuel mixture in the piston, reaching its ignition temperature and starting the process over again.

   The *Diesel hammer combustion* enhancement will involve creating a model of the combustion process - the increasing pressure and temperature due to the falling piston, the energy released by fuel ignition, and the resulting displacement of the piston.
   The model will provide a means of calculating the fuel needed to achieve different piston heights.
   Combined with a pile-driving log containing blows per minute (BPM) and blows per foot (BPF), the model will show the fuel consumption during the pile-driving process.

   The focus of this option is the cost of pile installation.


1. **Pile Driving Analysis (PDA) instrumentation**

   Pile Driving Analysis (PDA) is the name of a specific set of instruments used to measure wave transmission through a pile as it's driven.
   Generally, PDA is performed on only a small percentage of piles in a given project because it's expensive to perform and slows down the construction because of the instrument installation.
   PDA data contains measurements of **strain** and **acceleration** signals that can be used to calculate the force and speed of pressure waves traveling through the pile. 
   This data can be interpreted to determine an estimate of the pile's capacity, the maximum tension and compression stresses in the pile, and detect whether the pile has been damaged.

   The *PDA instrumentation* enhancement will use data from one or more blows at the end of driving to produce a capacity estimate to compare to the estimate from a pile-driving log. 
   Additionally, the pile stresses and damage indications (if any) will be reported and compared to the material strength as a quality control check on the pile's structural integrity. 

   The focus of this option is quality control and capacity verification.


2. **Environmental noise assessment**

   Pile-driving is a noisy process.
   The noise from pile-driving can be a nuisance to neighboring properties and disturbing (and even lethal) to wildlife.
   Sound from pile-driving comes from the impact between the pile and hammer and from the deformation of the pile as compression and tension waves travel through the pile.
   The noise from the waves traveling through the pile are particularly important under water, where they have the most impact on wildlife.

   The *Environmental noise assessment* enhancement will use the PDA strain and velocity measurements to estimate the volume in air and water from a single blow to the pile.
   The noise attenuation with distance from the pile will be compared to different thresholds, providing an estimate for the distance where various noise issues are of concern.
   Combined with a pile-driving log with blows per minute (BPM) and blows per foot (BPF), the noise model will provide a range of distances and time durations over which the noise issues are of concern.

   The focus of this option is environmental regulation compliance.


3. **Subsurface interpretation using data clustering**
   
   The data in the pile-driving log can be used to estimate the final pile capacity, but it also shows how the capacity of the pile changed as it was driven through the soil.
   Different soil layers are likely to have different levels of resistance to driving (and therefore different capacities).
   For a pile-driving project with several piles, combining all the pile-driving logs may provide clues to the number of distinct geologic layers the piles were driven through.

   The *Subsurface interpretation using data clustering* enhancement is **part of an active research project** on pile-driving data interpretation.
   This enhancement will use multiple (~100) pile-driving logs to develop a dataset of pile-driving resistances across a project site.
   Using data clustering techniques, an analysis of the dataset will produce a report on the number of distinct geologic layers at the site.

   The focus of this option is research of new data interpretation methods. 
   As such, it has the potential to be both exciting and challenging. 
   Exciting because it may show a result that no one's seen before.
   Challenging because there's less likely to be a "right" answer or a "best" approach to the problem.




The purpose of the app and instructions for using it should be clearly described in the notebook.

The support code should be imported traditionally, using functions and import statements.

Additionally, the supporting code should be well-documented with docstrings.
Any individual who understands Python should be able to view the supporting code and understand how each function works by reading the docstrings. 
At a minimum, docstrings should include:

1. A description of the function's purpose.
2. A list of the function's input parameters, including whether they have default values and what units the should be in.
3. A list of the function's output parameters, including what units they will be in.

### Choosing a pile-driving log file

The way a user chooses a pile-driving log file should only involve changing the file name in one of the code cells in the notebook.

Your assignment repository will include a small number of properly formatted pile-driving logs for you to test your notebook with.
You should assume that app users will want to add additional pile-driving logs and select them with your app.
You may assume that any pile-driving logs the user adds will follow the same format as the sample logs.

### Plot of the driving log data

The plots needed will depend on the enhancement option

### Plot of the pile's estimated capacity

Estimating the capacity from pile-driving logs should be done the same way as described in Part 2.

### Pile summary

Other summaries may be needed...

The text summary of the pile's final condition should include the pile ID, final tip elevation, and final load capacity.
An example is shown below (note - 1 "kip" = 1,000 pounds):

```
Pile ID: B-14
Pile tip elevation: -134 feet
Pile load capacity: 899 kips
```

## Submission

Your project will be submitted by pushing your work to GitHub (same as the homework submission procedure).
At a minimum, the submission should include:

1. Your app's notebook (one `.ipynb` file)
2. Your app's support script (one or more `.py` files)
3. At least one of the pile-driving log data files (one or more `.csv` files)


## Rubric
## Grading rubric

Your submission will be graded by the instructor with the following rubric:


| Category | Criteria | Points |
|----|----|----|
| Data reading | Users have a way to change which pile-driving log is being analyzed by the app. The app will work for any properly formatted pile-driving log in the directory that the sample log files are in so that if a user adds additional logs, they can be analyzed by the app |  __ / 10 |
| App instructions | The app instructions are clearly written such that an informed (i.e., familiar with pile-driving and Jupyter notebooks) user would be able to use the app. |  __ / 10  |
| Plots | Plots of BPM, BPF, and pile load capacity are generated from the log. All plots use elevation as the vertical axis. The units of data being plotted are included and correct. |  __ / 10 |
| Output |  A short summary of the pile analysis is displayed when the app is run. The output summary includes the correct units. The information in the summary is consistent with the pile log file and the plots. |  __ / 10|
| Support code |  The functions that perform the app's calculations are imported into the app from one or more supporting Python files. The functions are well documented (purpose, inputs and outputs described in a docstring). |  __ / 10 |