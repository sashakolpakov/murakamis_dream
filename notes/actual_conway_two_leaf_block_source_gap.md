# A whole-source gap from exact two-leaf Conway block transport

31 October 2026. Internally reviewed original-source theorem.
For every fixed closed $C(FG)$ built from seeds $A_s=h^s$, $s\ge2$,
actual turns and products, the full mixed source has a uniform alias gap
and a physical-color complement gap at both parities. No individual-leaf
certificate is required. The proof combines the exact finite contraction
below with the [uniform two-leaf block lemma](actual_conway_uniform_two_leaf_block_alias_gap.md),
whose exact rational certificate supplies a margin greater than $1/100$.
All Hermite normal directions, physical colors, phases and original targets
are retained. Isolated $C(A_2)$ remains excluded.

## 1. Original algebra and exact alias provenance

Put d=N-1, M=floor(d/2), q=exp(pi i/N), kappa=q^(d^2/2), and use the full
physical algebra H_N=C[z]/(2T_N(z/2)+2). Its normalized Newton basis is Bhat_r,
0<=r<=d, with sine factorial s_r=product_(u=1)^r 2sin(pi u/N).
The genuine turn T and marked cylindrical functional obey

$$
T\widehat B_r=\widehat B_{d-r},\qquad
\phi(\widehat B_i\widehat B_j)=\begin{cases}1&i+j=d,\\0&i+j\ne d.\end{cases}\tag{1}
$$

The EXACT full-algebra product is

$$
\begin{aligned}
\widehat B_i\widehat B_j&=\sum_{r=\max(i,j)}^{i+j}\mu_{i,j,r}\widehat B_r,\\
\mu_{i,j,r}&=\frac{s_{i+j}s_r}{s_i s_j s_{r-i}s_{r-j}s_{i+j-r}}>0,
\qquad i+j\le d.
\end{aligned}\tag{2}
$$

and is zero for i+j>=N. The latter is polynomial divisibility with node
multiplicities, so it does not discard Hermite normals. Formula(2) applies
to arbitrary i,j, including an input above M; no new product rule is used
for aliases.

For each actual auxiliary color 1<=j<=N, let the pure leaf have the exact
split h_j=C_j+A_j. For j=N-h, 0<=h<=M,

$$
C_j=\sum_{v=h}^{M}\frac{N^2s_{2v}}{s_v^2s_{v-h}s_{v+h}}\widehat B_v,
\qquad A_j=(-1)^N h_h,\qquad h_0=0.\tag{3}
$$

For j<=floor(N/2), C_j=0 and A_j=h_j. In particular A_N=0. In every case
A_j lies in span{Bhat_v:v>=ceil(N/2)}, with each coefficient bounded byN/2
in modulus. More precisely, for 1<=h<=floor(N/2),

$$
h_h=\sum_{t=0}^{h-1}(-1)^{h-1+t}b_{h,t}\widehat B_{d-t},\qquad
b_{h,t}=\frac{s_t^2s_{h+t}}{s_{2t+1}s_{h-t-1}}>0.\tag{4}
$$

These identities include every original auxiliary pivot, with no extra1/j
or1/N factor. They are the actual complete-circle source identities, not
spectral values with a guessed normal completion.

For epsilon=+-1 define the original half-twist transport

$$
\begin{aligned}
T_\epsilon(f)&=T\bigl(R^\epsilon T(f)\bigr),\\
T_\epsilon(\widehat B_v)&=\kappa^\epsilon(-1)^v
\sum_{r=0}^{v}q^{\epsilon v(r+1)}\binom vr_q\widehat B_r,\\
\binom vr_q&=\frac{s_v}{s_r s_{v-r}}.
\end{aligned}\tag{5}
$$

For epsilon=0 use the identity. Set C_j^epsilon=T_epsilon(C_j) and
A_j^epsilon=T_epsilon(A_j). Thus the changed physical leaf is EXACTLY
C_j^epsilon+A_j^epsilon=T(R^epsilon L_j), in the entire algebra.
The core has support r<=M at every sign; an odd alias may have any0<=r<=d.
The color-specific alias formula is the finite sum of (4) and (5), with
all their signs and q phases retained.

