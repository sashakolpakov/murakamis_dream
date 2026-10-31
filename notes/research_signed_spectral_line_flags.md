# Literal line flags for the signed spectral Green collar

Workspace research draft, 31 October 2026.
This gives local GROUP and selected-flag adapters at a protected face.
It makes no global circle-development or regulator assertion.

Put s=sin(pi delta), k=cos(pi delta), 0<delta<1/2. A real circle
reflection is represented by a determinant-minus-one anti-Mobius matrix
J; products are J_2 conjugate(J_1). A signed curvature records an
oriented circle, but multiplying its entire reflection matrix by -1
does not change its projective reflection. Its raw adjacent MAIN
products below have the prescribed trace -2.

## 1. A protected outer line, including the two-line corner

Set x=0, y>0. The original outer line is the real axis, and the y
circle has radius1/y and center i cos(2pi delta)/y. Use

    J_x=-i I,
    J_y=[[i cos(2pi delta), sin²(2pi delta)/y],
         [y, i cos(2pi delta)]].

For a possibly signed middle q choose the prescribed real root
T_q²=qy+q²s², and define

    J_q=[[i-2kT_q/y, -4k²(y+q s²)/y²],
         [q, i+2kT_q/y]].                                    (1)

For q!=0 this is the circle of signed radius1/q and center

    a_q+i/q, a_q=-2kT_q/(q y).

Its cooriented tangencies to x and y follow from
a_q²=4k²(y/q+s²)/y². This includes a negative output q=-c
with c>y/s² and T_q<0. That output circle is internally tangent
to y; it is not a nonexistent positive disk inserted in the strip.
All matrices in (1) have determinant-1.

At q=0, T_q=0 and (1) becomes

    J_0=[[i,-4k²/y],[0,i]],

the ACTUAL second line Y=2k²/y. Thus the two-line strip height and
its line flags survive the limit; no flag is inferred from a double
root. The q=0 expression is a finite matrix, with no division by q.

Set

    A_q=J_q conjugate(J_x), B_q=J_y conjugate(J_q),
    P=B_q A_q=J_y conjugate(J_x).

Then trace A_q=trace B_q=-2 and

    P=[[-cos(2pi delta), i sin²(2pi delta)/y],
       [iy, -cos(2pi delta)]],
    trace P=-2cos(2pi delta)=sigma.                            (2)

The selected eigenvalue J=-exp(-2pi i delta) fixes the ACTUAL
outer contact/intersection point +sin(2pi delta)/y on the real line.
The other eigenvalue fixes its negative. This specifies the branch,
not merely the unordered eigenvalue pair.

The MAIN contacts for q!=0 are, in their original order,

    fixed(A_q)=a_q,
    fixed(B_q)=2k[-T_q/y+ik]/(q+y).                            (3)

At q=0 these become infinity and 2ik²/y, respectively. They are the
literal contacts of the line q with the two outer circles. In
particular the q=0 flag pair is determined independently of (2).

Write

    E_q=y+2q s²+2s T_q.

For any two endpoints b,q in this chart, with their recorded roots,
the original Green projective collar is

    R0=E_b/E_q,
    C=I+(R0-1)/(J-J^(-1))(P-J^(-1)I).                         (4)

Direct multiplication, using T_q²=qy+q²s², gives
C A_b C^(-1)=A_q and C B_b C^(-1)=B_q. It therefore maps BOTH
ordered MAIN contacts in (3) and fixes the selected outer point.
This is the same ratio as the full signed-clock Gauss calculation,
not its reciprocal obtained by silently changing the selected flag.
The projective determinant is R0; its original physical lift is
chosen afterwards.

## 2. A protected middle line with two finite outers

Now x,y>0, A=x+y, P0=xy and D=A²-4P0 s²>0. Put the protected
middle line on the real axis. Give the x,y circles centers i/x
and a+i/y, with

    a=-2k/sqrt(P0).

The NEGATIVE sign fixes the source orientation: the protected input
line is on the positive side of the ordered x-to-y triangle. Their
reflection matrices are

    J_x=[[i,0],[x,i]],
    J_y=[[ay+i,-a²y],[y,-ay+i]].

For T_q²=P0+qA+q²s² define

    W_q=(2k²/D)[2P0+qA-2sqrt(P0)T_q],
    U_q=q a/2+(1/x-1/y)W_q/a,

    J_q=[[U_q+i(W_q-1),-2W_q/x],
         [q,-U_q+i(W_q-1)]].                                 (5)

The circle's signed radius is1/q and its center, when q!=0, is
(U_q+i(W_q-1))/q. The two cooriented tangency equations reduce to

    U_q²+W_q²=2W_q(1+q/x),
    a U_q=q a²/2+(1/x-1/y)W_q.

Solving these gives exactly (5), with the chosen root. They prove
det J_q=-1 and both raw MAIN traces -2. At q=0, T_q=sqrt(P0),
one has W_q=U_q=0 and J_q=-iI: the SAME actual protected line,
with its two tangent contacts0 and a.

The outer product P=J_y conjugate(J_x) has trace sigma. On the
selected eigenline J=-exp(-2pi i delta), the Green collar remains
(4), now with

    E_q=A+2q s²+2sT_q.

The reflection products and both conjugation identities follow by
the same tangency equations. This permits a protected input b=0
and a regular signed output q=-c, without reconstructing a line
from a vanished scalar clock. Choosing a positive a instead would
reverse the indicated ratio; that opposite-copy orientation is not
silently identified with this source chart.

## 3. The remaining local label orientations

Interchanging input and output replaces the collar by its inverse
and handles the corresponding RIGHT endpoint. Reversing the two
outer labels changes

    (A,B,P) -> (B^(-1),A^(-1),P^(-1)).

For this PURE outer reversal the same C conjugates both new heads.
Retain the SAME geometric selected eigenline: its P-eigenvalue label
changes J -> J^(-1), while the eigenratio of C on that line remains
R0. This is the convention used to obtain the y=0 coordinate chart
and then restore the original source labels. If instead one retains
the numerical label J for P^(-1), one has switched to the other old
eigenline and its ratio is R0^(-1). Those are different conventions;
the pure outer swap does not replace the actual conjugator by C^(-1).
No independent reversal is made at an occurrence of a globally
shared face.

Both outers cannot be the protected MAIN pair in the actual
simple-white dictionary, since their shared edge is MATCHING.
An overloaded protected middle is an exactly vanishing one-sided
sector. Thus Sections 1--2 cover the unavoidable protected-line
types in a nonvanishing regular signed Green datum, with the
specified ordered reversals.

## 4. Scope of what the flags now solve

The formulas retain the actual selected spectral point, both MAIN
contact points, the common outer product, and the primitive collar
even when a middle clock vanishes. They provide local reflection
data that can be used in a prospective GLOBAL signed development.

They do not prove that independently assembled local circles close
around every ordinary face, or that their two marked line fans
close to the same strip. Those require the full face stationary
equations, compatible shared phases and a holonomy proof with the
signed coorientations. Nor is an open local Gauss regulator being
declared invariant under the coordinate changes above. A relative
volume comparison must use the original global decorated chain.
