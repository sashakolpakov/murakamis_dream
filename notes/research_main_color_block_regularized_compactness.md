# Main-color preserving metrics in a bounded regularized source problem

24 November 2026. Research note. Written proof.

Main-color preserving gauges already suffice at the leading exponential
scale for the actual all-main-color source. The earlier proof establishes
an infimum over those gauges. Here that infimum is approximated inside an
explicit finite metric window, including when individual color values
vanish. The restricted regularized minimizer consequently has logarithmic
metric radius \(O(N)\) and the same leading rate as the unrestricted
problem. The proof retains the original closing in every color.

This removes color mixing from that bounded variational formulation at
the leading scale. It does not identify the remaining within-color
metrics with geometric data or prove a volume lower bound.

## 1. The actual sectors and a known input bound

Use the actual all-main-color compiler of [C, Section 5]. Fix a completed
braid word whose prescribed marked closure is one knot, with its original
zero-framing factors and partial pivotal trace. Let \(b\) be its fixed
braid width; each proper edge in color \(j\) is the full operator space
\(\operatorname{End}(V_{j,N}^{\otimes b})\).
Compile multiplication of its signed crossing operators as
a tree with \(m\ge2\) vertices, including the root readout. Select any set
\(\mathcal J\subset\{1,\ldots,N\}\) containing \(1\), with
\(2\le r:=|\mathcal J|\le N\). Keep those original color blocks and
their original readouts. An internal edge is an orthogonal direct sum
of these \(r\) physical color spaces. Every local tensor has blocks
\(T_{v,j}\), \(j\in\mathcal J\), and a contraction pairs only equal
color labels. The root output is exactly
\[
 Y_{\mathcal J,N}=(c_j)_{j\in\mathcal J},\qquad c_1=1,
 \qquad \|Y_{\mathcal J,N}\|\ge1,\qquad c_N=K_N.          \tag{1}
\]
The last identity refers to the original complete-color readout,
whether or not \(N\) was selected. Every selected physical space is
retained in full, including its reducible structure. No nonvanishing
of \(c_j\) for \(j>1\), or of \(K_N\), is assumed.

Orient edges toward the root. Write \(a_{e,j}\) for the actual open
subtree message in sector \(j\), before its parent is contracted.
These proper messages are products of invertible signed physical
crossings. They do not include the final closing. Fix a known \(B=B_N\ge2\)
which bounds
\[
 \|T_{v,j}\|_{\rm HS},\quad \|T_{v,j}\|_{\rm HS}^{-1},
 \quad \|a_{e,j}\|,\quad \|a_{e,j}\|^{-1}
                         \quad\hbox{for every }v,e,j.    \tag{2}
\]
Vector norms on the edge spaces are their physical Hilbert--Schmidt
norms. Norms of maps between those spaces below are induced operator
norms. Local tensor norms are coefficient Hilbert--Schmidt norms.

For every fixed actual word, such a \(B_N\) satisfies
\[
              \log B_N=O(N),\qquad
              \log D_N=O(\log N),\qquad
              D_N:=\sum_e\dim H_e.                       \tag{3}
\]
Here \(D_N\) includes all selected colors. To verify the first assertion, [M,
(10)--(12)] bounds both signed crossings and their inverses uniformly
over the entire main-color orbit. The inverse of a fixed proper word
is the reversed word of inverse crossings. Thus its operator norm and
inverse operator norm are \(\exp(O(N))\); tensoring spectator identities
adds polynomial factors. Its Hilbert--Schmidt norm has the same upper
bound and is at least the reciprocal of its inverse operator norm.
In every selected sector the multiplication and original readout blocks
have nonzero unit-modulus coefficients and polynomial norms. Their
reciprocal norms are therefore bounded too, even if that readout
evaluates to \(c_j=0\). These observations prove (2)--(3)
without any division by a closed color value.

Fixed signed powers or fixed short word blocks may be contracted first.
All constants can depend on that fixed presentation. The gauges below
use the complete open messages, not their principal symbols.

## 2. A finite sector-preserving competitor

For positive metrics \(H=(H_e)\), let
\[
 L_N(H)=\sum_v\log\|T_v\|_H,\qquad
 Z(H)=1+\sum_e\operatorname{tr}(H_e+H_e^{-1}).
                                                               \tag{4}
\]
The pairing is bilinear: a gauge \(g_e\) acts on the child output
and \(g_e^{-\mathsf T}\) on its parent input. In this section every
gauge preserves the color sectors. Put
\[
 C_{\rm block}
       =\left(\sum_{j\in\mathcal J}|c_j|^{2/m}\right)^{m/2}.
                                                               \tag{5}
\]
By [M, Section 5], this is the exact restricted product-norm infimum.
In particular every sector-preserving metric satisfies
\(L_N(H)\ge\log C_{\rm block}\). We prove a finite approximation
with a quantitative metric bound.

