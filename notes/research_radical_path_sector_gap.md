# Bounding radical edge contributions by the pieces of a path

Research proof, 3 November 2026. The high Newton sector can be
estimated after its exact contraction, without evaluating its
individual polynomials on a complex geometric contour. On a path,
the contracted source separates into pieces with physical boundary
values. Existing bounds over the whole boundary period control many
of these pieces.

This gives two conclusions proved below. For paths whose selected
powers have magnitude at least sixty-four, every nonempty radical
matching has a uniform strict rate gap. For the internal pair of
powers \(3,3\), its entire radical contribution also has a strict
gap, established by an elementary comparison of convex energies.
The latter result does not estimate the remaining low-sector trace.

## 1. What remains after a radical matching is contracted

Use the original kernel, trace, crossing, and radical decomposition
from [the exact contraction theorem](research_high_newton_radical_contraction.md).
Write \(m_N=\lfloor N/2\rfloor\),
\[
 K_N=K_N^{\rm low}+H_N^{\rm rad},\qquad
 W_{ab}=\sum_r b_{ra}b_{rb},\qquad
                 \sum_{a,b}|W_{ab}|\le4m_N^3.
 \tag{1}
\]
Every original crossing value \(R(c_a)^n\) has modulus one,
including for negative powers.

Let \(\Gamma\) be an original finite path. Its selected vertices
carry the original traces and fixed crossing powers. Any unselected
endpoints are ordinary boundary variables. Choose a matching
\(M\) of edges whose two endpoints are selected, and put
\(S=V(M)\). Consider the exact term in which edges in \(M\)
carry \(H_N^{\rm rad}\) and all other edges carry the full
kernel \(K_N\). Call this term \(\mathscr T_{M,N}\). These
are the terms, with signs, in the inverse expansion
\[
 Z_K-Z_{\rm low}
       =\sum_{M\ne\varnothing}(-1)^{|M|+1}\mathscr T_{M,N}.
 \tag{2}
\]

Delete only the edges in \(M\). At their endpoints replace the
traces by the physical values \(c_{a_v}\). Every other edge
remains. Denote the resulting path components by \(C\), and
their original source polynomials by \(F_{C,N}\). In this notation
the crossing values at \(S\) are kept outside \(F_{C,N}\).
An isolated evaluated vertex contributes one. A component with
one edge and no traced vertex contributes the bare kernel.

**Proposition 1.** The matching term is exactly
\[
 \mathscr T_{M,N}
 =\sum_{\mathbf a}
      \prod_{\{v,w\}\in M}W_{a_va_w}
      \prod_{v\in S}R(c_{a_v})^{n_v}
      \prod_C F_{C,N}(\mathbf c_{\partial C}),
 \qquad 0\le a_v<m_N.
 \tag{3}
\]
The boundary arguments of each component include its prescribed
original outside boundaries as well as the physical values at
\(S\).

**Proof.** The joint-spectator version of the radical contraction
theorem replaces each matching edge by \(W\). Every other edge
touching \(S\) becomes \(K_N(c_a,w)\) or \(K_N(c_a,c_b)\).
After the matching edges have been removed, the remaining products
and traces lie in disjoint components of the path, so they factor.
This proves (3), with all original first normals and boundary
polynomial dependence retained. \(\square\)

In particular, the edge between two neighboring matched pairs is
still present. Its factor \(K_N(c_a,c_b)\) can have exponential
size. It is a bare-edge component in (3), with complete-boundary
rate \(M_\infty=4G/\pi\), where \(G\) is Catalan's constant.
It must not be counted as a polynomial cost or replaced by one.

## 2. The rate comparison supplied by whole-boundary estimates

Write \(c_a=-2\cos u_a\), with
\(u_a=\pi-(2a+1)\pi/N\in[0,\pi]\).
Suppose every component in (3) has a proved bound
\[
 \sup_{\mathbf u\in[-\pi,\pi]^{\partial C}}
       |F_{C,N}(\mathbf u)|
       \le A_C N^{b_C}e^{N\mu_C},
 \tag{4}
\]
where \(\mu_C\) is its complete-boundary geometric rate.
For an isolated evaluated vertex take \(\mu_C=0\).

**Theorem 2.** Under (4),
\[
 |\mathscr T_{M,N}|
 \le (4m_N^3)^{|M|}
            \left(\prod_C A_C\right)N^{\sum_C b_C}
                         e^{N\sum_C\mu_C}.
 \tag{5}
\]
The estimate is uniform over the original real outside boundaries.

