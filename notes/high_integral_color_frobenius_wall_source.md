# An actual high integral color carries the degree-N Frobenius wall row

Research construction, 27 October 2026. The actual integral color of
dimension N(r+1), specialized at the level-N root, has a classical
Sym^r multiplicity space. Its generators are literal divided powers
of the original quantum matrices, not an auxiliary classical source.
For r=N a marked coherent co-source gives exactly the binomial wall
row with N+1 entries. The original reduced knot scalar is retained
by exact all-color periodicity.

This constructs the wall functional as an actual color insertion.
It does not yet intertwine both framing-current complexes, identify
whole quantum jets of different colors, or prove selected geometric
source survival or a volume norm.

## 1. The original integral matrix family

Let N>=2, r>=0, m=N(r+1)-1, and let D_m(q) have its integral Weyl
basis u_j, 0<=j<=m:

\[
 \begin{split}
 H u_j&=(m-2j)u_j,\quad K=q^H,\\
 E u_j&=[m-j+1]_q u_{j-1},\qquad
 F u_j=[j+1]_q u_{j+1},\\
 [a]_q&=(q^a-q^{-a})/(q-q^{-1}).
 \end{split}                                                    \tag{1.1}
\]

Out-of-range vectors are zero. These are the ACTUAL integral color
matrices used in [all-color periodicity](cyclotomic_mellin_residue.md),
not the generic-M typical module. Put q_N=exp(pi i/N), Q_N=q_N^2,
and write j=kN+s with 0<=k<=r and 0<=s<N. Make the unit sign change

\[
 w_{k,s}=\beta_{k,s}u_{kN+s},\qquad
 \beta_{k,s}=(-1)^{Nk(k-1)/2+ks}.                     \tag{1.2}
\]

At the root, both ordinary block edges vanish: F at s=N-1 has
coefficient [(k+1)N]=0, and E at s=0 has coefficient
[(r+1-k)N]=0. With D_(N-1) denoting the Steinberg head, direct adjacent
entries give

\[
 \begin{split}
 E&=I_{r+1}\otimes(-1)^rE_{\mathrm{St}},\qquad
 F=I_{r+1}\otimes F_{\mathrm{St}},\\
 K&=I_{r+1}\otimes(-1)^rK_{\mathrm{St}},\\
 H&=I_{r+1}\otimes H_{\mathrm{St}}
                  +N\operatorname{diag}(r-2k)\otimes I_N.
 \end{split}                                                    \tag{1.3}
\]

For example the F coefficient before gauging is (-1)^k[s+1],
and the consecutive beta ratio is (-1)^k. The E coefficient is
(-1)^(r-k)[N-s], whose beta ratio gives (-1)^r[N-s]. The K and H
identities follow from m-2j=N-1-2s+N(r-2k).

Thus the ordinary small quantum action has r+1 invariant Steinberg
blocks. The unrolled H is NOT constant on this multiplicity space.
A map mixing k is not automatically an unrolled intertwiner.

## 2. Divided powers have a nonzero classical block action

Keep the original generic matrices before specializing and define

\[
 \mathsf E=\left[E(q)^N/[N]_q!\right]_{q=q_N},\qquad
 \mathsf F=\left[F(q)^N/[N]_q!\right]_{q=q_N}.           \tag{2.1}
\]

These ratios are regular matrix Laurent polynomials. On u_j their
coefficients are the symmetric Gaussian polynomials

\[
 \mathsf F:u_j\longmapsto {j+N\brack N}_{q_N}u_{j+N},\qquad
 \mathsf E:u_j\longmapsto {m-j+N\brack N}_{q_N}u_{j-N}.
                                                               \tag{2.2}
\]

Here boundary maps are zero. This is a regular integral division
before specialization, not division of the zero root matrices.

The needed Gaussian evaluation has an elementary proof. The identity

