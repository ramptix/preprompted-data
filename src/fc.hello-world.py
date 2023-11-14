from preprompt import pf, Definitions

@pf
def plugin():
  """Run a plugin example."""
  return {
    "response": "Hello, World!"
  }

__definitions__: Definitions = {
  "preprompt-function": plugin(),
  "openai": None
}
