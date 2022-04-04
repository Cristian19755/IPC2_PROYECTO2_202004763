import graphviz

class graficar:
  def grafica(patron, name):
    name2 = str(name)+'.gv'
    h = graphviz.Digraph('g', filename=name2, format='png',
                        node_attr={'shape': 'record', 'height': '.1'})
    h.node('tab', label='''<<TABLE>'''+patron+'''</TABLE>>''')
    h.node(name)
    h.view()
