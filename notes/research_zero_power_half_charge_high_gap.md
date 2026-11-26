# A full-source lattice initializer on the lower half-charge cube

Private written proof, 16 November 2026.

The original zero-power source has a nonzero geometric asymptotic on
every compact subset of the lattice charge cube \((0,1/2]^S\). The
high Newton sectors have a uniform strict gap, including high boundary
edges and both level parities. The proof contracts their actual
radical normals first, and then bounds the remaining charged low
source with its shared indices intact. It does not use positivity of
the charged closing functional.

The archived radical contraction and path comparison already identify
physical cut sources. The additional estimate here uses the convex
zero-power height minimum to bound their charge cost. The all-low
Fourier proof is extended below only at actual lattice charges; no
off-lattice complex-charge initializer is asserted.

## 1. Original source and the charge-dependent pressure

Let \(T\) be a fixed finite tree, let \(S\) be a nonempty connected
proper selected set, and suppose every selected original degree
\(d_v\) is at least three. Let \(E_S\) contain every edge incident
to \(S\), once. Write \(k=|S|\), \(e=|E_S|\), and
\(b=|\partial S|\), so \(e=k-1+b\). All selected powers are zero.
Outside variables remain ordinary polynomials; complete outside
values are used to define the pressure.

Put \(N\ge2\), \(D=N-1\), \(\eta=(-1)^D\), \(m=\lfloor N/2\rfloor\), and
\[
 s_j=2\sin(\pi j/N),\quad S_j=\prod_{h=1}^j s_h,\quad
 c_a=2\cos((2a+1)\pi/N),\quad
 e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z).
 \tag{1}
\]
The original algebra and closing are
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,
 \qquad K_N(z,w)=\sum_{j=0}^D e_j(z)e_j(w).
 \tag{2}
\]
For integer \(1\le J_v\le N\), set \(\chi_v=J_v/N\) and retain the
actual coupon \(\mathcal C_{N,\chi_v}=T_{N-J_v}(-z_v/2)\), with
reduction only inside a traced variable. The source is
\[
 Z_N(\boldsymbol\chi;\mathbf u)=
 \left(\prod_{v\in S}\phi_N^{(v)}\right)
 \left[\prod_{v\in S}\mathcal C_{N,\chi_v}(z_v)
                 \prod_{vw\in E_S}K_N(z_v,z_w)\right],
 \qquad z_w=-2\cos u_w\quad(w\notin S).
 \tag{3}
\]
Each original boundary incidence is kept separately before any
ordinary identification of boundary variables. Let \(Z_N^{\rm low}\)
replace every kernel by its sum over \(2j<N\).

Use the original real edge potential
\[
 \begin{split}
 J(x)&=\int_0^x\log(2\sin\pi t)\,dt,\\
 B(x,h)&=\int_0^x\log(2\cos2\pi t+2\cosh h)\,dt-2J(x),\\
 V(h,g)&=\max_{0\le x\le1/2}\{B(x,h)+B(x,g)\},\\
 M(\boldsymbol\chi)&=\min_{\mathbf H\ge0}
       \left\{\sum_{vw\in E_S}V(H_v,H_w)
                         -\sum_{v\in S}\chi_vH_v\right\},
                  \qquad H_w=0\quad(w\notin S).
 \end{split}
 \tag{4}
\]
In particular \(V(0,0)=M_\infty=4G/\pi\), with \(G\) Catalan's
constant. The cube theorem supplies a unique regular positive minimum
\(\mathbf H(\boldsymbol\chi)\) throughout \((0,1)^S\), and
\[
 0<H_v(\boldsymbol\chi)
 \le2\operatorname{arsinh}\tan(\pi\chi_v/d_v).
 \tag{5}
\]
Its canonical critical action is \(M(\boldsymbol\chi)\), with phase
\(\sum_e\psi(t_v,t_w)-i\sum_v\chi_vt_v\) and
\(t_v=-iH_v\). All edge constants are included in (4).

