import unittest
from main import Poly, Point, Ray, Line

class TestPoint(unittest.TestCase):
    def test_point(self):
        p = Point(1,1)
        p2 = Point(1,1)
        p3 = Point(1,2)
        p4 = Point(2,1)
        self.assertTrue(p == p2)
        self.assertFalse(p == p3)
        self.assertFalse(p == p4)
        
        r = p.cast_ray('u')
        self.assertEqual(r,Ray(p,'u'))
    
    def test_get_neighbors(self):
        p = Point(1,1)
        neighbors = p.get_neighbors()
        self.assertTrue(Point(0.5,0.5) in neighbors)
        self.assertTrue(Point(0.5,1.5) in neighbors)
        self.assertTrue(Point(1.5,0.5) in neighbors)
        self.assertTrue(Point(1.5,1.5) in neighbors)
    
    def test_radiate(self):
        p = Point(5,1)
        rays = p.radiate()
        self.assertTrue(Ray(p,'u') in rays)
        self.assertTrue(Ray(p,'d') in rays)
        self.assertTrue(Ray(p,'l') in rays)
        self.assertTrue(Ray(p,'r') in rays)

class TestRay(unittest.TestCase):
    def test_ray(self):
        r1 = Ray(Point(1,1),'u')
        r2 = Ray(Point(1,1),'u')
        r3 = Ray(Point(1,2),'u')
        r4 = Ray(Point(1,1),'l')

        self.assertEqual(r1,r2)
        self.assertNotEqual(r1,r3)
        self.assertNotEqual(r1,r4)

class TestLine(unittest.TestCase):
    def test_line_orientation(self):
        vertical = Line(Point(1,1),Point(1,3))
        horizontal = Line(Point(1,1),Point(3,1))
        niether = Line(Point(1,1),Point(3,3))
        
        self.assertEqual(vertical.orientation(),'v')
        self.assertEqual(horizontal.orientation(),'h')
        self.assertFalse(niether.orientation())
    
    def test_intersect_ray(self):
        vertical = Line(Point(1,1),Point(1,3))
        horizontal = Line(Point(1,1),Point(3,1))

        lower = Point(2,0)
        lefter = Point(0,2)

        self.assertFalse(vertical.intersect_ray(lower.cast_ray('u')))
        self.assertFalse(vertical.intersect_ray(lower.cast_ray('d')))
        self.assertFalse(vertical.intersect_ray(lower.cast_ray('l')))
        self.assertFalse(vertical.intersect_ray(lower.cast_ray('r')))

        self.assertTrue(horizontal.intersect_ray(lower.cast_ray('u')))
        self.assertFalse(horizontal.intersect_ray(lower.cast_ray('d')))
        self.assertFalse(horizontal.intersect_ray(lower.cast_ray('l')))
        self.assertFalse(horizontal.intersect_ray(lower.cast_ray('r')))

        self.assertFalse(vertical.intersect_ray(lefter.cast_ray('u')))
        self.assertFalse(vertical.intersect_ray(lefter.cast_ray('d')))
        self.assertFalse(vertical.intersect_ray(lefter.cast_ray('l')))
        self.assertTrue(vertical.intersect_ray(lefter.cast_ray('r')))

        self.assertFalse(horizontal.intersect_ray(lefter.cast_ray('u')))
        self.assertFalse(horizontal.intersect_ray(lefter.cast_ray('d')))
        self.assertFalse(horizontal.intersect_ray(lefter.cast_ray('l')))
        self.assertFalse(horizontal.intersect_ray(lefter.cast_ray('r')))


class TestPoly(unittest.TestCase):
    def test_poly(self):
        p1 = Point(1,1)
        p2 = Point(1,3)
        p3 = Point(3,3)
        p4 = Point(3,1)
        l1 = Line(p1,p2)
        l2 = Line(p2,p3)
        l3 = Line(p3,p4)
        l4 = Line(p4,p1)
        p = Poly([l1,l2,l3,l4])

        # # Create the set of inner point:
        inner = set()
        for x in range(1,4):
            for y in range(1,4):
                inner.add(Point(x,y))

        for x in range(5):
            for y in range(5):
                point = Point(x,y)
                if point in inner:
                    self.assertTrue(point in p)
                else:
                    self.assertFalse(point in p)
                

if __name__ == '__main__':
    unittest.main()