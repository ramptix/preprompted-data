from preprompt import of, pf, Definitions

# preprompt functions
@pf()
def hello(name: str):
  """Say hello

  Args:
      name (str): Name
  """
  return {
    "response": "Hello, {}!".format(name)
  }

# openai function calling
@of()
def goodbye(name: str):
  """Says goodbye

  Args:
      name (str): Name
  """
  return {
    "response": "Bye, {}!".format(name)
  }

__definitions__: Definitions = {
  "preprompt-function": hello,
  "openai": goodbye
}
