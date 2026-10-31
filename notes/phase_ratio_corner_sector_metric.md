# A tame phase-ratio projector on the actual doubled corner sector

29 October 2026. This is a boundary metric theorem for the original
normalized Fermat cap, with all source normalizers retained. On its
selected doubled clock sector, every flat orthogonal projector is
exactly contractive for real cap parameters and polynomially bounded
throughout a fixed complex cap disk. It does not prove that an
interior crossing preserves that sector, or identify the character
constraints of a triangulation edge.

## 1. The actual source and its periodic positive metric

Let N>=2, d=N-1, Q=exp(2pi i/N), and 0<|epsilon|<=rho=1/16. Use
the marked root

    delta=(1-epsilon)^(1/N), u=Q^(-j)delta, v^N=epsilon,
    0<=j<N.                                                     (1)

Any marked Nth root v is allowed. In the literal cap orientation,

    P_a=v^a/product_(r=1)^a(1-uQ^r),
    L_a=v^(-a)product_(r=0)^(a-1)(1-uQ^r),  0<=a<N,
    h_a=|L_a|/|P_a|.                                           (2)

These are the original source frames of
[the source-balanced Gram theorem](phase_ratio_bell_weights_and_source_gram.md).
Because 1-u^N=v^N, both P and L, and hence h, extend N-periodically.
Their EXACT recurrence is

    h_(a+1)/h_a=|1-uQ^a| |1-uQ^(a+1)|/|v|^2.                   (3)

For j>=1 the actual cap normalization is

    Phat_a=v^(N-j)P_a/alpha_j,
    Lhat_a=v^j L_a/beta_j,
    alpha_j=F_(N-j), beta_j=N/F_(d-j),
    F_r=product_(k=1)^r(1-Q^k),
    alpha_j beta_j=N(1-Q^(-j)).                                 (4)

For j=0 retain P,L unchanged. Consequently the actual balanced
metric Hhat=diag(|Lhat_a|/|Phat_a|) is a single positive scalar
multiple of H=diag(h_a). The scalar in question is exactly
|v|^(2j-N)|alpha_j/beta_j|; it has NOT been assumed tame or omitted
from the original source. It cancels in every operator norm below.

The literal source cost is still

    Phat^* Hhat Phat=Lhat Hhat^(-1)Lhat^*
       =|epsilon| |1-u|/[N|1-Q^(-j)|]
                           sum_a 1/|1-uQ^a|,   j>=1,            (5)

and |1-u| sum_a 1/|1-uQ^a| for j=0. In particular it is bounded
by C(1+|epsilon|(1+log N)), as proved in the linked Gram note.
No normalizer has been replaced by a chosen unit source.

At fixed N, Phat and Lhat both tend to the coordinate corner e_j
as epsilon tends to zero on their marked root cover. For the
resonant entry of Phat, (1-delta)/epsilon tends to 1/N and the
remaining denominator factors together with F_(N-j) multiply to N.
For Lhat, its j-th numerator is exactly beta_j at epsilon=0.
Every other entry has a strictly positive residual power of v.
The j=0 assertion follows directly from (2).

## 2. The doubled sector and the exact projector criterion

Give the doubled head the product metric G=H tensor H. Its clock
sum sectors are

    V_s=span{|a,s-a mod N>:0<=a<N},
    G|_(V_s)=diag(g_a), g_a=h_a h_(s-a).                         (6)

The original conjugate double may equivalently be written using
the source-exact antiunitary reflection of
[the reflection theorem](phase_ratio_double_and_fermat_source.md).
That reflection preserves h and adds only its specified diagonal
unitary chirp. Thus it has the same metric (6), and the doubled
corner e_j tensor bare_j belongs to V_(2j mod N).

The clock-sector projector is diagonal and commutes with G, so
it is contractive on the entire doubled space. Inside V_s the
phase-ratio shift S^(-1) tensor S has the Fourier eigenvectors

    w_(s,r)=N^(-1/2)sum_a Q^(ra)|a,s-a>, 0<=r<N.

Unit-modulus scalar marks change the eigenvalues, not these
projectors. A rank-one flat character projector Pi_(s,r)=w w^*
has the EXACT restricted metric norm

    ||Pi_(s,r)||_G
       =[(N^(-1)sum_a g_a)(N^(-1)sum_a g_a^(-1))]^(1/2).        (7)

