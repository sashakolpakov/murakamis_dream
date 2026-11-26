# Positive geometry on the zero-power charge cube

Private written proof, 16 November 2026.

For a connected zero-power selected tree with original degrees at
least three, the original positive primitive solution exists on the
entire charge cube \(0<c_v\le1\), except at the upper corner of
the selected trivalent pair. In particular a supplied positive
unit-charge endpoint is joined to completeness by its positive
radial charge branch. This sharpens the sufficient degree condition
in the archived convex height potential. The zero-power knot family
was already treated by the separate Newton and Conway constructions;
no new quantum asymptotic or knot family is asserted here.

## 1. Original data and statement

Let \(T\) be a finite original circle tree and let \(S\ne\varnothing\)
be a connected proper set of vertices. Write \(d_v\) for the degree
of \(v\) in \(T\), including its edges to the outside. Include every
edge incident to \(S\) once, put every outside angle equal to zero,
and set every selected original crossing power equal to zero.
Keep the original complete branches and primitive equations
\[
 \sum_{e=vw}r_{v,e}(\mathbf t)=-\pi i c_v,\qquad
 r_{v,e}=\operatorname{arsinh}
       \bigl(\tan(t_v/2)\cos(t_w/2)\bigr),\qquad 0<c_v\le1.
 \tag{1}
\]
The sum uses the original incidences. Positivity means that all eight
tetrahedra of each included original edge block have positive
imaginary shapes on the branch from completeness, not positivity
after replacing the subdivision.

**Theorem 1.** Suppose \(d_v\ge3\) for every \(v\in S\).

1. For every charge vector in \((0,1]^S\), (1) has exactly one
   positive solution, except when \(S\) consists of two adjacent
   vertices of original degree three and both charges equal one.
   Every existing solution has \(t_v=-iH_v\), \(H_v>0\), and is
   locally holomorphic in the full complex charge vector.
2. The positive configurations depend continuously on the charges
   and stay in a compact subset of the original positive domain
   on every compact subset of the cube avoiding the exception.
   For each fixed charge vector \(\mathbf c^0\) at which the
   solution exists, the entire radial path
   \(\mathbf c=\lambda\mathbf c^0\), \(0\le\lambda\le1\),
   is positive and analytic, including its complete endpoint.
3. At the exceptional pair's upper corner the unique limiting
   heights are
   \[
                       H_v=H_w=2\operatorname{arsinh}1.
                       \tag{2}
   \]
   The internal edge has \(q=0\), its two selected return angles
   are \(-\pi/2\), and the four outside edges remain positive.
   There is no positive solution at that corner.

Thus the exact unit-charge criterion for an arbitrary connected
proper all-zero selected subtree is
\[
 \boxed{\quad d_v\ge3\text{ at every selected vertex, and }
 S\text{ is not a selected trivalent pair}.\quad}
 \tag{3}
\]
The pair has its other four original edges to complete outside
vertices. There is no bound on the size of \(S\).

## 2. The charge-scaled height minimum

Use the original height potential from the first pinned source:
\[
 \begin{split}
 J(x)&=\int_0^x\log(2\sin\pi s)\,ds,\\
 B(x,h)&=\int_0^x\log(2\cos2\pi s+2\cosh h)\,ds-2J(x),\\
 V(h,g)&=\max_{0\le x\le1/2}\{B(x,h)+B(x,g)\},
                         \qquad h,g\ge0.
 \end{split}
 \tag{4}
\]
Endpoint integrals have their continuous values. The maximizing
index is unique. Write \(r=\sinh(h/2)\), \(s=\sinh(g/2)\).
If \(rs<1\), the maximum is interior, and
\[
 \pi V_h(h,g)=\alpha(h,g)
       =\arcsin\frac{r\sqrt{1+s^2}}{\sqrt{1+r^2}}.
 \tag{5}
\]
If \(rs\ge1\), the maximum is \(x=1/2\), and
\[
                   V(h,g)=(h+g)/2,\qquad \pi V_h=\pi/2.
                   \tag{6}
\]
The first derivatives match continuously at \(rs=1\). Call an
edge regular when \(rs<1\), and saturated otherwise. An edge
to a complete outside vertex is always regular.

The source proves convexity of \(V\) on the nonnegative quadrant.
At a regular edge its two-variable Hessian is positive definite;
on an outside edge the remaining scalar Hessian is
\[
                         V_{hh}(h,0)=\frac1{2\pi\cosh(h/2)}>0.
                         \tag{7}
\]
At \(h=0\), with the other height finite, its one-sided height
derivative is zero. Define
\[
 \mathcal L_{\mathbf c}(\mathbf H)
    =\sum_{vw\ {\rm included}}V(H_v,H_w)-\sum_{v\in S}c_vH_v,
                  \qquad H_w=0\quad(w\notin S).
 \tag{8}
\]

