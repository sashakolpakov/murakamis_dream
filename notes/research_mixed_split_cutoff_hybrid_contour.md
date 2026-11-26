# A periodic contour retaining the proved left and independent-right regions

Research proof, 4 November 2026. This constructs one exact contour on
which two completed integration-region theorems can be combined. It
changes none of their source estimates. Mixed left/right configurations
and the low region remain outside the resulting estimate.

## 1. The seam obstruction to the literal one-sided proposal

Write \(H=7/500\), and let \(c_j=\Im r_j\) at an unselected
position and \(c_j=H\) at a selected type-four position. The proposed
one-sided left cutoff is zero below .1, rises to one by .22 (by .12
for selected positions), and then stays one through the right endpoint.
The independent right profile is
\[
 R_+(x)=\begin{cases}1,&0\le x\le.45,\\
                     400(.5-x)^2,&.45\le x\le.5,\\
                     0,&.5\le x\le1.
       \end{cases}                                           \tag{1}
\]
In particular this is the **quadratic** profile in the completed
right-taper theorem, not the linear right part of the minimum-neighbor
contour.

The literal expression \(c_jR_+(x_j)\min_{k\in N(j)}L(x_k)\)
need not be periodic. In a two-cycle, fix \(x_1=.3\) and
\(c_1\ne0\). As \(x_2\to1\), its first height tends to
\(c_1\); as \(x_2\to0\), it tends to zero. Multiplication by
the first coordinate's right profile does not remove a jump caused by
its neighbor. The one-cycle product happens to match at the seam, but
that does not fix the two-cycle obstruction. Thus the exact periodic
graph theorem cannot be applied to this literal proposal. Keeping a
discontinuous parametrization would require its seam currents; they
have not been shown to vanish for the original source.

## 2. A repair supported in the low region

Fix \(0<\varepsilon<.1\), independently of \(N\). For
\(b\in\{.22,.12\}\), define a continuous periodic cutoff by
\[
 L_b(x)=\begin{cases}
 1-x/\varepsilon,&0\le x\le\varepsilon,\\
 0,&\varepsilon\le x\le.1,\\
 (x-.1)/(b-.1),&.1\le x\le b,\\
 1,&b\le x\le1.
 \end{cases}                                                  \tag{2}
\]
Its values at zero and one are both one. Define another periodic
function by
\[
 R_\varepsilon(x)=\begin{cases}
 0,&0\le x\le\varepsilon,\\
 (x-\varepsilon)/(.1-\varepsilon),&\varepsilon\le x\le.1,\\
 1,&.1\le x\le.45,\\
 400(.5-x)^2,&.45\le x\le.5,\\
 0,&.5\le x\le1.
 \end{cases}                                                  \tag{3}
\]
Both values at the seam are zero. Put \(b_j=.12\) for a selected
position, and \(b_j=.22\) otherwise. The graph for a fixed selection
\(S\) is
\[
 z_j=x_j+i\mathcal H_{S,j}(x),\qquad
 \mathcal H_{S,j}(x)=c_jR_\varepsilon(x_j)
                       \min_{k\in N(j)}L_{b_j}(x_k),
 \quad N(j)=(j-1,j,j+1).                                    \tag{4}
\]
The cutoff in the minimum is chosen by the **row** \(j\), exactly
as in the earlier selected contour. It is not chosen by the type or
selection of its argument \(k\). Repeated indices retain their
literal meaning; repetition does not change a minimum.

Every low coordinate \(x_j\in[0,.1]\) has height zero. Indeed
\(R_\varepsilon(x_j)L_{b_j}(x_j)=0\), and the minimum in (4)
is at most that own-coordinate factor. On \([\varepsilon,.1]\)
a low coordinate also resets both neighboring heights completely.
On \([0,\varepsilon]\), however, the neighboring attenuation varies
from one to zero. In particular a low coordinate at the periodic seam
has height zero but does **not** reset its neighbors. This difference
from the old minimum-neighbor graph is necessary for the present
periodic repair and must be retained in any low-region estimate.

## 3. Exact finite integral and Jacobian

