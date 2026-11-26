# Complete-end barriers for the inverse-leg cotangents

Research lemma, 5 November 2026. Adding the original complete outside
incidence puts a private inverse leg into the same algebraic system as
an internal leg. The added incidence has cotangent imaginary part
strictly between zero and one. At a unit type-three vertex, each own
cotangent also has imaginary part greater than minus one. These
statements do not settle the type-four maximum argument or identify
the geometric point with the localized source point.

## 1. The complete outside incidence

Use the original positive path charge family, with integer powers
at least three and incidence degree at most two. At the selected
end of an edge write
\[
 \tau=a-iH,\quad C=\cosh H,\quad c=\cos a,\quad
 A=\cos^2(\tau/2),\quad \alpha=A^{-1}.
 \tag{1}
\]
The other end is complete, so its cosine square is one.
The actual parameter rectangles proved in
[the wire-before-leg theorem](research_mixed_wire_before_inverse_leg.md#1-a-uniform-bound-for-the-original-wire-cotangent)
are
\[
 (C,c)\in
 [1,6/5]\times[-3/5,1]\ \cup\
 [6/5,7/4]\times[-1/2,1].
 \tag{2}
\]
The original wire root is
\[
 q=p-ih,\qquad q^2=\alpha,\qquad p>h\ge0.
 \tag{3}
\]
The [sine-lens theorem](research_mixed_all_leg_half_plane.md)
gives \(\Re\alpha>1/2\); this also holds when the selected
end is complete.

Since \(|\alpha|=2/(C+c)\) and
\(\Re\alpha=2(1+Cc)/(C+c)^2\), (3) gives the exact formula
\[
             h^2=\frac{(C-1)(1-c)}{(C+c)^2}.
 \tag{4}
\]
The denominator is positive on (2). This expression is
nonincreasing in \(c\), since its derivative is
\[
           -\frac{(C-1)(C+2-c)}{(C+c)^3}\le0.
 \tag{5}
\]
On the first rectangle it is consequently at most
\[
 \frac{(8/5)(C-1)}{(C-3/5)^2}\le\frac89.
 \tag{6}
\]
The last expression increases for \(1\le C\le6/5\):
its derivative is \(40(7-5C)/(5C-3)^3>0\).
On the second rectangle, instead,
\[
 h^2\le\frac{(3/2)(C-1)}{(C-1/2)^2}\le\frac34,
 \qquad
 \frac34-\frac{(3/2)(C-1)}{(C-1/2)^2}
  =\frac{3(2C-3)^2}{4(2C-1)^2}\ge0.
 \tag{7}
\]
Thus every complete-end wire satisfies \(0\le h<1\).
This is stronger than the bound \(h<3/2\) needed for a general edge.

Let \(U_{\rm out}\) be the inverse leg at the complete outside end,
and let \(z_{\rm out}\) be its original logarithmic coordinate.
It is an auxiliary geometric incidence, not an additional variable
or factor in the finite source. The exact inverse formula gives
\[
 U_{\rm out}=\frac{-i}{2(q+i)-i},\qquad
 \zeta_{\rm out}:=\cot\pi z_{\rm out}
     =i+\frac1{q+i}
     =\frac{p}{D}
           +i\left(1-\frac{1-h}{D}\right),
 \quad D=p^2+(1-h)^2.
 \tag{8}
\]
Its real part is positive. Because \(h<1\), its imaginary
part is less than one. Also \(p^2-h^2=\Re\alpha>1/2\), so
\[
 D-(1-h)=p^2+h^2-h
     >2h^2-h+\frac12
      =2(h-\tfrac14)^2+\frac38>0.
 \tag{9}
\]
This proves the following strict boundary condition.

**Lemma 1.** At every complete outside incidence,
\[
              \Re\zeta_{\rm out}>0,\qquad
                    0<\Im\zeta_{\rm out}<1.
 \tag{10}
\]
It holds throughout the positive charge cube, including the
all-complete edge, where \(\zeta_{\rm out}=(1+i)/2\).
No new root enclosure or parameter subdivision is used.

## 2. The selected endpoint uses the ordinary unit equations

At any selected incidence write \(U=e^{-2\pi is}\),
\(\zeta=\cot\pi s\), and let \(\xi\) be the cotangent
of the opposite incidence on its shared edge. The inverse formula
and the shared root equation give
\[
 \zeta=i+\frac{\alpha}{q+i},\qquad
 \xi=i+\frac{\beta}{q+i},\qquad
 q^2=\alpha+\beta-1.
 \tag{11}
\]
Consequently
\[
           q=\zeta+\xi-i,\qquad
                  \alpha=(\zeta-i)(\zeta+\xi).
 \tag{12}
\]
These identities apply unchanged at a private selected leg:
there \(\beta=1\) and \(\xi=\zeta_{\rm out}\) from (8).

Let \(\eta\) be the other leg cotangent at the same selected
vertex. At an **own unit charge**, the exact type-three and
type-four vertex relations from
[unit-period elimination](research_mixed_unit_period_leg_elimination.md)
become, respectively,
\[
 \begin{array}{ll}
 n=3:&\displaystyle
        \alpha=-(\zeta+i)(\eta+i),\\[2mm]
 n=4:&\displaystyle
        \alpha=\frac{-2i(\zeta+i)(\eta+i)}
                            {\zeta+\eta+2i}.
 \end{array}
 \tag{13}
\]
The denominators are nonzero, since both leg cotangents
have positive real part. Combining (12) and (13) gives
\[
 \begin{array}{ll}
 n=3:&
 \zeta^2+\zeta(\xi+\eta)+i(\eta-\xi)-1=0,\\[1mm]
 n=4:&
 (\zeta+i)(\zeta+\xi)(\zeta+\eta)
                     =2i(\xi-i)(\eta+i).
 \end{array}
 \tag{14}
\]
In particular the selected endpoint has no exceptional equation
after its actual complete outside incidence is added.

This addition is legitimate for a maximum argument: one considers
the finitely many selected incidence cotangents together with these
two fixed geometric boundary values. By Lemma 1 an absolute imaginary
maximum of size at least one must occur on a selected incidence.
Only that incidence needs a unit equation. No unit equation is
imposed at a complete outside vertex. For a one-vertex word there
are two literal outside incidences and the same conclusion applies.

## 3. Two type-three consequences

The original lower-half-plane leg theorem gives
\(\Re\zeta,\Re\eta>0\). Write
\[
              \zeta=x+iy,\qquad \eta=B+i\beta,
                       \qquad x,B>0.
 \tag{15}
\]
At a unit type-three vertex, (13) says
\[
 \Re\alpha=(y+1)(\beta+1)-xB>0,\qquad
 -\Im\alpha=x(\beta+1)+B(y+1)>0.
 \tag{16}
\]
Both signs follow from the original upper-right-quadrant cosine
square, with its original inverse. The first inequality makes
\(y+1,\beta+1\) have the same nonzero sign; the second excludes
both being negative.

**Lemma 2.** At every unit type-three vertex, both incidence
cotangents have imaginary part strictly greater than \(-1\).
Equivalently, each inverse leg \(U\) satisfies \(\Re U<1\).
This conclusion uses the actual own unit relation; it is not a
consequence of the separate coarse angle bounds alone.

For reference, the full type-three maximum exclusion is also
immediate from (14). Write \(\xi=A+i\alpha_0\), \(A>0\).
The imaginary part of its first equation is
\[
 x(2y+\alpha_0+\beta)+A(y-1)+B(y+1)=0.
 \tag{17}
\]
If \(y=M\ge1\) is a global absolute imaginary maximum, then
\(\alpha_0,\beta\ge-M\), so the first two terms are nonnegative
and the last is positive. If \(y=-M\le-1\), then
\(\alpha_0,\beta\le M\), so the first and last terms are
nonpositive and the middle is negative. Both cases are impossible.
The neighboring variables here are literal incidences; repeated
values and the complete outside values cause no change in the signs.

Thus an absolute maximum of size at least one in a mixed unit word
could occur only at type four. The remaining type-four exclusion,
and any convex-chamber comparison with the localized source point,
are separate obligations. This note proves neither a finite-sum
estimate nor a new action-to-source-point identification.
