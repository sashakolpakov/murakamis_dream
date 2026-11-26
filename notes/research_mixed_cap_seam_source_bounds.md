# Scalar source ceilings for the cap at its outgoing seam

Research lemma, 5 November 2026. Keeping the inner endpoint sum
coherent gives sharper upper bounds for the two caps at \(X=1\).
Only two fixed critical-action evaluations are needed; the full real
private index is handled analytically. These bounds do not include
the adjacent conditional edge or its reference tangent and therefore
do not by themselves prove a boundary comparison.

## 1. The exact seam normalization

Use the literal cap and endpoint coefficient from
[the complete cap theorem](research_mixed_complete_first_cap_packet.md).
At \(X=1\), \(p_i(1)=P_i\), so
\[
 U_{\epsilon,N}(w,1)
   =\sum_{i=0}^{N-1}D_N(i/N)^{-1}\mathcal C_N(i/N,w)
                                 P_i^{1-\epsilon},
       \qquad \epsilon\in\{0,1\}.                       \tag{1}
\]
The factor \(D_N(i/N)\) has modulus one. Equivalently,
\(H_N(w,r^{-i})=P_iD_N(i/N)^{-1}\mathcal C_N(i/N,w)\).
Thus the absolute private-row sum in (1) has compact real-row rate
\[
 f_\epsilon(s)=\lambda(s)+(1-\epsilon)J(s),\qquad
 \lambda(s)=\Re S(s),\qquad S(s)=F(s,u_c(s)),              \tag{2}
\]
where \(S\) is the original full real-index endpoint action.
The [full-index theorem](research_complete_boundary_full_index_interval.md)
supplies this rate uniformly on every compact subinterval of
\((0,1)\), with both parities and the original ordinary color.
No raw upper estimate replaces its inner Newton sum.

## 2. Both real-row maxima reduce to fixed scalars

