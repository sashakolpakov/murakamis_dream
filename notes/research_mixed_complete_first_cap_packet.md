# The complete original first cap at the open-word geometric images

Research theorem, 5 November 2026. Both original cap types have a
nonzero ordinary-color packet near every outgoing image supplied by
the all-word endpoint localization. Every private finite row and both
level parities are retained. The outgoing domain is a fixed neighborhood
of those compact images; this is not a theorem on the whole outgoing
period or the full open-word invariant.

## 1. The exact polynomial and the outgoing domain

Use the literal source in
[open torus composition](research_mixed_conditional_torus_composition.md),
equations (17), (20)--(21):
\[
 U_{\epsilon,N}(w,X)=\sum_{i=0}^{N-1}
       \frac{H_N(w,r^{-i})p_i(X)}{P_i^{1+\epsilon}},
 \quad p_i(X)=(rX;r)_i,\quad P_i=(r;r)_i,
 \quad r=e^{-2\pi i/N},\quad\epsilon=0,1.                \tag{1}
\]
Here \(H_N\) is the original complete-end Newton polynomial, so
\(\deg_X U_{\epsilon,N}<N\). No physical row is deleted and no
continuation of a terminating physical formula replaces (1).

For each own type \(3+\epsilon\), let \(K_{3+\epsilon}\) be the
union of the attached-leg images of its two endpoint maps in
[open-word localization](research_mixed_open_word_critical_localization.md),
over the complete closed external disks, together with its one-vertex
outgoing point. The exact
[image extraction](research_mixed_open_word_endpoint_rectangles.md)
places these compact sets strictly inside
\[
 T_3=(.278,.391)+i(-.072,.021),\qquad
 T_4=(.246,.350)+i(-.108,-.020).                           \tag{2}
\]
For \(z\in K_{3+\epsilon}\), let \(e_*(z),u_*(z)\) be its original
private and auxiliary critical coordinates. If two map images overlap,
the cap's original two-variable logarithmic equations and their strictly
accretive Hessian identify the roots. Thus these coordinates glue
holomorphically near the whole compact outgoing image. The same
statement includes the separately certified one-vertex root.

The private coordinate lies strictly in
\[
 \mathcal R=[.27,.49]+i[-.055,.04].                       \tag{3}
\]
The [complete endpoint rectangle packet](research_mixed_endpoint_cap_rectangle.md)
supplies the actual finite coefficient \(\mathcal C_N(e,w)\) on a
fixed neighborhood of \(\mathcal R\times\{-2\}\), with phase
\(S(e,w)\), nonzero coefficient \(\mathcal A(e,w)\), and power
\(N^{-3/2}\). Its original critical coordinate at \(w=-2\) is
\(u_c(e)\), and \(u_*(z)=u_c(e_*(z))\).

## 2. Phase and coefficient without an additive ambiguity

