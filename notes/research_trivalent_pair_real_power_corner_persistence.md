# Corner minima persist at small opposite real powers

Private written proof, 16 November 2026.

The zero-power charge-cube theorem does not extend to arbitrary real
signed powers merely by retaining the original degree bound three.
For the original selected trivalent pair, every sufficiently small
nonzero pair of opposite real powers has a corner minimum at unit
charges. Its corner covector is strictly beyond the covectors of
finite geometric corner limits. This is a counterexample to that
proposed interiority implication, not a statement about integer
fillings, nonhyperbolicity, or quantum noncancellation.
The same construction gives charges strictly below one at which
the zero-power minimum is interior but the signed-power minimum
is a corner.

The archived corner KKT theorem already gives a nonzero integer-power
example at original degree two. The result here concerns original
degree three, arbitrarily small real powers, and locates unit charge
relative to the nearby sharp geometric wall.

## 1. The original graph and variational problem

Take the original six-vertex tree with adjacent selected vertices
\(v,w\), each having two additional distinct outside neighbors.
Every outside angle is zero. Thus the selected set is proper and
\(d_v=d_w=3\). Keep the original angle coordinates and marking.
Prescribe
\[
                 n_v=n,\qquad n_w=-n,\qquad c_v=c_w=c.
                 \tag{1}
\]
Here \(n\) is real. No interpretation as an integer filling slope
is assigned when \(n\notin\mathbb Z\).

At an actual edge write \(s=\Re t\), \(h=\Im t\),
\(g=\Im r\), and \(k=\Re r\). At a corner the dual length
coordinates \(h,k\) are initially formal. The
closed angle conditions are
\(|s_v|+2|g_{w,e}|\le\pi\) at both orientations of every
edge; strictness means both inequalities are strict.
For an oriented edge \(e=(v,w)\), the square coordinates and the
endpoint dual coordinates are
\[
\begin{aligned}
A_P&=s_v/4-g_w/2,&A_Q&=s_v/4+g_w/2,\\
y_P&=g_v/2+s_w/4,&y_Q&=g_v/2-s_w/4,\\
h_v&=2(B_P+B_Q),&h_w&=-2(x_P-x_Q),\\
k_v&=x_P+x_Q,&k_w&=B_P-B_Q.
\end{aligned}
\tag{2}
\]
The edge subscripts on the right are suppressed only in this display.
The full energy is \(4\sum_e(E_P+E_Q)\), with all five original
edges included. Its affine rows are
\[
       \sum_{e\ni v}g_{v,e}-n_vs_v/2=-\pi c_v.
       \tag{3}
\]
At a corner \((A,y)=(\pi/4,-\pi/4)\), the covector
\((U,-U)\) is a valid subgradient exactly when
\[
                  U>0,\qquad \sinh^2(2U)\ge1.
                  \tag{4}
\]
Equality is the finite geometric gradient-limit condition.
Strict inequality is allowed by convex optimality but is not a
finite original geometric corner.

We use the source's exact KKT criterion: the square covectors must
be actual gradients at interior squares and valid subgradients at
corners; all endpoint heights must match, including the zero outside
heights; and
\[
                  \sum_{e\ni v} k_{v,e}+n_vh_v/2=0.
                  \tag{5}
\]
These conditions, together with (3), prove global minimality.
Under strict feasibility the closed minimum is unique, and a positive
original shape solution exists if and only if that minimum is interior.

For \(c\) near one strict feasibility holds for every real \(n\):
set both selected real angles to zero, every selected incidence to
\(-\pi c/3\), and every outside incidence to zero. The rows hold,
and all edge inequalities are strict whenever \(0<c<3/2\).

**Theorem.** There is \(\delta>0\) such that, for \(0<|n|<\delta\)
and \(c=1\), the unique closed minimum has exactly one corner square.
All other squares are interior. Its corner subgradient satisfies
strict inequality in (4). Consequently there is no positive solution
in the original subdivision at these parameters.

The theorem is about small real powers. We may and do choose
\(\delta<1\), so it supplies no nonzero integer-power counterexample.

## 2. An exact two-variable corner certificate

Put
\[
 u_0=\tfrac12\operatorname{arsinh}1,\qquad H_0=4u_0,\qquad
 w(s)=-\tfrac12\operatorname{arsinh}(\cos s),\qquad
 H=2\{U-w(s)\}.
 \tag{6}
\]
The use of \(w(s)\) here denotes a scalar function, not the selected
vertex. At the internal edge choose
\[
 (A_P,y_P)=(\pi/4,-\pi/4),\quad (x_P,B_P)=(U,-U),
\]
\[
 (A_Q,y_Q)=(s/2-\pi/4,s/2-\pi/4),\quad
                         (x_Q,B_Q)=(w(s),w(s)).
 \tag{7}
\]
For \(0<s<\pi\), the \(Q\)-square is interior and its displayed
covector is its actual gradient. Indeed the square inverse is
\[
 E_A(A,y)=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),
 \quad
 E_y(A,y)=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)),
 \tag{8}
