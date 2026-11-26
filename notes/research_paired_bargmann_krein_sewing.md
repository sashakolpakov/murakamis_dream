# A homogeneous Bargmann kernel for the physical Krein pairing

Written research proof, 23 November 2026. The physical Hermitian
pairing has an exact double-Gaussian realization with one homogeneous
binomial kernel. The actual factorial frame is conformal for this
pairing, with scalar \(N\) per head. Its paired gluing therefore
requires neither an incomplete-exponential approximation nor an unknown
factorial-frame metric. Original exterior rows and both cap types remain.

The form is indefinite. Its explicit nonzero kernel symbol is not a
noncancellation theorem for an arbitrary marked closing. In particular,
the physical operator, coefficient-form matrix, and Gaussian Riesz
operator are distinguished throughout.

## 1. Original finite coefficients and Gaussian moments

Fix \(N\geq2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
and \(x=-q^{-1}\). On the original balanced head put
\[
 F_a=(Q;Q)_a,\quad G_F=\operatorname{diag}(F_a),\qquad
 H_N=q^{-1}Z^{-1}R_d,\quad H_N|a\rangle=qQ^a|d-a\rangle .
 \tag{1}
\]
Here \(Z|a\rangle=Q^a|a\rangle\), \(R_d|a\rangle=|d-a\rangle\),
and \(0\leq a\leq d\). Thus \(H_N^\dagger=H_N\), \(H_N^2=I\).
Use exactly the finite Gaussian calculus of [B]:
\[
 \begin{gathered}
 P_u(z)=\sum_{a=0}^d u_az^a,\qquad
 d\mu_N(z)=\frac N\pi e^{-N|z|^2}\,d^2z,\qquad
 h_a=\frac{a!}{N^a},\\
 \int z^a\bar z^{\,b}\,d\mu_N(z)=\delta_{ab}h_a,\qquad
 \mathcal K_A(z,w)=\sum_{a,b=0}^d z^aA_{ab}\frac{(Nw)^b}{b!}.
 \end{gathered}                                                   \tag{2}
\]
Angular integration and one elementary gamma integral prove the moment
identity. Finite kernels compose with this measure and have trace
integral \(\operatorname{Tr}A\). The identity kernel is
\(E_d(Nzw)\), \(E_d(s)=\sum_{a=0}^d s^a/a!\), retaining its full cutoff.

## 2. Exact paired integral

Let \(h=\operatorname{diag}(h_a)\). The Gaussian Riesz operator of
the coefficient form \(u^\dagger H_Nv\) is \(h^{-1}H_N\).
Its exact kernel is
\[
 \boxed{\quad
 \mathscr K_N(z,w):=\mathcal K_{h^{-1}H_N}(z,w)
                =q\frac{N^d}{d!}(z+Qw)^d .\quad}        \tag{3}
\]
Indeed column \(b\) has its sole nonzero entry in row \(d-b\),
giving coefficient \(qQ^bN^d/[(d-b)!b!]\). The ordinary binomial
theorem proves (3), including both endpoints. All its scalars remain.

For arbitrary full coefficient vectors \(u,v\),
\[
 \boxed{\quad u^\dagger H_Nv=
 \iint\overline{P_u(z)}\,\mathscr K_N(z,\bar w)P_v(w)
                                      \,d\mu_N(z)d\mu_N(w).\quad}
 \tag{4}
\]
The first integral pairs a row index with \(\bar u_a h_a\);
the second pairs \((N\bar w)^b/b!\) with \(v_b\). Their result is
\(u^\dagger h(h^{-1}H_N)v\). All sums are finite, so the double
Gaussian integral is absolutely convergent without asymptotic assumptions.
The kernel is Hermitian in the paired variables, since
\(\bar qQ^{-d}=q\).

For clarity, the operator \(H_N\) itself has a different kernel:
\[
 \mathcal K_{H_N}(z,w)=qz^dE_d(QNw/z).                 \tag{5}
\]
Its apparent singularity is removable by the finite sum. A cutoff
transition in (5) is not an obstruction to (4), which uses (3).
Also \((h^{-1}H_N)^2\) has diagonal entries
\(1/(h_ah_{d-a})\); the Gaussian Riesz operator is not an involution.
Only the coefficient-form matrix \(H_N\) squares to the identity.

## 3. The actual factorial congruence and row transport

There is an exact phased complement, stronger than a modulus identity:
\[
 F_a\overline{F_{d-a}}=N,\qquad
 \boxed{\quad G_F^\dagger H_NG_F=NH_N.\quad}           \tag{6}
\]
Indeed \(F_d=N\), and its factors from \(a+1\) through \(d\) are
the factors \(1-Q^{-j}\), \(1\leq j\leq d-a\), in reverse order.
Thus \(F_d/F_a=\overline{F_{d-a}}\). Inserting this in each
anti-diagonal entry proves the second formula.

On \(r\) heads put \(G=G_F^{\otimes r}\) and
\(\mathscr H_r=H_N^{\otimes r}\). Then
\[
 (Gu)^\dagger\mathscr H_r(Gv)=N^r u^\dagger\mathscr H_rv.
 \tag{7}
\]
The right side is the tensor product of the paired integrals (4),
with the displayed \(N^r\). This is precisely the factorial frame
used in [B], with all phases rather than only its singular values.
For \(T=G^{-1}AG\), any already proved identity
\(A^\dagger\mathscr H_rA=\mathscr H_r\) therefore implies
\(T^\dagger\mathscr H_rT=\mathscr H_r\). This applies to the
unreduced signed physical words of [H]. It does not identify the
reduced word of [B] with such an isometry after a head is eliminated.

Congruence is not similarity. The actual physical operator \(H_N\),
written in factorial coordinates, is
\[
 G_F^{-1}H_NG_F|a\rangle
       =qQ^a\frac{|F_a|^2}{N}|d-a\rangle .             \tag{8}
\]
It is neither the coefficient-form matrix \(H_N\) nor the Gaussian
Riesz matrix \(h^{-1}H_N\). No positive condition-number estimate
for the factorial frame follows from (6).

Every original bilinear row \(\lambda\) has the explicit coefficient
form-dual vector \(z_\lambda=\mathscr H_r\lambda^\dagger\), so that
\(\lambda y=z_\lambda^\dagger\mathscr H_ry\).
In factorial coordinates \(y=Gu\), the actual row is
\(\eta=\lambda G\). Its corresponding vector satisfies
\[
 v_\eta=\mathscr H_r\eta^\dagger=N^rG^{-1}z_\lambda,
 \qquad \lambda y=v_\eta^\dagger\mathscr H_ru .           \tag{9}
\]
Equations (4),(9) preserve an arbitrary original exterior. The original
Cartan-weighted traces and first meridian derivative in [B] are applied
by linearity to the same coefficient identities. They are not replaced
by a squared norm or an independently selected row.

## 4. Literal ordinary and marked cap functions

Set
\[
 c(z)_a=\frac{(N\bar z)^a}{a!},\qquad
 \mathcal F_N(t)=\sum_{a=0}^d F_a\frac{t^a}{a!},\qquad
 B_N(z,w)=\sum_{a=0}^d\binom da q^{a^2}z^aw^{d-a}.
 \tag{10}
\]
These are specified full finite packets and polynomials. The unrestricted
marked row is \(\ell_m|a,b\rangle=x^b/N^2\) [H]. Hence
\[
 \boxed{\quad
 \ell_m(G_Fc(z)\otimes G_Fc(w))
       =N^{-2}\mathcal F_N(N\bar z)\mathcal F_N(Nx\bar w).
 \quad}                                                   \tag{11}
\]
The ordinary cap is \(\ell_o|a,b\rangle=x^a\delta_{a+b,d}/N\).
Using \(F_aF_{d-a}=N(-1)^aQ^{a(a+1)/2}\) gives
\[
 \ell_o(G_Fc(z)\otimes G_Fc(w))
                      =\frac{N^d}{d!}B_N(\bar z,\bar w).
 \tag{12}
\]
Indeed \(x^a(-1)^aQ^{a(a+1)/2}=q^{a^2}\).
Only when the actual assembled source forces this pair to integer
degree \(d\) may the marked row be replaced by its restriction
\(\ell_{m,d}\). For that restriction the exact formula is
\[
 \ell_{m,d}(G_Fc(z)\otimes G_Fc(w))
          =\frac{x^dN^{d-1}}{d!}B_N(Q\bar z,\bar w).
 \tag{13}
\]
Its extra phase is \(q^{2a}=Q^a\). Equation (13) is not a formula
for the unrestricted row on an arbitrary exterior; (11) is.

These cap functions retain a known finite Gaussian chirp:
\[
 B_N(z,w)=\exp\!\left[\frac{\pi i}{N}(z\partial_z)^2\right](z+w)^d,
 \qquad
 \mathcal F_N'(t)=\mathcal F_N(t)-Q\mathcal F_N(Qt),\quad
 \mathcal F_N(0)=1 .                                    \tag{14}
\]
The first equality is a finite diagonal operation on degrees through
\(d\). The second follows from \(F_{a+1}=(1-Q^{a+1})F_a\);
the potential top term is zero because \(1-Q^N=0\).
No reflection rule for a separated ray moment is being assumed.
The original cup, pivots, framing/peripheral lines, and the full marked
row remain in (9) or (11); none becomes (3) by a choice of metric.

## 5. Local symbol and exact coefficient-dual packet inversion

For independent complex arguments let \(L_N=z+Qw\) and \(L=z+w\).
The only zero divisor of (3) is \(L_N=0\), of order \(d\).
On a fixed compact chart where \(L\ne0\), choose a local logarithm.
Stirling's formula and the first quantum shift give uniformly
\[
 \mathscr K_N(z,w)=N^{-1/2}
    \frac{\exp(2\pi i w/L)}{\sqrt{2\pi}\,L}
       \exp\{N(1+\Log L)\}(1+O(N^{-1})).               \tag{15}
\]
Indeed \(N^d/d!=e^N/\sqrt{2\pi N}(1+O(N^{-1}))\), and
\(N\Log L_N=N\Log L+2\pi i w/L+O(N^{-1})\).
The exact phase \(q\) and shift \(Q\) remain in (3); the shift
produces the nonzero finite amplitude factor in (15).

There is also an exact action on coefficient polynomials, without any
incomplete-exponential estimate:
\[
 \boxed{\qquad P_{H_Nu}(z)=qz^dP_u(Q/z).\qquad}         \tag{16}
\]
It is a polynomial even at zero. If a supplied actual coefficient
packet has a relative expansion
\(P_{u_N}(w)=c_NN^aA(w)e^{N\phi(w)}(1+O(N^{-1}))\)
on a fixed neighborhood of \(f\ne0\), then on a corresponding
neighborhood of \(f^{-1}\), (16) gives
\[
 P_{H_Nu_N}(z)=c_NN^a\frac{qA(Q/z)}z
       \exp\{N[\Log z+\phi(Q/z)]\}(1+O(N^{-1})).       \tag{17}
\]
The relative error is merely pulled back. The amplitude is nonzero
if the input amplitude is. Formula (17) concerns the coefficient
\(H_N\)-action or the specified coefficient form-dual packet.
It does not replace the physical similarity (8) or the Gaussian
Riesz operator by that action.

At principal order the occupation transforms as
\(z\partial_z[\Log z+\phi(1/z)]=1-w\phi'(w)\), \(w=1/z\).
Thus the lower resolved point \((f,0)\) of [B] is paired with an
upper occupation, with its distinct logarithmic mark retained.
The form kernel is regular at the associated matched seam: complexify
the Gaussian variables to \((z,\zeta,w,\omega)\). Its principal
seam phase is \(\Log(z+\omega)-z\zeta-w\omega\), giving
\[
 \zeta=w=\frac1{z+\omega},\qquad \zeta z+w\omega=1 .
 \tag{18}
\]
This is the Gaussian FORM-dual seam: its left row coordinates are
\((\zeta,z)\). It is different from (17), whose coefficient-action
output has polynomial coordinate \(z_{\rm out}\). The two maps are
not identified by their common occupation reflection.
For the lower right point \((w,\omega)=(f,0)\), this gives
\((\zeta,z)=(f,f^{-1})\) and kernel linear form \(f^{-1}\ne0\).
The mixed kernel derivative is \(-1/(z+\omega)^2\ne0\).
This verifies a nonzero local seam symbol on these matched charts,
uniformly for \(f\) in compact subsets of \(\mathbb C^*\).

It does not prove that the actual marked exterior is that dual packet,
that a full composed stationary Hessian is nondegenerate, or that
complementary regions have smaller rate. All finite integrals above
remain whole; no source-current component or integration region has
been discarded. The caps (11)--(13) still require their actual phase
analysis in a general short component. No scalar lower bound follows
from the indefinite form or local ellipticity alone.

## Complete proof sources and coverage

- [B] [Actual reduced word Bargmann source period](research_reduced_word_bargmann_source_period.md), 565 lines, SHA-256 `abbe118e89f2d80f82f4bcd591a71dc193fda852cd488262461d07b262696655`.
- [H] [Common physical tensor Krein form](research_physical_tensor_krein_crossing_form.md), 286 lines, SHA-256 `610b5ac7d889429163ec230e9d644d174d38382733dbad57826fce66cec8e348`.

The complete [common-spin first-jet dual](research_reduced_common_spin_first_jet_dual.md),
387 lines, SHA-256 `1ba0870e39871de7cf7b53a041e5c47d133dc8ee3755aa8b99df71ae810b9f6f`,
and [compact coherent source calculus](compact_coherent_source_period.md),
469 lines, SHA-256 `8c6c3277367a4aa6c69269da635139d5f881f3d3d0d894e04dd97028d76537e4`,
are coverage only. Coherent kernels and their resolutions are established
methods. The proof above specifies the physical indefinite pairing,
its exact factorial congruence, and its unchanged original boundary.
