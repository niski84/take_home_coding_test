
**The PII Problem**

Process PII (Personally Identifiable Information) int


----------


o JSON documents. Please use Java, JavaScript, PHP or Python to solve this problem. Extra credits for well thought out design and attention to quality.


Input to your program


A file with each line contains “PII”, information, which consists of a first name, last name, phone number, favorite color and zip code. The order and format of these lines vary in several ways, but for this test, the following three different formats are observed:

 LastName, FirstName, (703)-711-0996, Blue, 11013  FirstName LastName, Purple, 14537, 713 905 0383  FirstName, LastName, 12023, 636 121 1111, Yellow

Input file may contain invalid lines and should not interfere with the processing of subsequent valid lines. For simplicity, a line is invalid if its phone number does not contain the proper number of digits.

Output from your program

The program outputs a valid, formatted JSON object. The JSON representation should be indented with 2 spaces and the keys should be sorted in ascending alphabetical order by (last name, first name)

Successfully processed lines should result in a normalized addition to the list associated with the “entries” key. For lines that were unable to be processed, a line number i (where 0  ≤  i  <  n) for each faulty line should be appended to the list associated with the “errors” key.

Important note: Please format the JSON with exactly two spaces for every indentation. Our automated tests will not pass otherwise. Your program must execute the following way

Solution < inputfile.txt > outpufile.txt or Solution –in inputfile.txt -out outpufile.txt Attached are the sample input and output files.  
Please submit a zip file or a Git Repository with your solution.
