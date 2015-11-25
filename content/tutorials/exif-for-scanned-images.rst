Exif Data for scanned images
============================

:date: 2015-06-15
:category: Tutorial
:tags: exif

Lossless rotation of jpg files:

.. code-block:: bash

   $ for i in *.jpg; do jpegtran -rotate 90 -outfile rotate/$i $i; done


Preparing scanned images::

    -n
    -E
    -overwrite_original_in_place
    -Make=Canon
    -Model=EOS 500n
    -DateTimeOriginal=2004:01:05 12:00:00
    -CreateDate=2012:03:18 12:00:00
    -keywords=La Palma
    -UserComment<Scanner Make: Canon$/Scanner Model: FS2710$/Film Make: FUJI$/Film Type: S-200
    -Artist=Peter Reimer
    -Copyright=Peter Reimer
    -ISO=200
    -ImageUniqueID<FileName

Exiftools
