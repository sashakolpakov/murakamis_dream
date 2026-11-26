# Zero-collar repair with raw right exterior edges

Research deduction, 5 November 2026. The complete zero-collar replacement
inequality extends to a mixed coherent/raw exterior. Its loss is unchanged:
\(3/1000\) per collar coordinate, before a single finite-source tolerance.
This reduces the full-period zero-collar region to the ordinary nonlow
mixed upper envelope. It does not assume that the latter envelope is
already bounded globally, and proves no full-period asymptotic on its own.
No new parameter cover or critical root is required.

## 1. One raw edge and its exact height branches

Fix the right endpoint at \(1/2\), write the other endpoint as
\(z=x+ih\), and use the original conventions
\(\alpha\in\{0,1\}\) for its type, \(\sigma\in\{0,\alpha\}\)
for its selection, and \(d=1\) when it is the first argument.
The original own-factorial indicator is \(\epsilon\). With the
normalized primitive
\(g(z)=(\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6)/(2\pi i)\),
put
\[
\begin{split}
 Q(u,z)&=g(u+1/2)+g(u+z)-(2+\epsilon)g(u)
                 +2\pi i\{dz+(1-d)/2\}u,\\
 F_q(u,z)&=Q(u,z)-\left(1+\frac{\alpha-q}{2}\right)g(z)
                       +\pi i(\sigma-q)z,
                 \qquad q\in\{0,\sigma\}.
\end{split}                                                     \tag{1}
\]
These are the literal allocated branches of the
[raw-row theorem](research_mixed_raw_row_stationarity.md), including
its chirp and both Fourier alternatives. For type-four unselected
heights use \(h\le0\); for selected heights use \(h\ge0\).
Type three allows either sign. The right endpoint's formal Fourier
upper rate is zero. This says nothing about nonvanishing of its
actual Fourier polynomial.

For \(x\in[.1,.5]\), \(|h|\le.057\), the
[whole-row bracket](research_mixed_right_boundary_row_bracket.md)
gives the complete raw rate on those physical bands as
\[
 \mathcal R(h)=\max_{q\in\{0,\sigma\}}
                 \max_{u\in[1/5,2/5]}\Re F_q(u,x+ih).
 \tag{2}
\]
The unique maximizing row is interior. We use the fixed bracket in
(2), not a height-dependent interval of rows.

**Lemma 1.** On any physical height segment from zero to an admitted
hybrid height, \(\mathcal R\) is convex. In fact every fixed-row
branch in (2) is height-convex throughout the larger strip
\(x\in[.1,.5],\ |h|\le.057\).

For clarity this larger-strip assertion concerns the explicit raw
function (1), not existence of a coherent packet on an independently
enlarged parameter rectangle. To prove it, write
\[
 \Re\cot\pi(x+ih)=
       \frac{\sin(2\pi x)}{\cosh(2\pi h)-\cos(2\pi x)},\qquad
 \partial_x\Re\cot\pi(x+ih)=
 \frac{2\pi\{\cosh(2\pi h)\cos(2\pi x)-1\}}
      {\{\cosh(2\pi h)-\cos(2\pi x)\}^2}.
 \tag{3}
\]
The bracket theorem's elementary scalar bound gives
\(e^{2\pi|h|}<3/2\), whence \(\cosh(2\pi h)<13/12\).
Also \(\cos(\pi/5)=(1+\sqrt5)/4<13/16\). Therefore, on
\(.1\le x\le.5\),
\[
       \cosh(2\pi h)\cos(2\pi x)<169/192<1.                \tag{4}
\]
For negative cosine the inequality is immediate; for nonnegative
cosine use the displayed bounds. Thus the real cotangent decreases
strictly up to \(1/2\). After \(1/2\) and before 1 it is
nonpositive, whereas its value at the own real coordinate is
nonnegative. Since \(.3\le x+u\le.9\) and
\(1+(\alpha-q)/2\ge1\),
\[
 \partial_h^2\Re F_q(u,x+ih)
 =-\Re\left\{g''(x+u+ih)
            -\left(1+\frac{\alpha-q}{2}\right)g''(x+ih)\right\}>0.
 \tag{5}
\]
A supremum of convex functions on the same interval is convex.
This proves the lemma without replacing the real row maximum by
complex stationarity.

## 2. The old exterior fees also pay a raw edge

Let \(p\) and \(h\) be a neighboring coordinate's physical and
repaired heights, with \(p=\tau h\), \(0\le\tau\le1\), and
put \(\delta=h-p\). At height zero the factorial/frequency branch
\(q=0\) attains the maximum in (2), since
\(J(x)=\Re g(x)\le0\). Choose its maximizing row \(u_0\).
The imaginary part of its original outer marginal is exactly
\[
 \Im K_0(u_0,x)
 =\pi\left\{(2d-1)u_0-\frac\alpha2(1/2-x)+\sigma\right\}.
 \tag{6}
\]
The selected allocated half-correction is \(-\pi h\); this is
why the last coefficient in (6) is \(\sigma\), not
\(\sigma/2\). The right endpoint's possible forcing tie is
irrelevant to this derivative.

