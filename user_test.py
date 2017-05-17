from direct_p import *

print 'Direct task of magnetometry for simple figures'
print 'Available figures: '
print '1.uniformly magnetized sphere'
print '2.Horizonlal cylinder'
print '3.Cylinder with slanting magnetization'
print '4.Restricted vertical stock'
print '5.Deep stock'

def test(fig = input('Enter the number of desired figure: ')):
    if fig == 1:
        test1 = Sphere(input('Enter the h value: '), input('Enter the J value: '), input('Enter the r value: '))
        test1.gamma_sphere()
        test1.nTl_sphere()
        test1.get_sphere_output()
        test1.visualize_sphere()
    elif fig == 2:
        test2 = Cylinder(input('Enter the h value: '), input('Enter the r value: '), input('Enter the sigma value: '))
        test2.gamma_cylinder()
        test2.nTl_cylinder()
        test2.get_cylinder_output()
        visualize(test2.get_Ha2_nTl(), test2.get_Za2_nTl())
    elif fig == 3:
        test3 = Cylinder_slanting_m(input('Enter the h value: '), input('Enter the r value: '), input('Enter the sigma value: '))
        test3.gamma_slanting_m()
        test3.nTl_sl_cylinder()
        test3.get_slanting_m()
        visualize(test3.get_Ha3_nTl(), test3.get_Za3_nTl())
    elif fig == 4:
        test3 = Stock(input('Enter the h value: '), input('Enter the r value: '),input('Enter the sigma value: '),input('Enter the h1 value: '), input('Enter the a vakue: '))
        test3.gamma_stock()
        test3.nTl_stock()
        test3.get_stock()
        visualize(test3.get_Ha4_nTl(), test3.get_Za4_nTl())
    elif fig == 5:
        test5 = Stock_deep(input('Enter the h value: '),input('Enter the r value: '),input('Enter the J value: '))
        test5.gamma_deep_stock()
        test5.nTl_deep_stock()
        test5.get_deep_stock()
        visualize(test5.get_Ha5_nTl(),test5.get_Za5_nTl())
    else:
        print "You probably entered the wrong number!"
        test()

test()