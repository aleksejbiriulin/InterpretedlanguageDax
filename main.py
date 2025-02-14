import os
import sys

class Parse_str:
  type_parse = ""
  parser_string = ""
  
  def __init__(self, type_parse, parser_string):
    self.type_parse = type_parse
    self.parser_string = parser_string
  
    
class For(Parse_str):
  
  def __init__(self, parser_string):
    super().__init__("for", parser_string)


class While(Parse_str):
  
  def __init__(self, parser_string):
    super().__init__("for", parser_string)    
    
  
class If(Parse_str):
  
  def __init__(self, parser_string):
    super().__init__("for", parser_string)
    
class Elif(Parse_str):
  
  def __init__(self, parser_string):
    super().__init__("for", parser_string)
  
  
class Else(Parse_str):
  
  def __init__(self, parser_string):
    super().__init__("for", parser_string)
  
  
class Variable(Parse_str):
  
  def __init__(self, parser_string):
    super().__init__("Varible", parser_string)
  
  
class Block:
  list_childs : list["Block" | Parse_str] = []
  type_block  : str = ""
  
  def __init__(self, type_block : str = "global"):
    self.type_block = type_block
    
  def push(self, block: "Block"):
    self.list_childs.append(block)
    
    
def parse(lines : list[str]):
  stack_blocks : list[Block] = [Block]
  tabs_now: int = 0
  for line in lines:
    count_tabs = 0
    line = line.rstrip()
    if line == "":
      continue
    line = line.rstrip()
    line = line.replace("    ", "\t").replace(" ", " ").replace(" ", " ")
    while (count_tabs < len(line)):
      if (line[count_tabs] != "\t"):
        break
      count_tabs += 1
      line = line[count_tabs:]
      if count_tabs == tabs_now:
        if line.startswith("if"):
          line = line[2:].rstrip()
          stack_blocks[-1].push(If(line))
        elif line.startswith("elif"):
          line = line[4:].rstrip()
          stack_blocks[-1].push(Elif(line))
        elif line.startswith("else"):
          line = line[4:].rstrip()
          stack_blocks[-1].push(Else(line))
        elif line.startswith("for"):   
          line = line[3:].rstrip()
          stack_blocks[-1].push(For(line))
        elif line.startswith("while"):
          line = line[5:].rstrip()
          stack_blocks[-1].push(While(line))
        elif line.startswith("def"):
          line = line[3:].rstrip()
          # тут надо придумать более сложную идею
      if count_tabs < tabs_now:
        stack_blocks.pop()
      if count_tabs > tabs_now:
        stack_blocks.append(Block())
     
      

if __name__ == "__main__":
  file_name = sys.argv[1]
  with open(file=file_name, mode="r") as file:
    print(type(file))
    lines = file.readlines()
  parse(lines)
    
  
  