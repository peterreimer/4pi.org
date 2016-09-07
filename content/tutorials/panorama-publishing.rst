Panorama publishing workflow
============================

:date: 2015-06-15
:category: Tutorial
:tags: Panorama, workflow, exiftool

Several steps:

* fixing orientation and setting aperture:
  
  .. code-block:: bash

    $ exiftool -overwrite_original_in_place -FNumber=5.6 -Orientation=8 -n *.CR2

* copy gps information taken with the smartphone to panorama frames:
  
  .. code-block:: bash
    
    $ exiftool −overwrite_original_in_place -r -tagsFromFile phone.jpg -gps:all *.CR2

* copy exif from source image to panorama:

  .. code-block:: bash
    
    $ exiftool -tagsfromfile frame-01.CR2 -all:all -n -Orientation=1 panorama.jpg
    
* Samyang or zenitar: add metadata to source:

  .. code-block:: bash

    $ exiftool -@ ~/.ExifTool/samyang panorama.jpg

* prepend filename with focal length
  
  .. code-block:: bash
      
    $ exiftool '-filename<${focallength}_%f.%e'
  
  .ExifTool/samyang:
  
  .. code-block:: none
  
    -n
    -overwrite_original_in_place
    -LensModel=Samyang 8mm 1:3.5 FISH-EYE CS
    -LensType=Samyang 8mm 1:3.5 FISH-EYE CS
    -Lens=8
    -LensSerialNumber=D111G1769
    -MaxApertureValue=3.5
    -FocalLength=8

    
* add photosphere metadata:

.. raw:: html

    <script src="https://gist.github.com/peterreimer/d33f79555a05ee0c6002.js"></script>


Benchmark
---------

pto2mk -o bokul.pto.mk -o bokul bokul.pto

+----------------------------------------------------+------------+------------+
|command                                             | real       | user       |
+====================================================+============+============+
|Intel(R) Core(TM) i3-2120 CPU @ 3.30GHz                                       |
+----------------------------------------------------+------------+------------+
|make -f bokul.pto.mk all clean                      | 34m57.851s | 37m35.351s |
+----------------------------------------------------+------------+------------+
|make -f bokul.pto.mk ENBLEND='enblend-mp' all clean | 14m2.811s  | 49m30.374s |
+----------------------------------------------------+------------+------------+
|Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz                                       |
+----------------------------------------------------+------------+------------+
|make -f bokul.pto.mk all clean                      | 31m47.690s | 32m21.130s |
+----------------------------------------------------+------------+------------+
|make -f bokul.pto.mk ENBLEND='enblend-mp' all clean | 10m32.089s | 34m3.486s  |
+----------------------------------------------------+------------+------------+
|Intel(R) Core(TM) i7-4500U CPU @ 1.80GHz                                      |
+----------------------------------------------------+------------+------------+
|make -f bokul.pto.mk all clean                      | 33m10.220s | 36m20.288s |
+----------------------------------------------------+------------+------------+
|make -f bokul.pto.mk ENBLEND='enblend-mp' all clean | 15m6.964s  | 55m58.156s |
+----------------------------------------------------+------------+------------+
|Intel(R) Core(TM)2 CPU T5600  @ 1.83GHz                                       |
+----------------------------------------------------+------------+------------+
|make -f bokul.pto.mk all clean                      | 81m36.605s | 83m4.948s  |
+----------------------------------------------------+------------+------------+
|make -f bokul.pto.mk ENBLEND='enblend-mp' all clean | 44m48.599s | 85m4.464s  |
+----------------------------------------------------+------------+------------+

