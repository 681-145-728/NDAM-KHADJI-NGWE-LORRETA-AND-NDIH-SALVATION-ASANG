# -*- coding: utf-8 -*-
"""


@author: laureta
"""

def tower_of_hanoi(n, source, target, auxiliary):
    """

    
    Parameters:
        n (int): Number of disks 
        source (str): Name of the source 
        target (str): Name of the target 
        auxiliary (str): Name of the auxiliary 
    """
    if n == 1:
        # Move disk 1 from {source} to {target}
        print(f"Move disk 1 from {source} to {target}")
        return
    else:
        # Move n-1 disks from source to auxiliary using target as auxiliary
        tower_of_hanoi(n-1, source, auxiliary, target)
        
        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")
        
        # Move n-1 disks from auxiliary to target using source as auxiliary
        tower_of_hanoi(n-1, auxiliary, target, source)

# Test the function with 3 disks
tower_of_hanoi(3, 'A', 'C', 'B')
