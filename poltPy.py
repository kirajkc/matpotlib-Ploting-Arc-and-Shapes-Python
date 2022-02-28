import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Arc
          

points1={
     "Contour600": {
          "Exterior": [
               [
                    [
                         0.0,
                         15.0,
                         -0.0
                    ],
                    [
                         1537.91004,
                         15.0,
                         -0.0
                    ],
                    [
                         1755.67386,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {
                    "1": [
                         [
                              770.64993,
                              853.60414,
                              -0.0
                         ],
                         [
                              1070.64993,
                              853.60414,
                              -0.0
                         ],
                         [
                              1070.64993,
                              1250.0,
                              -0.0
                         ],
                         [
                              770.64993,
                              1250.0,
                              -0.0
                         ]
                    ]
               }
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour601": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1755.67386,
                         -0.0,
                         -0.0
                    ],
                    [
                         1873.62446,
                         668.93112,
                         -0.0
                    ],
                    [
                         1638.85739,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ],
               [
                    [
                         1510.62722,
                         585.93112,
                         -0.0
                    ],
                    [
                         1710.62722,
                         585.93112,
                         -0.0
                    ],
                    [
                         1710.62722,
                         745.93112,
                         -0.0
                    ],
                    [
                         1510.62722,
                         745.93112,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {
                    "1": [
                         [
                              770.64993,
                              -0.0,
                              -0.0
                         ],
                         [
                              1070.64993,
                              -0.0,
                              -0.0
                         ],
                         [
                              1070.64993,
                              853.60414,
                              -0.0
                         ],
                         [
                              770.64993,
                              853.60414,
                              -0.0
                         ]
                    ]
               },
               {}
          ],
          "Arc": [
               [],
               []
          ],
          "PointOnArc": [
               [],
               []
          ]
     },
     "Contour602": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1638.85739,
                         -0.0,
                         -0.0
                    ],
                    [
                         1133.82461,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {}
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour603": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1133.82461,
                         -0.0,
                         -0.0
                    ],
                    [
                         836.86534,
                         735.0,
                         -0.0
                    ],
                    [
                         0.0,
                         735.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {}
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour604": {
          "Exterior": [
               [
                    [
                         0.0,
                         15.0,
                         -0.0
                    ],
                    [
                         1537.90561,
                         15.00037,
                         -0.0
                    ],
                    [
                         1537.90555,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ],
               [
                    [
                         1381.82307,
                         15.00037,
                         -0.0
                    ],
                    [
                         1537.90561,
                         15.00037,
                         -0.0
                    ],
                    [
                         1537.90555,
                         95.00075,
                         -0.0
                    ],
                    [
                         1381.82307,
                         95.00075,
                         -0.0
                    ]
               ],
               [
                    [
                         1381.82307,
                         746.66925,
                         -0.0
                    ],
                    [
                         1537.90555,
                         746.66925,
                         -0.0
                    ],
                    [
                         1537.90555,
                         826.66925,
                         -0.0
                    ],
                    [
                         1381.82307,
                         826.66925,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {
                    "1": [
                         [
                              1537.90555,
                              826.66925,
                              -0.0
                         ]
                    ]
               },
               {},
               {}
          ],
          "Arc": [
               [],
               [],
               []
          ],
          "PointOnArc": [
               [],
               [],
               []
          ]
     },
     "Contour605": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1537.90809,
                         -0.0,
                         -0.0
                    ],
                    [
                         1537.90809,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ],
               [
                    [
                         1381.82307,
                         228.33525,
                         -0.0
                    ],
                    [
                         1537.90809,
                         228.33525,
                         -0.0
                    ],
                    [
                         1537.90809,
                         308.33525,
                         -0.0
                    ],
                    [
                         1381.82307,
                         308.33525,
                         -0.0
                    ]
               ],
               [
                    [
                         1381.82307,
                         960.00125,
                         -0.0
                    ],
                    [
                         1537.90809,
                         960.00125,
                         -0.0
                    ],
                    [
                         1537.90809,
                         1040.00125,
                         -0.0
                    ],
                    [
                         1381.82307,
                         1040.00125,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {
                    "1": [
                         [
                              1537.90809,
                              308.33525,
                              -0.0
                         ],
                         [
                              1537.90809,
                              1040.00125,
                              -0.0
                         ]
                    ]
               },
               {},
               {}
          ],
          "Arc": [
               [],
               [],
               []
          ],
          "PointOnArc": [
               [],
               [],
               []
          ]
     },
     "Contour606": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1537.91063,
                         -0.0,
                         -0.0
                    ],
                    [
                         1537.91063,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ],
               [],
               [
                    [
                         1381.82307,
                         441.66725,
                         -0.0
                    ],
                    [
                         1537.91063,
                         441.66725,
                         -0.0
                    ],
                    [
                         1537.91063,
                         521.66725,
                         -0.0
                    ],
                    [
                         1381.82307,
                         521.66725,
                         -0.0
                    ]
               ],
               [
                    [
                         1381.82307,
                         1173.33325,
                         -0.0
                    ],
                    [
                         1537.91063,
                         1173.33325,
                         -0.0
                    ],
                    [
                         1381.82307,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {
                    "1": [
                         [
                              1537.91063,
                              521.66725,
                              -0.0
                         ]
                    ]
               },
               {},
               {},
               {}
          ],
          "Arc": [
               [],
               [
                    [
                         1067.69263,
                         673.77258,
                         -0.0
                    ],
                    [
                         577.29999,
                         576.22742,
                         -0.0
                    ],
                    [
                         1067.69263,
                         673.77258,
                         -0.0
                    ]
               ],
               [],
               []
          ],
          "PointOnArc": [
               [],
               [
                    [
                         773.72373,
                         870.19632,
                         0.0
                    ],
                    [
                         871.26889,
                         379.80368,
                         0.0
                    ]
               ],
               [],
               []
          ]
     },
     "Contour607": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1537.91316,
                         -0.0,
                         -0.0
                    ],
                    [
                         1537.9133,
                         734.99925,
                         -0.0
                    ],
                    [
                         0.0,
                         735.0,
                         -0.0
                    ]
               ],
               [
                    [
                         1381.82307,
                         -0.0,
                         -0.0
                    ],
                    [
                         1537.91316,
                         3.33325,
                         -0.0
                    ],
                    [
                         1381.82307,
                         3.33325,
                         -0.0
                    ]
               ],
               [
                    [
                         1381.82307,
                         654.99925,
                         -0.0
                    ],
                    [
                         1537.91316,
                         654.99925,
                         -0.0
                    ],
                    [
                         1537.9133,
                         734.99925,
                         -0.0
                    ],
                    [
                         1381.82307,
                         734.99925,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {},
               {},
               {}
          ],
          "Arc": [
               [],
               [],
               []
          ],
          "PointOnArc": [
               [],
               [],
               []
          ]
     },
     "Contour608": {
          "Exterior": [
               [
                    [
                         0.0,
                         15.0,
                         -0.0
                    ],
                    [
                         836.86534,
                         15.0,
                         -0.0
                    ],
                    [
                         1335.83772,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {}
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour609": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1335.83772,
                         -0.0,
                         -0.0
                    ],
                    [
                         1840.87051,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {
                    "1": [
                         [
                              304.0325,
                              726.94239,
                              -0.0
                         ],
                         [
                              1540.35048,
                              1250.0,
                              -0.0
                         ],
                         [
                              304.0325,
                              1250.0,
                              -0.0
                         ]
                    ]
               }
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour610": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1840.87051,
                         -0.0,
                         -0.0
                    ],
                    [
                         1873.62446,
                         81.06888,
                         -0.0
                    ],
                    [
                         1667.51037,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {
                    "1": [
                         [
                              304.0325,
                              -0.0,
                              -0.0
                         ],
                         [
                              1540.35048,
                              -0.0,
                              -0.0
                         ],
                         [
                              1604.0325,
                              26.94239,
                              -0.0
                         ],
                         [
                              1604.0325,
                              776.94239,
                              -0.0
                         ],
                         [
                              304.0325,
                              776.94239,
                              -0.0
                         ]
                    ]
               }
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour611": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         1667.51037,
                         -0.0,
                         -0.0
                    ],
                    [
                         1537.91004,
                         735.0,
                         -0.0
                    ],
                    [
                         0.0,
                         735.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {}
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour612": {
          "Exterior": [
               [
                    [
                         0.0,
                         15.0,
                         -0.0
                    ],
                    [
                         836.86549,
                         15.0,
                         -0.0
                    ],
                    [
                         836.86549,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {}
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour613": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         836.86344,
                         -0.0,
                         -0.0
                    ],
                    [
                         836.86344,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {}
          ],
          "Arc": [
               []
          ],
          "PointOnArc": [
               []
          ]
     },
     "Contour614": {
          "Exterior": [
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         836.86139,
                         -0.0,
                         -0.0
                    ],
                    [
                         836.86139,
                         1250.0,
                         -0.0
                    ],
                    [
                         0.0,
                         1250.0,
                         -0.0
                    ]
               ],
               []
          ],
          "Interior": [
               {
                    "1": [
                         [
                              10.0,
                              1250.0,
                              -0.0
                         ],
                         [
                              610.0,
                              1250.0,
                              -0.0
                         ]
                    ]
               },
               {}
          ],
          "Arc": [
               [],
               [
                    [
                         610.0,
                         1250.0,
                         -0.0
                    ],
                    [
                         10.0,
                         1250.0,
                         -0.0
                    ]
               ]
          ],
          "PointOnArc": [
               [],
               [
                    [
                         310.0,
                         950.0,
                         0.0
                    ]
               ]
          ]
     },
     "Contour615": {
          "Exterior": [
               [],
               [
                    [
                         0.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         836.85935,
                         -0.0,
                         -0.0
                    ],
                    [
                         836.85935,
                         735.0,
                         -0.0
                    ],
                    [
                         0.0,
                         735.0,
                         -0.0
                    ]
               ]
          ],
          "Interior": [
               {},
               {
                    "1": [
                         [
                              10.0,
                              -0.0,
                              -0.0
                         ],
                         [
                              610.0,
                              -0.0,
                              -0.0
                         ]
                    ]
               }
          ],
          "Arc": [
               [
                    [
                         10.0,
                         -0.0,
                         -0.0
                    ],
                    [
                         610.0,
                         -0.0,
                         -0.0
                    ]
               ],
               []
          ],
          "PointOnArc": [
               [
                    [
                         310.0,
                         300.0,
                         0.0
                    ]
               ],
               []
          ]
     }
}

rng = np.random.default_rng()
pnt = rng.random((30, 2))   # 30 random points in 2-D
# print(pnt)
for i in range(0,16):
     if i > 9:
          key = 'Contour6'+str(i)
     else:
          key = 'Contour60'+str(i)
     print(key)
     
     fig = plt.figure(figsize=(2,5))
     ax = fig.add_subplot(1,1,1)
     ax.set_ylim(-1000, 1900)
     ax.set_xlim(-1000, 1900)
     
     #exterior points
     for i in range(len(points1[key]['Exterior'])):

               data = points1[key]['Exterior'][i]
               if data:
                         data.append(points1[key]['Exterior'][i][0])
               data = np.array(data)
               if data.any():
                    ax.plot(data[:,0], data[:,1])
               plt.title(key)
               count = 1
               for p in data:
                    ax.text(p[0], p[1], str(count), color="red", fontsize=8)
                    count = count+1
               
     #interior points          
     for i in range(len(points1[key]['Interior'])): 

                for value in points1[key]['Interior'][i].values():
                    data1 = value
                    if data1:
                                data1.append(value[0])
                    data1 = np.array(data1) 
                    if data1.any():
                            ax.plot(data1[:,0], data1[:,1])
                    if data1.any():
                            for p in data1:
                                ax.text(p[0], p[1], str(count), color="blue", fontsize=8)
                                count = count+1
                         
                         
               #arc
     arc_points =[]
     arc_pointsonarc=[]
     for i in range(len(points1[key]['Arc'])):  
               data1 = points1[key]['Arc'][i] 
               arc_points.append(data1)
     
     for i in range(len(points1[key]['PointOnArc'])):  
               data1 = points1[key]['PointOnArc'][i] 
               arc_pointsonarc.append(data1)
               
     for i in range(len(arc_points)):
          if arc_points[i] != []:
               check =1
               for j in range(len(arc_points[i]) - 1):
                    
                    if arc_points[i][j] != []:
                         p1 = arc_points[i][j]#start
                         p2 = arc_points[i][j+1]#end
                         p3 = arc_pointsonarc[i][j]#point on arc
                         
                         # Taking a 3 * 3 matrix
                         if check ==1 :
                              A = np.array([[p1[0]-p2[0],p1[1]-p2[1]],[p2[0]-p3[0],p2[1]-p3[1]]]) 
                              B =np.array([ [ p1[0]**2 - p2[0]**2 + p1[1]**2 - p2[1]**2 ] , [ p2[0]**2 - p3[0]**2 + p2[1]**2 - p3[1]**2] ])  
                              C = 0.5 * B
                              # Calculating the inverse of the matrix
                              I =np.linalg.inv(A)

                              centre = I@C #centre of arc
                              r = math.sqrt((centre[0]-p2[0])**2 + (centre[1]-p2[1])**2)#raduis of arc
                              
                              check = check +1
                         
                         length = len(arc_pointsonarc[i])
                         
                         if length != 0:
                              
                              p2 = arc_points[i][j+1]#end
                              p3 = arc_pointsonarc[i][j]#pointonarc
                         
                              a1 = math.degrees(math.atan2(p1[1]-centre[1],p1[0]-centre[0]))#start angle
                              a2 = math.degrees(math.atan2(p2[1]-centre[1],p2[0]-centre[0]))#end angle
                              a3 = math.degrees(math.atan2(p3[1]-centre[1],p3[0]-centre[0]))#epoint on arc angle
                              
                              if a3 > 0 and (a1 if a1 >= 0 else (360+a1)) > (a2 if a2 >= 0 else (360+a2)):
                                   a0 = a1
                                   a1 = a2
                                   a2 = a0
                              
                              if a3 < 0 and (a1 if a1 >= 0 else (360+a1)) < (a2 if a2 >= 0 else (360+a2)) :
                                   a0 = a1
                                   a1 = a2
                                   a2 = a0
                    
                              arc1= Arc((centre[0],centre[1]),r,r,theta1 = a1,theta2 = a2)
                              ax.add_patch(arc1)
                         
     
     plt.margins(0.1)
     plt.show()

