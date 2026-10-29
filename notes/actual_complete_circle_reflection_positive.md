# The complete crossing circle is positive after the literal face reflection

29 October 2026. The ORIGINAL complete-color crossing-circle operator
has a positive reflected tensor at every level and in every physical
integer-degree block. Its original ordinary cap has an exact polynomial
dual cost in this semidefinite form. Same-pair signed twists are exact
isometries. None of these statements identifies an arbitrary augmented
link contraction with a positive norm, or proves an open cusp-color
geometric-survival corridor.

## 1. Actual operator, reflection, and complete channels

Put (d=N-1), (q=e^{\pi i/N}), (Q=q^2), (x=q^d), and

\[
 s_a=|(Q;Q)_a|,\qquad s_0=1,\qquad 0\leq a\leq d.
\]

On the two ORIGINAL complete physical heads let \(\Omega\) be the
coproduct Casimir, including the original Cartan normalization. The
[literal mixed-circle calculation](actual_crossing_circle_source_and_filling.md)
proved, with the actual auxiliary pivot and no new color average,

\[
 L_N=(-1)^d U_d(\Omega/2),\qquad
 \mathcal P_N(\Omega)=0,\qquad
 \mathcal P_N(z)=2T_N(z/2)+2.                         \tag{1}
\]

Here the scalar polynomial \(U_d\) has \(U_0=1,U_1(z/2)=z\).
Let \(P|a,b\rangle=|b,a\rangle\) be the LITERAL tensor flip. It is
a face reflection, not an added crossing or a braid half-twist.

For total degree \(0\leq T\leq d\), use \(|u,T-u\rangle\),
\(0\leq u\leq T\). The original block \(J_T\) is complex symmetric,
and direct conjugation of its displayed entries in the
[complete channel theorem](actual_complete_casimir_hermite_packet.md)
gives

\[
 P\overline{J_T}=J_TP.                               \tag{2}
\]

Its nodes, with multiplicities retained, are

\[
 c_j=q^{2j+1}+q^{-2j-1},\quad 0\leq j\leq T,
 \qquad \nu_j=(-1)^j q^{j(j+1)}.
\]

Let \(v_j=f(c_j)\) be its canonical eigenvector with first component
one, as defined by the original continuant recurrence. Its last
component is \((v_j)_T=x^T\nu_j\). Thus uniqueness of its eigenline,
(2), and its first component give

\[
 P\overline{v_j}=\overline{(v_j)_T}\,v_j.              \tag{3}
\]

All formulas below use this specified physical normalization, not a
rescaled abstract Jordan basis.

## 2. Positive rank-one resolution in EVERY physical block

The exact theorem is

\[
 \boxed{\quad H_N=L_NP\succeq0,\qquad
                    C_N=PL_N=PH_NP\succeq0.\quad}    \tag{4}
\]

In a low block \(T\leq d\), its full nonzero rank-one resolution is

\[
 H_N\big|_T=\sum_{\substack{j<d-j\leq T}}
  \frac{2s_T^2}{s_{T-j}s_{T+j-d}}\,v_jv_j^*
 +\mathbf1_{N\ \mathrm{odd},\ d/2\leq T}
  \frac{s_T^2}{s_{T-d/2}^2}\,v_{d/2}v_{d/2}^*.        \tag{5}
\]

Every displayed coefficient is STRICTLY positive. Unpaired simple
nodes are killed. For \(T>d\), set \(K=2d-T\); translation of the
first physical index by \(T-d\) identifies the block with the low
block \(K\), including its literal reversal \(P\). Thus (5) covers
all \(N^2\) physical pair states. In particular

\[
 \operatorname{rank}H_N
   =\operatorname{rank}C_N=\lfloor(N+1)/2\rfloor^2.     \tag{6}
\]

Proof, including the signs. At a double node \(c=c_j=c_{d-j}\),
write \(Q_j(z)=\prod_{k\leq T,k\ne j,d-j}(z-c_k)\) and
\(B_T=(-1)^T s_T^2\). The exact bilinear CD measure is

\[
 \sigma_j=v_j^{\mathsf T}f'(c)
     =(v_j)_T Q_j(c)/B_T.
\]

Since \(L_N(c)=0\), its entire Jordan contribution, including its
normal part, is