For \(0<s<1\), continue the original square root as
\[
 \sqrt{1-2e^{2\pi is}}=a+ib,\qquad
 q=\sqrt{1-b^2},\qquad A=1+q+b.
                                                               \tag{3}
\]
It has \(a>0\), \(-1<b<1\), and
\(a^2+b^2=1+2q\). Its imaginary part is negative below
\(s=1/2\), zero there and positive above. The modulus calculation
in [the outer real-tail proof](research_mixed_outer_cap_real_tails.md#2-an-exact-derivative-identity-above-one-half)
uses only these algebraic identities and positive denominators.
It therefore also holds on the lower half, with \(b<0\):
\[
 \lambda'(s)-J'(s)=-2\log A,\qquad
 4\sin^2\pi s=2q(1+q),\qquad
 A^2=2(1+q)(1+b).                                       \tag{4}
\]
Every logarithm here is of a positive real modulus. Consequently
\[
 (\lambda+J)'(s)=\log\frac{q}{1+b}
       =\frac12\log\frac{1-b}{1+b}.                    \tag{5}
\]
This is positive below one half and negative above. Thus
\(f_0\) has its global real maximum at \(s=1/2\).

On \(0<s<1/2\), the original endpoint Schur argument proves
\(\lambda''(s)<0\). On \([1/2,1)\), the same identity (4)
gives \(\lambda'(s)\le-\log2\), as in the existing tail
proof. The whole lower half is bounded by the tangent at
\(s_0=7/20\):
\[
 \lambda(s)\le\lambda(s_0)+\lambda'(s_0)(s-s_0).
                                                               \tag{6}
\]
The focused outward scalar checks give
\[
\begin{split}
 \lambda(1/2)&<101/125=.808,\\
 \lambda'(7/20)&<0,\qquad
 \lambda(7/20)-(7/20)\lambda'(7/20)<433/500=.866.
\end{split}                                                   \tag{7}
\]
The first scalar is approximately \(.8076648680\); the tangent
ceiling is approximately \(.8657517313\). These displayed
approximations are not the acceptance test. Equations (5)--(7)
bound every compact real row, without a row grid or optimizer.

## 3. Literal endpoint rows

For completeness, the compact packet is not extrapolated to
\(s=0,1\). Put \(\delta=1/100\),
\(S_j=|P_j|\), and \(E_l=e_l(-2)\ge0\). At the complete
color the exact physical coefficient obeys
\[
 |\mathcal C_N(i/N,-2)|
       \le\sum_{l=0}^{i}\frac{E_l}{S_l S_{i-l}}.
                                                               \tag{8}
\]
For \(s=i/N\le\delta\), use \(E_l\le4^l/S_l^2\)
and the uniform sine-product bounds. Since \(J\) decreases on
\([0,\delta]\), their upper entropy is at most
\[
                 2s\log2-4J(s)\le2\delta\log2-4J(\delta)<1/4.
                                                               \tag{9}
\]
Multiplying by \(P_i\) when \(\epsilon=0\) only lowers
this rate. Polynomial prefactors are uniform through \(i=0\).

At the other end set \(k=N-1-i\). The exact reflection
\(S_{N-1-j}=N/S_j\) gives
\[
 |\mathcal C_N(i/N,-2)|
       \le\frac{2^k}{N}\sum_{l=0}^{i}E_l,
 \qquad
 |H_N(-2,r^{-i})|
       \le\frac{2^k}{S_k}\sum_{l=0}^{i}E_l.             \tag{10}
\]
Indeed \(S_{k+l}/S_l\le2^k\) on the complete displayed
support. The zero-safe Newton bound used in the old real-tail proof
gives \(\sum E_l\le N^C e^{3N/5}\); its entropy maximum is
\(-4J(1/4)<3/5\). For \(k/N\le\delta\), (10) consequently
has rates at most
\[
       3/5+\delta\log2<.61,
       \qquad3/5+\delta\log2-J(\delta)<.65.             \tag{11}
\]
These are smaller than the respective bounds in (7).
All endpoint estimates retain odd-level zeros rather than dividing
by a Newton coefficient. The same product regularization gives their
uniform small ordinary-color perturbations with an arbitrarily
small prescribed rate tolerance.

**Theorem 1.** Put \(b_0=101/125\), \(b_1=433/500\).
For every \(\eta>0\), there is a fixed ordinary-color
neighborhood of \(-2\) and constants \(C,A\) such that
\[
 |U_{\epsilon,N}(w,1)|
       \le\sum_{i<N}|\mathcal C_N(i/N,w)|\,|P_i|^{1-\epsilon}
       \le C N^A e^{N(b_\epsilon+\eta)}.                \tag{12}
\]
This holds at both level parities. Uniform holomorphy gives each
fixed ordinary derivative on a smaller color neighborhood, with
the same rate allowance. It is not a whole real-color angular
loss theorem.

The [existing real zero-collar product estimate](research_mixed_real_zero_collar.md)
also gives, for fixed \(0<\rho\le.001\),
\[
 |U_{\epsilon,N}(w,e^{-2\pi ix})|
       \le C N^A\exp N\{b_\epsilon+\Delta_\rho+\eta\},
 \quad0\le x\le\rho,\qquad
 \Delta_\rho=\rho\log2-J(\rho).                         \tag{13}
\]
Only the actual factor \(p_i(X)/P_i\) is transferred in this
step. Any diagonal \(d_N\) and selected monomial belonging to
the outer source are still to be included separately.

## 4. Calibration still required

The new ceiling is for the unweighted cap. Its reference value in a
left boundary comparison is the weighted phase
\(\mathcal T_{\epsilon_1}(r_1)-\epsilon_1 g(r_1)/2\),
combined with the adjacent allocated phase \(\phi_2(r_1,r_2)\).
Their derivatives in the first leg cancel, while the tangent
\(P_{2,b}(z_2-r_2)\) survives. A strict comparison must retain
that calibration and any induced exterior height change.

In particular, on the frozen periodic hybrid contour the exact
seam \(x=0\) has neighboring cutoff one, whereas \(x=\rho\)
has cutoff zero. An arbitrary complex neighbor is not set to the
real axis in (12)--(13). The exact identity
\(C_{0,N}(1,Y)=N d_N(Y)\), when used for the next block, remains
valid for that actual complex \(Y\).

The [private-row triangle obstruction](research_mixed_cap_private_row_triangle_obstruction.md)
near an actual type-four reference is unchanged: there the outgoing
target is far from this seam, and its private-row triangle sum is
exponentially too large. The present result is a source allowance
for a discarded outgoing region, not a replacement for the coherent
cap packet near its reference.
