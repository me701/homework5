import numpy as np
import matplotlib.pyplot as plt

class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return "Point(%.6F, %.6f) " % (self.x, self.y)
      
    def __repr__(self):
        return str(self)
    
    def __matmul__(self, P):
        new_P = Point(self.x*P.x, self.y*P.y)
        return new_P
    
    def __add__(self, P):
        return Point(self.x+P.x, self.y+P.y)
    
    def __mul__(self, a):
        return Point(self.x*a, self.y*a)
  
        
class Ray:
    
    def __init__(self, origin, direction):
        self.origin = origin
        # ensure the direction is normalized to unity, i.e., cos^2 + sin^2 = 1
        norm = np.sqrt(direction.x**2 + direction.y**2)
        self.direction = Point(direction.x/norm, direction.y/norm)
            
    def __str__(self):
        return "Ray: r_0(%10.6f, %10.6f), d(%.6f %.6f) " % \
               (self.origin.x, self.origin.y, self.direction.x, self.direction.y)

class Node:

    def contains(self, p):
        """Does the node contain the point?"""
        raise NotImplementedError

    def intersections(self, r):
        """Where does the node intersect the ray?"""
        raise NotImplementedError

class Primitive(Node):
    
    def __init__(self, surface, sense):
        self.surface, self.sense = surface, sense
        
    def contains(self, p):
        return (self.surface.f(p) < 0) == self.sense
        
    def intersections(self, r):
        return self.surface.intersections(r)
        

class Operator(Node):
    
    def __init__(self, L, R):
        self.L, self.R = L, R
        # some super checking algorithm

    def contains(self, p):
        raise NotImplementedError

    def intersections(self, r):
        # get intersections with left and right nodes
        pointsL = self.L.intersections(r)
        pointsR = self.R.intersections(r)
        # return the concatenated result (think lists!)
        return pointsL + pointsR
      

class Union(Operator):
    
    def __init__(self, L, R):
        Operator.__init__(L, R)
        
    def contains(self, p):
        inL = self.L.contains(p)
        inR = self.R.contains(p)
        return inL or inR
        
class Intersection(Operator):
    
    def __init__(self, L, R):
        Operator.__init__(L, R)
           
             
class Surface:
    
    def f(self, p):
        raise NotImplementedError
        
    def intersections(self, r):
        raise NotImplementedError
        
        
class QuadraticSurface(Surface):
    
    def __init__(self, A=0.0, B=0.0, C=0.0, D=0.0, E=0.0, F=0.0):
        self.M = np.array([[2*A,   C,   D],
                           [  C, 2*B,   E],
                           [  D, E,   2*F]])
        self.A, self.B, self.C, self.D, self.E, self.F = A,B,C,D,E,F
    
    def intersections(self, r):
        r0 = np.array([r.origin.x, r.origin.y, 1])
        d = np.array([r.direction.x, r.direction.y, 0])
        
        
        a = d@(self.M@d) 
        b = 2*d@(self.M@r0) # account from 2 in notes
        c = r0@(self.M@r0)
        
        tvals = []
        if abs(a) < 1e-14:
            # take to be linear
            # t*b + c = 0
            t = -c /(b)
            tvals = [t]
        else:
            if b**2 > 4*a*c:
                t0 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
                t1 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)         
                tvals = [t0, t1]
            elif b**2 == 4*a*c:
                tvals = [(-b + np.sqrt(b**2 - 4*a*c))/(2*a)]
        tvals.sort()
        ints = []
        for t in tvals:
            x = r0[0] + d[0]*t
            y = r0[1] + d[1]*t
            ints.append(Point(x, y))  
        return ints
    def f(self, p):
        r = np.array([p.x, p.y, 1])
        return 0.5*r.T@self.M@r
        
class Plane(QuadraticSurface):
    def __init__(self, slope, intercept):
        QuadraticSurface.__init__(self, D=-slope, E=1, F=-intercept)


class PlaneV(QuadraticSurface):
    def __init__(self, x0 = 0):
        QuadraticSurface.__init__(self, D=1, F=-x0)

class PlaneH(QuadraticSurface):
    def __init__(self, y0 = 0):
        QuadraticSurface.__init__(self, E=1, F=-y0)
        
class Circle(QuadraticSurface):
    def __init__(self, x0=0, y0=0, r=1):
        QuadraticSurface.__init__(self, A=1, B=1, C=0, D=-2*x0, E=-2*y0, F=x0**2+y0**2-r**2)

               
class Region:
    
    def __init__(self):
        self.node = None
    
    def append(self, node=None, surface=None, operation="U", sense=False):
        assert((node and not surface) or (surface and not node))
        if isinstance(surface, Surface):
            node = Primitive(surface, sense)
        if self.node is None:
            self.node = node
        else:
            O = Union if operation == "U" else Intersection
            self.node = O(self.node, node)
          
    def intersections(self, r):
        pass
        
class Geometry:
    
    # Attributes can be defined in the body of a class.  However, these
    # become "static" values that are the same for every object of the class.
    # Hence, they can be accessed either through object.attribute or 
    # classname.attribute.
    noregion = -1    
    
    def __init__(self,  xmin, xmax, ymin, ymax):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.regions = []
        
    def add_region(self, r):
        self.regions.append(r)

    def find_region(self, p):
        region = Geometry.noregion
        # look for the region containing p.
        return region
        
    def plot(self, nx, ny):
        pass
        
