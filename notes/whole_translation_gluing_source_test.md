# An exact whole-translation and gluing-source test

Research reduction, 27 October 2026. The new whole-clock endpoint
maps preserve the functions and carries needed by a comparison.
The existing cyclic/Koszul reduction still needs an actual
co-source calculation. This note supplies the signed local norm
table and the precise orbit/moment pairing to compute next.
It proves neither a nonzero global geometric contribution nor a
volume bound.

## 1. The exact signed crossing norms

Use the ORIGINAL coefficient ratios of
[the actual geometric normal period](actual_geometric_normal_period.md),
with Q primitive of order N, x=-M/q_N, Y=M^2 and Q x^2=Y.
For one local crossing write
\[
 U=A^N,\quad V=B^N,\quad W=C^N,\quad P=Y^N,\quad X=x^N.
\]
The norm of a ratio is the product over the N shifts of its
OWN variable, fixing the other two. The exact results are
\[
\begin{array}{c|c|c}
 &\text{positive crossing}&\text{negative crossing}\\ \hline
 A&\displaystyle\frac{VW}{X}\frac{1-P/U}{1-PW/U}
  &\displaystyle\frac{X}{V}\frac{1-UW}{1-U}\\[4pt]
 B&\displaystyle\frac{U}{WX}\frac{1-VW}{1-V}
  &\displaystyle\frac{X}{U}\frac{1-P/V}{1-PW/V}\\[4pt]
 C&\displaystyle-\frac{U}{VWX}
                  \frac{(1-VW)(1-PW/U)}{1-W}
  &\displaystyle\frac1X\frac{(1-UW)(1-PW/V)}{1-W}.
\end{array}                                                     \tag{1}
\]
This is an identity of rational functions on their common open
chart. It is proved by the elementary identity
prod_(j=0)^(N-1)(1-Q^j z)=1-z^N. The positive C ratio has an
additional Gaussian product. Its exact phase is
(-1)^N Q^(-N(N+1)/2)=-1, which gives the displayed minus sign
for EVERY N, including even N. No unspecified phase remains.

The full periphery is retained:
\[
               X=(-1)^{N+1}M^N,\qquad X^2=P.        \tag{2}
\]
The table uses Frobenius-power variables U,V,W,P. They must not
be silently identified with fixed semiclassical shape coordinates
or with the original M. The exact moving-central-character issue
in [the rational period torsor](rational_quantum_dilogarithm_torsor.md)
still applies.

Closure combines these local transport factors along the already
specified integral free-flow lattice, with its original pivot and
zero-framing factors. It does not replace them by one. They are
nonconstant rational gluing characters off the gluing equations.
A finite dominant cover cannot turn such a character H into a
root of unity: pullback is injective on function fields, so
H^r=1 after pullback would imply H^r=1 beforehand. Finite phases
can kill the Gaussian signs; they do not kill the rational norm
transport in (1). On the gluing quotient H=1 is instead an actual
equation, whose regularity is a different assertion.

There is also an essential whole-quantum distinction. If
T_i=r_i(q,mathbf A) sigma_(Q,i), its EXACT N-step operator is
\[
 T_i^N=H_{i,N}(q,\mathbf A)\,\sigma_{Z,i},
        \qquad Z=Q^N.                              \tag{3}
\]
Only at Z=1 does sigma_Z become the identity and the coefficient
specialize to (1). The new
[flat endpoint tower](whole_clock_function_algebra_and_endpoint_extension.md)
retains that displacement; it does not license dropping it before
all actual normal coefficients and endpoint rows are transported.

## 2. What the source-sensitive cyclic reduction actually asks

For one unit scalar orbit let T e_j=r_j e_(j+1), with the last
edge returning to e_0, and put
\[
 s_0=1,\quad s_j=\prod_{u=0}^{j-1}r_u,\quad
 H=\prod_{u=0}^{N-1}r_u .
\]
The basis v_j=s_j e_j gives the standard companion transport
T v_j=v_(j+1), T v_(N-1)=H v_0. It is unimodular precisely on
the chart where the r_j are units. Direct telescoping gives
\[
       (1-T)\omega=(1-H)e_0,\qquad
                      \omega=\sum_{j=0}^{N-1}s_j e_j. \tag{4}
\]
At H=1 the invariant line has generator omega. For the ORIGINAL
transported co-source Lambda its exact coefficient is
\[
                         a_N=\Lambda(\omega)
                            =\sum_j s_j\Lambda(e_j). \tag{5}
\]
For d commuting translations on the finite root cover, the same
calculation gives the joint generator
\[
 \omega=\prod_{i=1}^d(1+T_i+\cdots+T_i^{N-1})e_{\rm mark}.
                                                               \tag{6}
\]
Its coefficients are the specified cocycle products, including all
finite phases. Original sum versus average factors N^d stay as
given by the actual source; (6) is the UNNORMALIZED orbit.