For an internal edge define
\(\gamma_{vw}=M_\infty-\chi_vH_v-\chi_wH_w\); for a boundary
edge at \(v\) define \(\gamma_{vw}=M_\infty-\chi_vH_v\).

**Theorem 1.** Let \(\mathcal K\subset(0,1]^S\) be compact and
avoid the exceptional trivalent-pair corner of the cube theorem.
Suppose \(\gamma_{vw}\ge\gamma>0\) on \(\mathcal K\) for every
included edge. Then constants \(C,p\), uniform at both level parities,
satisfy
\[
 \sup_{\mathbf u\in\mathbb R^{\partial S}}
 |Z_N(\boldsymbol\chi;\mathbf u)-Z_N^{\rm low}
                  (\boldsymbol\chi;\mathbf u)|
 \le CN^p e^{N(M(\boldsymbol\chi)-\gamma)}
 \quad(\boldsymbol\chi\in\mathcal K\cap N^{-1}\mathbb Z^S).
 \tag{6}
\]
The hypotheses hold for every compact
\(\mathcal K\subset(0,1/2]^S\), with
\[
                    \gamma=M_\infty-\log3>31/990.
 \tag{7}
\]

## 2. The exact charged low trace and its uniform majorant

If \(f(t)=\sum_r a_re^{irt}\) is an even Laurent polynomial, extend
\(a_r\) by zero off its support. The original derivative-sampling
formula, applied to \(f(t)\cos((N-J)t)\), gives exactly
\[
 \begin{split}
 \phi_N(f\mathcal C_{N,J/N})
  =\frac{N^2}{2}\sum_{\ell\ge1}\ell\eta^{\ell+1}
  \big[&a_{(\ell-1)N+J-1}-a_{(\ell-1)N+J+1}\\
       &+a_{(\ell+1)N-J-1}-a_{(\ell+1)N-J+1}\big].
 \end{split}
 \tag{8}
\]
The multiplier is \(\ell N\), not \(J\); hence every original
repeated-root normal is retained. The identity tensorizes in the
selected variables. If the Laurent coefficients are nonnegative,
the same coefficient estimate as in the archived Fourier theorem yields
\[
 |\phi_N(f\mathcal C_{N,J/N})|
 \le N^2 f(-ih)
 \frac{2\cosh h\,e^{-Nh}\cosh((N-J)h)}{(1-e^{-Nh})^2},
                        \qquad h>0.
 \tag{9}
\]
More generally (9) applies to a coefficientwise absolute majorant.
In several variables its factors multiply, while \(f(-i\mathbf h)\)
retains all shared edge indices. For heights in a fixed positive
compact interval and charges in a compact subset of \((0,1)\),
the exponential penalty in (9) is \(e^{-N\chi h}\), up to a fixed
factor. No assignmentwise positivity of the charged trace is used.

The actual low Newton factors have nonnegative Laurent coefficients.
Their uniform product estimate is
\[
 \log\{e_j(-2\cosh h)e_j(-2\cosh g)\}
 =N\{B(j/N,h)+B(j/N,g)\}+O(\log N),\qquad 2j<N.
 \tag{10}
\]
It holds uniformly for bounded nonnegative heights, including zero
endpoints. One may check the uniformity directly: the numerator
logarithm is monotone on \([0,1/2]\), and the last midpoint of any
low product stays a distance at least \(1/(2N)\) from \(1/2\).
Its argument is bounded below by a constant times \(N^{-2}\), uniformly
for bounded \(h\ge0\). The midpoint sum/integral error is therefore
\(O(\log N)\); the usual endpoint-aware sine-factorial estimate
has the same uniform error. Thus (9), (10), and the polynomial number of assignments
bound a charged low network at any chosen surviving heights by the
exponential of its full expression in (4). This statement needs no
regularity of its wire maxima.

## 3. Contracting every high pattern before taking absolute values