A useful exact warning is visible already at h=1: h_1=Bhat_d and
[d choose r]_q=1. Consequently T_epsilon(h_1) has a nonzero modulus-one
coefficient at EVERY r (apart from its unit kappa factor). Its square has a
nonzero constant coefficient, namely the square of that constant. More
generally the product for either pair of odd signs has a nonzero constant.
A pure alias h_1 times an odd alias has its nonzero r=d coefficient.
Only the two-pure-alias product vanishes by the genuine nilradical square.
Thus an arbitrary signed A2 block cannot discard its double-alias sector.

## 2. Exact block kernel and supports

For arrays u_i,v_j in the same full Newton basis define

$$
\begin{aligned}
(u\star v)_r&=\sum_{(i,j)\in D_N(r)}\mu_{i,j,r}u_i v_j,\\
D_N(r)&=\{0\le i,j\le d:i+j\le d,\ \max(i,j)\le r\le i+j\}.
\end{aligned}\tag{6}
$$

For an A2 seed with actual independent physical colors and signs, its exact
four sectors are CC,AC,CA,AA under this kernel. Every seed coefficient is
the sum of those sectors; no nilradical quotient or covariance of a
projected coupon is being invoked. A CC sector restricts i,j<=M. An AC
sector restricts only its core index<=M; a pure alias further restricts its
own index>=ceil(N/2). An AA sector must still satisfy i+j<=d. In particular
TWO inputs above half cannot survive together, but ONE such input is allowed.

The same kernel applies at every higher product, independent of whether its
inputs already contain aliases or have been turned. A macro-turn reverses
its COMPLETE coefficient array: u_r becomes u_(d-r), with no extra phase.
At the root C(FG), equation(1) contracts precisely the pairs i+j=d. These
rules propagate every original sector and target through any finite tree.
They never introduce one variable per repeated occurrence of a wire.

Grouping the two leaves and their one gate as (6) is just associating finite
sums, not a change of tangle or a replacement source. Higher products and
turns remain the original physical operations. The inside gate appears
exactly once, the two circle factors remain exactly once each, and the
single global marked closure is unchanged.

## 3. Uniform closed-domain envelopes, including inputs above half

Use the ORIGINAL local upper rates

$$
\begin{aligned}
\widetilde g(x)&=g(\max(x,1/4)),\quad0\le x\le1/2,\\
k(x)&=-2J(x/2),\quad0\le x\le1,\\
J(x)&=\int_0^x\log(2\sin(\pi t))\,dt,\qquad g(x)=J(2x)-4J(x).
\end{aligned}\tag{7}
$$

Uniformly over all physical colors, signs, finite indices and both level
parities, core coefficients have rate<=gtilde and aliases have rate<=k,
with a single error e_N->0. A pure core is bounded by g<=gtilde; a pure alias
has polynomial coefficients and rate0<=k. These are the actual transport
bounds, not termwise estimates on an incorrectly truncated physical sum.

The uniform positive Newton product rate is

$$
\begin{aligned}
m(x,y,z)&=J(x+y)+J(z)-J(x)-J(y)\\
&\quad-J(z-x)-J(z-y)-J(x+y-z),\\
D&=\{x,y\ge0:\max(x,y)\le z\le x+y\le1\}.
\end{aligned}\tag{8}
$$

It stays continuous and concave on ALL of D, including x>1/2 or y>1/2.
To check this from the original atoms, put p=z-x,q=z-y,r=x+y-z,w=1-x-y.
Then the three normalized angle triples are

$$
(y,x,w),\qquad(p,q,2r+w),\qquad(p+q,r,r+w).
$$

All entries are nonnegative and each triple sums to1 on D; their volume
sum is pi m. No half-coordinate assumption occurs in this derivation.
The exact factorial formula gives log mu=N m(i/N,j/N,r/N)+O(log N)
uniformly on its finite support. An input sum above d is ZERO, not an
analytic continuation of (8).

For z in[0,1], define the closed seed envelopes

$$
\begin{aligned}
G_{CC}(z)&=\max_{D,\,x,y\le1/2}[\widetilde g(x)+\widetilde g(y)+m(x,y,z)],\\
G_{AC}(z)&=\max_{D,\,y\le1/2}[k(x)+\widetilde g(y)+m(x,y,z)],\\
G_{AA}(z)&=\max_D[k(x)+k(y)+m(x,y,z)].
\end{aligned}\tag{9}
$$

