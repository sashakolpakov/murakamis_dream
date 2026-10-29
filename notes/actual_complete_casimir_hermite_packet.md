# Complete actual Casimir packets and their recoupling measure

29 October 2026. Every physical integer-degree block has an explicit
complete Casimir frame, including all confluent derivative columns.
Its inverse is determined by a closed bilinear Christoffel--Darboux
measure. That measure has explicit sine-factorial profiles; at degree
N-1 all its double-node weights are polynomial. No tame eigenframe
is inferred from tame spectral jets.

The adjacent complete-channel change has an explicit all-entry product
formula before restriction to a total-three-head multiplicity module.
Its entries admit finite angle-factorial envelopes, with every inverse
normalizer accounted for. The original cup and both cap rows are kept.
The remaining marked-source norm and coherent overlap action are not
asserted to have the sharp volume bound.

## 1. Literal Jacobi blocks and the high-degree mirror

Put `q=exp(pi*i/N)`, `Q=q^2`, `d=N-1`, `x=q^d=-q^-1`.
Use the original balanced F,Ecal,K and tensor Casimir Omega as in
[the source Hermite theorem](actual_tame_c0_hermite_source_frame.md).
For total degree `0<=T<=d`, write physical states `|u,T-u>`,
`0<=u<=T`, and set `v=T-u`. The block J_T of Omega is COMPLEX
SYMMETRIC tridiagonal. Its offdiagonal from u to u+1 is

    A_u=Q^(-v)(1-Q^v)(1-Q^(u+1)), 0<=u<T.             (1)

Its diagonal is

    D_u=(Q^(-u)-1)xQ^(-v)(1-Q^u)
        +(Q^(-v)-1)x^(-1)Q^u(1-Q^v)
        +q x^2Q^(-T)+q^(-1)x^(-2)Q^T.               (2)

Both formulas are direct application of F_tot E_tot and the actual
Cartan. Every A_u is nonzero. The product is especially simple:

    B_T=product_(u=0)^(T-1) A_u=(-1)^T s_T^2,
    s_a=|(Q;Q)_a|.                                   (3)

For `T>d`, put `K=2d-T`, `a0=T-d`. Its block is the SAME J_K
after translating the physical first index by a0. One proof uses
the actual root Chevalley matrix `W|a>=(-1)^a|d-a>`:
`W F W^-1=Ecal`, `W Ecal W^-1=F`, `W K W^-1=K^-1`.
Chevalley followed by tensor flip commutes with Omega, and its
coefficient is constant on a fixed integer degree. Thus the high
blocks introduce no additional frame cost or missing channels.
The same comparison follows from direct entries (1)--(2).

## 2. Explicit polynomial columns and generic-q confluence

Define continuants

    p_0(z)=1, p_1(z)=z-D_0,
    p_(u+1)(z)=(z-D_u)p_u(z)-A_(u-1)^2 p_(u-1)(z).

For `0<=u<=T` put

    f_u(z)=p_u(z)/(A_0...A_(u-1)), f_0=1.            (4)

The characteristic polynomial is

    P_T(z)=p_(T+1)(z)=product_(j=0)^T(z-c_j),
    c_j=q^(2j+1)+q^(-2j-1).                         (5)

There are only simple or double nodes; a collision is exactly
`j+l=d`. The self-paired node j=d/2, when integral, is simple.
At a simple node take the column f(c_j); at a double node take BOTH

    f(c_j), f'(c_j).                                 (6)

The last-row recurrence gives `(J_T-z)f(z)=-P_T(z)e_T/B_T`.
Hence (6) is the exact Jordan chain `(J_T-c)f'=f` at a double node.

These are normalized ACTUAL Clebsch columns and their generic-q
divided differences, not an arbitrarily supplied Jordan basis.
To see this, vary q to zeta near q with ordinary highest weight d.
Its highest vector at degree j has coefficients b_0=1 and

    b_a=(-1)^a x^(-a) Q^[a(j-1)-a(a-1)/2]
              (Q^(N-j);Q)_a/(Q^(N-a);Q)_a,           (7)

