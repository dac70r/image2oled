# Project Summary
This mini-project serves to generate the binary code of an image so that it can be displayed on the 
oled module of a Basys 3 FPGA Board. 

# Introduction
As part of the final project for EE2026: Digital Design at NUS Singapore, we are tasked to work with an OLED and a mic connected to the 
Basys 3 FPGA board which was issued to us. 

# Details
1. In order to display images on the OLED, we first reresize the image to the desired length and width. 
2. Then we use the imageio library (pip install imageio) to read the image and convert it format to binary code. 
3. The binary code is then added with some necessary syntax that is required by Verilog.
4. The output can be copied and pasted into the Verilog code for the project. 
