# Grammar-test-input-generation

In order to clone the repo with the submodules, you can run : 

````
git submodule update --init --recursive
```

To pull from existing submodules : 
````
git pull --recurse-submodules 
````

## Grammarinator Refactoring 

Use antlr 4.11.1 jar file.

```
wget https://www.antlr.org/download/antlr-4.11.1-complete.jar
```

Create an `.env` file and add the path to this jar `ANTLR_JAR_PATH=`

## Grammarinator_fuzzing

In order to run it as a package, run this :

```
pip install -e grammarinator_fuzzing/
```

## custom_generator_sql

In order to run it as a package, run this :

```
pip install -e custom_generator_sql/
```

## cfg2pc

```
pip install -e cfg2pc/
```

## GrammarRefactoring 

````
pip install -e GrammarRefactoring/
````