**Lemma 2.** For every \(\mathbf c\in(0,1]^S\), (8) has a unique
minimizer on \([0,\infty)^S\). All its coordinates are finite
and positive, every selected vertex meets a regular edge, and
\[
                            \sum_{e\ni v}\alpha_{v,e}=\pi c_v.
                            \tag{9}
\]

**Proof.** Choosing \(x=1/2\) in (4), where \(B(1/2,h)=h/2\),
gives the uniform coercive bound
\[
 \mathcal L_{\mathbf c}(\mathbf H)
 \ge\sum_{v\in S}(d_v/2-c_v)H_v
 \ge\frac12\sum_{v\in S}H_v.
 \tag{10}
\]
Continuous sublevel sets are compact, so a minimum exists. At
\(H_v=0\) its one-sided derivative is \(-c_v<0\). Hence every
minimizing height is positive, and stationarity gives (9).
If every incidence at \(v\) were saturated, its derivative sum
would be \(d_v/2>c_v\), a contradiction.

The regular edges therefore cover all selected vertices. Their
Hessians, using (7) on outside edges, sum to a positive definite
form: any nonzero vector has a nonzero selected coordinate and
a regular edge incident to it. This partial sum is locally
strongly convex near the minimizer, while the remaining edge
potentials are convex. Two minima would make their connecting
segment constant, contradicting this local strictness.
\(\square\)

The minimizer varies continuously on the charge cube, including
at the exceptional upper corner. The bound (10) is uniform and
its value is at most \(\mathcal L_{\mathbf c}(0)\), independent
of \(\mathbf c\). Every convergent subsequence of minimizers is
optimal at the limiting charge vector by continuity; uniqueness
identifies its limit.

## 3. The saturated-edge inequality

At positive height, every incidence satisfies
\[
              \alpha_{v,e}\ge\arctan r_v,\qquad
              r_v=\sinh(H_v/2)>0.
              \tag{11}
\]
There is equality on a complete outside edge and strict inequality
on every edge to a selected neighbor. For a regular edge this
follows from (5); for a saturated edge it follows from
\(\pi/2>\arctan r_v\).

Suppose \(vw\) is saturated at the minimizer. Its own contribution
at each endpoint is exactly \(\pi/2\). Apply (11) only to the
remaining \(d_v-1\) and \(d_w-1\) incidences:
\[
 \arctan r_v\le\frac{\pi(c_v-1/2)}{d_v-1}\le\frac{\pi}{4},
 \qquad
 \arctan r_w\le\frac{\pi(c_w-1/2)}{d_w-1}\le\frac{\pi}{4}.
 \tag{12}
\]
If either charge is at most \(1/2\), the first inequality already
contradicts its positive height. Otherwise the displayed upper
bounds follow from \(d_v,d_w\ge3\) and \(c_v,c_w\le1\).
But \(r_vr_w\ge1\) implies
\[
                     \arctan r_v+\arctan r_w\ge\pi/2.
                     \tag{13}
\]
Every inequality in (12)--(13) must therefore be an equality.
Consequently
\[
             d_v=d_w=3,\quad c_v=c_w=1,\quad r_v=r_w=1.
             \tag{14}
\]
Neither vertex can have another selected neighbor, since that
would make its incidence estimate strict. Connectedness makes
\(S\) exactly this pair.

Conversely, for this pair at charges \((1,1)\), \(r_v=r_w=1\)
gives an internal contribution \(\pi/2\) and two outside
contributions \(\pi/4\) at each vertex. It solves (9);
convexity and Lemma 2 make it the unique minimum. This proves
the full saturated-edge classification.

The improvement over the archived sufficient degree condition is
the use of a saturated edge's entire \(\pi/2\) contribution before
estimating its remaining incidences. It is not an enumeration of
short words.

## 4. Original geometry and continuation

At an all-regular minimizer set \(t_v=-iH_v\), with outside heights
zero. Put
\[
 A_v=\tanh(H_v/2)=\frac{r_v}{\sqrt{1+r_v^2}},\qquad
 a_v=\tan(t_v/2)=-iA_v.
 \tag{15}
\]
Then every original edge satisfies
\[
 q_e^2=1-A_v^2-A_w^2
       =\frac{1-r_v^2r_w^2}{(1+r_v^2)(1+r_w^2)}>0.
 \tag{16}
\]
The second source's exact positivity criterion is
\(\Re q>\sqrt{(\Re a_v)^2+(\Re a_w)^2}\).
Thus the positive root in (16) gives the original eight positive
shapes, with all original face denominators regular.

