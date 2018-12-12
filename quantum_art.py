#Quantum art
#Created by Eng.Abedalbaset Hamam for the first time in history in 12/12/2018
#Maybe this kind of art will reveal some secrets of quantum state of electron one day :)


try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite
from svgwrite import cm, mm

#global variables
#file name of quantum data
file_name='result_randon_q'

stroke_circle_size='1cm'

#end global variables


#read quantum data

with open(file_name) as f:
    quantumdatacontent = f.readlines()


number_of_bits=len(quantumdatacontent)
number_of_pixels=int(number_of_bits/24)
loop_size_bits=number_of_pixels*24
pixels_array_R = []
pixels_array_G = []
pixels_array_B = []



#this loop to construct the pixels colors arrays
for c in range(number_of_pixels):
    R7=int(quantumdatacontent[c*24])
    R6=int(quantumdatacontent[c*24+3])
    R5=int(quantumdatacontent[c*24+6])
    R4=int(quantumdatacontent[c*24+9])
    R3=int(quantumdatacontent[c*24+12])
    R2=int(quantumdatacontent[c*24+15])
    R1=int(quantumdatacontent[c*24+18])
    R0=int(quantumdatacontent[c*24+21])
    #pixels_array_R.append((2^0)*R0+(2^1)*R1+(2^2)*R2+(2^3)*R3+(2^4)*R4+(2^5)*R5+(2^6)*R6+(2^7)*R7)
    pixels_array_R.append((1)*R0+(2)*R1+(4)*R2+(8)*R3+(16)*R4+(32)*R5+(64)*R6+(128)*R7)

    G7=int(quantumdatacontent[c*24+1])
    G6=int(quantumdatacontent[c*24+4])
    G5=int(quantumdatacontent[c*24+7])
    G4=int(quantumdatacontent[c*24+10])
    G3=int(quantumdatacontent[c*24+13])
    G2=int(quantumdatacontent[c*24+16])
    G1=int(quantumdatacontent[c*24+19])
    G0=int(quantumdatacontent[c*24+22])
    #pixels_array_G.append((2^0)*G0+(2^1)*G1+(2^2)*G2+(2^3)*G3+(2^4)*G4+(2^5)*G5+(2^6)*G6+(2^7)*G7)
    pixels_array_G.append((1)*G0+(2)*G1+(4)*G2+(8)*G3+(16)*G4+(32)*G5+(64)*G6+(128)*G7)

    B7=int(quantumdatacontent[c*24+2])
    B6=int(quantumdatacontent[c*24+5])
    B5=int(quantumdatacontent[c*24+8])
    B4=int(quantumdatacontent[c*24+11])
    B3=int(quantumdatacontent[c*24+14])
    B2=int(quantumdatacontent[c*24+17])
    B1=int(quantumdatacontent[c*24+20])
    B0=int(quantumdatacontent[c*24+23])
    pixels_array_B.append((1)*B0+(2)*B1+(4)*B2+(8)*B3+(16)*B4+(32)*B5+(64)*B6+(128)*B7)

print(len(pixels_array_B))
def quantum_circle_shapes(name):
    dwg = svgwrite.Drawing(filename=name, debug=True)
    hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
    for y in range(10+number_of_pixels*2):
        hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=((10+number_of_pixels*2)*cm, (2+y)*cm)))
    vlines = dwg.add(dwg.g(id='vline', stroke='blue'))
    for x in range(10+number_of_pixels*2):
        vlines.add(dwg.line(start=((2+x)*cm, 2*cm), end=((2+x)*cm, (10+number_of_pixels*2)*cm)))


    shapes = dwg.add(dwg.g(id='shapes'))
    for circle_count in range(number_of_pixels):
        rv=str(circle_count)+'cm'
        shapes.add(dwg.circle(center=(((10+number_of_pixels*2)/2)*cm, ((10+number_of_pixels*2)/2)*cm), r=rv, stroke=svgwrite.rgb(pixels_array_R[circle_count], pixels_array_G[circle_count], pixels_array_B[circle_count]), stroke_width='2cm').fill('red', opacity=0))

    #shapes.add(dwg.circle(center=(10*cm, 10*cm), r='4cm', stroke='#ff0000', stroke_width='2cm').fill('green', opacity=0.5))


    dwg.save()


if __name__ == '__main__':
    quantum_circle_shapes('quantum_art_cirlcle_Q.svg')
