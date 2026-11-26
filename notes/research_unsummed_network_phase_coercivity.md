# Coercivity of the network phase with its wire variables retained

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The complete-end contribution used in the earlier
[mixed-phase calculation](research_mixed_wire_phase_concavity.md)
is absent at a general interior vertex. The appropriate object is
therefore the Hessian of each original incidence, followed by the
Hessian of their actual sum. This gives an arbitrary-graph concavity
theorem on an explicit contour domain. Outside that domain there is
an exact network test, and positive geometry still gives an adapted
local contour. None of these phase statements chooses a coefficient
in the original finite quantum cycle.

## 1. The original incidence matrix

Let \(G\) be a finite graph. Every edge \(e\) has one retained wire
variable \(x_e\). A selected vertex \(v\) has an angular variable
\(t_v\), a real filling power \(n_v\), and the original unit charge.
An outside vertex has a fixed angle \(u_v\). Count an edge at each
of its endpoints. Throughout this note an edge has the same-index
kernel
\[
 K_T(z,w)=\sum_{j=0}^{N-1}e_j(z)e_j(w).
\]
This is the kernel on the original circle-tree paths. A general
Conway network may also have
\(K_I(z,w)=\sum_{j=0}^{N-1}e_j(z)e_{N-1-j}(w)\);
its reversed wire index has a different phase. The theorems below
do not silently replace those edges by \(K_T\). Such a replacement
would need a separate exact source reduction. For the specified
same-index graph, the phase is
\[
 \Phi=\sum_{(e,v)}b(x_e,t_v)
       +\sum_{v\ {\rm selected}}
             \left(\frac{in_vt_v^2}{4\pi}-it_v\right),
 \tag{1}
\]
where \(t_v=u_v\) at outside vertices, and
\[
 b(x,t)=-J(1/2-x+t/(2\pi))
        -J(1/2-x-t/(2\pi))-2J(x),\qquad
 J'(z)=\Log(2\sin\pi z).
 \tag{2}
\]
Fix its branches on a regular factorial chart. Put
\[
 s_v=\frac12-\frac{t_v}{2\pi}=b_v+iS_v,\qquad
 x_e=a_e+iY_e.
 \tag{3}
\]
The scalar \(b_v\) is a real coordinate; \(b(x,t)\) always denotes
the phase (2). Reflection of \(J\) gives
\[
 b(x,t)=J(s+x)-J(s-x)-2J(x).
 \tag{4}
\]
For one incidence define
\[
 u=\Re\cot\pi(s+x),\qquad
 v=\Re\cot\pi(s-x),\qquad
 w=\Re\cot\pi x.
 \tag{5}
\]
The negative Hessian of its real part in the real coordinates
\((a,b)\), with heights fixed, is exactly
\[
 H_{\rm inc}=\pi
 \begin{pmatrix}
 v+2w-u&-v-u\\
 -v-u&v-u
 \end{pmatrix}.
 \tag{6}
\]
In particular there is no complete-end term in its lower diagonal.
The real part of each filling term in (1) is affine in \(b_v\)
at fixed \(S_v\). It contributes nothing to this Hessian, for
either sign of the real number \(n_v\).

## 2. A concavity domain for every incidence

Define
\[
 \alpha(Y)=\frac1{2\pi}\arccos(\operatorname{sech}(2\pi Y))
                  \quad(Y\ge0).
 \tag{7}
\]

**Theorem 1.** Suppose
\[
 Y,S\ge0,\qquad
 \alpha(Y)<a<b\le\frac12,\qquad b\ge\frac14.
 \tag{8}
\]
Then (6) is positive definite. There is no required ordering
between \(Y\) and \(S\).