**Theorem.** For \(0<\eta\le1\), define
\[
 \begin{split}
 \delta&=\left(\frac{2\eta}{m(r+1)}\right)^{m/2},&
 t&=B^{m+1}/\delta,\\
 \mathcal L&=\log B+(m-1)\log t\\
 &=m^2\log B+
       \frac{m(m-1)}2\log\frac{m(r+1)}{2\eta},\\
 A_{\rm block}(B,D_N,\eta)
   &=\log(1+2D_N)+2(1+2m^2)\mathcal L .
 \end{split}                                               \tag{6}
\]
There are finite positive block-diagonal metrics with
\[
 0\le L_N(H)-\log C_{\rm block}\le\eta,\qquad
                  \log Z(H)\le A_{\rm block}(B,D_N,\eta).
                                                               \tag{7}
\]

Choose, independently on each edge and sector, a gauge sending
\(a_{e,j}\) to a fixed first unit vector \(e_0\), with its norm and
inverse norm at most \(B\). Rotate the unit direction first, then
scale its first coordinate by \(\|a_{e,j}\|^{-1}\).
All these gauges can be applied simultaneously: they cancel inside
every contracted subtree. At a proper vertex the slice with all
child indices zero is exactly \(e_0\) on its parent edge. At the root
that slice is \(c_j\). In particular a proper output-excited entry
with every child index zero vanishes exactly.

Before further filtering, each sector tensor has norm at most
\(B^{m+1}\). At an edge whose child has depth \(h\), with root depth
zero, apply the additional child-side gauge
\[
                  \operatorname{diag}(1,t^h,\ldots,t^h).
                                                               \tag{8}
\]
An excited output at a proper vertex of depth \(h\), with \(k\ge1\)
excited child indices, receives exponent
\(h-k(h+1)\le-1\). An unexcited output with any excited child is
also suppressed by at least \(t^{-1}\). The only remaining case,
an excited output with no excited child, was zero already.
The corresponding statement at the root is immediate.
Thus the norm of the entire nonselected slice is at most \(\delta\).
It is orthogonal in coefficient space to the unchanged selected slice.

Let \(a_{v,j}>0\) now denote these finite gauged local sector norms,
and set \(p_j=\prod_v a_{v,j}\). These are local tensor norms,
distinct from the open messages \(a_{e,j}\). Orthogonality gives
\[
 a_{v,j}\le\sqrt{1+\delta^2}\quad(v\ne{\rm root}),\qquad
 a_{{\rm root},j}\le\sqrt{|c_j|^2+\delta^2},
 \quad
 |c_j|\le p_j\le
 (1+\delta^2)^{(m-1)/2}\sqrt{|c_j|^2+\delta^2}.             \tag{9}
\]
The lower product inequality is tree Cauchy in that sector.
Every \(a_{v,j}\) is positive, even when \(c_j=0\), since its
original block was nonzero and every applied gauge is invertible.

The accumulated edge gauge and its inverse have norm at most
\(e^{\mathcal L}\). Applying the inverse gauges to a local tensor
and using (2) consequently also gives
\[
                         |\log a_{v,j}|\le m\mathcal L.   \tag{10}
\]
This lower bound is the step that makes finite scalar balancing
uniform at the zero-output sectors.

## 3. Scalar balancing and the metric radius

Within sector \(j\), prescribe the logarithmic vertex rescalings
\[
                \lambda_{v,j}
                 =\frac1m\log p_j-\log a_{v,j}.           \tag{11}
\]
Their sum is zero and \(|\lambda_{v,j}|\le2m\mathcal L\).
For an edge, assign the scalar gauge whose logarithm is the sum
of \(\lambda_{v,j}\) over the subtree below it. The incidence
identity on a rooted tree makes the resulting logarithmic change
at each vertex exactly \(\lambda_{v,j}\), including at the root.
Each edge scalar and its inverse are bounded by
\(\exp(2m^2\mathcal L)\). No scalar is defined from \(c_j^{-1}\).

