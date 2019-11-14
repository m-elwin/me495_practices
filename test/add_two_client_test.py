#!/usr/bin/env python
""" Create a unittest node that tests out the add_two service"""
import unittest
import rospy
import me495_practices.hardmath as hardmath
from me495_practices.srv import TwoResult

class HardCaseNode(unittest.TestCase):
    def __init__(self, *args):
        super(HardCaseNode, self).__init__(*args)
        rospy.init_node("test_client")

    def test_a_node(self):
        rospy.wait_for_service("add_two")
        add_two = rospy.ServiceProxy("add_two", TwoResult)
        resp = add_two(2, 3)
        self.assertEqual(resp.output, 5)
    
    def test_add_zeros(self):
        rospy.wait_for_service("add_two")
        add_two = rospy.ServiceProxy("add_two", TwoResult)
        resp = add_two(0, 0)
        self.assertEqual(resp.output, 0)

if __name__ == "__main__":
    import rostest
    rostest.rosrun('me495_practices', "hard_case_node", HardCaseNode)
