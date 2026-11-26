# The original wire saddle stays in its factorial chamber on every positive path

Research proof, 3 November 2026. This uses the coupled original period
equations, not merely separate bounds on the endpoint angles. It proves
the real wire order throughout the positive path charge cube for every
integer power at least three. The conclusion places the geometric
critical points in the original regular factorial chamber. It does
not assert that the geometric saddle dominates the full finite kernel
or that its coefficient in a general source is nonzero.

## 1. Inputs and a cosine maximum principle

Take the finite positive paths of the
[fractional-charge theorem](research_positive_path_fractional_charge_cube.md):
selected powers \(n_v\ge3\), charges \(0\le\chi_v\le1\),
original incidence degrees at most two, and the stated complete
outside endpoints. At an active vertex write
\[
 t_v=\vartheta_v-iH_v,\qquad
             0<\vartheta_v<\pi,\quad H_v>0.
 \tag{1}
\]
At zero-charge and complete vertices, \(t_v=0\).
The original return and both period equations are
\[
 \begin{split}
 r_{vu}&=k_{vu}+ig_{vu}
       =\operatorname{asinh}\bigl(\tan(t_v/2)\cos(t_u/2)\bigr),\\
 \sum_{u\sim v}k_{vu}&=\frac{n_vH_v}{2},&
 \sum_{u\sim v}g_{vu}&=\frac{n_v\vartheta_v}{2}-\pi\chi_v .
 \end{split}
 \tag{2}
\]
At an active endpoint, \(k_{vu}>0\) and
\(-\pi/2<g_{vu}<\pi/2\). The
[cosine-phase maximum principle](research_geometric_phase_maximum_principle.md)
supplies
\[
 \beta_v:=\arg\cos(t_v/2)\in(0,\pi/4),
 \qquad \beta_v=0\ \hbox{at a complete vertex}.
 \tag{3}
\]
Only the strict qualitative bound in (3) is needed below.

**Lemma 1.** Every active vertex satisfies
\[
                         |\cos(t_v/2)|<1.
 \tag{4}
\]

*Proof.* If (4) failed, choose an active vertex at which
\(C=|\cos(t_v/2)|\ge1\) is maximal over all selected and complete
vertices. Every neighbor then has
\(|\cos(t_u/2)|\le C\), so
\[
 |\sinh r_{vu}|
   =|\tan(t_v/2)\cos(t_u/2)|
                      \le|\sin(t_v/2)|.
 \tag{5}
\]
Since \(|\sinh(k+ig)|^2=\sinh^2k+\sin^2g\), this gives
\(k_{vu}\le\operatorname{asinh}|\sin(t_v/2)|\).
Put \(t_v=\vartheta-iH\). The supposition \(C\ge1\) implies
\[
 \cosh H+\cos\vartheta\ge2,\qquad
 |\sin(t_v/2)|^2=\frac{\cosh H-\cos\vartheta}{2}
                  \le2\sinh^2(H/2).
 \tag{6}
\]
But for every \(H>0\),
\[
 \operatorname{asinh}\bigl(\sqrt2\sinh(H/2)\bigr)<\frac{3H}{4}.
 \tag{7}
\]
Indeed \(\sinh(3H/4)>(3/2)\sinh(H/2)>
\sqrt2\sinh(H/2)\); the first inequality follows from the
strict increase of \(\sinh x/x\) on \(x>0\).
The degree bound and (5)--(7) would give
\(\sum k_{vu}<3H/2\), contradicting (2) and \(n_v\ge3\).
This proves (4). \(\square\)

This maximum principle itself uses neither the quantitative height
bound nor the charges' upper bound. It uses the original real
period equation, degree at most two, and the positivity of the
real returns. At complete vertices the cosine modulus is exactly one.

## 2. The selected wire lies in the upper quarter strip

For an edge \(vu\), put
\[
 A=\cos^2(t_v/2),\qquad B=\cos^2(t_u/2),\qquad
       k=\frac{AB}{A+B},\qquad
       x=\frac1\pi\arcsin\sqrt{k}.
 \tag{8}
\]
These are the selected branches continued from the complete edge,
where \(A=B=1\) and \(x=1/4\). By (3), \(A,B\) have positive
real part and nonnegative imaginary part. By Lemma 1 their moduli
are at most one, strictly less than one at an active endpoint.
For an edge with an active endpoint, \(k\) has positive real and
positive imaginary parts, so the branch in (8) has
\(0<\Re x<1/2\) and \(\Im x>0\).

