# An exact scalar cyclic-dilogarithm network for the original knot source

The subsequent
[continuous Gaussian theorem](actual_continuous_gaussian_cyclic_network.md)
completes this construction: its exact original-source period has
ordinary Gaussian weights and no finite Gaussian scalar kernel either.
The intermediate construction below retains the finite Gaussian
while proving the cyclic/Hardy support and initial-cycle identities.

28 October 2026. For every actual signed braid word, the scalar
Euler/Gaussian Cauchy representation can be replaced by one using
**the literature norm-one cyclic dilogarithm, its inverse, ordinary
Hardy Cauchy kernels, and the full finite marked Gaussian**.
All finite Dirichlet numerators and all scalar finite Euler
polynomials are absent from this presentation. The original period,
including its source and peripheral/framing line, is exactly unchanged.

This is an exact function-and-cycle representation, not a replacement
of the invariant by a positive model or an asymptotic substitution.
The initial cycle and every norm root are specified below. Moving
that cycle to a geometric Rivin chain remains unproved.

The [audit](../experiments/audit_actual_cyclic_hardy_dilog_network.py)
and [results](../experiments/actual_cyclic_hardy_dilog_network_results.json)
check the full literature normalization, nonzero added cyclic tails,
both actual signed crossings, and sixteen original whole-word
pivotal contractions. Exact rational radius chambers are checked
independently of those finite-field identities.

## 1. Fix the literature normalization as a function

Let $Q=e^{2\pi i/N}$, $N\ge2$. Use precisely the alternate
literature cyclic dilogarithm from
[four_cyclic_atoms.md](four_cyclic_atoms.md):

$$
 \mathcal V_N(t)=
 (1-t^N)^{(N-1)/(2N)}
       \prod_{\ell=1}^{N-1}(1-Q^\ell t)^{-\ell/N},
 \qquad
 \mathcal U_N(t)=\mathcal V_N(t)^{-1}.                 \tag{1}
$$

Every power is the analytic branch equal to one at $t=0$.
In particular the full factor $(1-t^N)^{(N-1)/(2N)}$ is
retained. This is the normalized function $\mathfrak d_N$,
not the unnormalized weighted product often denoted $D_N$.
Even-level half roots use this same anchor.

On $|t|<1$ its convergent logarithm is exactly

$$
 \log\mathcal V_N(t)=
   \sum_{\substack{m\ge1\\N\nmid m}}
        \frac{t^m}{m(Q^m-1)}.                        \tag{2}
$$

Indeed $\sum_{\ell=1}^{N-1}\ell Q^{\ell m}
=N/(Q^m-1)$ at nonresonant degrees. At $m=Nk$ the
norm factor in (1) cancels the resonant logarithm of the
weighted product. Thus

$$
 \prod_{j=0}^{N-1}\mathcal V_N(Q^jt)=1               \tag{3}
$$

on the anchored component.

For the ACTUAL finite Euler polynomials

$$
 u_N(t)=\sum_{h=0}^{N-1}t^h/F_h,\quad
 v_N(t)=\sum_{h=0}^{N-1}
            (-1)^hQ^{h(h-1)/2}t^h/F_h,
$$

comparison of their nilpotent logarithms gives

$$
 \mathcal U_N(t)-u_N(t)\in t^N\mathbb C[[t]],\qquad
 \mathcal V_N(t)-v_N(t)\in t^N\mathbb C[[t]].          \tag{4}
$$

This finite-jet observation alone is not a period theorem.
The ordered support argument below proves where ALL the
additional coefficients disappear in the actual source.

## 2. Three different support mechanisms

Work on nonnegative polynomial heads and use the Hardy Cauchy
kernel $K_+(t)=1/(1-t)$, as in
[the exact Hardy replacement](actual_hardy_cauchy_network.md).
Keep the original strict crossing order and original coefficients.

### Transfer atoms

Before EVERY transfer in the strict actual crossing and boundary
fusion words, both active indices lie in $0,\ldots,N-1$.
For a transfer $J_-\otimes J_+$, every added power of order
$h\ge N$ lowers the first index below zero. Hardy projection
annihilates it. The reversed transfer has the same property
on its second index. Therefore

$$
 \mathcal U_N(x^{-1}J_-\otimes J_+),\quad
 \mathcal V_N(x^{-1}J_-\otimes J_+)
$$

act exactly as the original finite transfer atoms on these
actual inputs. The infinite series terminates on each such
input by its LOWERING head; no upper truncation is imposed.

### Reciprocal factorial diagonals

The scalar kernel $u_N(z/w)$ is replaced by
$\mathcal U_N(z/w)$ at $|z/w|<1$. It now has genuinely
nonzero diagonal coefficients at indices above the original
head. However, the active input of every reciprocal-factorial
diagonal in the strict word is already in the head:

- the initial second head of inverse fusion is in the head;
- after its lowering transfer the first head is still in it;
- in the final fusion, the central transfer has only lowered
  its second head.

Thus none of the added diagonal coefficients is ever used.

### Positive factorial diagonals

The actual factorial kernel is

