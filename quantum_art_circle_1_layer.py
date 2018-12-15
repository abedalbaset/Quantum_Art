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
number_of_pixels=int(number_of_bits/8)
loop_size_bits=number_of_pixels*8
pixels_array_R = []
pixels_array_G = []
pixels_array_B = []



#this loop to construct the pixels colors arrays
for c in range(number_of_pixels):
    R7=int(quantumdatacontent[c*8])
    R6=int(quantumdatacontent[c*8+1])
    R5=int(quantumdatacontent[c*8+2])
    R4=int(quantumdatacontent[c*8+3])
    R3=int(quantumdatacontent[c*8+4])
    R2=int(quantumdatacontent[c*8+5])
    R1=int(quantumdatacontent[c*8+6])
    R0=int(quantumdatacontent[c*8+7])
    #pixels_array_R.append((2^0)*R0+(2^1)*R1+(2^2)*R2+(2^3)*R3+(2^4)*R4+(2^5)*R5+(2^6)*R6+(2^7)*R7)
    pixels_array_R.append((1)*R0+(2)*R1+(4)*R2+(8)*R3+(16)*R4+(32)*R5+(64)*R6+(128)*R7)

print(len(pixels_array_B))
def quantum_art_cirlcle_Q_1layer(name):
    dwg = svgwrite.Drawing(filename=name, debug=True)
    zoomratio=5

    hlines = dwg.add(dwg.g(id='hlines', stroke='#ffffff'))
    for y in range(10+number_of_pixels*2):
        hlines.add(dwg.line(start=(2*mm, (2+y)*mm), end=((10+number_of_pixels*2)*mm, (2+y)*mm)))
    vlines = dwg.add(dwg.g(id='vline', stroke='#ffffff'))
    for x in range(10+number_of_pixels*2):
        vlines.add(dwg.line(start=((2+x)*mm, 2*mm), end=((2+x)*mm, (10+number_of_pixels*2)*mm)))

    shapes = dwg.add(dwg.g(id='shapes'))
    for circle_count in range(number_of_pixels):
        rv=str(circle_count)+'mm'
        shapes.add(dwg.circle(center=(((10+number_of_pixels*2)/2)*mm, ((10+number_of_pixels*2)/2)*mm), r=rv, stroke=svgwrite.rgb(pixels_array_R[circle_count], 0, 0), stroke_width='2cm').fill('red', opacity=0))


    dwg.save()


if __name__ == '__main__':
    quantum_art_cirlcle_Q_1layer('quantum_art_cirlcle_Q_1layer.svg')