**Lemma 2.** Every edge with an active endpoint satisfies
\[
 0<\Re k<\frac12,\qquad
               0<\Re x<\frac14,\qquad
 \Re x>\alpha(\Im x),\quad
 \alpha(y)=\frac{\arccos(\operatorname{sech}(2\pi y))}{2\pi}.
 \tag{9}
\]

*Proof.* Write
\[
 1/A=r e^{-i\alpha},\qquad 1/B=s e^{-i\beta},
 \quad r,s\ge1,\quad 0\le\alpha,\beta<\pi/2.
 \tag{10}
\]
The function
\(|r e^{-i\alpha}+s e^{-i\beta}-1|^2\) is strictly increasing
in either radius for \(r,s\ge1\): half its \(r\)-derivative is
\(r+s\cos(\alpha-\beta)-\cos\alpha>0\), and similarly for \(s\).
At \(r=s=1\), subtracting one from this function gives
\[
 2\bigl[(1-\cos\alpha)(1-\cos\beta)+\sin\alpha\sin\beta\bigr]\ge0.
 \tag{11}
\]
At least one radius is strictly greater than one. Thus, with
\(Z=1/A+1/B\), one has \(|Z-1|>1\). Equivalently
\(|Z|^2>2\Re Z\), so \(\Re k=\Re(1/Z)<1/2\).
Its positivity was already noted after (8).

Now \(\cos(2\pi x)=1-2k\). Taking real parts shows
\[
             0<\cos(2\pi\Re x)\cosh(2\pi\Im x)<1.
 \tag{12}
\]
The first inequality implies \(\Re x<1/4\); the second is
exactly the last inequality in (9). \(\square\)

For an all-complete edge, \(x=1/4\); it is a constant part of the
geometric configuration. The selected square root
\[
 q=\cot(\pi x),\qquad
 q^2=1+\tan^2(t_v/2)+\tan^2(t_u/2)
 \tag{13}
\]
is the original one. Equation (13) follows from (8) and is
continued from \(q=1\).

## 3. The coupled equations force the real wire order

**Theorem 3.** On every edge of the original positive path,
throughout its whole charge cube,
\[
 \boxed{\quad
 \Re x<
 \min\left\{\frac12-\frac{\Re t_v}{2\pi},
             \frac12-\frac{\Re t_u}{2\pi}\right\}.
 \quad}
 \tag{14}
\]

*Proof.* It suffices to prove the inequality at one endpoint \(v\).
It is automatic when that endpoint is complete. Suppose it fails
at an active endpoint. Use radian coordinates
\[
 T=t_v/2=a-ih,\qquad W=\pi x=A_0+iY,
 \qquad A_0\ge\pi/2-a .
 \tag{15}
\]
Here \(0<a<\pi/2\), \(h>0\), and Lemma 2 gives
\(0<A_0<\pi/4,\ Y>0\). In particular \(a>\pi/4\).

The upper-right-quadrant property gives
\(\Re(A\bar B)>0\), hence \(|A+B|>|B|\), in the notation
of (8). Consequently
\[
 |\sin^2W|=|k|<|A|=|\cos^2T|.
 \tag{16}
\]
In (16) the two sides are
\(\sin^2A_0+\sinh^2Y\) and
\(\cos^2a+\sinh^2h\). Since
\(A_0\ge\pi/2-a\), their real trigonometric terms have the
opposite weak order. It follows that \(Y<h\).

The original return satisfies the exact identity
\[
 e^{2r_{vu}}
     =\frac{q+\tan T}{q-\tan T}
     =\frac{\cos(W-T)}{\cos(W+T)}.
 \tag{17}
\]
For the first equality use
\(\sinh r_{vu}=\tan T\cos(t_u/2)\) and
\(\cosh r_{vu}=q\cos(t_u/2)\). The latter square-root sign
is fixed at completeness and continues on the positive charge
cube; neither side vanishes there. The second equality uses
\(q=\cot W\). Thus (17) retains the original return.

In (15), \(0<a-A_0<\pi/2\) and \(Y+h>0\), so
\[
 0<\arg\cos(W-T)
       =\arctan\bigl(\tan(a-A_0)\tanh(Y+h)\bigr)
                       <a-A_0 .
 \tag{18}
\]
Also \(\pi/2\le A_0+a<3\pi/4\) and \(Y-h<0\).
The denominator in (17) therefore has nonpositive real
and strictly positive imaginary parts:
\[
                  \pi/2\le\arg\cos(W+T)<\pi .
 \tag{19}
\]
The argument of their quotient belongs to \((-\pi,0)\).
Since the original return has \(2g_{vu}\in(-\pi,\pi)\),
there is no additional \(2\pi\) ambiguity in (17).
Equations (18)--(19) yield the strict estimate
\[
             g_{vu}<\frac{a-A_0-\pi/2}{2}
                          \le a-\pi/2<0.
 \tag{20}
\]

