Fixing EXIF for manual lenses
=============================

:date: 2016-08-24
:category: Tutorial
:tags: Panorama, workflow, exiftool


* prepend filename with focal length
  
  .. code-block:: bash
      
    $ exiftool '-filename<${focallength}_%f.%e'
  
  