\]
and at \(A=y=s/2-\pi/4\) both expressions equal
\(\tfrac12\operatorname{arsinh}(-\cos s)\).
At \(s=0\), their limits are \(-u_0\).

Substitution into (2) gives exactly
\[
\begin{gathered}
 s_v=s,\quad s_w=-s,\quad
 g_{v,e}=g_{w,e}=s/2-\pi/2,\quad
 h_{v,e}=h_{w,e}=-H,\\
                   k_{v,e}=U+w(s),\qquad
                   k_{w,e}=-U-w(s).
\end{gathered}
\tag{9}
\]

On each of the two outside edges at \(v\), take the actual positive
configuration with selected angle \(t=s-iH\) and outside angle zero.
Its selected return on the original branch is
\[
           R(s,H)=\operatorname{arsinh}
                         \bigl(\tan((s-iH)/2)\bigr).
           \tag{10}
\]
This is holomorphic near \(t=-iH_0\), where
\[
 \tan(-iH_0/2)=-i/\sqrt2,\qquad R(0,H_0)=-i\pi/4.
 \tag{11}
\]
These are the positive outside edges of the known zero-power pair
limit; their strict positivity persists in a neighborhood. Formula
(10) uses the continuation from completeness along the imaginary
axis. No logarithmic branch is reset. The outside endpoint return
is zero. At \(w\), use the reflected angle \(-s-iH\); its selected
return is \(-\overline{R(s,H)}\), with the same imaginary part and
opposite real part.

All endpoint heights therefore match. The two real rows (5) reduce
to one equation, and likewise the two imaginary rows (3):
\[
\begin{aligned}
 F_1(U,s,n,c)&=U+w(s)+2\Re R(s,H)-nH/2=0,\\
 F_2(U,s,n,c)&=\pi/2-s/2-2\Im R(s,H)+ns/2-\pi c=0.
\end{aligned}
\tag{12}
\]
These are real-analytic equations near \((U,s,n,c)=(u_0,0,0,1)\).
Their real analyticity does not assert geometric realizability of
the internal corner covector when (4) is strict.

## 3. The implicit solution and global minimum

At the base point both equations (12) vanish. We have
\[
 w(0)=-u_0,\quad w'(0)=0,\quad
 \partial_t\operatorname{arsinh}\tan(t/2)\big|_{-iH_0}
                          =\frac1{2\sqrt2}.
 \tag{13}
\]
The last derivative is \(1/(2\cos(t/2))\) on this original local
branch. Since \(H_U=2\) and \(H_s=0\) at the base,
\[
 \frac{\partial(F_1,F_2)}{\partial(U,s)}
 =\begin{pmatrix}1&1/\sqrt2\\ \sqrt2&-1/2\end{pmatrix},
                    \qquad \det=-3/2.
 \tag{14}
\]
The real-analytic implicit-function theorem gives unique local
functions \(U(n,c),s(n,c)\). At \(c=1\), differentiating with
respect to \(n\) gives
\[
 \begin{pmatrix}1&1/\sqrt2\\ \sqrt2&-1/2\end{pmatrix}
 \binom{U_n}{s_n}=\binom{H_0/2}{0}.
 \tag{15}
\]
Consequently
\[
 U(n,1)=u_0+\frac{H_0}{6}n+O(n^2),\qquad
 s(n,1)=\frac{\sqrt2 H_0}{3}n+O(n^2).
 \tag{16}
\]
For all sufficiently small \(n>0\), we have \(U>u_0\),
\(0<s<\pi\), and \(H>0\). Thus (4) holds strictly, the
\(Q\)-square is interior, and the four outside edges remain
positive. The exact construction (7)--(12) satisfies every
square condition, matching condition, and affine/real row of
the original KKT theorem. It is therefore the global minimum.
Strict feasibility and the uniqueness theorem make it the unique
closed minimum. Its \(P\)-square is a corner, so it cannot be an
interior positive solution. Interchanging \(v,w\) proves the same
claim for \(n<0\). This proves the theorem.

The strict inequality \(\sinh^2(2U)>1\) is essential. These
matched dual coordinates do not describe a regular original
analytic period point at the corner. In particular one must not
insert their formal internal returns into the rational shape
equations. The conclusion is the absence of an interior minimizer
for this subdivision, not the failure of an independently continued
geometric solution or its quantum coefficient.

## 4. The nearby sharp wall and the side containing unit charge