Convexity first gives a chord comparison and then the supporting
line of this active branch at zero:
\[
 \begin{split}
 \mathcal R(p)-\mathcal R(h)
 &\le(1-\tau)\{\mathcal R(0)-\mathcal R(h)\}\\
 &\le(h-p)\Im K_0(u_0,x).
 \end{split}                                                   \tag{7}
\]
For \(h=0\) this is the equality zero. Since \(0\le u_0\le1/2\),
with \(\theta_x=\pi(1/2-x)\), (7) implies
\[
\begin{array}{ll}
 d=0:&\mathcal R(p)-\mathcal R(h)
 \le Q_L(x,h,p):=(\pi\sigma-\alpha\theta_x/2)\delta
                                      +(\pi/2)(-\delta)_+,\\[2mm]
 d=1:&\mathcal R(p)-\mathcal R(h)
 \le Q_R(x,h,p):=(\pi\sigma-\alpha\theta_x/2)\delta
                                      +(\pi/2)(\delta)_+.
\end{array}                                                     \tag{8}
\]
These are exactly the fees in
[general-angle seam replacement](research_mixed_general_angle_seam_replacement.md),
equation (9). For a neighbor on the left of a seam, its exterior
right-incident edge has order \(R\to A\), hence \(d=0\) and
fee \(Q_L\). On the right it has order \(A\to R\), hence
\(d=1\) and fee \(Q_R\). All original endpoint halfweights
are retained. The existing nonnegativity of these fees on the
physical height bands is unchanged.

## 3. The repaired raw benchmark dominates its coherent benchmark

After a seam coordinate is repaired to its reference real part and
made unselected, its target lies in the admitted unselected
reference-real height box. A neighboring right target is real
\(1/2\). The original bare conditional kernel on this product
has the nonzero complete packet supplied by the
[right-square theorem](research_mixed_unselected_right_taper_products.md).
The same kernel obeys the literal triangle inequality
\[
                  |C_{\epsilon,N}(X,Y)|
                     \le\sum_{j=0}^{N-1}|\text{original row}_j(X,Y)|.
 \tag{9}
\]
Its complete packet is a nonzero symbol times a fixed power of
\(N\) times its original exponential phase, with a relative error
tending to zero. The complete raw upper bound on the right has its
original row-envelope exponent and arbitrarily small exponential
tolerance. Taking exponential rates in (9) consequently shows that
the bare raw exponent is at least the real part of the original
bare coherent exponent. Otherwise those two established bounds
would contradict (9) for all large \(N\).