The functions in (4) are periodic, continuous and piecewise polynomial
with finitely many pieces. They have bounded first derivatives for the
fixed \(\varepsilon\). The
[closed-form contour identity](research_mixed_coupled_outer_graph.md),
Theorem 1, therefore gives, for each original selected Laurent term,
\[
 \operatorname{CT}\mathcal D_{N,S}
 =\int_{\mathbb T^m}
   \mathcal D_{N,S}(e^{-2\pi i(x+i\mathcal H_S(x))})
                  \det(I+iD\mathcal H_S(x))\,dx.              \tag{5}
\]
All finite conditional rows, the actual polynomial \(d_N\), the
selected factors \(X_j^{-N}\), the scalar
\(\kappa^{m+k}N^{m+k}\), and their original carriers are unchanged.
Equation (5) uses the complete Laurent polynomial. No factorial
approximation or off-grid interpolation is substituted in the deformation.
It has no omitted seam or internal joining currents, and requires no
nonvanishing condition on the complex determinant.

Here is a uniform bound sufficient for every fixed word. Let
\[
 K_\varepsilon=\max\{50,\varepsilon^{-1}\},\qquad
 B_\varepsilon=\frac{57}{1000}(40+K_\varepsilon).
\]
A row with \(x_j\in(0,.1)\) is identically zero, including all
its partial derivatives on each open differentiability piece.
Elsewhere, differentiating (4) gives at most the own-coordinate term
\(c_jR_\varepsilon'\min L\) and one term from a minimizing
argument. Here \(|R_\varepsilon'|\le40\), \(|L_b'|\le K_\varepsilon\),
and \(0\le R_\varepsilon,\min L\le1\). Hence
\[
 \sum_k|\partial_k\mathcal H_{S,j}|\le B_\varepsilon,
 \qquad
 |\det(I+iD\mathcal H_S)|
       \le(1+B_\varepsilon^2)^{m/2}.                         \tag{6}
\]
Ties with the same coordinate or a constant minimum introduce no extra
term; other ties have measure zero. The row bound is still valid if the
two displayed derivative terms occur in the same column. Thus (6)
includes cycles of lengths one and two. For example,
\(\varepsilon=1/1000\) gives the simpler bound \(60^m\).
This is independent of \(N\); \(\varepsilon\) is not allowed to
shrink with \(N\) in this assertion.

## 4. Literal agreement on the two completed regions

Put
\[
 Q_m=[.1,.45]^m,\qquad V_m=[.22,1]^m,\qquad
 P_m=[.22,.45]^m,\qquad U_m=Q_m\cup V_m.                     \tag{7}
\]
On \(Q_m\), the own factor in (3) is one. The values of (2) are
exactly the slow and fast left cutoffs in
[the earlier selected contour](research_mixed_early_selected_transport.md).
Therefore (4) is **the same graph**, for each selected subset, as the
graph of [the complete left-region theorem](research_mixed_full_left_region.md).
Its Jacobian agrees almost everywhere as well.

On \(V_m\), every cutoff in the minimum is one. Thus
\(\mathcal H_{S,j}=c_jR_\varepsilon(x_j)\), which is precisely
the independent \(\chi_1\) contour used in
[the complete selected right-taper assembly](research_mixed_selected_right_taper_support.md),
Section 5. Its plateau height is the actual \(c_j=\Im r_j\) when
unselected and exactly \(H=.014\) when selected. Its right part is
\(400(.5-x)^2\), and its height is zero on \([.5,1]\).
Consequently both the original integrand and its graph Jacobian agree
with that theorem, not just their exponential rates.

The intersection is exactly \(P_m\). On its interior both graphs
have their same constant selected or unselected heights and Jacobian
one. The original local unselected critical contribution is therefore
literally the same in all three region integrals.

**Theorem 1 (union-region contribution).** Let
\(M=\Re\Phi(r)\), and let \(\mu>0\) be the plateau Hessian
constant used in the complete left-region theorem. Sum all original
selected terms on (4), restricted to \(U_m\), and denote the result
by \(\mathcal Z_N^{\mathrm{hyb}}(U_m)\). Then
\[
 \mathcal Z_N^{\mathrm{hyb}}(U_m)
 =\mathcal I_{N,\varnothing}(P_m)
       +O\!\left(N^A e^{N(M-\delta)}\right),
 \qquad
 \delta=\min\{\mu/1600,1/160000\}>0.                         \tag{8}
\]
It has the original nonzero central coefficient, action, unit carrier
and cyclic level power \(N^0\), at all sufficiently large integer
levels and with both parities retained.

**Proof.** For every fixed selection, ordinary inclusion--exclusion
of the identical differential-form integrals gives exactly
\[
 \mathcal I^{\mathrm{hyb}}_{N,S}(U_m)
 =\mathcal I^{\mathrm{left}}_{N,S}(Q_m)
  +\mathcal I^{\mathrm{right}}_{N,S}(V_m)
  -\mathcal I_{N,S}(P_m).                                   \tag{9}
\]
This is an identity before taking absolute values or asymptotics.
The left-region theorem bounds its complete selected sum by the
unselected plateau integral plus an error with gap
\(\min\{1/2000,\mu/1600\}\). The independent-right assembly gives
the same plateau integral with gap \(1/160000\). The selected terms
on \(P_m\) have gap \(1/200\), so its complete selected sum is
also that same unselected integral plus such an error. Summing (9)
therefore counts the central integral as \(1+1-1=1\) and proves
(8). All full Fourier alternatives are already retained in these
three literal source theorems. The bounded graph Jacobian adds no
exponential cost. \(\square\)

## 5. What remains and what locality does give

Up to the common endpoint faces, the exact complement of (7) is
\[
 \{\min_jx_j<.1\}\ \cup\
 \{\min_jx_j\ge.1,\ \min_jx_j<.22,\ \max_jx_j>.45\}.         \tag{10}
\]
Thus (8) does not bound low configurations or configurations containing
both a genuine left-transition coordinate and a right-taper/right-half
coordinate. It supplies no whole-period or boundary-insertion theorem.

There is nevertheless a useful finite-range reduction. Compare (4)
with the independent own-coordinate graph \(c_jR_\varepsilon(x_j)\).
For a fixed selected subset let
\[
 B_S=\{k:L_{b_j}(x_k)<1\text{ for at least one row }j
                          \text{ whose }N(j)\text{ contains }k\}.
\]
The simpler selection-independent set \(B=\{k:x_k<.22\}\)
contains it. Every row with \(N(j)\cap B=\varnothing\) is
unchanged. Therefore every block whose two endpoint neighborhoods
miss \(B\) has its exact old independent-right arguments and source
bounds. On an open region of strict cutoff inequalities its Jacobian
rows are unchanged too. Only blocks meeting the one-neighborhood of
\(B\) can change; arbitrary distant right-run interiors need no new
source cover.

This is not a bound for the changed blocks. Their neighboring plateau
heights can change even when those plateau real coordinates remain
near the critical point. The original right-taper support theorem does
not permit arbitrary such plateau-height changes. The complete endpoint
source bounds allow a sufficiently small real seam argument and the
full typed range for its other height, but their local gaps alone do
not pay these additional neighboring-block costs. In particular the
both-real zero-collar theorem cannot be applied when the other target
height in (4) is nonzero.

For comparison, a second repair leaves \(L_b=0\) on the whole low
interval and sends it from one to zero in a collar
\([1-\varepsilon,1]\). Multiplying by the original (1) then gives
a periodic graph, with the same bound (6). It preserves the old minimum
left graph, including its low resets, and the independent-right graph
only on \([.22,1-\varepsilon]^m\). Its near-one collar changes the
neighboring rows and needs its own comparison. Neither repair licenses
reuse of the old minimum-neighbor low/plateau/right estimate on an
unmatched graph. The near-zero repair is useful because (8) follows
without a new numerical cover; no claim that its remaining interfaces
are easier has been assumed.

## 6. Reproduction

```sh
python3 experiments/check_mixed_split_cutoff_hybrid_contour.py
```

The checker verifies the exact cutoff matching, the seam obstruction,
normalization bookkeeping, the Jacobian arithmetic and the region
identity, and checks the current inherited record bindings. It does
not test a new source inequality or use a finite list of words to
replace the general contour argument.
