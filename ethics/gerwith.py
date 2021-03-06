import numpy as np

"""
Philosopher Alan Gewirth is known for ethical rationalism with his moral principle
the "Principle of Generic Consistency" (PCG, pgc). Every agent must act
in accodrance with his/her own and all other agents' generic rights.
For prospective purposive agents (PPA) we can derive claims.   
"""

class PPA():
    """
    For a PPA (ppa) we define features as it relates to rights and freedom.
    """
    def __init__(self, name, context, purpose):
        """
        Initialize with an arbitrarily chosen name of an individual, context, and purpose.
        """
        self.name = name
        self.context = context
        self.purpose = purpose

    def pgc():
       	"""
   	For some PPA we outline its irght to freedom and well-being.
    	"""
        P1 = True # P1 is "I act voluntarily on purpose."
        if P1:
            P1a = True # "I am a PPA."
        C2 = True # "My purpose is good for me."