The high polynomials are exactly \(e_{D-r}\), \(0\le r<m\).
They form the square-zero radical in the full physical algebra. Hence
a nonzero high-edge pattern \(A\subset E_S\) has at most one high
edge at each selected vertex. Outside vertices are not reduced and
impose no such restriction. Let \(T_A\subset S\) be the selected
endpoints of \(A\).

The original surviving normal is the exact divided difference
\[
 \phi_N(e_{D-r}f)=\sum_{a=0}^r b_{ra}f(c_a),\qquad
 b_{ra}=(-1)^{r+a}
     \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}},\qquad |b_{ra}|\le2.
 \tag{11}
\]
Indeed the perfect pairing identifies the left side with the Newton
coefficient \([e_r]\operatorname{rem}f\). The first \(r+1\) nodes
are distinct, so ordinary divided differences give its coefficient
as \((-1)^rS_r^2\sum_{a\le r}f(c_a)/\prod_{h\ne a}(c_a-c_h)\).
The denominator has sign \((-1)^a\) and magnitude
\(S_{r+a+1}S_{r-a}/s_{2a+1}\), proving (11). The bound follows
by writing the factorial ratio as
\[
 \frac{S_r^2}{S_{r-a}S_{r+a+1}}
 =\frac1{s_{r+a+1}}
       \prod_{j=1}^a\frac{s_{r-j+1}}{s_{r+j}}
 \le\frac1{s_{r+a+1}},
 \qquad \frac{s_{2a+1}}{s_{r+a+1}}\le2.
 \tag{12}
\]
The two sine inequalities use \(a\le r<m\). In (11) the high
factor vanishes at every physical value. Thus the derivative of
the spectator, including the derivative of its charge coupon,
vanishes from the product rule. The high factor's own derivative
is exactly (11). The odd simple-node contribution is zero.
At a lattice charge the remaining coupon value has modulus at most
one. No normal was discarded in obtaining this estimate.

At a physical node,
\[
 0\le e_j(c_a)\le e_j(-2)\quad(j\le a),\qquad e_j(c_a)=0\quad(j>a).
 \tag{13}
\]
Consequently each untouched low kernel meeting a contracted vertex
has a coefficientwise Laurent majorant obtained by making that
vertex complete. If both ends are contracted, keep the full scalar
\(K_N^{\rm low}(-2,-2)\). In particular an edge between distinct
high pairs remains present, with its full complete-edge rate.

For a high boundary edge its other factor is the original ordinary
polynomial \(e_{D-r}(-2\cos u)\). The radical Fourier bound gives
\[
             \sup_{u\in\mathbb R}|e_{D-r}(-2\cos u)|\le\sqrt{N-1}.
 \tag{14}
\]
This includes the even-level values and the odd-level vanishing at
the complete simple node. It does not impose a quotient on an outside
variable. Equations (11)--(14), summed over their polynomially many
indices and physical colors, give a polynomial-cost coefficientwise
majorant from the low network obtained as follows: delete only edges
in \(A\); make vertices in \(T_A\) complete and untraced; keep every
other edge and every remaining original trace and coupon. Apply (9)
to this majorant; its charged scalar is not asserted nonnegative.

Let its pressure be
\[
 M_A^{\rm cut}(\boldsymbol\chi)
 =\min_{H_v\ge0,\ v\in S\setminus T_A}
 \left\{\sum_{vw\in E_S\setminus A}V(H_v,H_w)
       -\sum_{v\in S\setminus T_A}\chi_vH_v\right\},
 \quad H_v=0\ (v\in T_A\text{ or outside}).
 \tag{15}
\]
Every remaining traced vertex keeps its original incident edges:
no edge of \(A\) meets it. Thus its degree has not silently dropped.
Edges with no remaining traced endpoint contribute \(V(0,0)\).
If no traced vertices remain, (15) is precisely the sum of those
constants, with no nonexistent trace or saddle introduced.