where in (7) `Q=zeta^2`, `x=zeta^d`. The E equation directly gives
its successive ratio. Its divided descendant
`F_tot^(T-j)h_j/(Q;Q)_(T-j)` has eigenvalue
`zeta^(2N-1-2j)+zeta^(-2N+1+2j)`. Its first physical component
is `x^(-(T-j))[T choose j]_Q`, nonzero near the root because
`T<N`. Thus normalizing that component to one gives the unique
first-row recurrence solution f(zeta,lambda_j(zeta)). This proves
(5) by generic distinctness and dimension T+1.

For colliding j,l the divided difference of these two normalized
columns converges to f'(c); the common zeta derivative cancels.
The eigenvalue gap has logarithmic derivative `2N` times
`q^(2j+1)-q^(-2j-1)`, up to its order sign, and is nonzero.
All denominators in (7) and in these low-degree descendants have
factorial indices at most d. Exact generic-q duality is retained;
no fixed-q meridian splitting is imposed on an exact dual cap.

## 3. The complete inverse, including every derivative normalizer

Let V_T have the columns (6), grouped by distinct nodes. Different
nodes and their chains are orthogonal for the BILINEAR pairing
`u^T v`, because J_T is symmetric. This is not a Hermitian positivity
assertion. Define `nu_j=(-1)^j q^(j(j+1))`.

At a simple node c_j, the bilinear block is the nonzero scalar

    sigma_j=x^T nu_j P_T'(c_j)/B_T.                  (8)

At a double node c=c_j=c_l, put
`Q_j(z)=P_T(z)/(z-c)^2` and let r'_j be the derivative of the
ORIGINAL normalized crossing polynomial at c. Its exact block is

    K_j=[[0,sigma_j],[sigma_j,sigma_j eta_j]],
    sigma_j=x^T nu_j Q_j(c)/B_T,
    eta_j=r'_j/nu_j+Q_j'(c)/Q_j(c).                  (9)

In particular `sigma_j` never vanishes. The full frame and inverse are

    V_T^T V_T=K_T=directsum K_j,
    V_T^(-1)=K_T^(-1)V_T^T,
    K_j^(-1)=sigma_j^(-1)[[-eta_j,1],[1,0]]          (10)

for a double block; a simple block has inverse `sigma_j^-1`.
This proves completeness and gives the ENTIRE inverse, without a
condition-number guess or loss of a Jordan channel.

Proof of the normalizers. Christoffel--Darboux for the continuants is

    sum_(u=0)^T f_u(z)f_u(w)
      =[P_T(z)p_T(w)-p_T(z)P_T(w)]/[(z-w)B_T^2].

Its simple-node specialization gives
`P_T'(c)p_T(c)/B_T^2`. At a double node it gives
`Q_j(c)p_T(c)/B_T^2` for f^T f', and
`[Q_j(c)p_T'(c)+Q_j'(c)p_T(c)]/B_T^2` for f'^T f'.
The first physical row of the ORIGINAL checked R in degree T has
only the last column, with coefficient `kappa x^-T`. Therefore

    f_T(c_j)=x^T nu_j,
    f_T'(c_j)=x^T r'_j at a double node.

Since `p_T=B_T f_T`, these formulas prove (8)--(9), including all
phases. The actual full Cartan kappa cancels in this argument; it
remains on R itself.

## 4. Exact sine-factorial measures, all parities and all degrees

Write `a_j=|1-Q^(2j+1)|`. For a simple UNPAIRED j (`j<d-T`),

    |sigma_j|=s_(T-j)s_(T+j+1)/(s_T^2 a_j).          (11)

For a double pair `j<l=d-j<=T`,

    |sigma_j|=N s_(T-j)s_(T+j-d)/(s_T^2 a_j^2).      (12)