where each maximization retains D. G_CA=G_AC by exact symmetry. These are
upper envelopes, not claimed coefficient rates or lower asymptotics. Their
values are finite, continuous and concave: the fibers are compact, admit
continuous feasible perturbations, and the joint actions are concave.
Uniformly for every actual output r and all physical colors,

$$
\left|[\widehat B_r](\mathrm{sector})\right|
\le\exp\!\left[N\bigl(G_{\mathrm{sector}}(r/N)+o(1)\bigr)\right].\tag{10}
$$

Indeed (6) has at mostN^2 summands, each satisfies the same compact-domain
bound, and the input restrictions in(9) contain its true support. Missing
boundary states, zero coefficients and exact cancellations can only improve
the upper bound. The O(logN) product error and uniform leaf error remain
o(N) after this finite multiplication.

One may retain the physical complementary-color parameter chi=h/N to use
k_chi(x)=J(x+chi)-J(x)-J(chi) for x<=1-2chi and k(x) otherwise, from the exact
old transport formula. This improves(9) without changing(6). Nothing here
requires maximizing colors independently before the physical filling sum.

## 4. The uniform block inequality at the actual complete state

At an actual complete A2 seed let both leaf coordinates be a and its output
be b. Its strict profile is F2(b)=2g(a)+m(a,a,b). With X=cot(pi a),

$$
\cot(\pi b)=X-\frac1{2X},\qquad Y=\frac1{2X},\qquad
F_2'(b)=-\log\bigl[(Y/X)^2\bigr]=2\log(2X^2)=:s(X).\tag{11}
$$

For a proper seed in the closed $s\ge2$ grammar, $1/2<X<1$.
The [uniform block lemma](actual_conway_uniform_two_leaf_block_alias_gap.md)
proves the following inequalities on the larger closed range $1/2\le X\le1$:

$$
\begin{aligned}
G_{AC}(z)&\le F_2(b)+s(X)(z-b)-\frac1{100},\\
G_{AA}(z)&\le F_2(b)+s(X)(z-b)-\frac1{100},\qquad0\le z\le1.
\end{aligned}\tag{12}
$$

One does not require that every alias
leaf separately lie below its complete tangent. Nor may one delete x+y<=1
when checking(12): that would bound a different, larger problem.

The corresponding CC inequality with zero loss already follows from the
original joint concavity and seed stationarity. At(a,a,b), a>1/4, so gtilde
agrees locally with g; the x,y derivatives of g(x)+g(y)+m vanish. Its joint
supporting plane therefore has ONLY the output slope s(X). This proves
G_CC(z)<=F2(b)+s(X)(z-b), with equality attained atz=b. Strictness of the
original state identifies its equality set locally, as needed below.

The companion proof encloses every transcendental quantity by rational
intervals and checks global supporting planes on sixteen exact intervals
of $s(X)/\log2\in[-2,2]$. Its smallest certified dual margin exceeds $1/25$;
the conservative $1/100$ in (12) is therefore uniform. The certificate
retains all vertices of the actual AC and AA product polytopes. It uses
feasible pure states for a lower bound and globally concave alias tangents
for an upper bound. Finite diagnostics are not used as proof, and (10)
alone would not imply (12).

## 5. The whole closed-tree source gap

Consider a fixed closed C(FG) in the s>=2 grammar. Expand the source by the
original choice of core or alias at EACH leaf. In every A2 seed group its
two choices and its internal gate by(6). Leave larger seeds expanded into
leaves and gates; all their complete leaves have the old automatic interval
1/4<a<atan(sqrt2)/pi and therefore retain a positive leaf tangent margin.

By the uniform block lemma, (12) holds at EVERY actual A2 seed of this
fixed complete optimizer. Its margin $1/100$ and the old positive margins
at the other leaves have a positive common lower bound $\gamma$.
For an expanded sector containing at least one alias, use a positive-loss
bound(12) on any contaminated A2 seed, or the old leaf bound on its alias in
a larger seed. Use the zero-loss CC block bound on unaffected A2 seeds and
the original complete tangents elsewhere.