$$
 \sum_{a=0}^{N-1}F_a t^a=N t^{N-1}v_N(Q/t).
$$

Replace it by the full Laurent function

$$
 \mathcal F_N(t)=N t^{N-1}\mathcal V_N(Q/t),
 \qquad |t|>1.                                      \tag{5}
$$

Its powers $t^a$ for $0\le a<N$ have exactly the original
coefficients $F_a$. It has NO power $t^a$ with $a\ge N$.
All added terms have $a<0$.

In a diagonal Cauchy contraction, a term $t^a=(z/w)^a$
can pair only with input index $a$. Nonnegative polynomial
inputs therefore do not see any of the added negative powers.
Consequently (5), despite being a different scalar function,
acts **exactly as the original finite factorial diagonal on
all nonnegative polynomial inputs**. In particular it still
kills every upper overflow. All factors $N$ and
$t^{N-1}$ in (5) are retained.

## 3. The support induction is simultaneous, not a circular assumption

Let $\mathcal F$ denote the operator represented by (5), and
let $\mathcal F^{-}$ be the operator with scalar kernel
$\mathcal U_N(z/w)$. On head inputs use the completed fusions

$$
\begin{split}
 \mathcal C&=\mathcal F_2\,
       \mathcal U_-(x)\,\mathcal F_1\,\mathcal F_2^{-},\\
 \overline{\mathcal C}&=\mathcal F_2\mathcal F_1^{-}
       \mathcal V_-(x)\,\mathcal F_2^{-}.
\end{split}                                                   \tag{6}
$$

Starting from a head input, the first reciprocal diagonal in
$\overline{\mathcal C}$ has a head input. Its transfer lowers
the first index, so all added powers vanish and the first
index remains in the head. The next reciprocal diagonal is
therefore also exact. The last positive factorial kills any
second-index overflow. This proves

$$
 \overline{\mathcal C}i=iC^{-1}.                     \tag{7}
$$

For $\mathcal C$, its first reciprocal diagonal is exact on
a head second index. The positive factorial on head one
enforces that head's support BEFORE the transfer. The
transfer is then exactly finite, and the last positive
factorial kills its possible second-head overflow.
Moreover $\mathcal C$ kills any nonnegative input outside
the head pair: an oversized first index is killed before
transfer; an oversized second index can only increase
before the final factorial kills it.

Hence $\mathcal C=P\mathcal CP$ and $\mathcal Ci=iC$.
The central transfer in either signed crossing receives
a head input by (7); its added high powers vanish. Its
possible first-head overflow is killed by $\mathcal C$.
The full marked Gaussian is kept exactly as before.
Therefore the two completed signed operators satisfy

$$
 \boxed{\qquad
 \mathcal R_\pm i=iR_\pm.
 \qquad}                                             \tag{8}
$$

The same proof applies to the typed unequal-color formula,
using the original input/output fusions and its prescribed
Euler argument. No common Cartan scalar is reset.

By induction, for EVERY signed word, with any original
finite-head coupons BETWEEN complete crossings,

$$
 \mathcal W(\beta)i_b=i_bW(\beta).                    \tag{9}
$$

This includes the full original source and Hopf Ward pairings.
It does not authorize arbitrary insertions between factors
inside (6), nor infer a source identity for an independently
chosen cyclic/geometric sector.

## 4. A simultaneous, explicit initial radius chamber

The scalar kernels in this representation are:

$$
\begin{array}{c|c}
\text{factor}&\text{active scalar function}\\ \hline
\text{transfer}&
 \mathcal U_N(x^{-1}w_j/w_i)
 \text{ or }\mathcal V_N(x^{-1}w_j/w_i)\\
\text{reciprocal factorial}&\mathcal U_N(z_i/w_i)\\
\text{positive factorial}&
 N(z_i/w_i)^{N-1}\mathcal V_N(Qw_i/z_i)\\
\text{Gaussian}&\Gamma_{\pm,N}(z_i/w_i)
\end{array}                                                   \tag{10}
$$

Every spectator contributes $K_+(z_j/w_j)$.
Transfers also have Hardy kernels on their active heads.
The complete finite Gaussian is retained, with its marked
meridian powers and chirp; it is not replaced by a guessed
Gaussian branch.

Fix $0<\rho<1$, for example $\rho=1/16$, and a positive lower
bound $\lambda$ for all active color moduli on the selected
meridian chart. Insert one identity Hardy layer before EACH
elementary factor. This preserves the exact polynomial operator.
Let $R_j>0$ be the preceding output radii, $r_j$ the reset
layer's output radii, and $s_j$ the factor's output radii.
The finite set of required inequalities is

$$
\begin{array}{c|l}
\text{reset}&r_j/R_j<\rho\quad\text{for all }j\\
\text{transfer}&r_j/r_i<\rho\lambda,\quad
                         s_h/r_h<\rho\quad\text{for all }h\\
\text{reciprocal factorial on }i&
                         s_h/r_h<\rho\quad\text{for all }h\\
\text{positive factorial on }i&
                         r_i/s_i<\rho,\quad
                         s_h/r_h<\rho\ (h\ne i)\\