After balancing, every local norm in sector \(j\) equals
\(p_j^{1/m}\). Hence the whole product is exactly
\[
                F_{\rm bal}
                  =\left(\sum_jp_j^{2/m}\right)^{m/2}.     \tag{12}
\]
Let \(S=\sum_j|c_j|^{2/m}\ge1\), using \(c_1=1\).
Concavity and (9) give
\[
 \begin{split}
 \log F_{\rm bal}-\log C_{\rm block}
 &\le\frac{m-1}{2}\log(1+\delta^2)
       +\frac m2\log\left(1+\frac{r\delta^{2/m}}S\right)\\
 &\le\frac{m(r+1)}2\delta^{2/m}=\eta .
 \end{split}                                               \tag{13}
\]
Here \((x+\delta^2)^{1/m}\le x^{1/m}+\delta^{2/m}\),
\(0<\delta\le1\), and \(\delta^2\le\delta^{2/m}\).
This estimate includes every zero \(c_j\).

The final full edge gauge and its inverse have norms at most
\(\exp[(1+2m^2)\mathcal L]\). Its polar metric \(H_e=g_e^*g_e\)
remains block diagonal. Removing the edge unitary factors preserves
all local norms and the original source. Therefore
\[
 Z(H)\le(1+2D_N)\exp[2(1+2m^2)\mathcal L].                \tag{14}
\]
Equations (12)--(14) prove (7).

## 4. The restricted regularized minimum

Keep exactly the regularizer of [R], and define
\[
 J_{N,\varepsilon}(H)=L_N(H)+\varepsilon\log Z(H),
 \qquad 0<\varepsilon\le1.                               \tag{15}
\]
Restrict all edge matrices to the positive block-diagonal cone.
This cone is geodesically stable. The strict geodesic convexity and
coercivity proof of [R] applies on it: \(L_N\ge\log C_{\rm block}\),
and a bound on \(Z\) bounds every metric eigenvalue and reciprocal.
Thus the restricted objective has a unique minimizer
\(H^{\rm block}_{N,\varepsilon}\).

Use the finite competitor (7) with \(\eta=\varepsilon\).
The lower bound \(L_N\ge\log C_{\rm block}\) then proves
\[
 \boxed{\begin{split}
 \log Z(H^{\rm block}_{N,\varepsilon})
       &\le1+A_{\rm block}(B,D_N,\varepsilon),\\
 0\le \min_{\rm block}J_{N,\varepsilon}
             -\log C_{\rm block}
       &\le\varepsilon[1+A_{\rm block}(B,D_N,\varepsilon)] .
 \end{split}}                                             \tag{16}
\]
Each optimizing eigenvalue and its reciprocal are bounded by this
\(Z\). For \(\varepsilon_N=N^{-2}\), (3) and (6) give
\[
 \sup_e\|\log H^{\rm block}_{e,N}\|_{\rm op}=O(N),\qquad
 \min_{\rm block}J_{N,\varepsilon_N}
                         =\log C_{\rm block}+O(N^{-1}).   \tag{17}
\]
Constants depend on the fixed actual tree and word, not on which
individual color values happen to vanish.

For the unrestricted positive cone, use the same objective (15).
Since it contains the block cone, [C,M] give
\[
 \boxed{\quad
 0\le\min_{\rm block}J_{N,\varepsilon_N}
           -\min_{\rm full}J_{N,\varepsilon_N}
       \le\frac{m-1}{2}\log r+O(N^{-1}) .
 \quad}                                                    \tag{18}
\]
Here the full cone is on the same selected-color compiler.
Its minimum is at least \(\log\|Y_{\mathcal J,N}\|\), while
\(\|Y_{\mathcal J,N}\|\le C_{\rm block}
\le r^{(m-1)/2}\|Y_{\mathcal J,N}\|\) by [M, (17)].
Thus color mixing changes neither the leading variational rate nor
the leading logarithmic output norm:
\[
 \frac{2\pi}{N}\min_{\rm block}J_{N,\varepsilon_N}
           -\frac{2\pi}{N}\log\|Y_{\mathcal J,N}\|
                                      \longrightarrow0.
                                                               \tag{19}
\]

## 5. Two actual colors suffice for a positive target rate