Put
\(B_v=\sinh H_v/\sin\vartheta_v\) and
\(\omega=\arctan B_v\). The argument of
\(\tan T\cos(t_u/2)\) is \(\beta_u-\omega\).
Its real part is positive, since it equals
\(\sinh k_{vu}\cos g_{vu}\).
When its argument is negative, the exact relation
\[
                  \tan g_{vu}
                    =\tanh k_{vu}\tan(\beta_u-\omega)
 \tag{21}
\]
shows that \(g_{vu}>\beta_u-\omega\ge-\omega\).
Thus (20) implies
\[
                              \omega>\pi/2-a .
 \tag{22}
\]

There can be only one further incidence at \(v\).
Its return imaginary part, or zero if the incidence is absent,
must satisfy the original period equation. By (20),
\[
 g_{\rm other}
  =n_va-\pi\chi_v-g_{vu}
    >(n_v-1)a-\pi/2
    \ge2a-\pi/2>0.
 \tag{23}
\]
A terminal vertex is already impossible. Otherwise let \(w\)
be the other neighbor. The positive version of (21) gives
\[
              0<g_{\rm other}<\beta_w-\omega .
 \tag{24}
\]
Combining (22)--(24) forces
\[
                  \beta_w>2a-\pi/2+\omega>a>\pi/4,
 \tag{25}
\]
contradicting (3). This excludes the failure in (15) and proves
(14) at both endpoints. \(\square\)

Only \(n_v\ge3,\ \chi_v\le1\) and the original degree bound were
used in (23). In particular the contradiction does not replace
the actual charge by one or alter an attaching degree.

## 4. What this proves about the original phase

For an active edge put
\(s_v=1/2-t_v/(2\pi)=b_v+iS_v\), and similarly at \(u\).
Equations (9), (14), and the geometric spectral half-plane give
\[
 Y,S_v,S_u\ge0,\qquad
 \alpha(Y)<\Re x<b_v,b_u,\qquad
                         \alpha(S_v)<b_v,\quad\alpha(S_u)<b_u.
 \tag{26}
\]
For the last two inequalities use
\(\cos(2\pi b_v)\cosh(2\pi S_v)=\Re(-2\cos t_v)/2<1\).
All original factorial arguments
\[
                x,\quad s_v-x,\quad1-s_v-x
 \tag{27}
\]
and their \(u\)-counterparts have real parts strictly between
zero and one. Thus the selected wire branch stays in the
original regular factorial chart along the entire charge cube.
The zero logarithmic lift of its stationary equation, fixed at
completeness, continues in this chart.

For fixed endpoint angles the real part of the principal wire
phase \(b(x,t_v)+b(x,t_u)\), on its fixed-height line, is strictly
concave on
\(\alpha(Y)<\Re x<\min(b_v,b_u)\).
Indeed, with the quantities in the
[mixed-phase calculation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_mixed_phase_height_extension_and_wire_order.md),
each incidence has \(v>0,w>0,u<w\). Its negative \(x\)-second
derivative is \(\pi(v+2w-u)>0\).
The geometric critical wire is therefore the unique maximum on
this central interval, with a positive curvature bound on compact
subintervals.

For an internal two-vertex piece with complete outer ends, the
complete-end-compensated mixed phase consequently has its actual
positive-charge critical point inside the concavity domain of
Proposition 1 in the linked note, without requiring any height
ordering. This gives strict horizontal concavity of that mixed
phase on its stated convex domain. Zero-charge faces are understood
by continuity and the direct nondegenerate Hessian at completeness.
A general interior vertex has no extra complete-end term; this
conclusion does not insert one there.

The earlier exact \(A=1,B=3/10+3i/5\) wire-order counterexample
obeys the separate endpoint bounds but was not an integer-filled
path. Theorem 3 explains precisely why the coupled equations exclude
such a failure on the actual family.

Finally, regularity and a strict central maximum do not control
the rest of the finite source. The
[all-three bare-kernel obstruction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_bare_kernel_power_three_obstruction.md)
still exhibits larger endpoint sectors before the original trace
contracts them. No assertion about those sectors, global mixed
currents, or the nonzero full-source saddle coefficient follows
solely from (14) or (26).
