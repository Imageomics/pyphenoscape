# pyphenoscape

Python package to interact with the [Phenoscape Knowledgebase API](https://kb.phenoscape.org/api/v2/docs/).

## Installation

```
pip install --upgrade pip
pip install git+https://github.com/Imageomics/pyphenoscape
```

## Usage

Import main package as "pkb":

```
import phenoscape.kb as pkb
```

### Search for terms

Use the `pkb.term_search` function to search for "dorsal fin".

```python
terms = pkb.term_search("dorsal fin")
print("Found", len(terms), "terms.")

first_term = terms[0]
print("First term:")
print("\tlabel:", first_term['label'])
print("\tmatchType:", first_term['matchType'])
print("\t@id:", first_term['@id'])
print("\tisDefinedBy:", first_term['isDefinedBy'])
```

Output:

```
Found 100 terms.
First term:
	label: dorsal fin
	matchType: exact
	@id: http://purl.obolibrary.org/obo/UBERON_0003097
	isDefinedBy: http://purl.obolibrary.org/obo/uberon.owl
```

### Search for exact terms

Use the `pkb.term_search` function to search for "dorsal fin".

```python
terms = pkb.term_search("dorsal fin", match_types=["exact"])
print("Found", len(terms), "terms.")
print("Term IRI", terms[0]["@id"])
```

Output:

```
Found 1 terms.
Term IRI http://purl.obolibrary.org/obo/UBERON_0003097
```

### Lookup information about a term IRI

```python
term_details = pkb.get_term("http://purl.obolibrary.org/obo/UBERON_0003097")
print("Label", term_details["label"])
print("Definition", term_details["definition"])
print()
print(term_details)
```

Output:

```
Term IRI http://purl.obolibrary.org/obo/UBERON_0003097
Label dorsal fin
Definition Median fin located on the dorsal surface of the organism.

{'synonyms': [], 'label': 'dorsal fin', 'relationships': [{'property': {'@id': 'http://purl.obolibrary.org/obo/BSPO_0005001', 'label': 'intersects midsagittal plane of'}, 'value': {'@id': 'http://purl.obolibrary.org/obo/UBERON_00...
```

## Run Tests

From a clone of this repo within a python environment run:

```
pip install --upgrade pip
pip install -e .[test]
tox
```
