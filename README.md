# iotsocialfitness

# Table of contents
1. [DISH IoT Hackathon Rules](#iotrules)
2. [Social Fitness Motivation](#socialfitness)
3. [Installation](#installation)
4. [Requirements](#requirements)
5. [Installation Steps](#installationsteps)
6. [API Documentation](#apidocumentation)

## DISH IoT Hackathon Rules <a name="iotrules"></a>

In February 2018, Dish Network hosted a two-day IoT Hackathon for 10 teams at their
Meridian campus headquarters in Englewood, CO; the goal was to inspire Dish employees
and outside entrepreneurs, engineers, and data scientists to create and execute
an IoT product that would answer the question, "How can we make Meridian better
using IoT?"  Judged by a panel of executives, the teams would be competing for a
chance to obtain executive sponsorship for their product.  The specific goal for
each team was to "come up with a working demo of a thing that senses or acts(or
  both) in the physical world, controlled via the internet, using Alexa to make
  Meridian better."  The resources given to each team were:
  * Raspberry Pi 3
  * MicroSD Card
  * Pi Wedge
  * Sparkfun Inventor's Kit (photocell, motor, servo, resistors, jumper wires, LEDs,
    buttons)
  * Resistor
  * Breadboard
  * Echo Dot
  * Access to AWS back-end platform
  * $100 Visa gift card

  Each team was given a rubric that the judges would be using to judge us on, specifically
  in the categories of:
  * Feasability
  * Innovation
  * Utility
  * Presentation

## Social Fitness Motivation <a name="socialfitness"></a>

"We live in the most technologically connected age in the history of civilization,
yet rates of loneliness have doubled since the 1980s."
                                                -Vivek Murthy, US Surgeon General

"An employee's work loneliness triggers emotional withdrawal from their organization."
                                                -INC, November 2017

"67% of US workers are NOT engaged at work.  Low-engagement companies have 41% higher
absenteeism, 59% higher turnover, 40% more defects, and 21% lower profitability."
                                                -2017 Gallup State of the American Workforce

Considering this research and the fact that DISH's executives created a 2018 KPI
to focus on workplace engagement, our team chose to create an IoT product that would
facilitate physical human conversations that connect people and create social capital.
But how do you do this using sensors, a Raspberry Pi, and an Alexa?  

If we were going to facilitate social interactions, when and how would we do that?
Realizing that employees most naturally take breaks from their work to go to the
bathroom or refill their coffee cup, we chose to program sensors that would measure
employees' coffee cups; when an employee's coffee cup was empty, Alexa would tell
him/her to go meet another employee, whose coffee cup was also flagged as empty,
at a specific location to refill their coffee and socialize with each other.  In
order to do this, we created two prototype coffee cups that each had a Raspberry
Pi and ultrasonic sensor attached at the top.

![Prototypes page](images/prototypes.jpg) 

The Raspberry Pi was programmed to
measure the depth of the coffee cups every 20 seconds;



Technology is making us lonelier and less engaged at work, which results in much
higher turnover, lower quality of work, and less profit.  

  2. [Social Fitness Motivation](#socialfitness)
  3. [Installation](#installation)
  4. [Requirements](#requirements)
  5. [Installation Steps](#installationsteps)
  6. [API Documentation](#apidocumentation)

2. [Data](#data)
3. [Feature Engineering](#feature_engineering)
4. [Exploratory Data Analysis](#EDA)
5. [Recommender Methods](#methods)
6. [Website](#website)
7. [Tech Stack](#techstack)
8. [Future Direction](#futuredirection)
8. [References](#references)
