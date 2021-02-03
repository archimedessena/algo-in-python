class GeometricProgression(Progression): # inherit from Progression
    ”””Iterator producing a geometric progression.”””
    
    def init (self, base=2, start=1):
    ”””Create a new geometric progression.
    
    base the fixed constant multiplied to each term (default 2)
    start the first term of the progression (default 1)
    ”””
     super(). init (start)
     self. base = base
    
     def advance(self): # override inherited version
     ”””Update current value by multiplying it by the base value.”””
     self. current = self. base