\[
 L_N\big|_{c}=\frac{L_N'(c)}{\sigma_j}v_jv_j^{\mathsf T},
 \qquad L_N'(c)=(-1)^d\frac{2N}{4-c^2}.                \tag{7}
\]

Equation (3) converts the reflected contribution to

\[
 (L_NP)\big|_c
   =\frac{L_N'(c)B_T}{Q_j(c)}v_jv_j^*.                \tag{8}
\]

There are exactly \(d-T\) unpaired nodes; all lie above every paired
node on the real line. Other paired factors in \(Q_j(c)\) are
squares, and a possible self-paired node \(-2\) lies below it.
Consequently \(\operatorname{sign}Q_j(c)=(-1)^{d-T}\).
Together with \(\operatorname{sign}B_T=(-1)^T\), this proves strict
positivity in (8), including even levels. The exact magnitude from
the sine-factorial CD formula is the first coefficient in (5).

At odd \(N\), the self-paired simple node \(-2\) has
\(L_N(-2)=N\). The same argument uses \(\mathcal P_T'(-2)\) in
place of \(Q_j(c)\); its sign is \((-1)^{d-T}=(-1)^T\), since
\(d\) is even. Its exact coefficient is the second in (5).
At any other simple node \(L_N(c_j)=0\). This proves (4)--(5).
Counting the paired nodes, with both physical high/low blocks,
gives (6).

At the selected total degree \(T=d\), (5) simplifies particularly:

\[
 H_N\big|_d=N\sum_{j\ \mathrm{distinct}}m_jv_jv_j^*,
 \qquad m_j=2\ \mathrm{at\ double\ nodes},\quad
 m_j=1\ \mathrm{at\ the\ odd\ simple\ node}.        \tag{9}
\]

## 3. Exact ordinary-cap cost and same-pair isometries

Keep the original cup \(p\), ordinary cap \(\ell\), and normalized
Hermite normal \(t\) from the
[source frame theorem](actual_tame_c0_hermite_source_frame.md). They
satisfy, with their literal scalar normalizations,

\[
 \ell=p^*P/N^2,\quad \ell t=1,\quad L_Np=0,
 \quad L_Nt=2Np.
\]

Therefore

\[
 C_Nt=2N^3\ell^*,\qquad
 \boxed{\quad \ell C_N^+\ell^*=\frac1{2N^3},\qquad
              \ell^*\ell\preceq\frac{C_N}{2N^3}.\quad} \tag{10}
\]

Here \(+\) is the positive Moore--Penrose inverse. The first
display explicitly puts \(\ell^*\) in the range of \(C_N\);
any inverse solution differs from \(t/(2N^3)\) by its kernel, which
\(\ell\) annihilates. Positive Cauchy then proves the second formula.
This is an ALL-INPUT inequality on the physical pair, extending by
zero outside degree \(d\) on its left and by the positive blocks on
its right. No inverse of \(L_N\) is used.

Tensoring (10), and tensoring with arbitrary spectator identities,
gives for every physical \(2r+1\)-head vector \(\psi\)

\[
 |(\ell^{\otimes r}\otimes\langle d|)\psi|^2
 \leq(2N^3)^{-r}\,
 \langle\psi,(C_N^{\otimes r}\otimes|d\rangle\langle d|)
                                                    \psi\rangle. \tag{11}
\]

It applies to the ORIGINAL marked scalar when the already proved
whole-intertwiner theorem converts that scalar to this specified
ordinary-cap matrix element. Arbitrary inserted marked exteriors
retain their actual marked row. In particular \(p\) lies in the
radical of \(C_N\), while the marked row has \(mp=1\); the marked
row is NOT bounded in this seminorm by an illicit local replacement.

The literal original same-pair crossing \(R\) satisfies
\(R^*PR=P\) and commutes with \(L_N\). This holds on every physical
block: (2) gives \(\Omega^*P=P\Omega\), and the actual polynomial
\(r_N\) has unit values and purely imaginary logarithmic derivatives
at the real double nodes. Thus \(\overline{r_N}r_N-1\) vanishes with
the full multiplicity of \(\mathcal P_N\). Its functional calculus
proves the assertion, with the original unit Cartan factor retained.
Hence

\[
 (R^a)^* C_N R^a=C_N,\qquad a\in\mathbb Z.            \tag{12}
\]

Thus every signed same-pair twist is an exact isometry on this
positive quotient. No invariance under an overlapping pair crossing
is asserted.

There is also a quantitative ordinary-color transmission bound on
this SAME inserted-circle quotient. Since
\(\Omega^*C_N=C_N\Omega\), its induced operator on
\((V_d\otimes V_d)/\ker C_N\) is selfadjoint. At a double node its
nilpotent value vector is in the radical, so the quotient has one
ordinary eigenline; at the odd simple node it has the ordinary line.
Every quotient eigenvalue is therefore one of the real \(c_j\).
For \(c=2\cos\theta\), \(|U_{j-1}(c/2)|\leq j\), hence

\[
 L_j^*C_NL_j\preceq j^2C_N,\qquad 1\leq j\leq N.      \tag{12a}
\]

If \(\gcd(j,N)=1\), its retained nodal values are all nonzero and
have modulus at least \(\sin(\pi/N)\geq2/N\). The possible odd
simple node is interpreted by its removable value \(L_j(-2)=j\).
Thus the inverse on this quotient has norm at most \(N/2\), and

\[
 \frac4{N^2}C_N\preceq L_j^*C_NL_j\preceq j^2C_N
                       \quad (\gcd(j,N)=1).            \tag{12b}
\]

These operator inequalities tensor with arbitrary spectators. They
bound a transmission inserted on an existing complete-circle form;
they do NOT express replacement of its defining \(L_N\) insertion
by \(L_j\). That distinction is essential at the original cup below.

## 4. A once-power positive angle coefficient and a nonzero local channel

For a paired node put

\[
 A=T-j,\quad B=T+j-d,\quad D=d-T.
\]

These are nonnegative ACTUAL integer indices with \(A+B+2D=d\).
The coefficient in (5) is exactly

\[
 h_{T,j}=\frac{2N^2}{s_As_Bs_D^2}.                    \tag{13}
\]

The odd simple coefficient has the same formula without the factor
2 and with \(A=B\). This uses \(s_Ts_{d-T}=N\); it is a positive
once-power four-angle factorial weight. It is not asserted to give
the full edge incidence of an augmented-link triangulation.

One original physical corner can be calculated without a Clebsch
envelope, since every \((v_j)_0=1\):

\[
 (H_N|_T)_{0,0}
 =s_T^2\sum_{a=0}^{2T-d}\frac1{s_as_{2T-d-a}},
                \quad 2T\geq d,                     \tag{14}
\]

and it is zero for \(2T<d\). The full sum over both members of a
double pair supplies its factor2; the odd simple midpoint is counted
once. Consequently the corner is strictly nonzero on every admitted
physical block.

The uniform all-index factorial estimate and midpoint maximization
give, with \(\tau=T/N\),

\[
 \log (H_N|_T)_{0,0}
 =\frac N\pi\left[-2\Lambda(\pi\tau)
       +2\Lambda\bigl(\pi(\tau-\tfrac12)\bigr)\right]
       +O(\log N),\qquad 2T\geq d.                   \tag{15}
\]

The formula is uniform through the endpoints, with the continuous
odd extension of \(\Lambda\) if \(\tau=1/2-1/(2N)\).
To verify midpoint maximization, at fixed sum \(s\leq1\) the function
\(\Lambda(\pi a)+\Lambda(\pi(s-a))\) increases up to \(s/2\)
and decreases after it: its derivative has the sign of
\(\sin(\pi(s-a))-\sin(\pi a)\). Selecting a nearest integer
midpoint gives the lower bound; summing at most \(N\) terms gives
the upper bound. Integer shifts by \(d=N-1\) cost only \(O(\log N)\).

The bracket in (15) has its unique maximum at \(\tau=3/4\), equal
to \(4\Lambda(\pi/4)=v_8/2\). Thus

\[
 \log\max_T (H_N|_T)_{0,0}
       =Nv_8/(2\pi)+O(\log N).                       \tag{16}
\]

This is a quantitative, positive, nonzero ORIGINAL local circle
channel at all levels. It is not a nonzero geometric coefficient of
an arbitrary assembled augmented-link source.

## 5. The open color corridor still requires an actual source argument

The positivity is special to the COMPLETE circle. For any
\(1\leq j<N\), the reflected ordinary circle \(PL_j\) is Hermitian
but INDEFINITE already on the original source plane. Indeed

\[
 L_jp=\lambda_jp,\qquad
 \lambda_j=(-1)^{j-1}\frac{\sin(\pi j/N)}{\sin(\pi/N)}\ne0.
\]

In the basis \(p,t\), its Hermitian quadratic form has top-left
entry zero and off-diagonal entry \(N^2\lambda_j\ne0\), so its
two-by-two determinant is negative. Thus a nonzero geometric
coefficient on an OPEN cusp-color corridor cannot be inferred by
continuing local positive-semidefiniteness. It may instead follow
from a source-preserving contour and analytic continuation, but that
requires its own original-cycle and Stokes/boundary estimates.

Likewise local positivity does not identify a whole planar augmented
network with a squared norm: all reflected leg identifications,
ordinary pivots, the sole modified cut and any extra complete
components have to match in the global tensor contraction.

[Audit](../experiments/audit_actual_complete_circle_reflection_positive.py)
checks every physical block, the exact CD positive resolution, original
cup/ordinary/marked typing, same-pair actual signed twists, and the
positive corner/profile, with separate literal mixed-circle checks.

Fresh replay: PASS six literal mixed universal/pivotal circles at
\(N=2,\ldots,7\); eleven complete physical PSD/CD/source/twist families
at \(N=2,\ldots,12\), including every high-degree mirror; four uniform
positive-corner profiles through \(N=128\).
