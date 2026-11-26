# A scaled height bound and its edge-deletion consequences

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The simultaneous activation of two adjacent power-three vertices has
a uniform height bound, independent of the surrounding positive path.
The complete sector-domain certificate and its separate replay have
both finished. Combined with the existing small-height proof, they give
\(H<59\chi/50\) throughout the activation.

This bound alone does not prove the desired energy comparison for an
arbitrary adjacent pair of powers three. It does prove that comparison
when both new powers are at least four, or when either is at least ten.
It also controls every connected run of at least two deleted edges,
without those additional restrictions on powers. These are geometric
comparisons. Applying them to quantum remainders still requires the
specified bounds for the remaining source components.

## 1. The scaled height theorem

Let \(\Gamma\) be a finite positive path with original selected
integer powers at least three and at least one complete outside
endpoint. Keep all original edges. Choose an edge joining two
selected vertices \(v,w\), give those vertices power three and the
same charge \(\chi\in[0,1]\), and allow the other charges to be any
fixed numbers in \([0,1]\).

The [fractional-charge theorem](research_positive_path_fractional_charge_cube.md)
supplies the positive stationary solution and its continuous
complete limits. At an active vertex write its angle as
\(t_j=a_j-iH_j\), where \(0<a_j<\pi\) and \(H_j>0\).
The already proved uniform bounds are
\[
 H_j<B:=\frac{23}{20},\qquad
             \sinh H_j<\sqrt3\sin a_j.
 \tag{1}
\]

**Theorem 1.** With \(H=\max(H_v,H_w)\),
\[
             H<\min\left\{\frac{59}{50}\chi,\frac{23}{20}\right\}
                  \quad(0<\chi\le1),\qquad H=0\quad(\chi=0).
 \tag{2}
\]