**Proof.** Since \(0<a<b\le1/2\), the real parts of the three
factorial arguments \(x,s-x,1-s-x\) lie in \((0,1)\), and
\(v,w>0\). If \(a+b\ge1/2\), then \(u\le0\), and
\[
 \pi^{-1}H_{\rm inc}
 =v\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
  +(-u)\begin{pmatrix}1&1\\1&1\end{pmatrix}
  +2w\begin{pmatrix}1&0\\0&0\end{pmatrix}>0.
 \tag{9}
\]

It remains to consider \(a+b<1/2\), so \(u>0\). Here
\(0<a<1/4\). Set
\[
 R=2\pi a,\quad T=2\pi b,\quad H=2\pi Y,\quad K=2\pi S.
 \tag{10}
\]
Thus \(0<R<\pi/2\), \(\pi/2\le T<\pi-R\), and
\(\cos R\cosh H<1\), by (7)--(8).
The identity
\[
 \frac1{\Re\cot\pi(r+ih)}
       =\frac{\cosh(2\pi h)-\cos(2\pi r)}
                    {\sin(2\pi r)}
 \tag{11}
\]
applies to all three positive real parts in (5). Expanding the
addition formulas gives
\[
 \frac1u-\frac1v-\frac2w
     =\frac{2\mathcal N}
              {\sin R\,\sin(T-R)\,\sin(T+R)},
 \tag{12}
\]
where
\[
 \begin{split}
 \mathcal N={}&
   \cosh H(\sin^2R-\sin^2T)+\cos R\sin^2T\\
 &-\cos T\cosh K\cosh H\sin^2R
   +\sin R\sin T\cos R\sinh K\sinh H.
 \end{split}
 \tag{13}
\]
The denominator in (12) is positive. The last two terms in (13)
are nonnegative, because \(\cos T\le0\). Also
\(\sin^2T>\sin^2R\), so \(\cosh H<1/\cos R\) gives
\[
 \cosh H(\sin^2R-\sin^2T)+\cos R\sin^2T
   >\frac{\sin^2R\cos^2T}{\cos R}\ge0.
 \tag{14}
\]
Consequently (12) is strictly positive.
This implies \(v>u\) and
\[
 \det(\pi^{-1}H_{\rm inc})
     =2wv\left(1-\frac uv-\frac{2u}w\right)>0.
 \tag{15}
\]
Both the lower diagonal and determinant are positive, proving the
claim. The computation used \(\sinh H,\sinh K\ge0\), but never
\(H\le K\) or \(K\le H\). \(\square\)

Conjugation gives the same theorem when all heights in the incidence
are nonpositive. A mixture of height signs is not covered by (8);
the exact matrix (6) remains valid.
There is also a larger simple subregion: the proof of (9) only
requires \(0<a<b\le1/2\) and \(a+b\ge1/2\). On that subregion
the heights can have arbitrary real values, and the condition
\(\alpha(Y)<a\) is unnecessary.

For a quantitative bound put
\[
 T_{\rm inc}=2(v+w-u),\qquad
 \Delta_{\rm inc}=2w(v-u)-4uv,\qquad
 m_{\rm inc}=\Delta_{\rm inc}/T_{\rm inc}>0.
 \tag{16}
\]
The smaller eigenvalue of (6) is at least
\(\pi m_{\rm inc}\), since the larger eigenvalue of
\(\pi^{-1}H_{\rm inc}\) is at most its trace.

## 3. Assembly on a finite graph

Fix \(Y_e,S_v\ge0\). Require (8) at each incidence, interpreting
the coordinates of an outside vertex as fixed. In particular a
complete outside vertex has \(b_v=1/2,S_v=0\) and is allowed.
The common domain in the variable real coordinates is convex: its
conditions are the linear inequalities
\[
 \alpha(Y_e)<a_e<b_v,\qquad
                    \frac14\le b_v\le\frac12.
 \tag{17}
\]
We assume each variable occurs in at least one incidence. Constant
parts of the graph may simply be omitted.

