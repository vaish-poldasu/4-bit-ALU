# 4-bit-ALU
## Overview
This project focuses on the design and analysis of a **4-Bit Arithmetic Logic Unit (ALU)** capable of performing four key operations: **Addition**, **Subtraction**, **Comparison**, and **ANDing**. The project involves estimating the **critical path** and **maximum delay** in the circuit, designing the **layout** of the ALU, and comparing **pre- and post-layout results**. The functionality of the ALU is verified using **Verilog**.

The project aims to design a fully functional ALU that can execute various operations based on the input control signals, and to verify its performance through simulation and layout verification.

## Tools Used
- **NG-SPICE**: Used for circuit design and simulation.
- **Magic**: Used for layout design and verification.
- **Verilog**: Used for ALU functionality and simulation verification.

## Project Structure
1. **ALU Block**:
   - The ALU block acts as a router for the computational circuits.
   - Operations controlled by the input signals **S1** and **S0**:
     - **00**: Addition
     - **01**: Subtraction
     - **10**: Comparison
     - **11**: ANDing
   - A **2-4 decoder** is used to control the ALU operation based on the values of **S1** and **S0**.
   - The **Enable Block** is responsible for enabling or disabling the computation blocks using **AND gates**.

2. **Enable Block**:
   - This block consists of 8 **AND gates** to send values from the input signals **A3A2A1A0** and **B3B2B1B0** to their respective computational blocks if enabled.
   - If enabled, the values are forwarded to the corresponding block (Adder, Subtractor, Comparator, or AND gate).

3. **Adder/Subtractor Block**:
   - A single block is used for both addition and subtraction operations by tying the **C0/M** input to **S0**.
   - **Addition Operation**: \( A3A2A1A0 + B3B2B1B0 \)
   - **Subtraction Operation**: \( A3A2A1A0 - B3B2B1B0 \)

4. **Comparator Block**:
   - Compares the 4-bit numbers **A3A2A1A0** and **B3B2B1B0**, and outputs a result indicating whether **A3A2A1A0** is greater than, less than, or equal to **B3B2B1B0**.

5. **AND Block**:
   - Performs a bitwise **AND operation** between corresponding bits of **A3A2A1A0** and **B3B2B1B0**.

## Design Flow
1. **ALU Design**:
   - The design of the ALU involves implementing the functional blocks and connecting them through the decoder and enable blocks.
   - Each block is designed using digital logic principles and verified using Verilog for functional correctness.
   
2. **Layout Design**:
   - The layout of the ALU is created using **Magic** to map the ALU design onto physical cells.
   - The layout includes placing standard cells for each functional block (Adder, Subtractor, Comparator, AND gate) and ensuring proper routing.

3. **Critical Path Estimation**:
   - The critical path is estimated by analyzing the longest delay in the circuit from input to output.
   - The maximum delay is calculated for each operation (addition, subtraction, comparison, and ANDing), considering the delays in each logic gate and the interconnections between them.

4. **Pre- and Post-Layout Comparison**:
   - The pre-layout results include the theoretical delay estimates based on the design.
   - The post-layout results are obtained after the layout is synthesized and routed, and they are compared to the pre-layout results to analyze the impact of physical design on circuit performance.

## Results
### Pre-Layout Results
- The pre-layout analysis provides an estimate of the critical path and maximum delay based on theoretical designs of the individual blocks.
- Simulation results of the ALU functionality (addition, subtraction, comparison, and ANDing) were verified using **Verilog**.

### Post-Layout Results
- The post-layout analysis includes the actual critical path and delay after the layout was completed in **Magic**.
- The impact of layout-specific factors such as wire delay, routing complexity, and cell placement is compared against the pre-layout estimates.