**Proof.** Use (4) inside (3), the unit moduli of the crossing
values, and (1) separately on each disjoint pair of colors.
\(\square\)

There is an exact geometric interpretation of the rate in (5).
Let \(\lambda^S\) set the charges at \(S\) to zero and keep
all other selected charges equal to one. Suppose the complete
geometries of the components and the original positive stationary
solution exist with the stated marking. Reinsert the matching
edges as complete edges. Their endpoints have angle zero, so
their zero-charge equations hold, and each inserted edge adds
\(M_\infty\) to the absolute stationary action. Consequently
\[
       \sum_C\mu_C
       =M_\Gamma(\lambda^S)-|M|M_\infty.
 \tag{6}
\]
This is the same complete-edge accounting as in
[the edge-cut energy identity](research_edge_cut_energy_comparison.md).

Thus, if the desired full rate is \(M_\Gamma(\mathbf1)\),
the sufficient strict comparison is
\[
 M_\Gamma(\lambda^S)-M_\Gamma(\mathbf1)<|M|M_\infty.
 \tag{7}
\]
Together, (4) and (7) give an actual upper bound on the whole
coherent radical term. The argument never substitutes the larger
product of absolute individual-color contributions for a remaining
trace. For fixed \(\Gamma\) there are finitely many matchings,
so strict gaps for all of them also bound their sum in (2).

The hypothesis (4) is already available for the bare edge, the
proved single-vertex two-boundary sources, and the other original
pieces with proved whole-boundary estimates. It is not presently
established for every connected cluster of short powers.

## 3. A strict radical gap for the proved long paths

**Corollary 3.** Suppose every selected power satisfies
\(|n_v|\ge64\), with independently chosen signs. Then every
nonempty matching obeys
\[
 |\mathscr T_{M,N}|
 \le C_MN^{a_M}
  \exp N\!\left[
 M_\Gamma(\mathbf1)
       -|M|\left(M_\infty-\frac1{200}\right)\right].
 \tag{8}
\]
Here complete outside boundaries are used to define
\(M_\Gamma(\mathbf1)\); the upper bound holds uniformly over
their real boundary periods when those endpoints are left free.

**Proof.** Every component after the cut is a long path with
one or two boundary endpoints, a bare edge, or a constant factor.
The one- and two-boundary estimates in
[the path trace theorem](research_uniform_path_trace_assembly.md),
Section 5, prove (4). The complete geometries and charge comparison
are supplied by
[the signed partial-charge theorem](research_positive_path_partial_charge_bounds.md),
Corollary 3. In its notation,
\[
 M_\Gamma(\lambda^S)-M_\Gamma(\mathbf1)
       <\sum_{v\in S}\frac{d_v}{800}
       \le\frac{|M|}{200},
 \tag{9}
\]
since \(|S|=2|M|\) and each original degree is at most two.
Combine (5), (6), and (9). All graph sizes and powers are fixed
before the level tends to infinity. \(\square\)

When a component has a proved nonzero complete-boundary
asymptotic, its whole-boundary bound also implies
\[
 \sup_{\mathbf u}|F_{C,N}(\mathbf u)|
                 \le C_CN^{d_C}|F_{C,N}(\mathbf0)|
 \tag{10}
\]
for all sufficiently large \(N\). This uses the nonzero leading
coefficient as well as the common exponential rate. It is not
asserted at a small level where the complete value might vanish.

## 4. The radical contribution of an internal pair of powers three

Consider the original two-boundary source
\[
 P_N(s,u)=\mathcal D_{3,N}^{(t)}\mathcal D_{3,N}^{(r)}
             [K_N(s,t)K_N(t,r)K_N(r,u)].
 \tag{11}
\]
Only the middle edge has both endpoints traced. Replace that
edge by \(H_N^{\rm rad}\) and call the result \(P_N^{\rm rad}\).
The two pieces in (3) are bare edges. The full real-angle bound
in [the centered kernel estimate](research_path_mixed_trace_currents.md),
equation (21), therefore gives
\[
 |P_N^{\rm rad}(s,u)|\le CN^a
 \exp N\!\left[
 2M_\infty-\frac{(1-\cos s)+(1-\cos u)}{200}\right]
                \qquad(s,u\in[-\pi,\pi]).
 \tag{12}
\]
The losses in the two internal physical angles may be dropped
when summing the bounded Gram weights. The outside losses remain.