The source-sensitive test is to compute Lambda_rel(omega) on the
marked Rivin/gluing branch, with Lambda_rel the actual whole
relative co-source. In a relative complex this means pairing its
bulk, endpoint and carry components, not just an ordinary row
chosen after discarding boundaries. The derivative rows must
also be compared. For an ordinary row lambda the literal defect
is
\[
 b_j=\lambda_j-r_j\lambda_{j+1},\qquad
                   \sum_j s_j b_j=(1-H)\lambda_0,     \tag{7}
\]
with the cyclic convention at the last edge. These b_j are the
actual co-source boundary data to transport through the reduction.

The regular-sequence theorem in
[the rational period pushforward](rational_period_pushforward.md)
eliminates higher constraint homology. It does not prove that (5)
is a unit or that the source in (7) is the desired geometric one.
For example unit weights r_0=-1,r_1=u-1 have H=1-u, a unique
etale gluing point u=0, and flat free orbit module. The normalized
pointing lambda=(1,1)/2, psi=(1,1) still has lambda psi=1 but
lambda omega=0 there. Transporting BOTH source and dual under a
rephasing preserves this zero. This two-state diagnostic is not
a knot counterexample; it rules out the proposed inference from
flatness and regular sequence alone.

## 3. Exact moment and carry data required for the actual test

For the ACTUAL uncollapsed word introduce its existing independent
couplings w_i for each free flow and retain
\[
 \omega(\mathbf w;p)=\sum_{\mathbf k\in[0,N-1]^d}
             \mathbf w^{\mathbf k}r_{\mathbf k}(p)
                                      e_{\mathbf k}. \tag{8}
\]
The precise algebraic/relative moments to calculate are
\[
 a_{N,\alpha}(p)=
 \left[\prod_i(N^{-1}w_i\partial_{w_i})^{\alpha_i}
                \Lambda_{\rm act,rel}(\omega(\mathbf w;p))
                                      \right]_{\mathbf w=1}.   \tag{9}
\]
The actual source maps are independent of these transfer couplings,
so the derivatives in (9) insert the literal normalized free-flow
moments. Raw Green moments retain their corresponding N powers.
This is the whole generating-family identity of
[the strict word transport](relative_word_green_transport.md), not
an ordinary-color interpolation or a WKB definition of the moments.
Equation (8) denotes the TRANSPORTED actual coupons. In a splitting
using head indices and Frobenius blocks, their exponent is the
original full index/difference, with its marked offset and memory
carry; it must not be replaced by the residual deck index alone.
The identification of those coefficients with an open cyclic
geometric chart is part of the test, not an asserted source equality.

To compare (8)--(9) with the actual source, retain at least:

- All original head projectors, phases, pivot, source pairing units
  and the full external peripheral/modified-dimension line.
- The shifted value g(ZC) in every whole Jackson current and the
  added top spectral endpoint in its flat function tower.
- The literal endpoint P(J+N), rather than P(J), for every marked
  logarithmic moment; polynomial degree h makes this finite but
  does not make the endpoint zero.
- The actual memory carry w^((N+1)Delta R), with its recorded
  crossing sign. At w=exp(z/N) its limit is a nontrivial e^(z Delta R).
- The explicit off-diagonal head-current correction to Jackson,
  and every charged head neighbor at the requested quantum-normal
  depth. Scalar character differentiation does not replace them.

These conditions are the specific next calculation. The positive
Rivin point supplies a reduced algebraic evaluation place for the
coefficients and the transverse regular sequence. It does not
supply the actual transported Lambda_rel or its value on (6).
Proving that actual value is the specified nonzero geometric
relative period would advance the full theorem. A local norm
table or a nonzero result alone would still not establish uniform
cross-level growth or global dominance.

[The exact local-norm audit](../experiments/audit_actual_signed_crossing_norms.py)
checks all six ORIGINAL ratios, including even-level Gaussian
signs and full peripheral powers. No asymptotic formula is used.