*Proof.* The [small-height theorem](research_pair_activation_small_height.md#4-extending-the-height-interval-by-the-exact-period-equation)
proves the scaled inequality whenever \(0<H\le3/100\).
It remains to exclude its failure for \(3/100\le H\le23/20\).
Choose the vertex of greater height and write its angle as \(a-iH\).
By (1),
\[
 \ell(H)\le a\le\pi-\ell(H),\qquad
 \ell(H)=\arcsin(\sinh H/\sqrt3).
 \tag{3}
\]
Thus its angle is represented by
\[
 a=\ell(H)+(\pi-2\ell(H))\xi,\qquad 0\le\xi\le1.
 \tag{4}
\]

Put \(A=\tan((a-iH)/2)\). Its two original returns are
\[
 r_1=\operatorname{asinh}(Ac_1),\qquad
 r_2=\operatorname{asinh}(Ac_2),\qquad
 r_1+r_2=\frac32H+i\left(\frac32a-\pi\chi\right).
 \tag{5}
\]
The other endpoint of the pair has height at most \(H\); the
remaining neighbor has height at most \(B\). Consequently
\[
 \begin{split}
 c_1&\in D_B,\qquad c_2\in D_H,\\
 D_C&=\left\{x+iy:x,y\ge0,\
       \frac{x^2}{\cosh^2(C/2)}
       +\frac{y^2}{\sinh^2(C/2)}\le1\right\}.
 \end{split}
 \tag{6}
\]
A complete neighbor has \(c=1\). An absent incidence is padded
by \(c=0\). Both belong to the indicated domains.

For each point of the closed parameter rectangle
\([0,1]\times[3/100,23/20]\), the completed certificate supplies
a rational slope \(s\le0\) and two rational budgets \(b_1,b_2\)
such that
\[
 \begin{split}
 \max_{c\in D_B}\{\Re\operatorname{asinh}(Ac)
                  -s\Im\operatorname{asinh}(Ac)\}&<b_1,\\
 \max_{c\in D_H}\{\Re\operatorname{asinh}(Ac)
                  -s\Im\operatorname{asinh}(Ac)\}&<b_2,\\
 b_1+b_2&<
       \frac32H-s\left(\frac32a-\pi\frac{50H}{59}\right).
 \end{split}
 \tag{7}
\]
The finite verification of these strict inequalities is described
in Section 2.

Suppose the scaled inequality in (2) fails. Then
\(\chi\le50H/59\). Applying the real linear functional
\(L_s(r)=\Re r-s\Im r\) to (5), its actual right side is at least
the right side of the last inequality in (7), because
\(\pi s(\chi-50H/59)\ge0\). Its left side is strictly smaller.
This is a contradiction. Combining the certified range with the
small-height theorem proves (2). At charge zero both selected
angles are complete by the charge-cube theorem. \(\square\)

## 2. What the certificate verifies

The [boundary reduction](research_pair_support_boundary_reduction.md)
proves that the support maximum on \(D_C\), for any \(s\le0\), occurs
on its ellipse arc
\[
 c_C(u)=\cosh(C/2)\cos(\pi u/2)
          +i\sinh(C/2)\sin(\pi u/2),\qquad 0\le u\le1.
 \tag{8}
\]
This includes the maxima on both straight sides and the value zero
at the origin. The original inverse hyperbolic sine is the continuous
right-half-plane branch. On these sector-restricted arcs its argument
has strictly positive real part.

The [author program](../experiments/certify_pair_height_sector.py)
subdivides (4) into rational rectangles. The angular range on each
rectangle is enclosed from all four parameter corners. For a proposed
rational slope, outward ball arithmetic verifies each budget over
complete rational partitions of both arcs. It also verifies the
last inequality in (7) throughout the parameter rectangle.
Numerical optimization chooses possible slopes and budgets only.

The [complete artifact](../repro/results/research-pair-height-sector-scaled.json)
has 77,088 accepted rectangles and no pending rectangles.
The [separate replayer](../experiments/replay_pair_height_sector.py)
imports no author or optimizer. It reconstructs the angle and
inverse-hyperbolic-sine enclosures, checks every rational arc
partition, and proves that the parameter rectangles cover the full
domain with multiplicity one. Its
[completed report](../repro/results/research-pair-height-sector-scaled-replay.json)
records:

| Quantity | Verified value |
|---|---:|
| Arithmetic precision | 160 bits |
| Parameter rectangles | 77,088 |
| Exact covered area | \(28/25\) |
| Height slabs in the coverage check | 1,989 |
| Sector-coordinate intervals | 3,907 |
| Verified arc intervals | 26,182,200 |
| Additional arc subdivisions during replay | 0 |
| Smallest strict replay margin | \(>1.7266950\cdot10^{-5}\) |

The report binds the complete artifact and the replay script by
SHA-256 hashes. The author artifact also binds its source and
geometric reduction inputs. This is a complete verification of (7)
on the sector domain (3), not on all angles in \([0,\pi]\).
No unfinished affine computation is used in Theorem 1.

## 3. An unconditional bound on the activation cost

Fix all other charges at zero or one. Write
\(\mathcal C(n,p)\) for the increase of the minimum square energy
when an adjacent pair with powers \(n,p\) is activated from charges
zero to charges one. All other powers and all original edge
constants remain fixed.
The [energy comparison](research_edge_cut_energy_comparison.md),
Corollary 7, proves
\(\mathcal C(n,p)\le\mathcal C(3,3)\) for \(n,p\ge3\).
The charge derivative gives
\[
 \frac{\mathcal C(3,3)}{\pi}
       =\int_0^1(H_v(\chi)+H_w(\chi))\,d\chi.
 \tag{9}
\]

**Corollary 2.** Uniformly in the finite path and the old powers,
\[
               0<\frac{\mathcal C(n,p)}{\pi}
                      <B_2:=\frac{2783}{2360}
                          \qquad(n,p\ge3).
 \tag{10}
\]

Indeed the two bounds in (2) meet at \(\chi=115/118\). Thus
\[
 \begin{split}
 \frac{\mathcal C(3,3)}{\pi}
 &<2\int_0^{115/118}\frac{59}{50}\chi\,d\chi
            +2\int_{115/118}^1\frac{23}{20}\,d\chi\\
 &=2\frac{23}{20}
       -\frac{(23/20)^2}{59/50}
 =\frac{2783}{2360}.
 \end{split}
 \tag{11}
\]
Strict positivity follows from the positive heights on the
activation interval. The same derivative statement holds for
the target integer powers.

The required complete-edge rate is
\[
                            M_\infty=\frac{4G}{\pi}.
 \tag{12}
\]
The bound \(B_2\) is larger than \(M_\infty\), so (10) alone
does not settle the power-three pair comparison. For example,
\(G<11/12\) and \(\pi>157/50\) give
\(M_\infty<550/471<2783/2360\).
The first bound follows from the alternating Catalan sum through
index 14, and the second from the two-term Machin estimate.

## 4. Increasing either or both powers

The same bound is sufficient away from a short list of adjacent
power types. The quantitative trials in Corollaries 8--9 of the
energy comparison retain the original constraints and let the old
coordinates relax. We use those trials without changing the
original path.

At a unit-charge vertex of reference power three, its real angle
is greater than \(\pi/4\), by Lemma 11 of that note. A single
activation has energy cost less than \(\pi B_1\), with
\(B_1=23/20\), by its Lemma 10.

**Corollary 3.** If \(n,p\ge3\), and either \(n,p\ge4\) or
\(\max(n,p)\ge10\), then
\[
          \frac{\mathcal C(n,p)}{\pi}
                   <M_\infty-\frac1{10000}.
 \tag{13}
\]

*Proof.* If both powers are at least four, Corollary 8 and the
reference angle bound give
\[
 \frac{\mathcal C(n,p)}{\pi}
       <\frac89 B_2=\frac{2783}{2655}.
 \tag{14}
\]
If \(n\ge10\), decrease the other new power to three in the
variational upper bound. The Bernoulli trial of Corollary 9 gives
\[
 \begin{split}
 \frac{\mathcal C(n,p)}{\pi}
 &\le\frac{\mathcal C(n,3)}{\pi}\\
 &<B_1+(B_2-B_1)\frac8{n+5}
 \le B_1+(B_2-B_1)\frac8{15}
 =\frac{6877}{5900}.
 \end{split}
 \tag{15}
\]
Here \(B_2>B_1\), so replacing the trial's actual parameter by
its upper bound \(8/(n+5)\) preserves the inequality. Interchange
the endpoints for \(p\ge10\).

The alternating sum through index 63 is a lower bound for \(G\).
Together with \(\pi<22/7\), exact rational arithmetic gives
\[
 M_\infty>
 \frac4{22/7}\sum_{j=0}^{63}\frac{(-1)^j}{(2j+1)^2}
       >\frac{11657}{10000}
       >\frac{6877}{5900}+\frac1{10000}.
 \tag{16}
\]
Also \(2783/2655<6877/5900\). This proves (13).
\(\square\)

This argument leaves the isolated adjacent types
\((3,j)\) and \((j,3)\), \(3\le j\le9\), unresolved.
It does not assert that their energy comparison fails.
The surrounding path and its old powers remain arbitrary, so this
list is not a finite-exception statement about knots or original
twist assignments.

## 5. A run of deleted edges has a gap even at power three

Let \(F\) be a set of edges joining selected vertices, and put
\(S=V(F)\). Let \(\lambda^S\) make exactly those vertices complete,
leaving the other selected charges one.
A connected component of \(F\) is a run of \(k\) consecutive
edges and \(k+1\) vertices.

**Corollary 4.** Every run with \(k\ge2\) has activation cost
less than
\[
                     \pi k\left(M_\infty-\frac1{1000}\right),
 \tag{17}
\]
with no power restriction beyond \(n_v\ge3\).
If every isolated edge of \(F\) satisfies Corollary 3, and \(a\)
is the number of isolated edges while \(b\) is the number of edges
in longer runs, then
\[
 \frac{F_\Gamma(\mathbf1)-F_\Gamma(\lambda^S)}{\pi}
     <(a+b)M_\infty-\frac{a}{10000}-\frac{b}{1000}.
 \tag{18}
\]

*Proof.* Partition the vertices of a run into adjacent pairs and,
if needed, one singleton. Starting from their zero charges,
activate these blocks successively. A pair costs less than
\(\pi B_2\) by (10), and a singleton less than \(\pi B_1\).
The remaining zero vertices separate complete-ended components,
so the same bounds apply at every step.

If \(k=2r\), the total normalized cost is less than
\(rB_2+B_1\), whose value per edge is at most
\((B_2+B_1)/2\). If \(k=2r-1\ge3\), it is less than \(rB_2\);
the same per-edge bound follows from \(B_2<3B_1\).
Finally,
\[
 \frac{B_2+B_1}{2}=\frac{5497}{4720}
       <\frac{11647}{10000}
       <M_\infty-\frac1{1000}.
 \tag{19}
\]
This proves (17). Use (13) for isolated edges and sum the block
bounds over the components of \(F\) to obtain (18).
\(\square\)

In the absolute phase normalization, deleting the edges of \(F\)
and making their endpoints complete leaves components \(C\) with
complete-boundary rates \(\mu_C\). Keep every uncut edge,
including an edge whose two endpoints have both been made complete.
The energy identity then reads
\[
 \sum_C\mu_C
   =M_\Gamma(\lambda^S)-|F|M_\infty
   <M_\Gamma(\mathbf1)-\frac{a}{10000}-\frac{b}{1000}.
 \tag{20}
\]
Each removed edge restores exactly one \(M_\infty\) when it is
reinserted between complete endpoints.

The [midpoint forcing reduction](research_radical_path_sector_gap.md#7-the-middle-newton-polynomials-on-the-whole-real-period)
therefore has a strict geometric gap for these edge sets.
For radical matchings every component of \(F\) is an isolated
edge, so their endpoints must satisfy Corollary 3.
In either application, a quantum upper bound still requires
whole-real-boundary estimates at the rates \(\mu_C\) for all
remaining source components, with their prescribed normal
derivatives. Neither those estimates nor a nonzero coefficient
of the main geometric cycle follows from (20).

## 6. Reproduction

The [scalar and provenance checker](../experiments/check_scaled_pair_activation_consequences.py)
checks the completed replay and its artifact hashes, the small-height
checker's saved result, and every rational cost comparison above.
It does not repeat the large interval computation.
Its [record](../repro/results/research-scaled-pair-activation-consequences.json)
retains the proof and input hashes.

~~~sh
python3 experiments/check_scaled_pair_activation_consequences.py
~~~

The affine height comparison remains unfinished. Theorem 1 and
Corollaries 2--4 do not depend on it.