\[
 \prod_{j=0}^{a-1}(1+Q^jz)
       =\sum_h Q^{h(h-1)/2}{a\brack h}_Q z^h
\]

follows by coefficient induction. For a=AN+s, 0<=s<N, at Q_N the
product is (1-(-z)^N)^A times a product of degree s. Its z^N
coefficient, divided by Q_N^(N(N-1)/2)=(-1)^(N-1), gives
\({AN+s\brack N}_{Q_N}=A\). The symmetric Gaussian convention is
\({a\brack N}_q=q^{-N(a-N)}{a\brack N}_{q^2}\). Therefore before
the beta gauge the signs and coefficients are exactly

\[
 \begin{split}
 \mathsf F u_{kN+s}&=(-1)^{kN+s}(k+1)u_{(k+1)N+s},\\
 \mathsf E u_{kN+s}&=(-1)^{N(r+1-k)-1-s}
                   (r+1-k)u_{(k-1)N+s}.
 \end{split}                                                    \tag{2.3}
\]

The beta ratios then give

\[
 \mathsf F w_{k,s}=(k+1)w_{k+1,s},\qquad
 \mathsf E w_{k,s}=\tau(r-k+1)w_{k-1,s},\quad
 \tau=(-1)^{Nr-1}.                                    \tag{2.4}
\]

Consequently

\[
 e_{\mathrm{cl}}=\tau\mathsf E,\quad f_{\mathrm{cl}}=\mathsf F,
 \quad h_{\mathrm{cl}}w_{k,s}=(r-2k)w_{k,s}                \tag{2.5}
\]

satisfy [e_cl,f_cl]=h_cl, [h_cl,e_cl]=2e_cl and
[h_cl,f_cl]=-2f_cl. They are the ordinary irreducible Sym^r action
on k and commute with the root E,F,K head action in (1.3).
Their nilpotence order is r+1, so r=N has the degree-N string
unavailable in a fixed number of original small-head factors.

This is a SINGLE-COLOR divided action. Divided powers on tensor
products have mixed coproduct terms. Its classical multiplicity
action must not silently be substituted for that entire tensor
action or for a Hopf action on all matrix observables.

## 3. The actual first-normal block edges recover the same generators

Extend the sign frame (1.2) constantly in q, put Z=Q^N=q^(2N),
delta=1-Z, and retain the actual generic matrices. Let F_cross and
E_cross be just their between-block entries. They are divisible
by delta. With rho=q_N-q_N^(-1), the exact regularized root values
are

\[
 \begin{split}
 [F_{\mathrm{cross}}/\delta]_{q_N}
       &=\rho^{-1} f_{\mathrm{cl}}\otimes E_{0,N-1},\\
 [E_{\mathrm{cross}}/\delta]_{q_N}
       &=(-1)^{r+1}\rho^{-1}e_{\mathrm{cl}}\otimes E_{N-1,0}.
 \end{split}                                                    \tag{3.1}
\]

To check every sign, the F edge has coefficient
(-1)^k[(k+1)N]_q and the E edge has coefficient
(-1)^(k-1)[(r+1-k)N]_q. For every positive integer a,

\[
 \left[\frac{[aN]_q}{1-Q^N}\right]_{q_N}
                 =\frac{(-1)^{a+1}a}{\rho}.           \tag{3.2}
\]

This follows by factoring Q^(aN)-1 by Q^N-1 before evaluating;
no derivative of a singular quotient is inferred from root values.
Equations (3.1) follow immediately. In the normal variable
h=Log(q/q_N), delta=-2Nh+O(h^2), so the same entries are respectively
-2N f_cl/rho and 2(-1)^r N e_cl/rho at first h-order.

Thus the classical source is encoded canonically in the actual
quantum-normal block edges. The root decomposition is not a product
decomposition of the generic high-color module.

## 4. A coherent divided source gives exactly the binomial wall row

On the multiplicity space write v_k for its basis. The actual divided
operators in (2.5) construct the finite source and co-source