Simultaneously multiplying the heights by \(0\le\lambda\le1\)
keeps their hyperbolic-sine products below one. This fixes the
complete branches, on which
\[
 r_{v,e}^{\rm orig}
   =-i\arcsin\!\left(\tanh(H_v/2)\cosh(H_w/2)\right)
   =-i\alpha_{v,e}.
 \tag{17}
\]
Equation (9) is exactly (1). This height contraction fixes the
logarithmic marking; it is not identified with the radial charge
solution path.

The original global uniqueness theorem makes this solution
unique among all complex positive configurations. Its complex
period Jacobian has positive definite Hermitian part. The
implicit-function theorem consequently gives a holomorphic
solution near each charge vector with a regular minimizer.
These branches agree by uniqueness. Together with continuity of
the minimizer, this also gives the compact-uniform assertion.

To exclude an unobserved positive solution at the exceptional
corner, first note that every positive solution of (1) is purely
imaginary. The reflection \(\mathbf t\mapsto-\overline{\mathbf t}\)
preserves positivity: \(a_v\mapsto-\overline{a_v}\) and
\(q_e\mapsto\overline{q_e}\) preserve the original criterion.
Its canonical returns are \(-\overline{r_{v,e}^{\rm orig}}\),
so it preserves (1). Global uniqueness fixes the reflected point.
At a purely imaginary positive edge the imaginary return has the
same sign as its endpoint's imaginary angle, because its argument
is \(i\tanh(\Im t_v/2)\cosh(\Im t_w/2)\) in \(i(-1,1)\).
The negative row in (1) therefore makes every selected angle
\(-iH_v\) with \(H_v>0\). Such a solution is all regular by
(16) and stationary for (8), contradicting the unique saturated
minimizer at the exceptional pair. No other positive solution
exists there.

At any minimizer, (9) and (11) also give
\[
 0<H_v(\mathbf c)\le
        2\operatorname{arsinh}\tan\!\left(\frac{\pi c_v}{d_v}\right).
 \tag{18}
\]
On a simultaneous radial charge path to zero the heights therefore
tend to zero. The original complete period Jacobian is
\(\tfrac12\operatorname{diag}(d_v)\); its analytic solution agrees
with these solutions by uniqueness. For a fixed nonexceptional
endpoint, the compact radial segment, including zero, is thus
contained in the positive domain. A radial path ending at the
exceptional corner is positive for \(\lambda<1\), and its
minimizer converges to (14). Equations (16)--(17) give (2), the
internal \(q=0\), and the claimed return angles.

For a singleton, no internal edge is present and the solution is
explicit:
\[
            H(c)=2\operatorname{arsinh}\tan(\pi c/d).
            \tag{19}
\]
It exists through unit charge precisely when \(d>2\).
At any positive zero-power unit solution the original canonical
bound \(|\Im r_{v,e}^{\rm orig}|<\pi/2\) likewise forces \(d_v>2\)
at every vertex. This proves the necessity in (3), and the theorem
proves sufficiency. For disconnected selected sets the same
classification applies separately to each selected component,
since all outside angles remain zero.

Compact uniformity above concerns compact subsets of the positive
charge cube avoiding its exceptional point, or fixed simultaneous
radial segments with regular endpoints. It is not uniformity on
all partially zero-charge faces: a zero-charge vertex can become
complete and change the effective selected components.

## 5. Scope and full direct-source readback

This settles radial continuation for the all-zero class. It does
not settle the same question for adjacent nonzero signed powers:
their real angles need not vanish, and the nonnegative incidence
estimate (11) is not supplied by their original equations.

The theorem concerns the original positive subdivision and full
marked primitive periods. The trivalent-pair failure does not
assert nonhyperbolicity of its partially filled parent; the
archived Newton/Conway treatment uses other coordinates. No
charged quantum asymptotic, original-cycle coefficient, or
arbitrary-short hyperbolic coverage follows here.

Both complete direct sources were read and their used implications
checked:

* [Zero-power convex height potential](research_zero_power_subtree_convex_potential.md),
  SHA256
  c0ab73c2869ed3db7a0152634cbf3a315c573eed2f5fc99e437dacadcceb8eb8:
  Sections 2--4 give \(V\), its all-regime derivatives, convexity,
  regular Hessians, and the original unit-charge minimum. The
  proof above supplies the charge cube and sharp classification.
* [Original positive geometry and periods](research_positive_edge_global_monotonicity.md),
  SHA256
  da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500:
  Sections 1--3 give the actual shapes and complete branches;
  Sections 5 and 7 give the original primitive equations,
  global uniqueness, positive Jacobian, and complete initializer.

Only written derivation, source-text reads and file hashes were
used. No mathematical code, tests, numerical experiments or
compilation were run. Frozen notes and public manuscripts were
not changed.