**Theorem 2.** On (17), the real part of (1) is strictly concave,
for arbitrary real powers \(n_v\) and any finite graph.
On a compact convex subset \(Q\), let
\[
                    m_Q=\min_{(e,v)}\inf_Qm_{e,v}>0.
 \tag{18}
\]
If a holomorphic critical point \(z_*\) lies on this contour, then
\[
 \Re\Phi(z)\le\Re\Phi(z_*)-\frac{\pi m_Q}{2}
       \left(\sum_e(a_e-a_{e,*})^2
                       +\sum_{v\ {\rm selected}}(b_v-b_{v,*})^2\right)
 \tag{19}
\]
for \(z\in Q\).

**Proof.** Extend each incidence matrix by zero in all other
coordinates and sum. Its quadratic form is at least
\(\pi m_Q[(\delta a_e)^2+(\delta b_v)^2]\); a fixed outside
coordinate has \(\delta b_v=0\). Every variable is counted at
least once, so the full negative Hessian dominates
\(\pi m_Q I\). The filling terms have zero real Hessian.
Integrating along the segment from the critical point gives (19).
\(\square\)

This is a phase theorem for graphs of arbitrary size. It does not
assert that a geometric point for every filling power lies in (17).
For example, the homogeneous positive degree-two power-three point
has \(\Re t>\pi/2\), hence \(b<1/4\). Nor does a statement valid
for every real \(n_v\) on this fixed contour say that the selected
geometry of mixed signs has these same heights.

## 4. The exact network test outside this chamber

The full matrix is also explicit without (8). At a regular point
write, for every incidence,
\[
 A_{e,v}=v_{e,v}+2w_e-u_{e,v},\quad
 B_{e,v}=v_{e,v}-u_{e,v},\quad
 C_{e,v}=v_{e,v}+u_{e,v}.
 \tag{20}
\]
Let \(A_e\) be the sum of \(A_{e,v}\) over both endpoints,
including fixed endpoints, and let \(B_v=\sum_{e\ni v}B_{e,v}\)
for selected vertices. Form the edge-by-selected-vertex matrix \(C\)
from \(C_{e,v}\), with zero entries for nonincidences.
If an edge meets the same vertex twice, add its two entries.
Then the full negative real Hessian is
\[
 H_G=\pi
 \begin{pmatrix}
    \operatorname{diag}(A_e)&-C\\
    -C^{\mathsf T}&\operatorname{diag}(B_v)
 \end{pmatrix}.
 \tag{21}
\]

**Proposition 3.** The matrix (21) is positive definite if and only if
\[
 A_e>0\quad\hbox{for every edge},\qquad
 \operatorname{diag}(B_v)
       -C^{\mathsf T}\operatorname{diag}(A_e^{-1})C>0.
 \tag{22}
\]
These are conditions on the real Hessian, not the holomorphic
Schur complement obtained by eliminating stationary wires.

**Proof.** Complete the square in the real wire variables. \(\square\)

For example, a sufficient condition that avoids computing the
eigenvalues of (21) is the existence of positive weights \(p_e,q_v\)
such that
\[
 \begin{split}
 A_e-\sum_v|C_{e,v}|q_v/p_e&>0,\\
 B_v-\sum_e|C_{e,v}|p_e/q_v&>0.
 \end{split}
 \tag{23}
\]
The minimum of these margins, times \(\pi\), is a coercivity
constant. Indeed apply
\(2|XY|\le(q_v/p_e)X^2+(p_e/q_v)Y^2\)
to each cross term. Equations (22)--(23) permit compensation
between incidences; they do not require every individual incidence
matrix to be positive.

Thus a further general extension has a precise target: prove (22),
or construct weights in (23), on a specified connected family of
original contour domains. Positive geometry after wire elimination
alone does not prove (22).