Indeed a rank-one map xy^* has weighted norm
||G^(1/2)x|| ||G^(-1/2)y||. Formula (7) is independent of r and
equals one precisely when g is constant.

More generally, a flat orthogonal projector Pi is contractive in
a positive metric G precisely when [Pi,G]=0. Necessity follows
by applying contractivity to x+t y with x in its range and y in
its kernel, and varying complex t: it forces their G-orthogonality.
Sufficiency follows by the resulting orthogonal splitting. In
general ||Pi||_G<=sqrt(cond G).

## 3. Exact contractivity and its complex extension

**Theorem.** For the actual normalized cap (1)--(4), every flat
orthogonal projector whose range and domain lie in V_(2j mod N)
satisfies

    ||Pi||_(Hhat tensor Hhat)
           <=exp[8|epsilon|(1+log N)]
           <=e^(8rho)N^(8rho).                                 (8)

Here the norm means the restriction to that sector, or equivalently
the extension by zero on its orthogonal complement. If epsilon
is real, the norm of every nonzero such projector is EXACTLY one.
In particular this applies to all shift-character projectors and
their orthogonal sums on the selected doubled corner sector.

Proof. Put z_k=|1-delta Q^k|, periodically in k. Applying (3) to
the two reflected indices gives, for 1<=ell<N,

    g_(j+ell)/g_j
       =(z_ell/z_(-ell))
                     product_(k=1)^(ell-1)(z_k/z_(-k))^2,
    g_j=h_j^2,  s=2j mod N.                                   (9)

The potentially arbitrarily small resonant chord z_0 cancels
EXACTLY. If epsilon is real then delta is real and positive,
including when epsilon<0 and delta>1. Thus z_k=z_(-k) and every
g_a=h_j^2. The metric is scalar on this sector, proving exact
contractivity without a limiting argument.

For complex epsilon the marked logarithm gives
|delta-1|<=2|epsilon|/N. For k!=0 mod N, with m=min(k,N-k),

    |1-Q^k|>=4m/N,
    |z_(+/-k)/|1-Q^k|-1|<=|epsilon|/(2m)=:t_k<=1/32.

It follows that

    |log(z_k/z_(-k))|
       <=log((1+t_k)/(1-t_k))<=3|epsilon|/(2m).                 (10)

Since sum_(k=1)^(N-1)1/min(k,N-k)<=2(1+log N), equations (9)--(10)
give

    |log(g_a/h_j^2)|<=8|epsilon|(1+log N).

Thus the restricted condition number is at most
exp[16|epsilon|(1+log N)]. The general projector estimate of
section 2 proves (8). Replacing H by Hhat only multiplies the
doubled metric by a common positive scalar, so the proof retains
all alpha,beta factors in (4). This also proves uniformity for
epsilon depending arbitrarily on N, even exponentially close to
zero. If |epsilon|log N tends to zero, the upper bound tends to one.

The opposite root orientation follows by Q->Q^(-1) and the
corresponding reflected cap labels; the same real chord estimates
and source normalization proof apply.

## 4. Exact scope at the original source

The theorem controls a genuine boundary sector selected by the
original corner limit, not an arbitrarily chosen geometric sector.
For epsilon!=0 the complete cap column has nonzero entries in
every coordinate, so its conjugate double also has other V_s
components. These components cannot be discarded inside a Cauchy
cap contour. A general V_s has the exact norm (7), with no scalar
metric conclusion unless its own reflected products are constant.

Nor has a crossing been proved to preserve the local sector
s=2j, or a change to an adjacent Fermat chart proved contractive
in this metric. Global total-degree conservation does not imply
those local assertions. If a specified physical/edge projector
acts inside the selected sector as a flat orthogonal projector,
(8) bounds that projector with the actual cap metric. Identifying
all interior edge projectors and controlling their intervening
transport remain separate requirements. All off-Fermat beta
currents and both Bell half-phase chambers of the linked notes
remain in the complete original source.

## 5. Independent finite audit

[The audit](../experiments/audit_phase_ratio_corner_sector_metric.py)
checks the literal normalized frames, the alpha beta product,
periodic recurrence, reflected product (9), and all cap labels
at a range of levels and real/complex cap parameters. It also
compares (7) with direct weighted singular values of character
projectors and their nontrivial sums. The tests include cap
parameters exponentially small in N; none substitutes epsilon=0
before constructing the metric. The accompanying result file is
written only after all assertions pass.

The phase-ratio checks do not establish preservation of the interior domain.