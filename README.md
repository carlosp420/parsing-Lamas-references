## Requirements
Requires redis, and [anystyle-parser](https://github.com/inukshuk/anystyle-parser)

## Workflow
* Use the MS Word document of the Butterfly Bibliography and convert to text of
  1 column.
* Save the MS Word file as .html format (so that we preserve the italics on 
  butterfly names and other formatting).
* Convert the .html file to markdown format using pandoc (avoid wrapping the lines):
  ``pandoc file.html -o file.md --no-wrap``
* Keep only the biblio references in the .md file by removing any uninformative
  text. See image below:
  
![](https://rawgit.com/carlosp420/parsing-Lamas-references/master/media/example_of_input.png)

* Add the author names to all the references with the Python script:
  ``python fill_in_authors.py -i file.md``:
* The output file (``output.txt``) should look [like this](https://github.com/carlosp420/parsing-Lamas-references/blob/master/lamas_A_with_authors.txt):

```markdown
**Aaron, Eugene Murray**. 1884a. *Erycides okeechobee*, Worthington. *Papilio* 4(1): 22 (20 February) [Cuba]
**Aaron, Eugene Murray**. 1884b. *Eudamus tityrus*, Fabr., and its varieties. *Papilio* 4(2): 26-30 (15 March) [Central America, Antilles]
**Aaron, Eugene Murray**. 1885\. *Pamphila baracoa*, Luc. in Florida. *Papilio* 4(7/8): 150 (29 January) [West Indies]
**Aaron, Eugene Murray**. 1888\. The determination of Hesperidae. *Entomologica ameri-cana* 4(7): 142-143 (October) [general]
**Aaron, Eugene Murray**. 1889\. A vulnerable "new species". *Entomologica americana* 5(12): 221-226 (December) [*Agraulis vanillae* (Linnaeus)]
**Aaron, Eugene Murray**. 1890\. North American Hesperidae. *Entomological News* 1(2): 23-26 (15 January) [*Erycides urania* Doubleday, *Eudamus hesus* Doubleday; Mexico]
**Aaron, Eugene Murray**. 1893\. New localities for *Papilio homerus*. *Canadian Ento-mologist* 25(10): 258-259 (5 October) [Jamaica, Haiti, República Dominicana]
**Aaron, Eugene Murray**. 1894\. *The butterfly hunters in the Caribbees*. New York, Charles Scribner's Sons. xiii + [1] + 269 pp., 8 pls., 1 fig., 1 map. [general; biogeography]
```

Text between double asterisks indicate bold font face and text between single 
asterisks indicate italics.

* Find some spare time and manually tag many references so that we can use the data
  to train the machine-learning biblio parser. Follow [this model](https://github.com/carlosp420/parsing-Lamas-references/blob/master/training_A.txt)
