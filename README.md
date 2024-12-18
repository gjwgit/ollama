# An MLHub Package for Ollama

This [MLHUB](https://mlhub.ai/) package provides a command line tool
based on [ollama](https://github.com/ollama/ollama-python), a large
language model from Meta. See the [MLHub Desktop Survival
Guide](https://survivor.togaware.com/mlhub/ollama.html) for details.

## Usage

* To install mlhub (Ubuntu 24.04 LTS)
  ```bash
  pip3 install mlhub
  ml configure
  ```

* To install and configure the package
  ```bash
  ml install gjwgit/ollama@main
  ml configure ollama
  ml readme ollama
  ml commands ollama
  ```

* Command line tools
  ```bash
  ml chat ollama "PROMPT"
  ```

* Quick test

  ```bash
  ml chat ollama "How do I develop a great prompt for ollama?"
  ```

to see

  ```console
  To write a great prompt for OLLA (Online Language Learning
  Assistant), follow these guidelines:

	1. **Be specific**: Clearly state what you want to achieve or
   	   learn with the conversation.

	2. **Use natural language**: Write in a conversational tone, using
	   everyday language and avoiding jargon or overly technical
	   terms.

	3. **Provide context**: Give OLLA some background information
	   about your topic or question, so it can better understand your
	   needs.

	4. **Ask open-ended questions**: Encourage OLLA to provide more
   	   than just yes/no answers by asking open-ended questions that begin
	   with "what," "how," or "why."

	5. **Show what you're struggling with**: If you're having trouble
	   understanding a concept, let OLLA know so it can adapt its
	   response to your needs.

	6. **Use relevant keywords**: Include relevant keywords or phrases
	   from your language of interest to help OLLA provide more accurate
	   and targeted responses.

	7. **Be patient and flexible**: Remember that OLLA is a machine
	   learning model, so be prepared for imperfect responses and don't
	   get discouraged if it doesn't quite understand what you want.

  Here are some examples of great prompts:

	* "What's the difference between 'accordo' and 'concordo' in
	   Italian?"

    * "Can you explain the grammar rules for the subjunctive mood in
	   Spanish? I'm having trouble understanding when to use it."

    * "How do I say 'I love this city' in French? Can you give me some
	   tips on pronunciation and idiomatic expressions?"

    * "What's the most common way to express gratitude in Chinese
	  culture?"

  By following these guidelines, you can craft effective prompts that
  help OLLA provide accurate, helpful, and engaging responses.
  ```

## Options for chat

Not yet available.

* `-m`, `--model`: Specify the model to use. Supported models are
**llama3.2**, .

* `-f`, `--format`: Specify the output format.  Supported formats are
.

* `-o`, `--output`: Specify the output file name and format.
For example, `-o output.txt` will save the output text as the txt format to a
file named `output.txt` in the same directory.

*Without `-o`, by default, the output text will be printed to the console.*

Format:
`ml chat ollama [-m MODEL] [-f FORMAT] "PROMPT"`
`ml chat ollama [-m MODEL] [-o OUTPUT_FILENAME_AND_FORMAT] "PROMPT"`

Examples:
```bash
ml chat ollama -m lamma3.2 -f txt "In dart whay type of quotes should I use?"
ml chat ollama --output dart_quotes.txt "What are some quotes about dart as a programming language?"
```

## Pre-requisites:

```bash
pip install ollama
ollama pull llama3.2
```

The ollama3.2 model download is 2GB.

In python to pull the model:

```python
ollama.pull('llama3.2')
```