The same exact equations locate the finite geometric corner.
Impose \(U=u_0\). Since \(F_{1,s}=1/\sqrt2\) at the base, the
first equation in (12) determines \(s=s_b(n)\), with
\[
                 s_b(n)=\frac{H_0}{\sqrt2}n+O(n^2).
                 \tag{17}
\]
Define \(c_b(n)\) from the second equation. Then
\[
                 c_b(n)=1-\frac{H_0}{2\sqrt2\pi}n+O(n^2).
                 \tag{18}
\]
For \(n>0\) small this is a charge strictly between zero and one.

Here the corner is genuinely sharp: \(U=u_0\) satisfies equality
in (4), and it is the finite gradient limit with equal inward
square slopes. The other square and outside edges are positive.
The exact coordinate identities (2), with these gradient-limit
covectors, match their original angles and returns. Thus (12)
at \(c=c_b(n)\) is an original finite one-square corner period
solution, as opposed to the strict-subgradient unit-charge point.

For an explicit branch check, the \(P\) strip and its companion
coordinate are
\[
 P=u_0-i\pi/4,\qquad
 f(P)=\arctan\tanh P=\pi/4-iu_0.
 \tag{19}
\]
The \(Q\) strip has \(Q=w(s)+i(s/2-\pi/4)\) and
\(f(Q)=s/2-\pi/4+iw(s)\). The original identities
\(t=2(f(P)+f(Q))\), \(u=-2i(P-Q)\),
\(r_t=P+Q\), \(r_u=i(f(Q)-f(P))\) give precisely (9),
with \(U=u_0\). These identities are also recovered directly
from the square-coordinate dictionary (2) and its inverse.
Both disk coordinates are away from the four excluded points;
the \(P\) disk point is \(e^{-i\pi/4}\) and the \(Q\) point is
interior for \(s>0\). This verifies the regular one-square scope.

Finally (14) gives
\[
                         U_c(0,1)=\sqrt2\pi/3>0.
                         \tag{20}
\]
After reducing the neighborhood, \(U_c>0\) throughout it.
For each sufficiently small fixed \(n>0\), the unit charge lies
above \(c_b(n)\), on the \(U>u_0\) side. Equations (16) and
the exact KKT proof show that it lies on the strict supporting-
covector side of this wall. This comparison does not identify
that covector with the geometric analytic continuation through
the wall. No assertion about a different positive subdivision
is made.

**Corollary.** Interiority of the zero-power minimum at a fixed
charge vector in \((0,1)^S\) does not imply interiority after
assigning arbitrary real signed powers.

**Proof.** On the same selected pair, take \(n>0\) small and set
\[
                  c(n)=1-\frac{H_0}{4\sqrt2\pi}n.
                  \tag{21}
\]
In addition to (20), equation (14) gives \(s_c(0,1)=-2\pi/3\).
Therefore the exact solutions of (12) at these charges satisfy
\[
 U(n,c(n))=u_0+\frac{H_0}{12}n+O(n^2),\qquad
 s(n,c(n))=\frac{5\sqrt2 H_0}{12}n+O(n^2).
 \tag{22}
\]
They have a valid strict corner subgradient and an interior
\(Q\)-square, so the same KKT proof gives their unique corner
minimum. But \(0<c(n)<1\), and the zero-power charge-cube
theorem supplies the unique interior positive solution at these
identical charges when the two powers are zero. Its angle
assignment has \(s_v=s_w=0\), so it remains a strictly feasible
test assignment for the new powers. Thus availability of that
positive test assignment, and the resulting comparison of minimum
energies, do not force an interior minimum. \(\square\)

## 5. Coverage, scope, and source readback

The source coverage check found the zero-power trivalent-pair
exception and the degree-two integer-power \((2,-2)\) KKT example.
Neither is the small-real-power degree-three family proved here.
The new conclusion is a falsification of the proposed extension
from zero-power charge-cube positivity to all real signed powers.
It does not create a knot family or obstruct the separate large-
degree geometry and source theorems.

All three complete direct source versions were read, their used
implications checked, and their hashes verified:

- [Original convex variation](research_positive_filling_convex_variation.md),
  SHA256 2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0:
  square inverse, exact coordinate dictionary, original primitive
  variational equations, strict feasibility, and uniqueness of the
  closed minimum.
- [Corner KKT theorem](research_positive_filling_corner_kkt.md),
  SHA256 6c70541966289535c95cd223050ca68e1748b076a2bb3021f941f2744df26a71:
  sharp versus strict corner subgradients, the full graph certificate,
  and the prior degree-two example.
- [Zero-power charge cube](research_zero_power_charge_cube_positivity.md),
  SHA256 91b0a03a677c9139bbfd04f9ef6b06b23e6c3fab435c1a974a2d243189925faf:
  original trivalent-pair base, its four positive outside edges,
  canonical returns, and the precise zero-power exception being tested.

Only written mathematics, source reads and file hashes are used.
No mathematical program, numerical experiment, test or compilation
is run. Frozen notes, manuscripts and public documents are unchanged.