Let \(M_{3,3}\) be the complete-boundary geometric rate of
(11). The positive solution exists by the integer corridor theorem
in [the variational path proof](research_negative_corridor_variational_bounds.md),
Theorem 15, after mirroring its negative-power convention.

**Theorem 4.** One has
\[
                       M_{3,3}>2M_\infty+\frac1{100}.
 \tag{13}
\]
Consequently the entire radical term in (11) has a strict
exponential gap below its geometric rate. This also holds for
the mirrored pair \(-3,-3\).

**Proof.** Use the square energy \(E(A,y)\), normalized to
vanish at zero, from the convex filling variation. It is even
in each coordinate and satisfies
\[
 E_A=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),
 \qquad
 E_y=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)).
 \tag{14}
\]
The total energy is four times the sum of the two square
energies on every edge. Its minimum \(F\) satisfies
\[
                 F=\pi(3M_\infty-M_{3,3}).
 \tag{15}
\]
This is the absolute energy identity, with all three original
edges included.

Choose a feasible trial with real angle \(s_v=\pi/2\) at
both selected vertices, imaginary return \(g_{v,e}=-\pi/8\)
at each of their two incidences, and \(s=g=0\) at the two
outside endpoints. Each selected constraint is
\(\sum_e g_{v,e}-3s_v/2=-\pi\). All edge inequalities are
strict. The middle edge has square pairs
\((3\pi/16,\pi/16)\) and \((\pi/16,-3\pi/16)\).
Each attaching edge has two copies of
\((\pi/8,-\pi/16)\), up to the square symmetries.
By symmetry of \(E\),
\[
 F\le8E(3\pi/16,\pi/16)+16E(\pi/8,\pi/16).
 \tag{16}
\]