Now add the same formal allocated Fourier upper rates to both
sides. At the repaired unselected type-four endpoint the actual
height is nonpositive and its real part is below \(.5\), so that
formal rate is \(-\Re g/2\). At the right endpoint it is zero.
Type three has no Fourier factor. Thus
\[
       \mathcal R_e(z^\#_{j-1},z^\#_j)
                \ge e_e(z^\#_{j-1},z^\#_j)
                  \quad\text{on every repaired SR boundary edge},
 \tag{10}
\]
where \(e_e\) is precisely the coherent allocated benchmark used
in the closed-half seam proof. Any original selection at the real
right endpoint has correction zero.

This deduction divides by no actual Fourier polynomial and requires
no lower bound for it at \(X=-1\). It compares exponents of the
bare kernel first. The only coherent packets invoked here are on
the already proved repaired products, not at the original zero
seam and not at an angle exceeding \(1/2\).

## 4. A source allocation with seam priority

Fix \(0<\rho\le.001\), independently of \(N\), and use the original
periodic hybrid contour. Give the original coordinates disjoint labels
\[
 S=\{j:0\le x_j\le\rho\},\qquad
 R=\{j:x_j\ge.5\},\qquad
 A=\{j:\rho<x_j<.5\}.
 \tag{11}
\]
Use the following complete upper envelope \(\mathcal U_S(x,\sigma)\):

* Every SS edge uses the closed seam-seam raw ceiling.
* Every other S-incident edge uses its height-resolved collar profile,
  including its collar numerator and Fourier costs, even if the other
  endpoint is R.
* Every remaining R-incident edge uses the complete raw row envelope.
* All remaining edges use their original coherent allocated rate.

These are bounds for the same literal allocated finite blocks, whose
two halves restore every original factorial, selected monomial and
Fourier polynomial once. The
[height-profile theorem](research_mixed_height_resolved_seam_sources.md)
is uniform in the other real angle on the whole period and in its
physical height bands. Thus the second item is valid on SR as well
as SA. This choice is not an assertion that a previously chosen
R-priority envelope is numerically below a collar profile.

First put every original R coordinate at \(1/2\). On an S-incident
edge its profile is unchanged, since the right height stays zero and
the profile is independent of that real angle. Every remaining raw
right-edge rate increases by the
[complete right-row comparison](research_mixed_complex_right_row_reduction.md).
All other targets remain unchanged because the slow and fast left
cutoffs equal one throughout R. Next raise every A coordinate below
\(.1\) to \(.1\). Its own and both neighboring heights remain
zero throughout that motion. The
[exact low transport](research_mixed_exact_low_transport.md)
shows that its coherent AA and raw AR rates increase; its S-incident
profile is unchanged. Write the resulting configuration as \(\widehat x\).
Then
\[
                \mathcal U_S(x,\sigma)
                         \le\mathcal U_S(\widehat x,\sigma).
 \tag{12}
\]
All nonseam coordinates of \(\widehat x\) lie in \([.1,.5]\),
and the original R labels are retained at \(1/2\).

Now replace every seam real coordinate by \(\Re r_s\), erase its
selection, and recompute every height on the same hybrid graph.
Denote these targets by \(z^\#\), their real coordinates by
\(x^\#\), and the selections by \(\sigma^\#\). Every nonseam
height changes from \(p\) to \(h\) with the same sign and
\(|p|\le|h|\). All original collar attenuations
\(1-x_s/\rho\in[0,1]\) are retained in \(p\); they are not
replaced by the early bound \(1/6\).

Let \(\mathcal E_R(x^\#,\sigma^\#)\) be the ordinary nonlow
mixed envelope: raw on every edge with an original R endpoint,
coherent on all other edges. Newly repaired S positions are not
relabelled R.

**Theorem 2 (mixed exterior seam repair).** The original envelope satisfies
\[
 \boxed{\quad
 \mathcal U_S(x,\sigma)
       \le\mathcal E_R(x^\#,\sigma^\#)-3|S|/1000 .
 \quad}                                                       \tag{13}
\]
Here \(x^\#\in[.1,.5]^m\), with every original R coordinate at
\(1/2\). For \(S=\varnothing\), omit the last term and the seam
replacement; (12) gives the stated reduction.

## 5. Why the existing run proof transfers without new constants

Use Sections 2--3 of the
[closed-half theorem](research_mixed_closed_half_period.md), stopping
before its final comparison with \(M\). Its local inequalities
compare the complete seam-incident source to the repaired coherent
edges and reserve the fees \(Q_L,Q_R\) for exterior height changes.
They allow every physical and repaired height pair in its full
triangle, all selections, and all neighboring angles in \([.1,.5]\).

An SS repaired edge is coherent and retains its strict reserve
\(1/3\). A proper run of \(k\ge2\) seam vertices has boundary
deficit less than \(.09\) on the left and a nonpositive deficit
on the right, both including the reserved exterior fee. Hence its
loss is at least
\[
                 (k-1)/3-.09\ge3k/1000.
 \tag{14}
\]
A singleton uses the original general-angle pair inequality with
loss \(3/1000\). If a run boundary meets R, replace its repaired
coherent benchmark by the larger raw one using (10); this weakens
none of these comparisons.

For an exterior edge that remains coherent, its old fee argument is
unchanged. For an exterior raw edge the changed endpoint is A,
while its right endpoint has height zero throughout; (8) supplies
exactly the old reserved fee. An RR edge never changes. If both
endpoints of an exterior coherent edge change, telescope their two
changes once as in the old proof. A nonseam vertex with one seam
neighbor has at most one exterior incidence; with two seam neighbors
it has none. The fees are nonnegative, so reservations for absent
incidences are harmless. No original edge or halfweight is consumed
twice.

If the entire cycle is S, every edge is SS and its repaired target
is the actual reference; the stronger reserve \(m/3\) applies.
A one-cycle therefore has no missing boundary case. A mixed
two-cycle retains its two parallel edges and has no exterior edge
at its nonseam vertex. Shared neighbors in longer cycles obey the
same incidence argument. These facts prove (13) for arbitrary
words and seam runs, with no word-length enumeration.

## 6. Literal finite-source consequence and scope

For each fixed word, fixed collar and fixed total tolerance
\(\delta>0\), the existing sources and the exact graph Jacobian give, at every
differentiability point of the graph and hence almost everywhere,
\[
 |\mathcal D_{N,\sigma}(z(x))\det(I+iD\mathcal H_\sigma(x))|
 \le C_\delta N^A
 \exp N\{\mathcal E_R(x^\#,\sigma^\#)-3|S|/1000+\delta\}.
 \tag{15}
\]
The tolerance is spent once over the physical edges. All original
scalars, carriers, finite rows and Fourier alternatives are retained,
including both level parities and zeros. The comparison is of upper
rates; it is not a change of variables or an inequality between
finite kernel values at the two targets.

In particular, **if** the ordinary nonlow mixed envelope on the right
of (15) has a proved uniform bound \(M\), then every nonempty seam
region has finite loss at least \(|S|/500\) after choosing total
\(\delta<1/1000\). Any proved stricter nonlow bound can likewise
be retained. This note supplies that implication and the unconditional
reduction (13); it does not assert the remaining global nonlow bound,
a new knot-family result, or partial-filling stability.

Reproduction (exact identities and current source bindings only):

    python3 experiments/check_mixed_seam_raw_exterior_repair.py
    python3 experiments/check_mixed_seam_raw_exterior_repair.py --input repro/results/research-mixed-seam-raw-exterior-repair.json --output repro/results/research-mixed-seam-raw-exterior-repair-replay.json
