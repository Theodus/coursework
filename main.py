from graphviz import Digraph

class Class:
  def __init__(self, code, name, credits, term, prereqs):
    self.code = code
    self.name = name
    self.credits = credits
    self.term = term
    self.prereqs = prereqs

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
  Class("ENGL 102", "Composition and Rhetoric II", 3.0, 1.2, ["ENGL 101"]),
  Class("ENGR 102", "Engineering Design Lab II", 2.0, 1.2, ["ENGR 101"]),
  Class("ENGR 122", "Computation Lab II", 1.0, 1.2, []),
  Class("MATH 122", "Calculus II", 4.0, 1.2, ["MATH 121"]),
  Class("PHYS 101", "Fundamentals of Physics I", 4.0, 1.2, []),
  # Freshman 3
  Class("BIO 141", "Essential Biology", 4.5, 1.3, ["CHEM 101"]),
  Class("COOP 101", "Career Mgmt/Profess Dev", 0, 1.3, []),
  Class("ENGL 103", "Composition and Rhetoric III", 3.0, 1.3, ["ENGL 102"]),
  Class("ENGR 103", "Engineering Design Lab III", 2.0, 1.3, ["ENGR 102"]),
  Class("MATH 200", "Multivariate Calculus", 4.0, 1.3, ["MATH 122"]),
  Class("PHYS 102", "Fundamentals of Physics II", 4.0, 1.3, ["PHYS 101"]),
  # Sophomore 1
  Class("ECE 200", "Digital Logic Design", 4.0, 2.1, []),
  Class("ECE 203", "Programming for Engineers", 3.0, 2.1, []),
  Class("ENGR 201", "Eval & Pres of Exper Data I", 3.0, 2.1, []),
  Class("ENGR 220", "Fundamentals of Materials", 4.0, 2.1, ["CHEM 101", "MATH 122", "PHYS 101"]),
  Class("ENGR 231", "Linear Engineering Systems", 3.0, 2.1, ["ENGR 121"]),
  Class("PHIL 111", "Symbolic Logic I", 3.0, 2.1, []),
  # Sophomore 2
  Class("ECE 201", "Foundations of Electric Circuits", 4.0, 2.2, ["PHYS 102"]),
  Class("ECEC 201", "Adv Programming for Engineers", 3.0, 2.2, ["ECE 203"]),
  Class("ENGR 202", "Eval & Pres of Exper Data II", 3.0, 2.2, ["ENGR 201"]),
  Class("ENGR 232", "Dynamic Engineering Systems", 3.0, 2.2, ["ENGR 231"]),
  Class("MATH 221", "Discrete Mathematics", 3.0, 2.2, ["ECE 200"]),
  # Pre-Junior 1
  Class("CS 265", "Advanced Programming Tools and Techniques", 3.0, 3.1, ["ECEC 201"]),
  Class("ECE 361", "Probability for Engineers", 4.0, 3.1, ["ENGR 232"]),
  Class("ECEC 302", "Digital Systems Projects", 3.0, 3.1, ["ECE 203", "ECE 200"]),
  Class("ECEC 357", "Introduction to Computer Networks", 3.0, 3.1, ["ECE 203"]),
  Class("ECES 301", "Signals and Systems I", 4.0, 3.1, ["ECE 200", "ECE 201", "ENGR 103"]),
  # Pre-Junior 2
  Class("CS 260", "Data Structures", 3.0, 3.2, ["CS 265"]),
  Class("ECEC 204", "Design with Microcontrollers", 3.0, 3.2, ["ECE 200", "ECEC 201"]),
  Class("ECEC I399", "Vision Processing Hardware", 3.0, 3.2, []),
  Class("ECEC 353", "Systems Programming", 3.0, 3.2, ["ECEC 201"]),
  Class("ECEC 355", "Computer Architecture", 3.0, 3.2, ["ECEC 302"]),
  Class("PHIL 315", "Engineering Ethics", 3.0, 3.2, []),
  # Junior 1
  Class("ECE 303", "ECE Laboratory", 3.0, 4.1, ["ECE 201", "ENGR 103"]),
  Class("ECEC 412", "Modern Processor Design", 3.0, 4.1, ["ECEC 355"]),
  Class("ECON 201", "Principles of Microeconomics", 4.0, 4.1, []),
  Class("PHYS 201", "Fundamentals of Physics III", 4.0, 4.1, ["PHYS 102", "MATH 122"]),
  Class("PSY 101 ", "General Psychology I", 3.0, 4.1, []),
  # Junior 2
  Class("ECE 391", "Intro to Engr Design Methods", 1.0, 4.2, []),
  Class("ECEC-T 480", "Advanced Topics in Computer Architecture", 3.0, 4.2, ["ECEC 355"]),
  Class("ECEC 474", "ASIC Design I", 3.0, 4.2, ["ECE 200", "ECEC 355"]),
  Class("CS 383", "Machine Learning", 3.0, 4.2, ["CS 260", "ENGR 231", "MATH 221", "ECE 361"]),
  # Senior 1
  Class("ECE 491", "Senior Design Project I", 3.0, 5.1, ["ECE 391", "ECE 361"]),
  Class("ECE 370", "Electronic Devices", 3.0, 5.1, ["ECE 200"]),
  # Senior 2
  Class("ECE 492", "Senior Design Project II", 3.0, 5.2, ["ECE 491"]),
  # Senior 3
  Class("ECE 493", "Senior Design Project III", 4.0, 5.3, ["ECE 492"]),
  Class("PHIL 207", "Symbolic Logic II", 3.0, 5.3, ["PHIL 111"]),
  # Incomplete
  Class("TEMP COE", "ECE/COE/BMES Electives", 6.0, -1.0, []),

  # CS 303, Algorithmic Number Theory and Cryptography
  # CS 361, Concurrent Programming
  # CS 370, Operating Systems
  # CS 377, Software Security
  # ECEC 352, Secure Computer Systems: Design Concepts
  # BLAW 360, Intellectual Property and Cyber Law
  # ECON 202, Principles of Macroeconomics
]

g = Digraph(name="Classes")
g.attr(newrank="true")

terms = [0.0, 1.1, 1.2, 1.3, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1, 5.2, 5.3, -1.0]
in_progress = [5.1]

insert_ranks = ""

for i, t in enumerate(terms):
  node_color = "orange"
  if t == -1.0: node_color = "red"
  elif t < in_progress[0]: node_color = "darkgreen"
  elif t in in_progress: node_color = "blue"

  cs = [c for c in classes if c.term == t]

  term_label = "{} ({})".format(t, sum([c.credits for c in cs]))
  g.node(str(t), term_label, shape="plaintext")
  if i > 0:
    g.edge(str(terms[i-1]), str(t), style="invis")

  same_rank = " ".join(['"{}"'.format(c.code) for c in cs])
  insert_ranks += '\t{{rank=same; "{}" {}}}\n'.format(t, same_rank)

  for c in cs:
    class_label = '<{} ({})<BR /><FONT POINT-SIZE="10">{}</FONT>>'.format(
      c.code, c.credits, c.name.replace("&", "&amp;"))
    g.node(c.code, class_label, color=node_color)
    for p in c.prereqs:
      g.edge(p, c.code)

src = g.source
print(src[:-1] + insert_ranks + src[-1:])