In particular take the two original main colors
\(\mathcal J=\{1,N\}\). Their selected output is exactly
\[
 Y_{\{1,N\},N}=(1,K_N),\qquad
 C_2=(1+|K_N|^{2/m})^{m/2},\qquad
 \sqrt{1+|K_N|^2}\le C_2
       \le2^{(m-1)/2}\sqrt{1+|K_N|^2}.                   \tag{20}
\]
Equations (16)--(17) become
\[
 \min_{\rm block}J_{N,N^{-2}}=\log C_2+O(N^{-1}),\qquad
 \sup_e\|\log H^{\rm block}_{e,N}\|_{\rm op}=O(N).        \tag{21}
\]
For every \(V>0\) this gives the exact target equivalence
\[
 \lim_N\frac{2\pi}{N}\min_{\rm block}J_{N,N^{-2}}=V
 \quad\Longleftrightarrow\quad
 \lim_N\frac{2\pi}{N}\log|K_N|=V .                       \tag{22}
\]
Indeed \(\log C_2\) differs from
\(\max(0,\log|K_N|)\) by at most \((m/2)\log2\).
A strictly positive limiting rate removes that maximum and implies
eventual nonvanishing. This argument needs no estimate for the other
ordinary-color remainder.

Each internal edge here is two copies of the raw physical operator
space \(\operatorname{End}(V_{j,N}^{\otimes b})\), of total dimension
\(2N^{2b}\). These are two actual main-color sectors, with the original
crossings and root readouts. They are not a newly appended constant
coordinate. The orthogonally anchored Conway construction [A] already
has output \((1,K_N)\) in a different, smaller boundary presentation.
No new anchoring principle or improvement of its dimension is claimed.
The new assertion is finite controlled-window near-attainment of
the exact sector infimum and its regularized consequence.

There is also a direct comparison with [A]'s fixed-degree quartic
minimum \(Q_N\) for the same original Conway source. That theorem gives
\(1+|K_N|^2\le Q_N\le(1+1/N)(1+|K_N|^2)\). With
\(j_{2,N}=\min_{\rm block}J_{N,N^{-2}}\), equations (20)--(21) imply
\[
 -\tfrac12\log(1+1/N)
 \le j_{2,N}-\tfrac12\log Q_N
 \le\tfrac{m-1}{2}\log2+O(N^{-1}).                       \tag{23}
\]
This is a bounded additive difference of logarithmic values.
It identifies neither minimizers nor pointwise objectives.

For all \(N\) colors the output remains the one in [C],
\(\|Y_{\{1,\ldots,N\},N}\|^2=|K_N|^2+R_N\), with its original
polynomial ordinary-color remainder. No original source value changes
when that larger selected set is used instead.

## 6. Scope of the reduction

The new conclusion is a finite-window realization and regularized
version of the sector infimum already proved in [M, Section 5].
The normalizing directions are exact open source packets, and the
balancing scalars use actual finite local tensor norms. This is not
a construction of those directions from a classical angle structure.
The original cap stays at the root, and a zero complete-color value
is permitted throughout.

The restricted minimizer is not asserted to equal the full minimizer.
Pinching an arbitrary gauge is not asserted to improve the objective.
Restricted stationarity controls only the permitted block variations;
it does not imply the full marginal balance of [C,R]. No within-color
dimension reduction, principal-symbol limit, interchange of an
infimum and a limit, or geometric noncancellation follows.

All statements concern the raw multiplication tree of a fixed completed
one-component knot. Proper packets are invertible word operators;
arbitrary Conway packets or components containing internal partial
traces need not have this property. Constants may depend on the fixed
word, filling assignment and braid width. No uniformity in unbounded
word length, or anchor for an unfilled auxiliary link, is asserted.
There is no new volume identity or finite-exception theorem.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| M | [Metric compactness and sector infima](research_regularized_source_metric_compactness.md) | 337 | fd8dae7561eff37089e8481b4eb8c8344acb56da86b502350292f6d2be9c8818 |
| R | [Regularized actual-source problem](research_regularized_actual_source_capacity.md) | 377 | 0cea0d52182eb24b4610538f354dbe5158fa54aa6f9cf7f9fc280c72ab090ff8 |
| C | [Actual all-main-color tree capacity](research_scalar_tree_full_gauge_capacity.md) | 466 | 2997b732aa73e063c66e81d6487a1d9927509609d61842c1dbb43d9345df1d6d |
| A | [Earlier anchored Conway source](research_anchored_conway_positive_variational_period.md) | 392 | e83c35d16c79faa13ac6556db78b9b57da2a2371d3fc04c4673ecd74e1d336f7 |

Only written mathematics, text reads and metadata operations were used.
Earlier final notes, the progress ledger and public manuscripts are unchanged.
