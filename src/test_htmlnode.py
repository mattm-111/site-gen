import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):


    def test_eq(self):
        node1 = HTMLNode("h1",
                           "this is dummy text",
                            ["child1", "child2", "child3", "child4"],
                            {"href": "https://fakesite.com",
                             "target": "_blank"
                             }
                             )
        node2 = HTMLNode("h1",
                           "this is dummy text",
                            ["child1", "child2", "child3", "child4"],
                            {"href": "https://fakesite.com",
                             "target": "_blank"
                             }
                             )
        
        self.assertEqual(node1, node2)




    def test_not_eq(self):
        node1 = HTMLNode("h1",
                           "this is dummy text",
                            ["child1", "child2", "child3", "child4"],
                            {"href": "https://m.com",
                             "target": "_blank"
                             }
                             )
        node2 = HTMLNode("h1",
                           "this is dummy text",
                            ["child1", "child2", "child3", "child4"],
                            {"href": "https://fakesite.com",
                             "target": "_blank"
                             }
                             )
        
        self.assertNotEqual(node1, node2)


    def test_empty_values(self):
        node1 = HTMLNode("", "", [], {})
                             
        node2 = HTMLNode("", "", [], {})
        
        self.assertEqual(node1, node2)



    def test_none_values(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)










if __name__ == "__main__":
    unittest.main()