There is an explicit regular positive edge where (22) fails.
Take the exact angles
\[
              t=\frac{21}{10}-\frac{3i}{4},\qquad
              r=\frac34-\frac{3i}{20}.
 \tag{24}
\]
At its stationary wire, all original factorial arguments have real
parts in \((0,1)\), and all eight original tetrahedra have positive
imaginary parts. Nevertheless the \(s_t,s_t\) entry of the
unsummed negative real Hessian is less than \(-59/100\).
The [exact-interval checker](../experiments/check_positive_edge_horizontal_hessian_obstruction.py)
and [saved bounds](../repro/results/research-positive-edge-horizontal-hessian-obstruction.json)
verify these strict inequalities, the original logarithmic
stationary equation, and positivity of the reduced edge Hessian.
This is a counterexample to an implication from positive edge
geometry to fixed-horizontal concavity. It is not asserted to
satisfy any integer unit-filling equation.

## 5. What positive geometry does imply locally

There is a different local statement at every regular positive
geometric configuration. For an edge with angles \(t,r\), put
\[
 a=\tan(t/2),\qquad c=\tan(r/2),\qquad
 q^2=1+a^2+c^2.
 \tag{25}
\]
The original positive branch has
\(\Re q>\sqrt{(\Re a)^2+(\Re c)^2}\), by the
[positive-edge theorem](research_positive_edge_global_monotonicity.md).
The stationary equation for
\(F_e(x;t,r)=b(x,t)+b(x,r)\) gives
\[
                  \cot(\pi x_e^*)=q.
 \tag{26}
\]
To verify it, put \(z=\sin^2\pi x\). Exponentiating the
stationary equation gives
\[
 \frac{(\cos^2(t/2)-z)(\cos^2(r/2)-z)}{z^2}=1,
 \quad
 z=\frac{\cos^2(t/2)\cos^2(r/2)}
          {\cos^2(t/2)+\cos^2(r/2)}
   =\frac1{1+q^2}.
 \tag{27}
\]
More explicitly, choose
\(x_e^*=\pi^{-1}\arctan(1/q)\), continued from \(q=1\).
The right-half-plane condition on \(q\) fixes this holomorphic
branch. The wire factorial sines do not vanish on the regular
positive component: their vanishing would require \(q=\pm a\)
or \(q=\pm c\), excluded by the strict positive-edge inequality.
Thus the exponentiated gradient equal to one in (27) has a
continuous logarithmic lift, which remains zero from completeness.

The same continuation fixes the critical value as \(\psi(t,r)\).
Indeed its \(t\)-derivative is
\[
 -\frac1{2\pi}\Log\frac{\sin\pi(s_t+x_e^*)}
                           {\sin\pi(s_t-x_e^*)}
 =-\frac1{2\pi}\Log\frac{q+a}{q-a}
 =\psi_t(t,r),
\]
with the original logarithms continued from zero; the other
derivative is identical with the endpoints exchanged.
The constants agree at completeness. These are identities of the
continued holomorphic phase, not assertions that one asymptotic
branch dominates the finite factorial source. Direct
differentiation at the stationary wire gives
\[
 H_e=-F_{e,xx}(x_e^*;t,r)
    =\frac{2\pi q(1+q^2)^2}{(1+a^2)(1+c^2)}\ne0.
 \tag{28}
\]
The nonvanishing follows from \(\Re q>0\) and regularity of the
angle coordinates. Its real part need not be assumed positive.

At a fixed positive point, the holomorphic Morse construction with
parameters supplies a local coordinate \(\xi_e\), with
\(\partial_x\xi_e=\sqrt{H_e}\) at the stationary point, such that
\[
           F_e(x;t,r)=\psi(t,r)-\frac{\xi_e^2}{2}.
 \tag{29}
\]
For clarity, this requires no choice of a new phase: divide
\(2\{\psi(t,r)-F_e(x;t,r)\}\) by
\((x-x_e^*(t,r))^2\). The quotient extends holomorphically and
equals \(H_e\ne0\) at the center. Choose its local square root and
multiply it by \(x-x_e^*(t,r)\). The inverse-function theorem
gives (29). The critical value uses the original complete-branch
normalization of \(\psi\).

