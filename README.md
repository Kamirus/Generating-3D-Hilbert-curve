# Generating-3D-Hilbert-curve

# Project has two versions:

1) hilbert3D_postscript directory includes code, which generates 3D curve, modifies it by rotation and projection. Then it's printing postscript file with that modified curve.

	Run run.py to see example 
Also arguments for this script are explained there

GhostScript can convert ps file into pdf with that comand:
	$ps2pdf ps_file.ps pdf_file.pdf


2) hilbert_withVPython directory includes code, which generates 3D curve, centers and shows it using VPython curve. Generated curve can be moved by clicking right mouse button and draging mouse.
