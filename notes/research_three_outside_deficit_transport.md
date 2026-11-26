# Transporting a real outside-color deficit through three-crossing sources

Research lemma, 4 November 2026. Frozen manuscripts are unchanged.

This is an upper-only conditional statement. It assumes a uniform
outside-color estimate for the initial original source and transports
its deficit through any fixed number of attachments. It does not
assert that the initial estimate has been proved, or infer an
outside-color packet from an internal-wire envelope.

The separate [actual boundary-decay theorem](research_three_chain_outside_boundary_decay.md)
now proves a stronger pair of local and global source bounds and preserves
their deficit without the reserve below. This lemma records what follows
from the weaker global-real hypothesis alone.

## 1. The exact source and the assumed input

Use
\[
 A_N=JM^3,\quad T_N=A_N-E_{\lfloor N/40\rfloor},\quad
 x_h=\frac16+\frac{i\log2}{2\pi},\quad
 K_N(x,y)=h(x)^TT_Nh(y),\quad \zeta(u)=-2\cos u.
 \tag{1}
\]
For the actual initial source and its exact attachments write
\[
 F_{0,N}(x,u)=v(\zeta(u))^TA_N^3h(x),\qquad
 F_{j+1,N}(y,u)=N\int_{x_h-1/2}^{x_h+1/2}
                          F_{j,N}(x,u)K_N(x,y)\,dx.
 \tag{2}
\]
The bilinear cardinal identity gives
\(F_{j,N}(y,u)=v(\zeta(u))^TA_N^3T_N^jh(y)\) exactly,
with both level parities and the original ordinary normal data.

Set
\[
 \begin{gathered}
 K=|k_0|=4\pi/\sqrt{21},\quad A=29/20,\quad a=3/2,
 \quad H_0\le H_*:=57/10000,\quad
 v_0(t)=\min\{\operatorname{dist}(t,\mathbb Z),3/100\},\\
 \rho=(5-\sqrt{21})/2,\quad D=5+\sqrt{21},\quad
 Z=\frac{(21/20)\rho}{1-3\rho/10},\quad
 C_0=\frac{K(D+3/5)}{2(D-3/5)^2}.
 \end{gathered}
 \tag{3}
\]
The proved complete-color source induction supplies the actual phases
\(S_j\), centers \(M_j=\Re S_j(x_h,0)\), certified bounds
\(H_j=Z^jH_0\), and
\[
 |M_j-M_0-2jc|
 \le d_j:=C_0H_0^2\frac{1-Z^{2j}}{1-Z^2}.
 \tag{4}
\]
Only this complete-color normalization is used below.

**Outside input hypothesis.** Suppose some \(\varepsilon\ge0\)
and nonnegative, even periodic function \(\delta(u)\), with
\(\delta(0)=0\), satisfy
\[
 |F_{0,N}(x_h+t,u)|\le CN^q
 \exp N\{M_0+\varepsilon-\delta(u)
                    +KH_0v_0(t)-A v_0(t)^2\}
 \quad(t,u\in\mathbb R).
 \tag{5}
\]
When ordinary derivatives are desired, assume the same rate in (5)
for each required fixed \(\partial_\zeta^rF_{0,N}\), with its
own polynomial factor. These are ordinary color derivatives,
including the ramified angles \(u=0,\pi\); angular derivatives
alone are not substituted. Hypothesis (5) is an input
of this lemma. In particular no local phase or nonzero coefficient
at \(u\ne0\) is assumed.

## 2. One smoothing cost, independent of subsequent length

**Lemma 1.** For each fixed \(j\ge1\), (5) implies
\[
 |F_{j,N}(x_h+t,u)|\le C_jN^{q_j}
 e^{N\{M_j+\varepsilon-\delta(u)+E_j-a v_0(t)^2\}},
 \quad
 E_j=\frac{K^2H_0^2}{4(A+a)}+d_j.
 \tag{6}
\]
It holds uniformly on both real periods and for every ordinary
derivative supplied in (5). In particular
\[
 E_j\le E_\infty
 :=\frac{K^2H_0^2}{4(A+a)}+\frac{C_0H_0^2}{1-Z^2}
 <.000026652.
 \tag{7}
\]
The exponential reserve is independent of \(j\); the polynomial
constants need not be uniform for a length growing with \(N\).