\text{Gaussian on }i&
                         s_i>0,\quad s_h/r_h<\rho\ (h\ne i).
\end{array}                                                   \tag{11}
$$

They always have a simultaneous solution. Inductively put
$r_h=\rho R_h/2$. Before a transfer, decrease its numerator
radius further, if needed, to

$$
 r_j\le\frac{\rho\lambda}{2}r_i.
$$

Put $s_h=\rho r_h/2$ except at an active positive factorial,
where set $s_i=2r_i/\rho$, and at an active Gaussian, where
set $s_i=r_i$. Every inequality in (11) is then strict.
The construction proceeds forward in word time; there is
no terminal-to-initial Hardy inequality.

All cyclic atom arguments are in $|t|<\rho$, so their branches
are exactly those of (1). The reflected factorial is expanded
at its specified infinity sector. Every scalar series is
uniformly absolutely convergent on the compact product tori.
Termwise constant-term extraction and composition are justified.
Thus the operator proof yields a genuine compact Cauchy-cycle
identity, not only a formal equality of jets.

For a fixed meridian compact chart with nonzero colors,
these radii and strict margins can be chosen independently
of $N$. The number of reset layers and integration variables
depends on the fixed word and bridge count, not on $N$.

## 5. The original fixed charged period

Use the existing full fused-plat source

$$
 P_{\beta,N}=\chi_{\beta,N}N^{1-k}
   \langle e_{\rm out},B_\beta e_{\rm in}\rangle,
$$

with its specified $(d,0)$ input pairs, $(0,d)$ ordinary
output pairs and $(d,0)$ marked output pair. The full-word
Ward corner is used only after assembly, as in its original
proof. Expand $B_\beta$ into the actual factors, replace them
by (10), and insert the reset identities above.

If the resulting scalar kernels are $\mathcal K_\ell$, the
same ORIGINAL period is exactly

$$
 \boxed{\quad
 P_{\beta,N}=\chi_{\beta,N}N^{1-k}
 \operatorname{CT}
   (z^0)^{a_{\rm in}}(z^{L})^{-a_{\rm out}}
                \prod_{\ell=1}^{L}
                  \mathcal K_\ell(z^\ell,z^{\ell-1}).
 \quad}                                                \tag{12}
$$

Its contours are the product circles just constructed, with
the anchored lifts from (1). All original peripheral,
Cartan, pivot and framing factors are included exactly once.
The equality holds at all primitive levels, even or composite,
and in the original root-meridian family.

Consequently any specified root-specialized quantum A-operator
annihilating that original meridian period also annihilates
(12), with its full peripheral factors. This is equality of
the selected function, not a new assertion identifying an
operator's classical symbol with the geometric A-polynomial.

There are no scalar finite $u_N/v_N$ truncations and no
finite Dirichlet numerator factors in (12). This does not
erase boundary information: it specifies which global
functions and initial cycle reproduce that information.
Their norm divisors and matched residue/branch corrections
must be retained in any subsequent contour transport.

The integer source charge is unchanged: total plat degree
is $k(N-1)$, and after the ordinary caps the remaining pair
has $D+1=N$. That is the actual cap charge. Equation (12)
does not identify an unassigned geometric Pachner edge with
that class.

### An exact internal three-index charge is already available

There is also a genuine internal affine charge in this particular
network. In (5), a nonnegative head index $a$ and the selected
cyclic Taylor index $r$ satisfy exactly

$$
 a+r=N-1,\qquad a+r+1=N.                             \tag{13}
$$

The $+1$ is forced by the original reflected monomial
$t^{N-1}$, not chosen by a flattening convention.
For an actual fusion coefficient write

$$
 h=a-u=v-b,\qquad r_1=N-1-a,\qquad r_2=N-1-v.
$$

The two positive-factorial kernels in that fusion then give

$$
 \boxed{\quad
 (u+1)+h+r_1=N,\qquad (b+1)+h+r_2=N.
 \quad}                                             \tag{14}
$$

All entries are nonnegative, and the first entry of each
triple is positive. Interior routes with $h,r_i>0$ give
strictly positive triples. The inverse fusion retains the
second equation, from its positive output factorial.

Thus actual fusion-network clocks can form an exact
three-index charge-one sector, with its original affine shift.
This is a more specific dictionary than total-degree conservation
alone. It does not yet identify either triple in (14) with the
three angles around the last geometric Pachner edge. Such an
identification must come from the typed five-term/source map,
not from renaming these index variables.

The remaining conjectural step is therefore genuinely global:
transport this marked scalar cyclic-dilogarithm/Gaussian
cycle to the positive ideal geometric chain, with all norm
divisors, compatible root frames and original source charges
retained, and prove its geometric coefficient and dominance.
No such transport or volume limit is inferred from the
exact identity (12).

In the stronger continuous version just linked, the Gaussian is
also an ordinary integral over a specified fibered Cauchy cycle.
Joint absolute convergence and uniform initial-cycle leading
symbols are proved there. The remaining global-cycle statement
is unchanged; a finite Gaussian endpoint sector is no longer
an unresolved part of the scalar representation.
