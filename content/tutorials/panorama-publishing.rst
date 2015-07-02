Panorama publishing workflow
============================

:date: 2015-06-15
:category: Tutorial
:tags: Panorama, workflow, exiftool

Several steps:

* copy exif from source image to panorama::
    
    exiftool -tagsfromfile frame-01.CR2 -all:all -n -Orientation=1 panorama.jpg
    
* Samyang or zenitar: add metadata to source

    exiftool -@ ~/.ExifTool/samyang panorama.jpg
  
  .ExifTool/samyang::
  
    -n
    -overwrite_original_in_place
    -LensModel=Samyang 8mm 1:3.5 FISH-EYE CS
    -LensType=Samyang 8mm 1:3.5 FISH-EYE CS
    -Lens=8
    -LensSerialNumber=D111G1769
    -MaxApertureValue=3.5
    -FocalLength=8

    
* add photosphere metadata