\[
 \psi_+=\exp(f_{\mathrm{cl}})v_0=\sum_{k=0}^rv_k,\qquad
 \lambda_+=2^{-r}v_0^*\exp(e_{\mathrm{cl}}),
 \quad \lambda_+(v_k)=2^{-r}{r\choose k}.              \tag{4.1}
\]

Both exponentials terminate. Direct multiplication gives
lambda_+(psi_+)=1. The rank-one coupon e_+=psi_+lambda_+ is idempotent
and has trace one. These are Frobenius/divided coherent operators
on the ACTUAL high integral color, not an ordinary Sym^r action
postulated on the old fixed-N head.

Let J=(J_0,...,J_r) be any array over a characteristic-zero
commutative coefficient algebra, and insert its literal diagonal
block operator diag(J_k) tensor I_N. Let P_s be any rank-one head
coordinate projector and tau_high=Tr/[N(r+1)]. Then

\[
 (r+1)\tau_{\mathrm{high}}
       [(e_+\otimes P_s)(\operatorname{diag}J\otimes I_N)]
          =\frac1{N2^r}\sum_{k=0}^r{r\choose k}J_k.     \tag{4.2}
\]

For r=N this is EXACTLY the actual wall row B_N(J), including its
1/N and the k=N endpoint. The coupling to the original Green array
is explicit: the multiplicity block k takes the original entry J_k,
equivalently the Kronecker coupling delta_(k,j). Formula (4.2) is
valid pointwise for all remaining flow variables and hence after
their finite sums. It applies to polynomial or retained logarithmic
moment coefficients as a linear functional; no multiplication or
Toeplitz-symbol identification is used.

If P_s is replaced by I_N, the coherent functional has value one
on the identity and the right side is N times (4.2). The marked
rank-one head accounts for the wall normalization; it must not be
dropped while claiming equality of source rows.

This realizes B_N as a marked co-source on an actual larger color.
It does not prove that the delta_(k,j) coupling intertwines the
second framing current or its entire divided Hopf coproduct.
Those equations must still be checked, with their endpoint carries.

### The coherent source has a canonical actual whole quantum germ

There is no need to extend the root binomial row arbitrarily. The
generic integral divided matrices E_N(q)=E(q)^N/[N]_q! and
F_N(q)=F(q)^N/[N]_q! are regular, and preserve every residue s
while moving the block index k. On the fixed s-string define

\[
 \begin{split}
 \Psi_s(q)&=\exp(F_N(q))w_{0,s},\\
 \Lambda_s(q)&=2^{-r}w_{0,s}^*\exp(\tau E_N(q)),\\
 u_s(q)&=\Lambda_s(q)\Psi_s(q),\qquad
 e_s(q)=\Psi_s(q)\Lambda_s(q)/u_s(q).
 \end{split}                                                    \tag{4.3}
\]

The finite exponentials terminate. At q_N, u_s=1 by (4.1), so its
whole germ is a unit, with no root pole canceled by hand. Equation
(4.3) is a regular idempotent of trace one. Different s-strings
are disjoint, hence E_coh(q)=sum_s e_s(q) is an idempotent of trace N.
For the ACTUAL generic high-color scalar long-knot operator,

\[
 \frac1N\operatorname{Tr}[E_{\mathrm{coh}}(q)C_{\mathrm{high}}(q)]
                          =C_{N(r+1)}(Q)              \tag{4.4}
\]

identically as a whole germ. The marked string e_s(q) gives
the exact whole wall weights
\(N^{-1}\Lambda_s\operatorname{diag}(J_k)\Psi_s/u_s\).
At the root these reduce to (4.2). Their quantum derivatives are
determined by the original divided matrices and the retained unit
u_s, rather than inferred from the numerical binomial row.

Equation (4.4) compares this color with itself. It is not an
off-root equality with C_N(Q), and does not make e_s(q) an
unrolled intertwiner or prove a current-complex map.

