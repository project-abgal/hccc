# Handwritten Cuneiform Character Collection

## About

Handwritten Cuneiform Character Collection (HCCC) is a imageset built for developing OCR system to detect
cuneiform characters from the existing hand copies of the tablets.
The construction of this dataset is undergoing now and our goal is to collect images for 100 character classes
(currently covered 50 classes) that are most frequently appeared in several corpora. 
The target glyph of character is of Ur III (Neo-Sumerian) era.

Images for each character class are contained under the directory of the class, e.g. A, AN.
The format of images is 64x64 square PNG grayscale. These are manually cleaned and arranged with 
Assyriologists and Hittitologist.

## Notice

Since we cannot distinguish glyphs of E2 and KID without context in Ur III era, we collect character images for 
that two glyph types without distinction.

## Source Documents

The images are fully acquired from [Cuneiform Digital Library Initiative](https://cdli.ucla.edu/) (CDLI) and
following public domain documents in [Internet Archive](https://archive.org).

1. Thureau-Dangin, François. [Recueil de tablettes chaldéennes](https://archive.org/details/recueildetablett00thuruoft). *Ernest Leroux*. 1903.
2. Hussey, Mary Inda. [Sumerian tablets in the Harvard Semitic Museum Part II](https://archive.org/details/sumeriantabletsi02huss). *Harvard University*. 1915.
3. Langdon, Stephan. [Tablets from the archives of Drehem with a complete account of the origin of the Sumerian calendar, translation, commentary and 23 plates](https://archive.org/details/tabletsfromarchi00languoft). *Librairie orientaliste Paul Geuthner*. 1911
4. Nies, B. James. [Ur Dynasty Tablets](https://archive.org/details/urdynastytablets00niesuoft). *J. C. Hinrichs*. 1920.
5. Price, Ira Maurice. [The great cylinder inscriptions A & B of Gudea](https://archive.org/details/greatcylinderins01pricuoft). *J. C. Hinrichs*. 1899.
6. Langdon, Stephan. [Langdon, Stephan. Babylonian Liturgies](https://archive.org/details/babylonianliturg00langrich). *Librairie orientaliste Paul Geuthner*. 1913.
7. Genouillac, de Henri [Textes Économiques D'Oumma De L’époque D’Our](https://archive.org/details/textesconomiqu00genouoft). *Librairie orientaliste Paul Geuthner*. 1922.

## TODO

* Increase the size of the datasets
* Collect images for the all target character classes.
* Collect images for the glyphs of other era (esp. Neo-Assyrian and Hittite)

## Citations
If you use the dataset in your work, please cite it as:

BibTeX
```
@Inproceedings{Yamauchi:2018,
author = {Kenji Yamauchi and Hajime Yamamoto and Wakaha Mori},
title = {Building A Handwritten Cuneiform Character Imageset},
booktitle = {Proceedings of 11th Language Resources and Evaluation Conference},
year = {2018}
},
```

## License

Follow the term of use of [Internet Archive](https://archive.org/about/terms.php) and [CDLI](https://cdli.ucla.edu/?q=terms-of-use).

## Contributors

* Yamauchi, Kenji. Kyoto University. yamauchi@nlp.ist.i.kyoto-u.ac.jp (Technical Support)
* Yamamoto, Hajime. Kyoto University (Hittitologist)
* Mori, Wakaba.  Kokushikan University (Assyriologist)