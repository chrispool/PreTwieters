DUTCH PHONOLOGY, WORDFORMS


The dpw.cd file contains the following fields:

    1.      IdNum
    2.      Word
    3.      IdNumLemma
    4.      PhonStrsDISC
    5.      PhonCVBr
    6.      PhonSylBCLX

The awk directory contains the following functions:

        function AddFullStops(String):                      addstop.fnc
        function InvCommaToQuote(String):                   comm2quo.fnc
        function ConvertBrackets(String):                   convbrkt.fnc
        function CountSyllables(String):                    countsyl.fnc
        function MakeStressPattern(String):                 mkstress.fnc
        function NumOfChar(String):                         numofchr.fnc
        function StripStressMarkers(String):                stripstr.fnc
        function StripSyllableMarkers(String):              stripsyl.fnc
        function SyllableMarkersToFullStops(String):        syl2stop.fnc

One function has been written in C. It can be found in the C directory:

        chngrepr (binary)
        chngrepr.c (source)
        chngrepr.exe (MS-DOS executable)

It is used as follows:

        chngrepr <File> <Representation> <Field> [<Repr> <Field>...]

Here <File> denotes the input lexicon file, <Representation> denotes
the kind of phonetic alphabet required,
      SP : SAM-PA
      CX : CELEX
      CP : CPA
and <Field> the number of the column in <File> which contains the
DISC representation. The first column is numbered 1. Fields should
be separated by a '\'. The maximum number of pairs that chngrepr can
convert in one call is 10.

These functions may be used to obtain those columns listed in the CELEX
User Guide that do not appear in the above list, as follows:

   DPW-fields in CELEX.        DPW-fields on CD-ROM 
   
   1.      IdNum               $1
   2.      PhonSAM             chngrepr{AddFullStops(PhonDISC)}
   3.      PhonCLX             chngrepr{AddFullStops(PhonDISC)}
   4.      PhonCPA             chngrepr{AddFullStops(PhonDISC)}
   5.      PhonDISC            StripSyllableMarkers(PhonSylDISC)
   6.      PhonCnt             NumOfChar(PhonDISC)
   7.      PhonSylSAM          chngrepr{PhonSylDISC}
   8.      PhonSylCLX          chngrepr{PhonSylDISC}
   9.      PhonSylBCLX         $6
   10.     PhonSylCPA          chngrepr{SyllableMarkersToFullStops(PhonSylDISC)}
   11.     PhonSylDISC         StripStressMarkers(PhonStrsDISC)
   12.     SylCnt              CountSyllables(PhonSylDISC)
   13.     PhonStrsSAM         chngrepr{InvCommaToQuote(PhonStrsDISC)}
   14.     PhonStrsCLX         chngrepr{PhonDISC}
   15.     PhonStrsCPA         chngrepr{PhonDISC}
   16.     PhonStrsDISC        $4
   17.     StrsPat             MakeStressPattern(PhonStrsDISC)
   18.     PhonCVBr            $5
   19.     PhonCV              ConvertBrackets(PhonCVBr);


For instance, to obtain PhonSAM, first reconstruct the CELEX PhonDISC column
using awk script (1).


    {
        print AddFullStops(StripSyllableMarkers(StripStressMarkers($4)));
    }

    function AddFullStops(String) {
        ...
        ...
    }

    function StripSyllableMarkers(String) {
        ...
        ...
    }

    function StripStressMarkers(String) {
        ...
        ...
    }

    (1) AN AWK SCRIPT TO OBTAIN THE PHONDISC REPRESENTATION FROM DPW.CD


Next apply chngrepr to the output file (your_PhonDISC_file) as in (2):


    chngrepr your_PhonDISC_file SP 1 > your_PhonSAM_file

    (2) HOW TO USE CHNGREPR