## 5. The reduced scalar is the original one; whole Q-jets are different

The actual zero-framed long-knot operator on D_m(q) is C_(m+1)(Q)
times identity, by the original integral color construction. Its
regular root specialization is still scalar. The independently
proved all-color identity gives

\[
                  C_{N(r+1)}(Q_N)=C_N(Q_N)=K_N.        \tag{5.1}
\]

Thus the normalized coherent functional with unmarked head identity
returns K_N. Its marked wall version returns K_N/N, as expected
from B_N(1)=1/N. The full original ADO normalization is still the
old marked line eta_N K_N/N, with its peripheral meridian germ;
one does NOT replace it by an imagined eta_(N(r+1))/[N(r+1)] line.

The high-color meridian path before specializing is

\[
 M_{\mathrm{high}}=-q^{N(r+1)},\quad
 Y_{\mathrm{high}}=M_{\mathrm{high}}^2=Z^{r+1},\qquad
 M_{\mathrm{low}}=-q^N,\quad Y_{\mathrm{low}}=Z.                \tag{5.2}
\]

At the root M_high=(-1)^r. In particular r=N uses the other lift
at odd N. The one-dimensional shift and its zero-framing phase
must be retained in comparing it with the original ideal lift.
For the external modified-dimension line the exact sign-chart law is
\(d_N(\sigma e^u)=\sigma^{1-N}d_N(e^u)\), with sigma=(-1)^r.
Its retained adapter sigma^(N-1)=(-1)^(r(N-1)) is identically one
when r=N. This does not install a new modified trace on the large
ordinary Weyl module: the original external d_N line is retained.
The fixed-color whole functions C_(N(r+1))(Q) and C_N(Q) have not
been identified away from Q_N. Their normal meridian slopes already
differ in (5.2), and (3.1) is the actual block-extension normal data.
For a nontrivial adequate knot their different quadratic degree
spans prove that the two whole Laurent polynomials are unequal.

Consequently this source elevation is an exact ROOT and first-normal
MODULE construction, not yet a source-preserving equality of the
whole Q-jets needed by Mellin reconstruction. It supplies the missing
degree-N wall representation while retaining the precise additional
normal comparison which remains to be established.

## 6. Verification and remaining network map

The following audit checks (1.3), every divided coefficient including
both boundaries, the full classical commutators, coherent source and
co-source normalization, the literal wall row, and both normal block
edges at even, odd and composite levels. The actual high-color
braiding/closure proof and its independent audit are recorded below.

The remaining network question is whether the explicit block/Green
coupling in (4.2), together with (3.1), transports the FULL actual
two-current relative source complex. No cancellation of the second
framing current or nonzero final geometric projection follows from
the existence of the coherent wall row alone.

[Divided-source audit](../experiments/audit_high_integral_color_frobenius_source.py).
[Results](../experiments/high_integral_color_frobenius_source_results.json).

## 7. The actual braiding retains a definite mixed half-Cartan sign

Here is an independent direct crossing and closure proof, with no
tensor-product theorem used as a premise. Put n=N(r+1), m=n-1,
and let W be the N-dimensional root color

    W=D_(N-1) tensor C_(Nr),
    H_W(i)=m-2i, 0<=i<N.

In the gauged basis of Section 1 the high color has the same
ordinary E,F,K as W on every block, while

    H_high(w_(a,i))=H_W(i)-2Na.

The generic universal R specializes integrally: on integral Weyl
vectors its kth factorial coefficient is a product of two Gaussian
polynomials and [k]_q!. Thus every k>=N term vanishes at q_N;
there is no division by [N] at the root. For k<N its nilpotent
part preserves the two block indices and is exactly that of W.

The remaining Cartan ratio is

    q_N^(-N[a H_W(j)+b H_W(i)]+2N^2ab)
       =epsilon^(a+b), epsilon=(-1)^m.             (7.1)

