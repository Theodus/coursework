from graphviz import Digraph
from itertools import izip

class Class:
  def __init__(self, code, name, credits, term, prereqs):
    self.code = code
    self.name = name
    self.credits = credits
    self.term = term
    self.prereqs = prereqs

# Class("", "", 0, 0.0, [])

classes = [
  # Transfer (AP)
  Class("CS 190", "Selected Computer Language", 3.0, 0.0, []),
  Class("SPAN 101", "Spanish I", 4.0, 0.0, []),
  Class("TGFE 099", "Transfer General Free Elective", 4.0, 0.0, []),
  # Freshman 1
  Class("CHEM 101", "General Chemistry I", 3.5, 1.1, []),
  Class("ENGL 101", "Composition and Rhetoric I", 3.0, 1.1, []),
  Class("ENGR 100", "Beginning CAD for Design", 1.0, 1.1, []),
  Class("ENGR 101", "Engineering Design Lab I", 2.0, 1.1, []),
  Class("ENGR 121", "Computation Lab I", 2.0, 1.1, []),
  Class("MATH 121", "Calculus I", 4.0, 1.1, []),
  Class("UNIV 101", "The Drexel Experience", 1.0, 1.1, []),
  # Freshman 2
  Class("CHEM 102", "General Chemistry II", 4.5, 1.2, ["CHEM 101"]),
  Class("CIVC 101", "Intro to Civic Engagement", 1.0, 1.2, []),
  Class("ENGL 102", "Composition and Rhetoric II", 0, 1.2, ["ENGL 101"]),
  Class("ENGR 102", "Engineering Design Lab II", 0, 1.2, ["ENGR 101"]),
  Class("ENGR 122", "Computation Lab II", 0, 1.2, []),
  Class("MATH 122", "Calculus II", 0, 1.2, ["MATH 121"]),
  Class("PHYS 101", "Fundamentals of Physics I", 0, 1.2, []),
  # Freshman 3
  Class("BIO 141", "Essential Biology", 4.5, 1.3, ["CHEM 101"]),
  Class("COOP 101", "Career Mgmt/Profess Dev", 0, 1.3, []),
  Class("ENGL 103", "Composition and Rhetoric III", 3.0, 1.3, ["ENGL 102"]),
  Class("ENGR 103", "Engineering Design Lab III", 2.0, 1.3, ["ENGR 102"]),
  Class("MATH 200", "Multivariate Calculus", 4.0, 1.3, ["MATH 122"]),
  Class("PHYS 102", "Fundamentals of Physics II", 4.0, 1.3, ["PHYS 101"]),
]

g = Digraph(name="Classes")

terms = [-1.0, 0.0, 1.1, 1.2, 1.3]
current_term = 3.1

for i, t in enumerate(terms):
  term_graph_attrs = {"rank": "same", "style": "invis"}
  term_node_attrs = {}
  if t == -1.0: term_node_attrs["color"] = "red"
  elif t < current_term: term_node_attrs["color"] = "darkgreen"
  elif t == current_term: term_node_attrs["color"] = "orange"

  with g.subgraph(name="cluster_"+str(t), graph_attr=term_graph_attrs, node_attr=term_node_attrs) as sg:
    sg.node(str(t), shape="plaintext", style="invis")
    if i > 0:
      g.edge(str(terms[i-1]), str(t), style="invis")

    cs = filter(lambda c: c.term == t, classes)
    for c in cs:
      sg.node(c.code, c.code)
      for p in c.prereqs:
        sg.edge(p, c.code)

print(g.source)
g.render("tmp.gv", view=True)