For the simple SELF-paired node `j=d/2<=T` at odd N,

    |sigma_j|=N s_(T-j)^2/s_T^2.                    (13)

Every index lies in `0,...,d`. To prove these, factor each nonzero
node difference into

    |c_j-c_k|=|1-Q^(j-k)| |1-Q^(j+k+1)|.

The first product gives `s_j s_(T-j)`, deleting the partner factor
when present. The second is the circular interval j+1,...,j+T+1:
delete its self factor, and its unique root-zero partner if present.
Root complementation `s_d=N` gives exactly (11)--(13). No separate
factorwise N^O(N) bound is used.

At T=d this simplifies to

    |sigma_j|=1/|1-Q^(2j+1)|^2 for EVERY double node,
    |sigma_(d/2)|=1 at the simple odd-level node.      (14)

Thus the full degree-d channel MEASURE is polynomial; this does not
say the Clebsch frame or its Hermitian inverse is tame.
For all double blocks, nonzero node gaps are at least `16/N^2` and
the independently derived actual jets obey `|r'_j/nu_j|<=N^2/8`.
Consequently `|eta_j|<=C N^3`. The inverse block in (10) has no
additional exponential factor beyond its explicit `1/|sigma_j|`.

## 5. Explicit q-Hahn sums and a quantitative angle profile

For `T<=d`, set `r=T-j` and
`I={max(0,u-r),...,min(j,u)}`. At the actual root the value column is

    f_u(c_j)=x^r/[T choose j]_Q * sum_(a in I)
       (-1)^a x^[-(r-u+2a)] Q^[a(a-1)/2+a(r-u+a)]
          [j choose a]_Q [u choose a]_Q
                                   [T-u choose j-a]_Q.       (15)

This follows by expanding the actual highest vector (7) at the root,
then applying the divided coproduct descendant. All three binomial
factors retain their true root phases. In particular it is a closed
finite Clebsch/q-Hahn sum, with no unknown knot period.

Let beta denote the positive sine-binomial magnitude and put

    E_(T,j,u)=sum_(a in I) beta_(j,a)beta_(u,a)
                          beta_(T-u,j-a)/beta_(T,j).          (16)

Then `|f_u(c_j)|<=E_(T,j,u)`. For a double pair j,l,

    |f_u'(c_j)|<=C N^2(1+log N)
                              [E_(T,j,u)+E_(T,l,u)].         (17)

For (17), differentiate the ACTUAL generic-q sums before their
confluence. Each factorial has index below N and
`|D_logzeta log F_a|<=N^2(1+log N)` at the root. There are a bounded
number of factorial ratios and quadratic monomials in every summand
and its endpoint normalizer. The eigenvalue-gap derivative has
modulus at least eight. Thus differentiation costs only the displayed
polynomial times the SAME positive factorial profiles. No exponential
frame factor is put into the error term.

Every beta in (16) is `N w_d(k,L-k,d-L)`, with exact sum d.
Equivalently E is `N^2` times a finite sum of THREE such positive
cell weights divided by the known boundary weight
`w_d(j,T-j,d-T)`. Their charges and the range I are literal integer
Clebsch incidence; the denominator is a compulsory boundary metric.
Equations (10)--(13),(16)--(17) give a quantitative profile for the
entire frame AND inverse, including every Jordan derivative.
They are bounds, not assertions that the q-Hahn phases can be deleted
at the sharp exponent or that these cells already form geometric edges.
For high physical T extend the notation by
`E_(T,j,u)=E_(2d-T,j,u-(T-d))`, and use the corresponding low-block
measure sigma; inadmissible physical indices have value zero.

## 6. Complete adjacent-channel kernel at arbitrary width

Lift the block frames to the full physical pair, preserving total T.
Before restricting the THREE-head total Casimir, its complete pair
coordinate change has the following exact entry. For input pair
degree T, channel gamma (value or derivative type), and third physical
index c, choose an output first physical index u. Put

    b=T-u, T'=b+c.