All these minima exist uniformly. Choosing \(x=1/2\) in \(V\)
gives the coercive bound
\(\sum_v(d_v/2-\chi_v)H_v\ge\tfrac12\sum_vH_v\) on surviving
vertices, apart from harmless constant edges. Their minima therefore
lie in a fixed compact height box. At a surviving height zero the
one-sided derivative is \(-\chi_v<0\), since \(V_h(0,g)=0\).
Continuity of this derivative for bounded \(g\) gives a uniform
positive lower bound for every surviving minimizing height on
\(\mathcal K\). This argument does not assume a regular cut minimum,
or import an asymptotic for a whole cut source.

Use these minimizing heights in the joint majorant (9). It proves
directly, with the other edges and their shared labels retained,
\[
 \sup_{\mathbf u\text{ real}}|Z_N^A(\boldsymbol\chi;\mathbf u)|
          \le CN^p e^{N M_A^{\rm cut}(\boldsymbol\chi)}.
 \tag{16}
\]

## 4. A charge cost for every matching, and the strict half-cube gap

Extend (4) to charges in \([0,1]^S\) by the same minimum.
It is a concave function of the charges, being an infimum of
affine functions. Let \(\boldsymbol\chi^A\) equal \(\boldsymbol\chi\)
off \(T_A\) and zero on \(T_A\). Since \(V\) is nondecreasing
in each nonnegative height, a minimum at these zero charges can
be taken with \(H_v=0\) on \(T_A\). Restoring exactly the deleted
edges adds \(|A|M_\infty\). Therefore
\[
                 M(\boldsymbol\chi^A)
                       =M_A^{\rm cut}(\boldsymbol\chi)+|A|M_\infty.
 \tag{17}
\]
Evaluating the variational problem at its original minimizer gives
the supporting inequality directly:
\[
 M(\boldsymbol\chi^A)
 \le M(\boldsymbol\chi)+\sum_{v\in T_A}\chi_vH_v(\boldsymbol\chi).
 \tag{18}
\]
Thus
\[
 M(\boldsymbol\chi)-M_A^{\rm cut}(\boldsymbol\chi)
 \ge |A|M_\infty-\sum_{v\in T_A}\chi_vH_v
                    =\sum_{vw\in A}\gamma_{vw}.
 \tag{19}
\]
The equality uses the exact condition that selected endpoints of high
edges do not repeat. It allows repeated untraced outside endpoints.
Combining (16), (19), and the finitely many nonempty patterns proves
(6).

If \(0<\chi_v\le1/2\), (5) gives
\[
 H_v\le2\operatorname{arsinh}(1/\sqrt3)=\log3,
                   \qquad \chi_vH_v\le\tfrac12\log3.
 \tag{20}
\]
Every high edge has at most two selected ends, proving (7). An
elementary strict numerical-free margin follows from
\(G>1-1/9=8/9\), \(\pi<22/7\), and
\[
 \log3=2\sum_{j\ge0}\frac{(1/2)^{2j+1}}{2j+1}
 <1+\frac1{12}+\frac1{60}=\frac{11}{10}.
 \tag{21}
\]
Consequently \(M_\infty-\log3>112/99-11/10=31/990\).
This comparison uses the full coupled minimizer; it does not optimize
the incident edges independently or discard a connecting low edge.

**Corollary 2 (larger original degrees).** If every selected
\(d_v\ge12\), the high estimate (6) holds on every compact
\(\mathcal K\subset(0,1]^S\), including charges equal to one,
with
\[
 \gamma=M_\infty-4\operatorname{arsinh}(2-\sqrt3)>4/99.
 \tag{21a}
\]
In fact (5) bounds every \(\chi_vH_v\) by
\(2\operatorname{arsinh}\tan(\pi/12)
=2\operatorname{arsinh}(2-\sqrt3)\). An internal edge has at
most twice this cost, and a boundary edge has less. Finally
\(\operatorname{arsinh}x<x\) for \(x>0\), and
\(\sqrt3>19/11\), so the internal cost is less than
\(12/11\). The lower bound \(M_\infty>112/99\) proves (21a).
This is a high-sector estimate through the unit-charge face; it
does not assert the separated-companion asymptotic below uniformly
at that face.

