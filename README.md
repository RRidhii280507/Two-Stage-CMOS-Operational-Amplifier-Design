# Two-Stage CMOS Operational Amplifier Design & Simulation

A fully differential/single-ended two-stage CMOS operational amplifier with cascode active loads designed, simulated, and verified using the **SkyWater Sky130 PDK**, **Xschem**, and **Ngspice**.

---

## 📌 Project Overview

This project presents the design, schematic capture, and SPICE-based simulation of a high-gain two-stage CMOS operational amplifier utilizing the open-source **SkyWater 130nm PDK (Sky130)**. The circuit incorporates a cascode active load architecture and internal Miller compensation to achieve high open-loop gain, wide gain-bandwidth product (GBW), and robust frequency stability.

---

## ⚡ Design Specifications & Target Metrics

| Parameter | Target / Achieved Value |
| :--- | :--- |
| **Technology** | SkyWater Sky130nm CMOS PDK |
| **Supply Voltage ($V_{dd}$)** | 3.3 V DC |
| **Open-Loop Gain** | > 80 dB (~ 91.6 dB achieved). |
| **Gain-Bandwidth Product (GBW)** | ~ 10.9 MHz. |
| **Phase Margin** | Optimized for frequency stability |
| **Load Capacitance ($C_L$)** | 0.25 pF |
| **Bias Current** | 0.5 uA reference |

---

## 🔑 Key Features & Methodology

* **Topology:** Two-stage CMOS operational amplifier with single-ended output and cascode active loads.
* **Compensation:** Internal single-pole Miller compensation network (R_z, C_c) for stability.
* **Design Flow:** Performed transistor sizing, MOSFET $W/L$ ratio optimization, and bias point calculations.
* **Simulation Framework:** Executed AC, DC, and transient analyses using **Ngspice** integrated with **Xschem** schematic capture.

---

## 📐 Circuit Schematic (Xschem)

The complete schematic built in Xschem using Sky130 primitives, featuring differential input pairs, current mirror loads, level shifters, and Miller compensation:

**Schematic Design**  
<img width="983" height="522" alt="image" src="https://github.com/user-attachments/assets/fa1f2be0-7715-4633-bd40-335c46698088" />


---

## 📊 Simulation Results & Analysis

The circuit was analyzed for AC frequency response (Bode plots showing gain and phase margin) and transient performance under test signals:

**1. Transient Response ($V_{in}$ vs $V_{out}$)**  
<img width="475" height="420" alt="image" src="https://github.com/user-attachments/assets/f85fdda3-43a9-44f6-842e-1d5396d44f40" />


**2. Bode Phase Plot ($\text{Phase}^{\circ}$ vs Frequency)**  
<img width="475" height="420" alt="image" src="https://github.com/user-attachments/assets/31ccb72b-a4bd-4ba8-a4d1-87fb20c347f6" />


**3. Bode Gain Plot ($\text{Gain in dB}$ vs Frequency)**  
<img width="477" height="413" alt="image" src="https://github.com/user-attachments/assets/326c969d-a42e-4f40-8dbc-7a2c663da5e7" />


---

## 🛠️ Software Tools Used

* **Xschem** – Schematic capture and hierarchical circuit design using Sky130 symbols.
* **Ngspice** – Backend SPICE engine for AC sweep, DC operating point, and transient simulations.
* **SkyWater 130nm PDK (Sky130)** – Open-source semiconductor process design kit for accurate MOSFET modeling.
