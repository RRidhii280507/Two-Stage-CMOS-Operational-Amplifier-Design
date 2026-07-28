# Two-Stage CMOS Operational Amplifier Design

## Overview

This project presents the design and simulation of a **two-stage single-ended CMOS operational amplifier** using a **0.8 μm bulk CMOS process**. The design uses **±2.5 V split supply rails** and **internal Miller compensation** to achieve high open-loop gain, stable frequency response, and low-power operation.

## Design Specifications

| Parameter                | Target       |
| ------------------------ | ------------ |
| Technology               | 0.8 μm CMOS  |
| Supply Voltage           | ±2.5 V       |
| Open-Loop Gain           | > 5000 V/V   |
| Gain-Bandwidth Product   | 5 MHz        |
| Slew Rate                | > 10 V/μs    |
| Maximum Load Capacitance | 10 pF        |
| Phase Margin             | ≥ 60°        |
| Input Common-Mode Range  | −1 V to +2 V |
| Output Swing             | ≥ ±2 V       |
| Power Dissipation        | ≤ 2 mW       |
| Channel Length           | 1 μm         |

## Key Features

* Two-stage CMOS operational amplifier with **single-ended output**
* **Internal single-pole Miller compensation** for frequency stability
* Optimized **MOSFET W/L ratios** and bias currents
* Designed for **high gain, high slew rate, and low power consumption**
* Analysis of **pole locations and frequency response**
* Evaluation of **CMRR, PSRR, input impedance, and output impedance**

## Design Methodology

1. Performed preliminary **hand calculations** to determine transistor dimensions, bias currents, gain, and compensation requirements.
2. Designed and sized the MOSFETs based on the given **0.8 μm CMOS process parameters**.
3. Selected a physically realizable **Miller compensation capacitor** based on the required frequency response.
4. Verified the design using **SPICE AC, DC, and transient simulations**.
5. Iteratively optimized the circuit to meet the required **gain, GBW, phase margin, slew rate, power, and voltage swing** specifications.

## Simulation & Analysis

The circuit was analyzed for:

* Open-loop DC gain
* Gain-bandwidth product
* Phase margin and stability
* Slew rate
* Input common-mode range
* Output voltage swing
* Power dissipation
* CMRR and PSRR
* Open-loop input and output impedance
* Pole locations and frequency response

## Tools Used

* **LTspice / SPICE**
* Analog circuit hand calculations
* CMOS transistor-level design
