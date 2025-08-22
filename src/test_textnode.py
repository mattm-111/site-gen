import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://testnode:8888")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://testnode:8888")
        self.assertEqual(node, node2)

    def test_text_string(self):
        node = TextNode("", TextType.BOLD, "http://testnode:8888")
        node2 = TextNode(" ", TextType.BOLD, "http://testnode:8888")
        self.assertNotEqual(node, node2)




if __name__ == "__main__":
    unittest.main()