**Corollary 3 (the whole nonzero lattice block).** The constants
\(C,p\) in (6) can be chosen independently of the charge vector
throughout either of these finite blocks:

* \(1\le J_v\le\lfloor N/2\rfloor\) for all \(v\), with the
  gap (7);
* \(1\le J_v\le N\) for all \(v\), if every \(d_v\ge12\),
  with the gap (21a).

Only the high-sector estimate is asserted uniformly in these blocks.
To prove it, all cut minima lie in a fixed box \(0\le H_v\le B\):
coercivity and the value at zero permit \(B=2eM_\infty\).
Choose \(h_0>0\) so
\(\tanh(h_0/2)\cosh(B/2)\le1/2\). If a surviving minimizing
height satisfies \(H_v\le h_0\), every incident edge is regular
at that endpoint and
\[
 \alpha_{v,e}
 =\arcsin\{\tanh(H_v/2)\cosh(H_w/2)\}
 \le H_v\cosh(B/2).
 \tag{21b}
\]
Use \(\arcsin x\le2x\) on \([0,1/2]\) and
\(\tanh(H_v/2)\le H_v/2\). The stationary row
\(\sum_e\alpha_{v,e}=\pi\chi_v\) then gives
\[
 H_v\ge c\chi_v\ge c/N,\qquad
 c=\min\{h_0,\pi/(d_{\max}\cosh(B/2))\}>0.
 \tag{21c}
\]
If \(H_v>h_0\), the same inequality holds because \(\chi_v\le1\).
Thus the denominators in (9) are uniformly bounded away from zero.
All numerator factors there are uniformly bounded after extracting
\(e^{-N\chi_vH_v}\). The uniform version of (10), the polynomial
physical contractions, and the finite pattern count now prove (16)
with charge-independent constants. Inequality (19) and its two
uniform edge-cost bounds finish the proof. Vertices of zeroed charge
remain untraced and require no Fourier denominator.

## 5. The resulting nonzero original lattice-source asymptotic

For completeness, the needed charge version of the archived all-low
proof follows from its written estimates without assuming a complex
charge initializer. On a compact \(\mathcal K\Subset(0,1)^S\), the
cube theorem gives positive heights, strict wire maxima and compact
uniformity. Formula (9) removes all low assignments outside small
intervals around these maxima with a strict gap, exactly as the
uncharged discarded-index argument, now with penalty \(-\chi_vH_v\).

