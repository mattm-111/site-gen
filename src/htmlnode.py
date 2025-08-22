


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props




    def to_html(self):
        raise NotImplementedError
    

    def props_to_html(self):
        if self.props is None:
            return ""
        temp_list = []
        
        for k, v in self.props.items():
            temp_list.append(f' {k}="{v}"')
        return ("".join(temp_list))
    

    def __repr__(self):
        return f'HTMLNode = (Tag = {self.tag}, Value = {self.value}\n Children = {self.children}\n Props = {self.props})'
    

    def __eq__(self, other):
        if not isinstance(self, HTMLNode) or not isinstance(other, HTMLNode):
            raise Exception("stop trying to break my stuff")
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

            