*Proof.* The actual
[two-wire real bound](research_three_vertex_two_wire_large_cap_bound.md)
is
\[
 |K_N(x_h+s,x_h+t)|\le CN^q
 e^{N\{2c-a v_0(s)^2-a v_0(t)^2\}}.
 \tag{8}
\]
The first attachment pays only the square completion
\(KH_0v-(A+a)v^2\le K^2H_0^2/[4(A+a)]\).
Its outgoing bound has the pure quadratic loss \(-a v_0(t)^2\),
with no linear term. Multiplying that loss by the input loss of
the next kernel gives \(-2a v^2\le0\); there is no further
square-completion cost. Iteration therefore gives the absolute
center \(M_0+2jc+\varepsilon-\delta(u)+K^2H_0^2/[4(A+a)]\).
Use (4) once to obtain (6). The exact measure \(N\), fixed
period length, and repeated Gaussian upper bounds cost only
polynomial factors for fixed \(j\).

The kernel is independent of the outside color. Differentiate (2)
before estimating to obtain the same proof for the assumed ordinary
jets. At no point is a far-color local packet needed. \(\square\)

For a uniform formula including \(j=0\), define
\[
 (e_j,\ell_j,B_j)=
 \begin{cases}
 (0,KH_0,A),&j=0,\\
 (E_j,0,a),&j\ge1.
 \end{cases}
 \tag{9}
\]
Then the outside-color exponent is
\(M_j+\varepsilon-\delta(u)+e_j+\ell_jv_0-B_jv_0^2\).

## 3. One or two outside colors at the exact bilinear closing

Use two independently initialized sides, allowing different
\(\varepsilon_L,\delta_L\) and \(\varepsilon_R,\delta_R\).
Their complete-color centers and gradient bounds are denoted
\(M_j^L,H_j^L\), \(M_k^R,H_k^R\), respectively. Both initial
gradient bounds are at most \(H_*\). The exact closed word is
\[
 Q_{j,k,N}(u,w)=N\int F_{j,N}(x,u)G_{k,N}(x,w)\,dx
   =v(\zeta(u))^TA_N^3T_N^{j+k}A_N^3v(\zeta(w)).
 \tag{10}
\]
The right word is transposed and reversed; no conjugation is used.

Let \(\Xi_{j,k}\) be the actual complete-color closing critical
action, and set
\[
 D_{\rm cl}=2\sqrt{21},\quad b_{\rm cl}=9/25,\quad
 C_{\rm cl}=\frac{K(D_{\rm cl}+b_{\rm cl})}
                     {2(D_{\rm cl}-b_{\rm cl})^2}.
 \tag{11}
\]
The original closing-action estimate is
\[
 \Re\Xi_{j,k}\ge M_j^L+M_k^R
                 -C_{\rm cl}(H_j^L+H_k^R)^2.
 \tag{12}
\]
Indeed the complete critical equation gives
\(|z_c|\le(H_j^L+H_k^R)/(D_{\rm cl}-b_{\rm cl})<.0013\),
inside the source disk even at the largest allowed gradients.
Integrating the stationary action twice gives (12), exactly as in
[the bilinear closing proof](research_three_small_source_closure.md).
This analytic action comparison does not by itself give a nonzero
quantum closing coefficient.
For \(j,k\ge2\), this is a proved nonzero complete-source
closing by the small-source theorem. The
[larger closing theorem](research_three_larger_source_closure.md)
also establishes the complete closing for the actual entrance caps
at all \(j,k\ge0\): two unpropagated caps use its stronger raw
entrance bound, and any propagated cap gives its unequal-preparation
case. The upper comparisons below do not establish a closing
coefficient by themselves.

**Lemma 2.** With the left outside hypothesis only and the right
color complete, the rate relative to \(\Re\Xi_{j,k}\) is at most
\[
 \varepsilon_L-\delta_L(u)+
 e_j^L+\frac{(\ell_j^L+KH_k^R)^2}{4(B_j^L+A)}
                         +C_{\rm cl}(H_j^L+H_k^R)^2.
 \tag{13}
\]
With both outside hypotheses, it is at most
\[
 \begin{split}
 \varepsilon_L+\varepsilon_R-\delta_L(u)-\delta_R(w)
 +e_j^L+e_k^R
 +\frac{(\ell_j^L+\ell_k^R)^2}{4(B_j^L+B_k^R)}
 +C_{\rm cl}(H_j^L+H_k^R)^2.
 \end{split}
 \tag{14}
\]
Each assertion is an upper bound for the integral of the absolute
value, and includes the assumed fixed ordinary derivatives.

*Proof.* For (13), multiply the bound (9) by the already proved
complete-color envelope
\(M_k^R+KH_k^Rv_0-A v_0^2\). Complete the remaining real
quadratic and use (12). For (14), instead multiply the two
bounds (9). The measure and integration length again change only
the polynomial prefactor. Differentiating the exact finite bilinear
integral handles the ordinary jets. \(\square\)