For lattice \(\chi_v=J_v/N\), the literal cosine is an even
\(2\pi\)-periodic Laurent polynomial. Hence the original full trace
equals the full lower-circle integral of that cosine times its
spectator; its opposite vertical sides cancel. On this circle, write
\(W_N(t)=e^{-iNt}/(1-\eta e^{-iNt})^2\). Then
\[
 W_N(t)\cos((N-J)t)
 =\tfrac12e^{-iJt}
     \frac{1+e^{-2i(N-J)t}}{(1-\eta e^{-iNt})^2}.
 \tag{22}
\]
The second numerator term and every nonconstant denominator mode
have a uniform exponential gap, since the heights and \(1-\chi\)
have positive compact lower bounds. This retains the companion
\(2N-J\), every higher alias, and the exact original normal weights.
The selected term has phase
\[
 F_{\boldsymbol\chi}(\mathbf t,\mathbf u)
      =\sum_{vw\in E_S}\psi(t_v,t_w)-i\sum_{v\in S}\chi_vt_v.
 \tag{23}
\]
The archived low edge expansion and its strict angular bound apply
at these compactly regular imaginary points. The only angular
maximum is \(\mathbf t=-i\mathbf H\); its negative Hessian is the
positive definite height Hessian. Thus its Gaussian coefficient is
nonzero. Each factor \(1/2\) in (22) remains in that coefficient.
The index-cotangent connectors and all fixed boundary derivatives
are controlled by the same compact strict gaps in the low-source
proof. This proves, uniformly over the lattice charges in
\(\mathcal K\),
\[
 Z_N^{\rm low}(\boldsymbol\chi;\mathbf u)
 =N^{-3(b-1)/2}A(\boldsymbol\chi,\mathbf u)
       e^{N W(\boldsymbol\chi,\mathbf u)}(1+O(N^{-1})).
 \tag{24}
\]
Here \(W=F_{\boldsymbol\chi}(\mathbf t^*(\boldsymbol\chi,\mathbf u),
\mathbf u)\), \(W(\boldsymbol\chi,0)=M(\boldsymbol\chi)\), and,
with \(\mathcal L_{\boldsymbol\chi}\) denoting the height functional
inside braces in (4) and \(a_e\) the original positive edge amplitudes,
\[
 A(\boldsymbol\chi,0)=2^{-k}(2/\pi)^{k/2}
 \frac{\prod_v\sinh H_v\prod_e a_e(-iH_v,-iH_w)}
 {\sqrt{\det\nabla^2_{\mathbf H}\mathcal L_{\boldsymbol\chi}}}>0.
 \tag{25}
\]
The power of \(N\) and every scalar normalization are unchanged.

Under Theorem 1, (24) holds for the original full source (3).
Indeed (6) is exponentially smaller. Its real-boundary bound extends
to a sufficiently small fixed complex boundary polydisk: every
boundary angular degree is at most \(D\), so Fourier coefficient
bounds cost only a polynomial times \(e^{D\sum|\Im u_e|}\).
Shrink the polydisk to retain the gap relative to \(\Re W\).
Cauchy estimates preserve every fixed ordinary boundary derivative.
In particular the conclusion holds on every compact lower half-charge
cube, at both parities, and gives an actual nonzero initializer there.

The functions \(W,A\) have local holomorphic continuations in charges
by the geometric implicit-function theorem, but (24) here is asserted
only at the lattice charges. Off lattice the lower-circle replacement
has an original vertical current; it cannot be omitted. This theorem
also gives no uniform low-source Gaussian expansion as a charge tends
to zero, no full unit-block reconstruction error, and no arbitrary-short filled-source
conclusion. Charges outside the edge-cost criterion require a different
estimate of the coherent high sectors.

## Direct sources and author readback

The complete final proof and all four complete direct sources were
read; their directly used implications and versions were checked.

- [Zero-power charge-cube geometry](research_zero_power_charge_cube_positivity.md),
  `91b0a03a677c9139bbfd04f9ef6b06b23e6c3fab435c1a974a2d243189925faf`:
  the potential, compact regular minima, height bound and original
  marked positive branches.
- [Original low Fourier bounds](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_zero_power_subtree_fourier_bound.md),
  `9c7e71319ba9f416f5ea510dee472e481894396d0c8a3cebf6ff9cce05816c58`:
  Laurent coefficients, derivative sampling, uniform product profiles,
  and original matching support.
- [Regular low-source asymptotic](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_regular_zero_subtree_low_source.md),
  `06e4b7c14e3a61616dea61642103e2d2803709fcd465ae9860258119db3299d1`:
  local edge amplitude, strict angular and index gaps, Gaussian
  normalization, and boundary continuation. Equations (8), (22) above
  supply the additional lattice-charge calculation.
- [Full high-radical contraction](research_high_newton_radical_contraction.md),
  `1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03`:
  complete normal contraction, bounded divided-difference coefficients,
  square-zero support and the whole-real-period radical bound.

Only written proofs, source-text reads and hashes were used. No
mathematical programs, tests, numerical experiments, or public-file
changes were made.
