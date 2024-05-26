class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag 
    self.value = value 
    self.children = children 
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    if self.props is None:
      return ""
    html_attributes = []
    for attribute in self.props:
      html_attributes.append(f'{attribute}="{self.props[attribute]}"') 
    return " ".join(html_attributes)
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  
