Title: A PTMorpher Example
Date: 2004-03-07 
Modified: 2014-09-24
Category: Tutorial
Tags: PanoTools, PTMorpher

Choose your subject
-------------------

In September 2002 elections take place in Germany and now, during the election
campains, the candidates of the two biggest parties give interviews wherever they can.
In the ADAC Motorwelt 7/2002, a monthly journal for members of this automobile club, 
i found this two similar pictures of chancellor Schröder and his challenger Stoiber. 
Since this pictures where taken from almost identical angles, 
it would be easy to identify enough control points for a test with PTMorpher. 


Preparing the input images
--------------------------

The images where scanned with a flatbed scanner and cropped to the same 
dimensions, 950 pixel wide and 1200 pixel high in this case. The full sized 
images can be downloaded by clicking on the thumbnails below. 

![Portrait Schröder]({filename}/images/schroeder150.jpg)
![Portrait Stoiber]({filename}/images/stoiber150.jpg)


Script
------

Although you can create a basic script with PTPicker, the Java frontend 
of PanoTools, i found it easier to create one from scratch, since you 
have to modify it anyway.

PTMorpher needs information about the input, given in the lines starting 
with 'i' and about the desired output, given in the 'p' line. Since the
PanoTools package is mainly intended for the stitching of multiple 
images into a panorama, the script contains many informations important
for *PTStitcher*, but which is not really relevant for *PTMorpher*: 

    p f0 w238 h300 v5 a0 b1 c0.05 n"JPEG"

    i f0 w950 h1200 y0 p0 r0 v5 n"schroeder.jpg"
    i f0 w950 h1200 y0 p0 r0 v5 n"stoiber.jpg"


'i' lines
:   The two 'i' lines hold the information about the input images. w950 and h1200
    denote the image dimensions and f0 specifies the projection format, which is 
    rectlinear in this case. The yaw (y0), pitch (p0) and roll (r0) angles should be
    zero and the field of view can be set to an arbitrary value (v5), 5° in this case.

'p' line
:   This line holds the information about the desired morphing sequence.
    The projection format and the field of view should be the same as for 
    the input images: f0 and v5. h238 and h300 give the height and width
    of the resulting images. The actual morphing sequence is specified 
    by a0 b1 c0.05, which has nothing to do with the correction factors 
    for lens distortions. a denotes starting value, b end value and c increment.
    0 is left, 1 is right image. The above command morphs two images and
    creates 20 intermediate frames. (See also the file Optimizer_Script.txt 
    in the subdirectory Script of PanoTools)


Setting control points
----------------------

Start ptpicker with the following command and load the script file.
I'm working with Debian Linux and Sun's Java and this works for me:

    $ java -Djava.library.path=/usr/lib -mx128m -jar ptpicker.jar

You have to select lots of control points for a smooth transition between the two images.

![PTPicker Window with control points]({filename}/images/morph1s.jpg)


Setting triangles
-----------------

When you have set all control points, you have to define triangles. This is
done by selecting three points, either by drawing a frame around them or by
clicking on each point with the shift key pressed down and then go to
'Edit>Set Triangle'. It is advisable to switch to the 'Select mode', 
which allows the quick selection of points without accidently setting
new ones (Menu Edit>Select).

Another, faster way is to perform an automatic triangulation of all points
and finally do some finetuning by changing or removing some triangles. I'm
not sure if it is supposed to work like this, since this method differs
somewhat from the original 'Readme.html', but the following way works for me:

It doesn't matter if you have selected any points, just go to 'Edit>Triangulate',
which will initiate the automatic triangulation. ptpicker doesn't respond for a
while and at first glance nothing seems to have happend. But when you select
now one or more points, all of a sudden the triangles are created and our two
politicians look like victims of spiderman (see next screenshoot, click on it
to get a magnified view). The triangles are only created in one window, but
they can be copied to the second window by 'Edit>Copy Triangles'. 