If the physical indices are admissible, the output pair channel delta
has coefficient

    Rcal_((u,T',delta);(T,gamma,c))
         =V_T[u,gamma] (V_T'^(-1))[delta,b].         (18)

Otherwise it is zero. Here high blocks use the unitary index
translation from Section1. Equation (18) is simply the two ACTUAL
pair frames sewn at the shared physical index; no complete channel
or derivative row has been suppressed. Its entries are products of
the finite q-Hahn columns and explicit inverse rows (10).

For a double channel use `Ebar=E_j+E_l`, and for a simple channel
use E_j. Equations (10),(16)--(17) give, uniformly in all admissible
ports, an all-channel estimate of the form

    |Rcal|<=C N^5(1+log N)^2
             Ebar_(T,gamma,u) Ebar_(T',delta,b)/|sigma_delta|. (19)

All exponential factors on the right are the stated sine-factorial
angle profiles. Restricting (18) to a fixed total-three-head Casimir
or a source-generated Hom space is the subsequent genuine Racah
contraction; it cannot be assumed from (18) alone. This distinction
avoids a spurious tensor-multiplicity assertion at the root.

The original signed pair crossing in these frames is exactly kappa
times blocks `nu_j` at simple nodes and
`[[nu_j,r'_j],[0,nu_j]]` at double nodes; its literal inverse retains
the inverse derivative. Thus twist phases remain coherent when (18)
is used in an arbitrary original braid. This is an all-exterior
operator/source coordinate change, not a replacement invariant.
The original pivot, framing, modified-dimension germ and peripheral
line are transported unchanged. None is divided by the spectral
measure sigma or selected afterward from the knot value.

## 7. The original source and the remaining estimate

At degree d the c_* block may be replaced, by its explicit two-by-two
adapter, with the uniformly conditioned p,t source frame of
[the source Hermite theorem](actual_tame_c0_hermite_source_frame.md).
If g_0=x^-d, its columns in the canonical f,f' coordinates are

    p=N g_0 f(c_*),
    t=-(mu_N/gamma_N)p+(g_0/gamma_N)f'(c_*).        (20)

This retains the ORIGINAL cup, ordinary cap and marked row. Ordinary
caps vanish on other Casimir blocks and select the corresponding
source derivative row; the cup lies in the source value channel.
The marked row does NOT vanish on arbitrary other channels. Its
complete coefficients are the explicit sums `m V_T`; in an assembled
original plat integer degree forces the final marked pair to degree d,
as before. No sectorwise marked-corner substitution is made here.

For example a positive spectral packet metric can be specified by
giving each canonical simple/double block the positive scalar
`|sigma_j|` times identity, with the source block (20) handled in
its actual p,t frame. This defines a full positive Gram by pullback
through the COMPLETE frame. Its original marked dual norm and its
adjacent overlap energies are explicit via (10),(15),(18), but no
polynomial or sharp-volume bound for them is asserted.

The new result supplies the actual all-channel frame, inverse measure
and factorial/angle envelopes needed to ask that question. The
remaining sharp step is a coherent estimate of (18) after its actual
source-generated restrictions and closure, rather than separate
absolute maximization of (16) or of twist eigenvalues.

The subsequent [source-generated complete module](actual_complete_source_multiplicity_module.md)
and [positive-source Gram calculation](actual_complete_channel_positive_gram.md)
do give polynomial BOTH boundary norms after the actual J recoupling.
However its fixed canonical positive-channel energy is
[nonsharp already for the original figure-eight](actual_figure_eight_complete_channel_energy.md).
This does not invalidate the frames or measures above; a sharp
norm estimate must retain a more selective coherent packet, such as
the [source-exact terminal construction](actual_terminal_packet_positive_gram.md),
and control its general propagation.

[Audit](../experiments/audit_actual_complete_casimir_hermite_packet.py):
original generator-built blocks, all nodes and derivative columns,
full inverse/bilinear measures and phases, finite Clebsch sums,
high-degree mirror and original signed crossings/source adapters.
