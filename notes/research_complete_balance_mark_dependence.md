# Complete-radius balance depends on the original marked cap

PRIVATE exact observation, 31 October 2026. This concerns the finite geometric
sufficient condition, not invariance or failure of the actual knot invariant.
It uses TWO legitimate original top-cap marks on the SAME literal source word.
No arbitrary local re-framing or new quantum mark is introduced.

Use the already proved width-three word D=(1,3,2,4,1,3). Its face labels are
u,a0,a1,a2,e1,e2,b1,b2 =0,...,7, and its original quartets are

 (1,0,4,2),(2,0,5,3),(4,2,6,5),
 (5,3,7,0),(1,4,0,6),(6,5,0,7).                            (1)

With the FIRST top cap marked the protected pair is(0,1). Its normalized
packing is exactly

 a1=(sqrt2,1;1), a2=(2-sqrt2,r;r),
 e1=(0,3/2;1/2), e2=(0,1/2;1/2),
 b1=(-sqrt2,1;1), b2=(sqrt2-2,r;r), r=3-2sqrt2,

between linesY=0,2. This original mark passes Q-balance at all six ports.

The SECOND original top-cap mark has protected pair(0,6), as the literal
Morse compiler confirms. Its contact on Y=0 is p=-sqrt2. The ONE global
Möbius transformation

                         w=-4/(z+sqrt2)                   (2)

sends that contact to infinity, keeps the lower halfplane as u, and sends
the b1 disk to the upper halfplaneY>=2. It maps the entire same packing,
retaining all source labels and contact orders. Its actual curvatures are

 (u,a0,a1,a2,e1,e2,b1,b2)
          =(0,1,2,3+2sqrt2,2,1,0,1).                       (3)

Indeed a circle(X,Y;R) not through p has transformed curvature
[((X-p)^2+Y^2-R^2)/(4R)]; the old lineY=2 becomes curvature1.
The original b1 disk becomes the zero-curvature upper line. Every other
listed value follows directly. This formula is a common whole-packing
mark change, not independent modification of triangle weights.

At the fourth port(5,3,7,0), the new quartet is

                  (x,b,c,y)=(1,3+2sqrt2,1,0).

Let F(r)=Q(1,r,0)=(2/pi)Ti2(sqrt r), with the original source constant.
Put t=sqrt2-1 and G=Ti2(1), Catalan's constant. The balance gap at this
port is exactly

 F((1+sqrt2)^2)+F(1)-log((1+sqrt2)^2)
        =(2/pi)[Ti2(t)+G]-log(1+sqrt2).                    (4)

It is strictly NEGATIVE, with an elementary rational certificate:

 Ti2(t)<t<29/70,
 G<1-1/9+1/25=209/225,
 pi>31/10,
 log(1+sqrt2)>log(12/5)
   >2[7/17+(7/17)^3/3+(7/17)^5/5].                        (5)

For completeness, sqrt2>140/99 and <99/70 follow by squaring rational
bounds. Thus t>41/99, and pi=8atan(t)>8[41/99-(41/99)^3/3]
=9092816/2910897>31/10. The Ti2 and Catalan estimates are their elementary
integral/alternating series bounds; the logarithm bound is the positive
atanh series. The exact difference of the lower logarithm and upper first
term in(4) is

 2[7/17+(7/17)^3/3+(7/17)^5/5]
 -(20/31)(209/225+29/70)
       =114290888/13864903605 >1/200.

Therefore the second-cap marked source fails complete-radius balance by
at least1/200 at this actual port, whereas the first-cap marked source is
balanced. In particular a legitimate different protected edge CAN remove
a failed balance test for the same literal diagram (choose the first cap
instead of the second).

The conclusion is only presentation/mark dependence of this sufficient
geometric test. It does not show a failure of any source volume equality,
and it does not assert that every failing diagram has a successful mark.
Applying a quantum theorem after changing a mark must still retain that
original cap's exact source conventions; no generic open-word regulator
invariance is used here.