Let \(J'(v)=\operatorname{Log}(2\sin\pi v)\), \(J(0)=0\), and
\(g(v)=J(v)+i\pi(v-v^2)/2\), with the original strip branches.
Define
\[
 \Psi_\epsilon(e,z,w)=S(e,w)+J(e+z)-J(z)-i\pi ez
                                      -\epsilon g(e).    \tag{4}
\]
For \(w\) near the complete color, let \(e_\epsilon(z,w)\) continue
the zero of \(\Psi_{\epsilon,e}\) at \(e_*(z)\), and put
\[
 \mathcal T_\epsilon(z,w)=
          \Psi_\epsilon(e_\epsilon(z,w),z,w).             \tag{5}
\]
The nondegenerate critical point and its phase are holomorphic on a
fixed neighborhood of \(K_{3+\epsilon}\times\{-2\}\).

At the critical coordinate \(e=e_\epsilon(z,w)\), define
\[
 \mathcal B_\epsilon(z,w)=
 \frac{\sqrt{2\pi}}{\sqrt{-\Psi_{\epsilon,ee}(e,z,w)}}
 \mathcal A(e,w)
 \sqrt{\frac{\sin\pi(e+z)}{\sin\pi z}}
 (2\sin\pi e)^{-\epsilon/2}e^{i\epsilon\pi e/2}.          \tag{6}
\]
All sine and Gaussian roots have the continuations fixed by the original
factorial and endpoint packet. At the complete color the negative real
part of \(\Psi_{ee}\) is positive, fixing its Gaussian square root
with positive real part. None of the factors in (6) vanishes.

**Theorem 1.** There is a fixed open neighborhood of
\(K_{3+\epsilon}\times\{-2\}\) on which the literal polynomial (1)
satisfies, at both parities,
\[
 U_{\epsilon,N}(w,e^{-2\pi iz})
 =N^{-1-\epsilon/2}\mathcal B_\epsilon(z,w)
       e^{N\mathcal T_\epsilon(z,w)}(1+O(N^{-1})).         \tag{7}
\]
The normalized relative error is holomorphic, uniformly with every
fixed joint derivative on smaller neighborhoods. In particular the
whole private finite sum has a nonzero leading coefficient there.

For the original signed ordinary jets
\(U_{\epsilon,k,N}=(-1)^k\partial_w^k U_{\epsilon,N}|_{w=-2}\),
\[
 U_{\epsilon,k,N}(e^{-2\pi iz})
 =N^{k-1-\epsilon/2}\mathcal B_\epsilon(z,-2)
 \left(\frac{\tan\pi u_*(z)}{4\pi}\right)^k
 e^{N\mathcal T_\epsilon(z,-2)}(1+O_k(N^{-1})).           \tag{8}
\]
Its displayed coefficient is nonzero for every fixed \(k\).

## 3. Every real row and every outer contour current

The exact endpoint identity gives, for every \(X\),
\[
 U_{\epsilon,N}(w,X)=\sum_{i=0}^{N-1}
 D_N(i/N)^{-1}\mathcal C_N(i/N,w)
                              \frac{p_i(X)}{P_i^\epsilon}.
                                                               \tag{9}
\]
This is the interpolation and normalization audited in
[the complete-current reduction](research_mixed_cap_outer_contour_reduction.md).
On (3) the retained summand has phase (4), power
\(N^{-(3+\epsilon)/2}\), and the coefficient in (6) before its
outer Gaussian factor. The order-one factors from \(D_N^{-1}\)
and the marked numerator ratio cancel exactly; the own reciprocal
factorial contributes \(e^{i\epsilon\pi e/2}\).

Here is the exact bridge between its two rate descriptions. For real
\(c=.27,.49\), the shifted arguments satisfy
\(0<\Re z<\Re(c+z)<1\), and
\[
 \Re[g(c+z)-g(z)]
   =\int_0^c\log|1-e^{-2\pi i(z+s)}|\,ds=I_h(c,\Re z).
                                                               \tag{10}
\]
Since \(g(c+z)-g(z)=J(c+z)-J(z)-i\pi cz+i\pi(c-c^2)/2\)
and \(\Re g(c)=J(c)\), the full real-row rate satisfies
\[
 R_\epsilon(c,z)=\Re\Psi_\epsilon(c,z,-2).               \tag{11}
\]
There is no additional constant or missing chirp at this junction.

The correlated [real-cut certificate](research_mixed_cap_real_cut_gaps.md)
uses all 5,258 endpoint-map disks and both one-vertex disks. It proves
\[
 M_\epsilon(z):=\Re\mathcal T_\epsilon(z,-2)>1,\qquad
 M_\epsilon(z)-R_\epsilon(c,z)>1/2000
 \quad(c=.27,.49).                                      \tag{12}
\]
The [full real-tail theorem](research_mixed_outer_cap_real_tails.md)
bounds the original lower tail by
\(\max(R_\epsilon(.27,z),1/4)\), and the upper tail by
\(\max(R_\epsilon(.49,z),3/4)\), with one arbitrarily small
finite-source rate tolerance. This includes all revived off-grid
Pochhammer rows, both level parities, and the literal rows near zero
and one. It does not extrapolate a compact endpoint packet to those
two physical endpoints. By (12), a single tolerance smaller than
\(1/4000\) leaves a finite gap of at least \(1/4000\) below
\(M_\epsilon\) in both discarded tails, after reducing the ordinary
color neighborhood if necessary.

On the retained rectangle, the complete-current reduction proves
\(-\Re\Psi_{ee}>0\). Its outward curvature certificate gives
\(A+B^2/A<24\) for \(\Psi_{ee}=-A+iB\), over the entire product
of (3) with both attached rectangles. Therefore both whole horizontal
aliases have gaps greater than \(3/20\) and \(6/25\). Vertical
convexity bounds every alias side by its real cut and horizontal
endpoints. The constant mode, whose exact coefficient is \(+N\),
is moved to the horizontal line through \(e_*\). It has a unique
maximum there; strict horizontal curvature and the positive distance
of the private image from both cuts give endpoint gaps. Vertical
convexity then bounds both joining currents by those endpoints and
the real cut values. Half-grid cuts differing by \(O(N^{-1})\)
preserve every strict estimate. These are all pieces of the original
outer residue formula.

The remaining Gaussian integral contributes \(N^{-1/2}\). Combining
it with the exact \(+N\) constant mode and the summand power gives
\(N^{-(3+\epsilon)/2}N N^{-1/2}=N^{-1-\epsilon/2}\), with
precisely (6). The first odd local correction integrates to zero,
giving relative error \(O(N^{-1})\).

The zero-safe Newton-product bound preserves the discarded-row gaps
for the whole ordinary polynomial near \(-2\), while the retained
factorial symbols and all contour bounds persist by holomorphy and
their strict margins. Compactness gives a fixed joint neighborhood;
Cauchy's formula gives the normalized derivative estimates. Finally
stationarity and the original endpoint packet give
\(\partial_w\mathcal T_\epsilon=-\tan(\pi u_*)/(4\pi)\) at
the complete color. Since \(0<\Re u_*<1/2\), this is nonzero,
which proves (8).

## 4. What this changes in the exact open source

The theorem is for the original \(U_{\epsilon,N}\) itself. The exact
torus formula still contains
\[
                  W_N(X)^\epsilon,
 \qquad W_N(X)=d_N(X)(1+X^{-N}),                          \tag{13}
\]
with its original scalar carrier and all other kernel factors.
Nothing in (7) removes either Fourier branch or changes the degree
projection in that identity. If instead one chooses the older
type-three terminating replacement \(N\mathcal K_NW_N\), that
alternative identity retains its additional \(W_N\) exactly; it is
not the source used to prove (7).

Thus the local outgoing limitation of the older cap theorem is repaired
on the actual all-word endpoint images, and type four is included.
The whole outgoing period, the simultaneous contour for the remaining
open word, and the identification of its critical action with the marked
positive geometric solution are separate obligations. This cap theorem
alone proves neither the full open-word asymptotic nor a new knot family
or an arbitrary short-filling theorem.

## 5. Reproduction

The focused checker validates the complete source/cut/tail/alias records
and their saved replays, and checks the exact phase, power, and tolerance
bookkeeping. It does not rerun any root or interval cover.

```sh
python3 experiments/check_mixed_complete_first_cap_packet.py
python3 experiments/check_mixed_complete_first_cap_packet.py --input repro/results/research-mixed-complete-first-cap-packet.json --output repro/results/research-mixed-complete-first-cap-packet-replay.json
```

The saved numerical inputs and this assembly are available as one focused
reproduction group:

```sh
python3 repro/run_research_checks.py mixed-first-cap
```