**Proposition 4.** At any regular positive geometric critical point
of a finite graph, there is a local contour retaining every wire
on which the real phase has a strictly negative Hessian.
The contour keeps the imaginary angular coordinates fixed and
takes all the coordinates \(\xi_e\) in (29) real.

**Proof.** Every wire has its own coordinate (29), so on this contour
the phase is exactly
\[
 \sum_{e=vw}\psi(t_v,t_w)
       +\sum_{v\ {\rm selected}}
                  \left(\frac{in_vt_v^2}{4\pi}-it_v\right)
       -\frac12\sum_e\xi_e^2.
 \tag{30}
\]
The positive-edge theorem gives
\(\Re[-\psi''(t_v,t_w)]>0\) at each edge. Restrict fixed outside
angles and sum these matrices over the graph. Every selected
variable is incident to an edge, so the reduced negative real
angular Hessian is positive definite. Filling terms again have
zero real Hessian on the fixed-height angular contour. The wire
block in (30) is the identity. Positivity persists on a sufficiently
small neighborhood, giving a quadratic real-part gap. \(\square\)

The coordinate changes in (29) have nonzero holomorphic Jacobians.
Accordingly a nonzero original analytic amplitude remains nonzero
under this local change of variables. This does not establish that
the original finite integration cycle has a nonzero coefficient
on this contour, nor that its other pieces are smaller.

The distinction between (22) and (30) matters. The former tests a
fixed horizontal contour for the unsummed phase. The latter changes
the wire directions with the angular variables. A complex
holomorphic Schur complement does not imply the real-matrix
inequality (22). The adapted contour proves local coercivity
without making that invalid inference.

## 6. A common central domain for positive paths of power at least seven

The pair bootstrap extends to paths, but each interior vertex can
have two returns with positive imaginary part. Keeping both of them
gives the following uniform bounds. This section concerns the
positive charge family already proved for paths with a stipulated
complete outside endpoint. It does not extend that existence
theorem to an all-selected path or a general graph.

**Theorem 5 (path geometry).** Take the family in the
[positive fractional-charge theorem](research_positive_path_fractional_charge_cube.md),
with original degrees at most two, integer powers \(n_v\ge7\),
and \(0\le\chi_v\le1\). At an active vertex write
\(t_v=a_v-iH_v\). Then
\[
 0<a_v<\frac{2\pi\chi_v}{n_v-7/20}
                    \le\frac{40\pi}{133}<\frac{19}{20},
 \qquad 0<H_v<\frac3{10}.
 \tag{31}
\]
At every edge with at least one active endpoint the selected
wire \(x_e=\xi_e+iY_e\) satisfies
\[
               \frac15<\xi_e<\frac14,\qquad
                            0<2\pi Y_e<\frac14 .
 \tag{32}
\]
An edge with two complete endpoints has \(x_e=1/4\).
All constants are independent of the path length and of the
individual powers in this range.