All these tangents are taken at the SAME original global complete optimum.
The internal derivatives of an eliminated A2 seed vanish; its output
coefficient is exactly(11). Thus replacing that subaction by its profile
tangent preserves every derivative at the uncontracted original boundary
wire. Sum the remaining actual gate tangents and retain every turn relation
and the final root input relation. Original stationarity cancels ALL free
linear terms. The result for this alias sector is at most F0-gamma.

At finite N use r/N, not a silently shifted lattice. Product inequalities
remain inD; turn and closing equations have right side d/N=1-1/N. Every
fixed tangent has finite slope, so the affine cancellation error isO(1/N),
henceO(1) in the exponent. For fixed H there are only polynomially many
remaining wire states and finitely many sectors. The finite coefficient
bounds in(10) therefore imply, after decreasing gamma,

$$
\sup_{\text{all physical colors}}|Z_N-Z_N^{\mathrm{core}}|
\le\exp\!\left[N(F_0-\gamma/2)\right].\tag{13}
$$

for all sufficiently large N, at both parities. Every original normal term,
physical color, unit Cartan phase and actual mark remains in this bound.
There is no coefficientwise statement about an arbitrary external source;
this is the stated closed original tree at its own complete stationarity.

The remaining physical-color complement proof is inherited without requiring
an open block lower bound. Before block contraction, the all-core majorant
is the concave sum of gtilde and the same gates on the full original polytope.
It agrees locally with the strict pure action, so the complete optimum is
its unique global maximum. Outside a fixed strict full-wire window it has a
compact gap. Inside, every leaf lies below a fixed beta<1/2; if some original
color is outside the small complete corridor, the existing strict actual
core recurrence estimate loses a positive amount at that leaf. These two
regions give a uniform whole-core complement gap. Add(13) to get the entire
physical-source complement gap. The already reviewed exact complex packet,
primitive lattice and marked geometric interfaces are unchanged.

More explicitly, for each sufficiently small fixed $\delta>0$ there is
$\gamma_\delta>0$ such that

$$
\sup_{\exists\,l:\,N-j_l\ge\delta N}|Z_N(j_1,\ldots,j_H)|
\le\exp\!\left[N(F_0-\gamma_\delta)\right]
\tag{14}
$$

for all sufficiently large $N$. The expression and its half-twist signs
are fixed before this limit; all physical colors are included. Because
(12) holds on the FULL proper-seed range, no individual-leaf algebraic
cutoff remains in (13)–(14). These are the missing whole-source inputs
for the existing exact packet and original long-filling transfer. After
all auxiliary fillings and a loop-free parity choice, that transfer's
geometric conclusion concerns the hyperbolic volume of the knot complement.
The separate primitive slope, nonzero normalization and fixed sufficiently
long filling hypotheses remain those of the original transfer theorem.
This does not identify every arborescent template with the stated grammar.

## Inputs and review scope

Exact identities(1)–(6): [original positive Newton multiplication](actual_positive_newton_multiplication.md) §§1–2;
[exact pure-color core and alias](actual_pure_conway_auxiliary_color_leaf.md) §§1–4,6;
[full half-twist transport](actual_odd_conway_newton_transport.md) §§1–2. Uniform envelopes and concavity:
[original mixed-source supporting-plane argument](actual_odd_conway_uniform_mixed_source_gap.md) §§3–5 and
[original variational action](actual_positive_conway_variational_limit.md) §§1–2,4. Strict complete state,
ports and unchanged packet: [two-leaf source and packet interface](actual_conway_two_leaf_seed_source.md) and
[two-leaf complete and marked geometry](actual_conway_two_leaf_seed_geometry.md). No private diagnostic is an input.
Author finite/source proof complete. The primary agent, the coherent-source
reviewer and the geometric reviewer each independently fully read sections
1–5 of the finite/block argument: PASS. The separate uniform block lemma
received full mathematical and exact-code reviews and independent rational
replays; its result supplies (12) here. These internal reviews retain the
original coefficient, packet and marked-geometry inputs rather than
claiming independent reproofs of those earlier theorems. No floating-point
optimization or numerical asymptotic extrapolation is used in the proof.
