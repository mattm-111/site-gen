from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode



def main():


    dummy_node = TextNode("Hello World", TextType.LINK, "https://fakesite.com")
    dummy_text = dummy_node.__repr__()

    print(f' dummy node = {dummy_text}')

    dummy_html = HTMLNode("h1",
                           "this is dummy text",
                            ["child1", "child2", "child3", "child4"],
                            {"href": "https://fakesite.com",
                             "target": "_blank"
                             }
                             )
    
    html_text = dummy_html.__repr__()
    print(f'dummy HTML = {html_text}')

    print(".\n.\n.\n.\n.")

    last_test = dummy_html.props_to_html()

    print(last_test)
          







if __name__ == "__main__":
    main()