*Proof.* The existing
[phase maximum principle](research_geometric_phase_maximum_principle.md#3-a-local-angle-bound-in-terms-of-the-charge)
gives \(a_v<40\pi\chi_v/(17n_v)<\pi/2\).
The [cosine modulus maximum principle](research_positive_path_real_wire_order.md#1-inputs-and-a-cosine-maximum-principle)
gives \(|\cos(t_v/2)|<1\), with value one at complete
vertices. Hence \(|\tan(t_v/2)|<1\).
Write each original return as
\[
 r_{vw}=k_{vw}+ig_{vw}
   =\operatorname{asinh}\{\tan(t_v/2)\cos(t_w/2)\},
 \quad
 \sum_wk_{vw}=\frac{n_vH_v}{2},\quad
 \sum_wg_{vw}=\frac{n_va_v}{2}-\pi\chi_v .
 \tag{33}
\]
Its branch has \(k_{vw}>0\) and \(|g_{vw}|<\pi/2\).
Since \(\Re\operatorname{asinh}z\le\operatorname{asinh}|z|\),
the degree bound implies
\[
 H_v<\frac{4\operatorname{asinh}1}{7}<\frac{18}{35}.
 \tag{34}
\]
Here \(\operatorname{asinh}1<9/10\), as follows from
the first three positive terms of \(\sinh(9/10)\).

For \(C_w=\cos(t_w/2)\), the first angle bound and (34)
give
\(\Im C_w<(5/7)\sinh(9/35)<1/5\).
Also \(\Re C_w>0\), \(\Im\tan(t_v/2)<0\), and
\(\Re\tan(t_v/2)\le\tan(a_v/2)\).
If \(g_{vw}>0\), the identity
\(\sin g_{vw}
=\Im\{\tan(t_v/2)C_w\}/\cosh k_{vw}\)
and \(\arcsin z<(25/24)z\) for \(0<z\le1/5\)
give
\(g_{vw}\le(5/24)\tan(a_v/2)\).
This upper bound also holds when \(g_{vw}\le0\).
There are at most two incidences, so the real period yields
\[
 n_va_v
 \le2\pi\chi_v+\frac56\tan(a_v/2)
 \le2\pi\chi_v+\frac5{3\pi}a_v
 <2\pi\chi_v+\frac8{15}a_v .
 \tag{35}
\]
We used the chord bound
\(\tan(a/2)\le2a/\pi\) on \(0\le a\le\pi/2\), and
\(\pi>25/8\). Thus
\(a_v<30\pi/97<660/679<1\) at every active vertex.

This improves the neighbor estimate to
\[
 \Im C_w<\frac12\sinh(9/35)<\frac2{15},\qquad
 \tan(a_v/2)<\tan(1/2)<\frac47 .
 \tag{36}
\]
For a complete neighbor the first inequality is immediate.
The scalar sinh bound follows from
\(\sinh z\le z/(1-z^2/6)\), and
\(\tan(1/2)<4/7\) follows from
\(\sin(1/2)<1/2\), \(\cos(1/2)>7/8\).
Therefore a positive imaginary return satisfies
\[
 g_{vw}\le\arcsin\!\left\{\frac2{15}\tan(a_v/2)\right\}
     <\frac{101}{750}\tan(a_v/2).
 \tag{37}
\]
Indeed the argument is less than \(8/105\), and
\((101/100)^2\{1-(8/105)^2\}>1\) bounds the derivative
of arcsine by \(101/100\) on this interval.
Sum the two possible positive contributions again. Since
\(404/(375\pi)<3232/9375<7/20\),
\[
 n_va_v
 <2\pi\chi_v+\frac{202}{375}\tan(a_v/2)
 \le2\pi\chi_v+\frac{404}{375\pi}a_v
 <2\pi\chi_v+\frac7{20}a_v .
 \tag{38}
\]
This proves the angle assertion in (31), using
\(40\pi/133<880/931<19/20\).

In particular \(\cos a_v>29/50\). The two height
improvements from the pair bootstrap now apply incidence
by incidence, without a complete neighbor assumption:
\[
 \begin{split}
 |\tan(t_v/2)|^2
 &<\frac{8/7-29/50}{8/7+29/50}
     =\frac{197}{603}<\sinh^2(14/25),
       &&H_v<\frac8{25},\\
 |\tan(t_v/2)|^2
 &<\frac{53/50-29/50}{53/50+29/50}
     =\frac{12}{41}<\sinh^2(21/40),
       &&H_v<\frac3{10}.
 \end{split}
 \tag{39}
\]
The first line uses \(\cosh(18/35)<8/7\); the second
uses \(\cosh(8/25)<53/50\). Each real return is at most
\(\operatorname{asinh}|\tan(t_v/2)|\), because
\(|C_w|\le1\). Equation (33) and degree at most two
therefore give the height bounds displayed in (39).
All these scalar comparisons follow from the positive
hyperbolic series and the alternating cosine series.

For an edge put \(A=\cos^2(t_v/2)\),
\(B=\cos^2(t_w/2)\). The new bounds give
\[
 |A-1|,|B-1|<r,\qquad
 r=\left(\frac{19}{40}\right)^2+
       \left(\frac{3/20}{1-(3/20)^2/6}\right)^2
   =\frac{252350449}{1016334400}<\frac14 .
 \tag{40}
\]
Inversion maps \(D(1,r)\) to a convex disk, so its
harmonic mean stays in \(D(1,r)\). Thus
\(k=AB/(A+B)=\sin^2(\pi x_e)\) belongs to
\(D(1/2,r/2)\), and
\[
 \cosh(2\pi Y_e)=|k|+|1-k|\le\sqrt{1+r^2},
                       \qquad 2\pi Y_e<1/4 .
 \tag{41}
\]
The existing wire-order theorem gives
\(0<\xi_e<1/4\), \(Y_e>0\), on an edge incident to an
active vertex. Since \(\Re k>3/8\),
\(\cos(2\pi\xi_e)<1/4<\cos(2\pi/5)\).
This proves (32). At two complete endpoints the selected
wire is \(1/4\) directly. \(\square\)

**Corollary 6 (a closed central phase domain).** At unit
charges, retain the actual wire and trace heights from
Theorem 5, and the real-coordinate box
\[
 \frac15\le\Re x_e\le\frac3{10},\qquad
                |\Re t_v|\le\frac{2\pi}{5}.
 \tag{42}
\]
In its open regular interior the unsummed original phase
has a uniformly negative real Hessian, with its unique
maximum at the geometric critical point. Its continuous
upper phase has a strict gap on the boundary of this box.
The same incidence positivity statement holds for arbitrary
signs of the fixed heights, though the critical-point
conclusion refers to the actual upper geometric heights.

*Proof.* At a selected incidence \(3/10\le b_v\le7/10\).
The real parts of \(s_v+x_e\) and \(s_v-x_e\) lie,
respectively, in \([1/2,1]\) and \([0,1/2]\).
Consequently \(u\le0\), \(v\ge0\), and \(w>0\)
where the cotangents are finite, independently of height
signs. Use the positive decomposition (9), which does
not include a complete-end contribution. The numbers
\(-u\) and \(v\) cannot both vanish on this box:
the simultaneous real-coordinate endpoint possibilities
would require \((a,b)=(1/4,1/4)\) or
\((1/4,3/4)\), or \(a=0,1/2\), all outside (42).
For an outside complete vertex \(b=1/2\), the same
strict positivity applies to its variable wire coordinate.

On a closed factorial wall a cotangent can diverge when
its imaginary argument also vanishes. No finite Hessian
value at such a corner is asserted. The diverging term
is positive semidefinite in (9). Discard it locally;
the other nonzero incidence term and \(w>0\) retain
a positive lower bound. A finite cover of the compact
box gives a uniform bound on its open regular interior.
Sum the incidence matrices exactly as in Theorem 2.
The geometric point lies strictly inside (42), by (31)–(32).
Integrating the Hessian bound along segments from it gives
a quadratic phase loss. The original real primitive
\(J\) is continuous at zero and one, so passage to the
closed factorial walls preserves the inequality.
This proves the boundary gap. \(\square\)

**Corollary 7 (the cost of completing selected vertices).**
Retain the full original edge constants and let
\(M(\chi)=\Re\Phi_\chi(t(\chi))\) be the stationary
action on the family of Theorem 5. Define
\[
 U_{n,d}=\frac{14\pi d/5}
                   {(n-2d/5)^2+(7d/5)^2}.
 \tag{43}
\]
For \(0\le\lambda\le\mu\le1\), componentwise,
\[
 0\le M(\lambda)-M(\mu)
 \le\frac12\sum_v U_{n_v,d_v}(\mu_v^2-\lambda_v^2)
 <\frac1{10}\sum_vd_v(\mu_v^2-\lambda_v^2)
 \tag{44}
\]
when at least one coordinate changes. In particular, replacing
the unit charges on a set \(S\) by zero increases the stationary
action by less than \(\sum_{v\in S}d_v/10\), independently
of the other charges and the path length.

*Proof.* Theorem 5 places the entire actual charge family in
\(|\Re t|<1,|\Im t|<1/3\). The exact incidence calculation
(16)--(19) of the
[partial-charge note](research_positive_path_partial_charge_bounds.md#2-the-exact-return-map-is-a-contraction)
therefore applies to this already constructed family, regardless
of the threshold used there to construct it by contraction.
With the removable quotient \(Q_v=\sum_{w\sim v}r_{vw}/t_v\),
it gives
\[
 |Q_v-d_v/2|<d_v/5,\qquad
 t_v=\frac{2\pi\chi_v}{n_v+2iQ_v},\qquad
                   H_v\le U_{n_v,d_v}\chi_v.
 \tag{45}
\]
For the last inequality, write \(Q_v=A+iB\). The expression
\(4\pi\chi_v A/[(n_v-2B)^2+4A^2]\) increases in both
\(A\) and \(B\) on
\(3d_v/10<A<7d_v/10, |B|<d_v/5\), since
\(n_v>9d_v/5\). Its upper corner is (43).
Stationarity gives \(\partial_{\chi_v}M=-H_v\), so
integration yields the non-strict bounds in (44).

For each \(d=1,2\), \(U_{n,d}\) decreases with \(n\ge7\).
At \(n=7\), the two denominators in (43) are respectively
\(1138/25\) and \(1157/25\). Consequently
\[
 \frac{U_{n,d}}{2d}
       \le\frac{35\pi}{1138}<\frac1{10}.
 \tag{46}
\]
This proves the strict last bound whenever a coordinate changes.
All equations keep a zero-charge vertex and its incident complete
edge factors; no edge is deleted by this comparison. \(\square\)

The centered finite-kernel loss \(21/200\) in
[the large-angle incidence lemma](research_path_mixed_trace_currents.md#8-a-stronger-centered-loss-for-a-removed-incidence)
therefore exceeds this action cost by more than \(1/200\)
per affected incidence. This is a local numerical budget,
not a complete source decomposition: every affected edge and
every normal must still satisfy the relevant finite-kernel
bound on the contours actually used.

This is a geometric and phase result. It does not establish
the coefficient of the central piece in the full finite
source or control any discarded wire or angular sector.
The incidence-only theorem in Sections 2–3 already provides
concavity on a larger positive-angle domain; (42) is useful
because it is a common signed-angle box containing every
unit-charge saddle in Theorem 5.

The full-path threshold \(64\) also uses a source estimate
on the complement, not just a saddle location. Its proof
compares each removed vertex with the stationary action
after setting that vertex's charge to zero. A complete-rate
bound for every untouched edge would accumulate an error
with path length and does not make this comparison.
The [wide finite-kernel theorem](research_bare_kernel_thin_rectangle.md#6-the-full-rectangle-through-real-angle-pi-over-two)
and the centered incidence estimates now cover the entire
retained angular contour and its remaining complex endpoints.
The [full path-source theorem](research_uniform_path_trace_assembly.md#7-the-source-theorem-at-powers-seven-and-eight)
combines them with (43)–(46). The geometric and phase results
in this section remain distinct inputs to that source proof;
they do not independently assign a coefficient to its cycle.

The focused exact scalar checks are reproduced by
\(\texttt{python3 experiments/check\_positive\_path\_seven\_geometry.py}\);
the saved record is
[research-positive-path-seven-geometry.json](../repro/results/research-positive-path-seven-geometry.json).
The written maximum-principle and branch arguments, rather
than a numerical path sample, prove the arbitrary-length
scope.