All head weights have parity m, so this sign is independent of
i,j and the transfer. The same calculation applies whether the
Cartan is evaluated before or after the nilpotent term, since
the head weights change by even integers. Inversion retains the
same sign. Consequently, for BOTH checked crossing signs,

    Rcheck_high^(+/-)(w_(a,i) tensor w_(b,j))
      =epsilon^(a+b) sum_(k,l)(Rcheck_W^(+/-))_(ij)^(kl)
                                      w_(b,k) tensor w_(a,l). (7.2)

The common highest-weight half-Cartan scalar is the original one
on the marked exponential sheet. It is the same for high and W
in (7.2); it is not set to one. The sign in (7.1) is genuinely
nontrivial for some even/odd levels and block pairs. Thus the
factorization is not an unmarked flip on arbitrary inserted
arrays. Mixed source or current coupons must carry this sign.

The original root pivot has no additional block factor:

    q_N^((1-N)(H_W(i)-2Na))=q_N^((1-N)H_W(i)).       (7.3)

The twist is also the same on every block. Shifting a highest
weight m by -2Na changes the ordinary twist exponent
h(h+2)/2 by -2Na(m+1)+2N^2a^2, whose q_N-power is one.

For a CLOSED BRAID whose closure is one knot, the multiplicity
index is transported by the permutation without changing along
the component. Closure therefore makes it a single value a.
Every mixed crossing sign in (7.2) is then epsilon^(2a)=1.
Equations (7.3) and the twist calculation show that its reduced
zero-framed head scalar is precisely the scalar of W.

To compare W with the original Steinberg color, retain the
one-dimensional shift h=Nr. With b braid strands and writhe w,
the actual crossing constant is

    s_0=q_N^(h^2/2)(-1)^(r(N-1)),
    g_h=q_N^((1-N)h)=(-1)^(r(1-N)).

The crossing index coboundaries telescope around the knot.
Crossings contribute s_0^w, closed pivots g_h^(b-1), and the
specified zero-framing twist contributes (s_0 g_h)^(-w).
Their product is g_h^(b-1-w)=1, since the parity of a one-cycle
braid permutation gives b-1-w even. This is the same direct
phase calculation used in the
[all-color periodicity proof](cyclotomic_mellin_residue.md).
It proves for the ACTUAL high-color long-knot operator

    C_high(q_N)=K_N I_(N(r+1)).                    (7.4)

In particular a normalized Frobenius source/co-source and the
original head cut retain K_N exactly. The full ordinary normalized
trace corresponds instead to the normalized trace on the
multiplicity factor; both evaluate (7.4) to K_N. The wall coupon
with a rank-one head projector has normalization 1/N, precisely
as in (4.2), rather than normalization one. The old external
modified-dimension line and its sign law remain those of Section 5.

This proof compares actual ROOT periods. Whole generic colors and
their quantum-normal slopes are different as (5.2) records.
Nor does (7.4) identify inserted Green networks: their block-changing
normal arrows and mixed signs require their literal couplings.

[Independent signed-crossing and original-period audit](../experiments/audit_frobenius_high_color_braiding.py).
[Results](../experiments/frobenius_high_color_braiding_results.json).

## 8. Coverage

Divided-power quantum groups and Steinberg/Frobenius tensor structures
are established representation-theoretic constructions. For coverage,
[Sutton--Tubbenhauer--Wedrich--Zhu, 2105.07724](https://arxiv.org/abs/2105.07724)
studies SL2 tilting modules, quantum-number root conventions and
integral divided-power models, including the complex root-of-unity
case. No tensor-product, trace, or braiding proof from that paper is
a premise here. The calculations above prove the explicit all-parity
module signs, actual first-normal edge, coherent wall coupon, its
whole high-color source germ, and the original marked scalar adapter
in the conventions used by the actual knot state.