These formulas have useful explicit reserves. For \(j,k\ge2\),
the added cost in (13) is less than \(27\cdot10^{-6}\), and
the added cost in (14) is less than \(54\cdot10^{-6}\).
Indeed \(H_j,H_k\le H_2:=Z^2H_*\), so it suffices to check
\[
 \begin{split}
 E_\infty+\frac{K^2H_2^2}{4(A+a)}+4C_{\rm cl}H_2^2
       &<27\cdot10^{-6},\\
 2E_\infty+4C_{\rm cl}H_2^2&<54\cdot10^{-6}.
 \end{split}
 \tag{15}
\]
The two left sides are respectively below \(.000026779\) and
\(.000053369\). The sharper finite-length versions remain
(13)--(14).

For the shorter complete closings, the same algebra gives
the following length-independent table. The closing coefficient is
supplied separately as specified after (12).

| Attachments on the two sides | One outside-color cost | Two outside-color cost |
|---|---:|---:|
| \(j=k=0\) | \(<107\cdot10^{-6}\) | \(<107\cdot10^{-6}\) |
| \(j+k\ge1\) | \(<56\cdot10^{-6}\) | \(<56\cdot10^{-6}\) |
| \(j,k\ge2\) | \(<27\cdot10^{-6}\) | \(<54\cdot10^{-6}\) |

To verify the middle row, split into zero/positive and positive/positive
attachment counts. Put \(H_1=ZH_*\) and bound positive-count
reserves by \(E_\infty\). The required quantities are
\[
 \begin{gathered}
 \frac{K^2(H_*+H_1)^2}{8A}+C_{\rm cl}(H_*+H_1)^2,
 \quad E_\infty+\frac{K^2H_*^2}{4(A+a)}
                       +C_{\rm cl}(H_*+H_1)^2,\\
 2E_\infty+4C_{\rm cl}H_1^2,
 \quad E_\infty+\frac{K^2H_1^2}{4(A+a)}+4C_{\rm cl}H_1^2.
 \end{gathered}
 \tag{16}
\]
All are below \(56\cdot10^{-6}\). The first row uses
\(K^2(2H_*)^2/(8A)+C_{\rm cl}(2H_*)^2<107\cdot10^{-6}\).
No unknown critical coefficient enters these numerical budgets.

## 4. Restoring the original word and the exact remaining condition

For the complete-ended chain with \(j,k\ge2\), put
\(m=6+j+k\). Its original source differs from (10) by
\[
 v(\zeta(u))^T\{A_N^m-A_N^3T_N^{j+k}A_N^3\}v(\zeta(w)).
 \tag{17}
\]
The original corner-transfer norm proof is uniform over both
real ordinary colors and fixed ordinary derivatives. Its left
vector estimate is explicitly uniform on \([-2,2]\); on the
right use \(\|Mv^{(r)}\|\le\|M\|\|v^{(r)}\|\), the
real Newton-vector bound and Markov's inequality. The same exact
word telescope therefore bounds (17) by
\(CN^q e^{N[(2m-1)c+M_\infty+27/200]}\). The actual complete
geometric action exceeds this rate by \(31/600\), as proved in
[the original corner-transfer theorem](research_three_chain_fourier_corner_transfer.md#4-a-larger-deleted-corner-for-a-larger-source-domain).

Consequently, for one outside color the full original source has
upper rate
\[
 \Re\Xi_{j,k}-
 \min\{\delta_L(u)-\varepsilon_L-27\cdot10^{-6},\ 31/600\}.
 \tag{18}
\]
For two outside colors replace the first argument of the minimum by
\[
 \delta_L(u)+\delta_R(w)-\varepsilon_L-\varepsilon_R
                                      -54\cdot10^{-6}.
 \tag{19}
\]
Thus a uniform initial deficit exceeding the stated reserve on a
specified real outside arc gives a uniform strict upper gap there,
for every fixed length covered by the complete-source closing.
Both the original finite normals and the original boundary
polynomials are retained.

The input (5) has not been proved here. Nor does a constant-loss
transport automatically yield a positive multiple of
\(1-\cos u\) arbitrarily near \(u=0\), or a quadratic estimate
on a complex outside strip. Those require additional initial or
local estimates. The internal Fourier-wire envelopes and the
outside ordinary-color envelopes are different assertions.

## 5. Reproduction

```sh
python3 experiments/check_three_outside_deficit_transport.py --precision 192
```

The [focused checker](../experiments/check_three_outside_deficit_transport.py)
and [record](../repro/results/research-three-outside-deficit-transport.json)
check the exact geometric-series and word identities and all scalar
reserves. The proof uses the already established complete-source
induction and closing normalization, rather than a norm-to-observation
inference. No marked-knot or cofinite-filling statement is added.