For \(0\le A,y<\pi/4\), equation (14) implies
\(E(A,y)\le E(A,0)+E(0,y)\). Write \(E_0(A)=E(A,0)\).
Since \(\operatorname{arsinh}(\tan x)'=\sec x\) on this
interval, integration twice gives
\[
 E_0(A)=\frac14\int_0^{2A}(2A-t)\sec t\,dt.
 \tag{17}
\]
The function \(\sec t\) is convex. Bound it above by its
linear interpolants on \([0,A]\) and \([A,2A]\), and
integrate these two affine functions exactly. This yields
\[
 E_0(A)\le\frac{A^2}{24}
                         (5+6\sec A+\sec(2A)).
 \tag{18}
\]
Combining (16)--(18),
\[
                  F\le24E_0(\pi/16)
                     +16E_0(\pi/8)+8E_0(3\pi/16).
 \tag{19}
\]

The following elementary rational upper bounds suffice:
\[
 \sec\frac\pi{16}<\frac{51}{50},\quad
 \sec\frac\pi8<\frac{13}{12},\quad
 \sec\frac\pi4<\frac{10}{7},\quad
 \sec\frac{3\pi}{16}<\frac{121}{100},\quad
 \sec\frac{3\pi}8<\frac{21}{8}.
 \tag{20}
\]
Here is one way to check all five without approximate trigonometry.
For \(0\le x\le33/28\),
\[
 \cos x\ge p_6(x):=1-\frac{x^2}{2}
                  +\frac{x^4}{24}-\frac{x^6}{720}.
\]
The alternating Taylor remainder has the stated sign, and
\(p_6\) is decreasing on this interval. Substitute the respective
upper arguments \(11/56,11/28,11/14,33/56,33/28\), using
\(\pi<22/7\). Direct rational arithmetic gives lower bounds
strictly larger than the reciprocals in (20).
Substituting (20) and \(\pi<22/7\) in (19) gives
\[
                  F<\frac{9283241}{2634240}<\frac{18}{5}.
 \tag{21}
\]
Finally, the alternating series defining Catalan's constant gives
\[
 G>1-\frac19+\frac1{25}-\frac1{49}.
\]
These rational bounds imply
\[
 \frac{4G-18/5}{\pi}
 >\frac{4(1-1/9+1/25-1/49)-18/5}{22/7}
 =\frac{187}{17325}>\frac1{100}.
 \tag{22}
\]
Use \(\pi M_\infty=4G\) in (15) to conclude (13).
Conjugation gives the mirrored statement. \(\square\)

The seven rational inequalities in (20)--(22) are reproduced by
[the exact-fraction checker](../experiments/check_three_pair_radical_energy_gap.py):

```sh
python3 experiments/check_three_pair_radical_energy_gap.py
```

Its [saved result](../repro/results/research-three-pair-radical-energy-gap.json)
records the exact positive margins. The checker verifies these
scalar inequalities; the feasible-angle construction, variational
identity, and quantum radical bound are the written arguments above.

The strict gap persists on a sufficiently small complex neighborhood
of \(s=u=0\). Indeed \(P_N^{\rm rad}\) has degree at most
\(N-1\) in each outside spectral variable; the elementary Laurent
polynomial bound extends (12) with added exponent
\(N(|\Im s|+|\Im u|)\). The positive geometric critical point
and its action continue holomorphically nearby. Shrinking the
neighborhood preserves a fixed portion of the gap in (13).
This observation controls the radical error in a prospective local
two-boundary theorem; it does not prove that theorem's remaining
low-sector asymptotic.

## 5. Why ordinary-color bounds do not settle the remaining pieces

The colors \(c_a\) above are physical values of an auxiliary
pair Casimir. The main strands still carry their original complete
root color. The ordinary-color comparison in
[the representation audit](actual_ordinary_color_comparison_audit.md)
instead specializes the main knot color and uses the one-component
quotient argument to replace all its strands by an ordinary color.
Those hypotheses do not follow from fixing auxiliary Casimir values.

In particular, a general bound (4) cannot be imported from that
ordinary-color theorem. Nor do the existing bounds for the normal
determinant at each color establish it: they permit exponential
cancellation between different physical colors. For arbitrary
short path components, their complete-boundary rate and their
whole-boundary upper bound must still be compared within the
original source. The results above remove this issue for the
explicitly identified components and for the radical sector of
the internal \(3,3\) pair, while leaving its low-sector problem
visible.

## 6. A uniform estimate for every positive pair of powers at least three

The energy comparison for the pair \(3,3\) extends to every pair
of real powers \(n,p\ge3\). The complete outside endpoints are
essential in the following proof of interiority. A pair embedded
in a longer selected path has different boundary conditions, and
this argument does not establish the corresponding comparison there.

**Theorem 5.** Consider two consecutive selected vertices, each
joined at its other end to a complete outside vertex. Give the
selected vertices real powers \(n,p\ge3\) and unit charges.
Their convex filling problem has its unique minimum in the
interior of every edge square. It therefore determines the unique
positive stationary solution with the original logarithmic
normalization. Its complete-boundary rate satisfies
\[
             M_{n,p}>2M_\infty+\frac1{100}.
 \tag{23}
\]
For integer \(n,p\ge3\), let
\[
 P_{n,p,N}(s,u)=
 \mathcal D_{n,N}^{(t)}\mathcal D_{p,N}^{(r)}
       [K_N(s,t)K_N(t,r)K_N(r,u)].
 \tag{24}
\]
Its middle-edge radical term obeys
\[
 |P_{n,p,N}^{\rm rad}(s,u)|
 \le CN^a\exp N\!\left[
 M_{n,p}-\frac1{100}
       -\frac{(1-\cos s)+(1-\cos u)}{200}\right]
 \quad(s,u\in[-\pi,\pi]).
 \tag{25}
\]
The same conclusions hold for the mirrored pair \(-n,-p\).
The real-power statement concerns the geometric variational problem;
the finite quantum statement here uses integer crossing powers.

**Proof of interiority.** Work first with the negative-power
convention of the
[variational corridor proof](research_negative_corridor_variational_bounds.md).
Its strict-feasibility and corner arguments in Propositions 1--3
use real inequalities \(b_v\ge2\), without rounding a power to an
integer. They therefore apply to \(b_v=n,b_w=p\).
Alternatively, strict feasibility follows directly by reversing
the signs of the real angles in the trial constructed below.
These arguments give a unique minimum, exclude open sides, and
show that the two outside edges are interior. Their selected
incidences are strictly negative. Every selected real return and
dual height is also strictly negative.

Suppose the middle edge had a corner. Orient it so that \(v\)
has the negative corner incidence, and write
\(\theta=-s_v\), \(\phi=-s_w\). The corner classification gives
\(\theta>\pi/2\), \(0<\phi<\pi\), and
\[
 g_{v,e}=-\frac{\pi-\phi}{2},\qquad
 g_{w,e}=\frac{\pi-\theta}{2}.
 \tag{26}
\]
Write \(g_v^{\rm out},g_w^{\rm out}<0\) for the incidences
on the outside edges. The two imaginary period equations read
\[
 n\theta=\pi+\phi+2g_v^{\rm out}<\pi+\phi,\qquad
 p\phi=3\pi-\theta+2g_w^{\rm out}<3\pi-\theta.
 \tag{27}
\]
The first equation and \(n\ge3\) imply
\[
       \frac{\pi}{2}<\theta<\frac{2\pi}{n}
                    \le\frac{2\pi}{3},
       \qquad \phi>n\theta-\pi>\frac{\pi}{2}.
 \tag{28}
\]
The second equation then gives \(p<5\).

For completeness, the remaining corner contradiction uses only
real inequalities, not the integrality of either power.
Let \(X>0,H>0\) be the magnitudes of the relevant covectors of
the companion interior square, and \(U,V>0\) those of the corner.
The corner subgradient and companion-square formulas, as in
equations (74)--(77) of the corridor proof, give
\[
 \begin{split}
 \sinh(2X)&=(-\cot\theta)\sin\phi,\\
 u_w&=X-U>0,\qquad -k_{w,e}=V+H,\\
 V&\ge V_0(U):=
       \tfrac12\operatorname{arsinh}(\operatorname{csch}(2U)).
 \end{split}
 \tag{29}
\]
Here \(u_w=-h_w/2\). The real period equation at \(w\),
including its strictly negative outside return, implies
\[
 V+H<p(X-U)<6(X-U).
 \tag{30}
\]
Consequently
\[
 6X>6U+V_0(U)\ge
 C_6:=\frac{6\operatorname{arsinh}(1/6)
                       +\operatorname{arsinh}6}{2}
                  >\frac32\log3.
 \tag{31}
\]
The minimum occurs at \(\sinh(2U)=1/6\), by differentiation.
For the last strict inequality, use
\(\operatorname{arsinh}6>\log12\),
\(6\operatorname{arsinh}(1/6)>6/7>5/6\), and
\(\log(9/4)\le5/6\).
On the other hand, (28)--(29) give
\[
 X\le\tfrac12\operatorname{arsinh}(1/\sqrt3)
                            =\tfrac14\log3,
 \tag{32}
\]
contradicting (31). Thus there is no corner. The variational
reconstruction gives the unique positive primitive solution.
Mirroring returns to the positive-power convention.

**Proof of the energy bound.** Put
\[
 b=\frac{\pi}{16},\qquad
 s_v=\frac{3\pi}{2n},\quad s_w=\frac{3\pi}{2p},
 \qquad a=\frac{s_v}{4},\quad c=\frac{s_w}{4}.
 \tag{33}
\]
Set each of the four selected incidences equal to \(-\pi/8\),
and both outside incidences and angles equal to zero. Then
\(\sum g_{v,e}-ns_v/2=-\pi\), and likewise at \(w\).
Moreover \(0<a,c\le2b\), so every edge inequality is strict.
The total energy of this trial is
\[
 F_{\rm trial}(a,c)=
 8E(a,b)+8E(c,b)
 +4\{E(a+b,c-b)+E(a-b,c+b)\}.
 \tag{34}
\]
The first two terms are at most \(16E(2b,b)\), since
\(E_A\ge0\) for nonnegative coordinates. The expression in
braces is convex jointly in \(a,c\) on \([0,2b]^2\).
Every point of this rectangle is a convex combination of its
four corners, so its value is at most the largest corner value.
Evenness and coordinate symmetry of \(E\) give those values as
\[
 \begin{array}{c|c}
 (a,c)&E(a+b,c-b)+E(a-b,c+b)\\ \hline
 (0,0)&2E(b,b)\\
 (2b,0),(0,2b)&E(3b,b)+E(b,b)\\
 (2b,2b)&2E(3b,b).
 \end{array}
 \tag{35}
\]
Because \(E(b,b)\le E(3b,b)\), the last entry is the largest.
Thus the actual minimum satisfies
\[
 F_{n,p}\le F_{\rm trial}(a,c)
 \le16E(\pi/8,\pi/16)+8E(3\pi/16,\pi/16)
 <\frac{18}{5}.
 \tag{36}
\]
The last inequality is exactly the rational estimate (16)--(21);
no further numerical estimate is needed. The interiority just
proved permits the absolute energy identity
\(F_{n,p}=\pi(3M_\infty-M_{n,p})\).
Equation (22) now proves (23).

**Proof of the quantum consequence.** The exact radical
contraction evaluates both crossing factors at physical colors.
Their moduli are one for every integer \(n,p\). Thus the same
bare-edge estimate used in (12) gives that inequality with
\(P_N^{\rm rad}\) replaced by \(P_{n,p,N}^{\rm rad}\).
Combining it with (23) proves (25). Conjugation gives the
same-sign negative pair. \(\square\)

This theorem removes the radical sector for every internal
two-vertex source (24) with same-sign magnitudes at least three.
It does not establish its low-sector asymptotic, a nonzero
coefficient for its geometric contribution, or a bound for an
arbitrary longer cluster of short powers. Those are separate
questions about the original finite trace.

## 7. The middle Newton polynomials on the whole real period

The cutoff in the low kernel also has a simple exact Fourier
description. Set
\[
 m=\lfloor N/2\rfloor,\qquad L=N-1-m,\qquad
 \theta=\pi/N,\qquad s_1=2\sin\theta.
 \tag{37}
\]
The original polynomial \(e_L\) is the last one retained in
\(K_N^{\rm low}\). It is not a radical element at either parity.

**Lemma 6.** For every \(N\ge2\) and every complex \(t\),
\[
 e_L(-2\cos t)=
 \begin{cases}
 \displaystyle\frac1N\sum_{k=-L}^L e^{ikt},
                                      &N\text{ odd},\\[2mm]
 \displaystyle\frac4{Ns_1}\sum_{k=-L}^L
                   \cos(k\theta)e^{ikt},&N\text{ even}.
 \end{cases}
 \tag{38}
\]
Consequently
\[
 \sup_{t\in\mathbb R}|e_L(-2\cos t)|
 \le
 \begin{cases}
 1,&N\text{ odd},\\
 N,&N\text{ even}.
 \end{cases}
 \tag{39}
\]
All angular derivatives of fixed order cost at most the additional
factor \(L^r\). All ordinary derivatives in the spectral variable
\(z\in[-2,2]\) also have polynomial bounds, including at \(z=-2\).

*Proof.* Use the full physical angular grid
\[
 t_j=\frac{\pi(N-1-2j)}N,\qquad 0\le j<N.
 \tag{40}
\]
At odd \(N=2m+1\), the Newton product vanishes at every distinct
physical node except \(z=-2\). At that node \(e_m(-2)=1\).
Indeed \(S_m^2=N\), and the numerator
\(\prod_{a=0}^{m-1}(c_a+2)\) is \(N\). The latter equality also
follows by differentiating
\[
 2T_N(z/2)+2=(z+2)\prod_{a=0}^{m-1}(z-c_a)^2
\]
at \(-2\): its derivative there is \(N^2\), and all factors
\(c_a+2\) are positive. Thus the values on (40) are one at
\(t=0\) and zero at the other \(N-1\) points. The polynomial in
\(-2\cos t\) has frequencies \(-m,\ldots,m\). The unique Fourier
interpolant on these \(N\) points is the first line of (38).

At even \(N=2m\), the only nonzero physical value is at
\(c_{m-1}=-2\cos\theta\), represented twice in (40), at
\(t=\pm\theta\). The exact value is
\[
 e_{m-1}(c_{m-1})
   =\frac{S_{N-2}}{S_{m-1}^2}
   =\frac{N/s_1}{N/2}=\frac2{s_1}.
 \tag{41}
\]
The product evaluation is the one used in the
[middle-normal calculation](research_bare_kernel_power_three_obstruction.md#6-the-midpoint-forcing-after-the-original-internal-pair-trace),
equations (38)--(41). Discrete Fourier inversion on (40) therefore
gives coefficient \(4\cos(k\theta)/(Ns_1)\). The possible Nyquist
coefficient vanishes because \(\cos(m\theta)=0\). The remaining
frequencies are exactly \(-L,\ldots,L\), proving the second line.
Since both sides are trigonometric polynomials, the equalities
hold for complex \(t\) as well.

Every coefficient displayed in (38) is nonnegative. At even
levels their sum is
\[
 \frac4{Ns_1}\sum_{k=-m+1}^{m-1}\cos(k\theta)
       =\frac1{N\sin^2(\theta/2)}\le N,
 \tag{42}
\]
using \(\sin(\pi/(2N))\ge1/N\). The odd sum is one.
This proves (39) and the angular derivative bound.
For ordinary spectral derivatives, apply Markov's inequality
directly to \(e_L(z)\) on \([-2,2]\), whose degree is \(L\).
There is no division by \(\sin t\), so the bound includes the
parabolic endpoints. \(\square\)

The next polynomial \(e_{L+1}\) belongs to the radical sector.
The [radical Fourier estimate](research_high_newton_radical_contraction.md)
gives
\[
 \sup_{t\in\mathbb R}|e_{L+1}(-2\cos t)|
                         \le\sqrt{N-1}.
 \tag{43}
\]
The two bounds concern the actual finite polynomials with their
normals. They do not give geometric-rate estimates on a fixed
complex internal contour. Such an estimate for the low kernel
is explicitly false at some actual all-three path configurations.

The [finite identity checker](../experiments/check_middle_newton_fourier_formula.py)
compares (38) with the defining Newton product at levels \(2\)
through \(18\), including every physical value and first ordinary
normal and several complex angles. Its
[saved record](../repro/results/research-middle-newton-fourier-formula.json)
contains 493 comparisons at 100 decimal digits. These verify the
finite normalizations; the proof for all levels is the Fourier
inversion above.

## 8. Contracting several cutoff forcings before estimating them

Orient any nonempty set \(F\) of selected edges of the original
path. On each \(e=(v,w)\in F\), replace its kernel by the literal
right side of the low-kernel difference equation:
\[
 J_{e,N}(z_v,z_w)
      =-s_{L+1}^2 e_L(z_v)e_{L+1}(z_w).
 \tag{44}
\]
Leave every other edge equal to its full original kernel, and take
all the original crossing traces. Denote this finite source by
\(\mathscr J_{F,N}\). The edges of \(F\) need not form a matching.
This definition specifies a product of actual cutoff forcings;
it does not assert that applying arbitrary difference operators
to a network produces only these terms.

Delete the edges of \(F\), replace their endpoints \(S=V(F)\) by
free physical boundary variables, and let \(C\) denote the remaining
components. An uncut edge between two vertices of \(S\) stays
present. Let \(F_{C,N}\) be the original source of each such
component, excluding the crossings at the evaluated vertices.

**Proposition 7.** For fixed powers and a fixed path,
\[
 |\mathscr J_{F,N}|
   \le C_{\Gamma,\mathbf n,F}N^{a_{\Gamma,F}}
       \prod_C
       \sup_{\mathbf u\in[-\pi,\pi]^{\partial C}}
                    |F_{C,N}(\mathbf u)|.
 \tag{45}
\]
This estimate is uniform in every real original outside angle.
Every fixed collection of ordinary outside derivatives satisfies
the same estimate with a possibly larger polynomial factor.
Each component on the right has at most \(|I|-2\) traced vertices.

*Proof.* At a vertex \(v\in S\), collect its incident factors from
(44) into \(Q_v(z)\). Its degree is at most \(2(N-1)\), since the
original degree of \(v\) is at most two. Equations (39) and (43)
give \(\|Q_v\|_{[-2,2]}\le N^2\); Markov's inequality gives
\(\|Q_v'\|_{[-2,2]}\le2N^4\). The factors \(s_{L+1}^2\) have
absolute value at most four.

Apply the full physical residue formula to
\(\phi_N(R^{n_v}Q_v f)\). At a double physical root \(c\), its
contribution is exactly
\[
 \eta\bigl[
 (4-c^2)(R^{n_v}Q_v)'(c)-cR^{n_v}(c)Q_v(c)
 \bigr]f(c)
 +\eta(4-c^2)R^{n_v}(c)Q_v(c)f'(c).
 \tag{46}
\]
At the odd simple root \(-2\), the contribution is
\(R^{n_v}(-2)Q_v(-2)f(-2)\), with no derivative.
The original crossing has unit modulus at physical roots and
\[
 |(R^{n_v})'(c)|\le C_{n_v}N^2
 \tag{47}
\]
at the double roots. This follows from the exact crossing-normal
formula and the sine chord bound; it is valid for each fixed
signed integer power. Thus all coefficients in (46), and their
total absolute sum over the at most \(N\) roots, are bounded by
powers of \(N\). No normal has been removed.

After performing these functionals at every \(v\in S\), the
remaining traces factor into the original components \(C\).
Each removed vertex has at most one uncut incidence. Accordingly
each differentiation in (46) is a first ordinary derivative in
one component's boundary variable. Several such derivatives can
act on the same component, but they are in its distinct boundary
variables. Its original boundary polynomial has degree at most
\(N-1\) in each one. Applying Markov's inequality successively
bounds all these mixed derivatives by its whole-real-boundary
supremum at polynomial cost. This proves (45).

There are at least two removed traced vertices, since \(F\ne
\varnothing\). Every component therefore has at most \(|I|-2\)
traced vertices. For ordinary derivatives at the original outside
boundary, use the same polynomial estimate after obtaining (45).
\(\square\)

If these smaller sources have their whole-boundary upper bounds
\(\|F_{C,N}\|\le A_CN^{b_C}e^{N\mu_C}\), then (45) gives rate
\(\sum_C\mu_C\). For positive paths, the
[all-edge-subset comparison](research_positive_path_pair_activation_gap.md#5-removing-any-set-of-selected-edges)
identifies this rate as
\[
 \sum_C\mu_C
    =M_\Gamma(\lambda^S)-|F|M_\infty
    <M_\Gamma(\mathbf1)-\frac{|F|}{1000}.
 \tag{48}
\]
The last strict bound remains conditional on the two support
certificates specified in that note. Once those inequalities are
established, it applies to every fixed literal forcing (44), not
only to the two-vertex calculation in the earlier midpoint note.

## 9. What this does and does not supply in an induction

Suppose whole-real-boundary upper bounds at the complete geometric
rate are known for every original path source with fewer than
\(m\) traced vertices. Under the geometric comparison just
specified, all nonempty radical matching terms of an \(m\)-vertex
path, and all terms (44), have a strict gap below its geometric
rate. Their bounds consume only sources with at most \(m-2\)
traced vertices. They require no nonzero leading coefficient in
those shorter sources.

Let \(Z_{\Gamma,N}^{\rm low}\) replace precisely the edges joining
selected vertices by \(K_N^{\rm low}\); edges to the original
outside boundary remain full. The exact radical expansion and
the induction hypothesis give
\[
 \sup_{\mathbf u\in[-\pi,\pi]^{\partial\Gamma}}
 |Z_{\Gamma,N}(\mathbf u)-Z_{\Gamma,N}^{\rm low}(\mathbf u)|
       \le C N^a e^{N(M_\Gamma(\mathbf1)-1/1000)}.
 \tag{49}
\]
Hence an upper bound at rate \(M_\Gamma(\mathbf1)\) for the
original \(m\)-vertex source is equivalent to the same upper
bound for its joint low-sector source, up to polynomial factors.
At complete boundary values a nonzero leading geometric
asymptotic for either source transfers to the other unchanged.

The remainder in (49) is an ordinary polynomial of degree at
most \(N-1\) in each original boundary variable. Chebyshev
expansion therefore extends (49) to complex outside angles at
the additional rate
\[
                         \sum_j|\Im u_j|.
 \tag{50}
\]
Fixed ordinary derivatives cost further powers of \(N\).
This is sufficient to preserve a strict gap on a sufficiently
small fixed boundary neighborhood; it is not a free
geometric-rate bound on a large complex internal domain.

The remaining induction step is the joint low-sector contour.
The [unsummed phase theorem](research_unsummed_network_phase_coercivity.md)
supplies a nondegenerate local geometric contour. It does not
identify every complementary current with (44) or with a radical
matching. The [exact facet rule](research_factorial_core_contour_compiler.md)
lists where general factorial currents are supported, but gives
no reduction of all of them to shorter physical-boundary sources.
Moreover, a geometric upper bound for the individual low kernels
is false on some actual positive all-three paths, by
[the low-kernel obstruction](research_bare_kernel_power_three_obstruction.md#5-removing-the-radical-still-leaves-a-larger-cutoff-current).
Summing each vertex first does not solve that issue either:
[the traced three-crossing vertex](research_traced_three_vertex_endpoint.md)
has a larger endpoint term near such configurations.

Thus the missing assertion is specific: a contour identity for
the joint low source whose main geometric term has its original
nonzero coefficient, and whose entire complementary part either
has a proved direct gap or reduces to the shorter sources bounded
above. None of the preceding upper bounds alone provides that
identity or its coefficient.
