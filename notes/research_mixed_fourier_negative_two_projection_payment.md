# A paid endpoint observation after two negative crossings

Research deduction, 7 November 2026. The exact first coefficient
after the signed run \(-2\) is an already paid physical endpoint
of the original coherent Fourier cap. This gives a finite-source
gap, and a local holomorphic estimate relative to the original
whole-cap packet, without estimating an unmarked terminal-power
vector in place of its actual observation.

The comparison action is the original cap action. No action or
nonzero packet for the complete twice-crossed source is inferred.
No numerical evaluation is used.

## 1. The exact observation is the original final coherent row

Use the conventions of
[the signed coefficient dictionary](research_mixed_fourier_signed_crossing_coefficients.md):
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 r=q^{-2},\quad P_j=(r;r)_j,\quad \kappa=q^{D^2/2},
 \qquad X=e^{-2\pi ia},\quad Y=e^{2\pi iy}.
 \tag{1}
\]
The original cap and its first Fourier projector are
\[
 Z_N(a,y)=\sum_{l=0}^{D}C_{1,N}(X,r^l)f_l(y),
 \qquad
 \Pi_0G=[f_0]G\,f_0,\qquad
 f_0(y)=\frac{e^{-\pi iDy}(1-Y^N)}{N(1-Y)}.
 \tag{2}
\]
The exact signed crossing is \(\mathcal M_{-2}\), with all the
normal data and the original \(\kappa^{-2}\) normalization retained.
Equation (20) of the signed dictionary gives
\[
 [f_0]\mathcal M_{-2}Z_N
       =\frac{\kappa^{-2}}{N^2}\sum_{j=0}^{D}X^{-j}.
 \tag{3}
\]
Consequently, writing \(\mathcal P_{-2,N}=\Pi_0\mathcal M_{-2}Z_N\),
\[
 \boxed{\quad
 \mathcal P_{-2,N}(a,y)=
 \frac{\kappa^{-2}e^{-\pi i(N-1)y}
       X^{-(N-1)}(1-X^N)(1-Y^N)}
      {N^3(1-X)(1-Y)}
             =\kappa^{-2}c_N(y)T_{D,N}(a,y).
 \quad}
 \tag{4}
\]
The quotients in (4) are interpreted by their finite polynomial
identities at \(X=1\) or \(Y=1\). The last equality is exactly
equation (22) of
[the coherent endpoint payment](research_mixed_fourier_right_cap_endpoint_payment.md),
with its original \(c_N,T_{D,N}\).
In particular this is one whole outgoing contraction, not a
term chosen after taking absolute values in the outgoing sum.

For completeness, its degree-zero Wall factor is one, while
\[
 (rX;r)_D=\frac{1-X^N}{1-X},\qquad P_D=N.
 \tag{5}
\]
Thus the endpoint has precisely the three factors \(1/N\) in
(4): its two retained factorials and the original cardinal.
No additional sum or crossing scalar is suppressed. The derivation
of (3), and hence (4), used the full \(M^*J\) observation in the
signed dictionary before its special simplification at \(n=-2\).

## 2. Its allocated finite-source gap on the original plateau

Fix an actual reference \(a_*\in K_{3+\eta}\), \(\eta=0,1\),
and its original correlated Fourier-cap critical point at
\(y=x_0\). The incoming target is
\[
 a=x+i\Im a_*,\qquad x\in P=[11/50,9/20].
 \tag{6}
\]
For \(\eta=1\) retain the original unselected incoming height
and halfweight. Write the original plane as
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                  -\kappa_*(x-\Re a_*)^2,\qquad
 \kappa_*=\frac1{2500000}.
 \tag{7}
\]
Here \(\kappa_*\) is a real curvature coefficient, distinct
from the unit crossing scalar \(\kappa\) in (1).

The exact endpoint rate and its proved comparison are
\[
\begin{split}
 E_{\rm end,\eta}(a;x_0)
   &=2\pi(-\Im a_*)_++\pi\Im x_0
                           -\frac{\eta}{2}\Re g(a),\\
 E_{\rm end,\eta}(a;x_0)
   &<B_\eta(x)-\frac{387}{70000}.
\end{split}
 \tag{8}
\]
These are equations (19)--(20) of the endpoint-payment theorem.
They use the completed original inner last-row inequality and
the actual outgoing cardinal surplus. They require neither an
extension of the unit-circle Wall packet nor a new root.

Since \(|\kappa|=1\), the individual final-row estimate in that
proof applies directly to (4). For every \(\tau>0\),
\[
 |d_N(X)|^{\eta/2}|\mathcal P_{-2,N}(a,x_0)|
 \le C_\tau N^{A_\tau}
    \exp N\left\{B_\eta(x)-\frac{387}{70000}+\tau\right\}.
 \tag{9}
\]
In particular, for sufficiently large levels of both parities,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}|\mathcal P_{-2,N}(a,x_0)|
              \le e^{N\{B_\eta(x)-1/200\}}.
 \quad}
 \tag{10}
\]
Every incoming zero is retained. This argument does not divide
by \(d_N\) on the horizontal target interval, or infer an
individual row bound by subtracting two canceled finite sums.

## 3. A local comparison with the original whole cap

The gap also gives a holomorphic statement near each actual
reference, with all fixed derivatives. Let
\(\lambda_0=(a_*,x_0)\), and use the original phase
\(\Phi(a,y)\) and nonzero amplitude \(\mathcal A(a,y)\) of
[the complete holomorphic cap packet](research_mixed_fourier_right_cap_holomorphic_packet.md):
\[
 Z_N(a,y)=N^{-3/2}\mathcal A(a,y)e^{N\Phi(a,y)}
                                         (1+O(N^{-1})).
 \tag{11}
\]
The unallocated endpoint rate is the continuous function
\[
              e_{\rm end}(a,y)=2\pi(-\Im a)_++\pi\Im y .
 \tag{12}
\]
At the center, the incoming allocation cancels between the
two sides of (8), because
\[
 M_\eta=\Re\Phi(a_*,x_0)-\frac{\eta}{2}\Re g(a_*).
 \tag{13}
\]
Hence
\[
 e_{\rm end}(\lambda_0)
              <\Re\Phi(\lambda_0)-\frac{387}{70000}.
 \tag{14}
\]
The exact expression (4), on any sufficiently small compact
parameter neighborhood with \(|Y|<1\) and \(X,Y\ne1\), gives
\[
 |\mathcal P_{-2,N}(a,y)|
                \le C N^{-3}e^{N e_{\rm end}(a,y)}.
 \tag{15}
\]
For (15), use the finite expression
\(X^{-D}(1-X^N)=X^{-D}-X\); its two terms are bounded
uniformly by a constant times \(e^{2\pi N(-\Im a)_+}\).
The factor \(1-Y^N\) is uniformly bounded. Thus (15) remains
valid across \(\Im a=0\), including its exact zeros.

Choose a smaller fixed neighborhood \(U\) on which
\[
 e_{\rm end}(a,y)-\Re\Phi(a,y)<-\delta_1,\qquad
                  \frac1{200}<\delta_1<\frac{387}{70000}.
 \tag{16}
\]
It exists by (14) and continuity, after shrinking the
neighborhood in (11). The whole cap is nonzero there for all
sufficiently large \(N\). Consequently
\[
 R_{-2,N}(a,y)=\frac{\mathcal P_{-2,N}(a,y)}{Z_N(a,y)}
 \tag{17}
\]
is holomorphic on \(U\), and (11), (15)--(16) bound it by
\(C N^{-3/2}e^{-N\delta_1}\).
For every \(U'\Subset U\) and fixed multi-index \(\alpha\),
Cauchy's inequality on intermediate parameter polydisks gives
\[
 \boxed{\qquad
 \sup_{U'}|\partial^\alpha R_{-2,N}|
                         \le C_{\alpha,U'}e^{-N/200}.
 \qquad}
 \tag{18}
\]
No weight division is needed for this deduction: (14) is a
phase comparison at the center, and (15) is an unallocated
exact finite-source bound.

When \(\Im a_*<0\), the projected observation itself has the
additional elementary nonzero packet
\[
 \mathcal P_{-2,N}(a,y)
   =\kappa^{-2}N^{-3}
       \frac{X e^{\pi iy}}{(1-X)(1-Y)}
       e^{N(2\pi ia-\pi iy)}(1-X^N)(1-Y^N).
 \tag{19}
\]
On a smaller neighborhood \(|X|,|Y|<1\), the last two
factors equal \(1+O(e^{-\epsilon N})\), with the same
property for every fixed derivative after reducing
\(\epsilon>0\). Its displayed amplitude is nonzero there.
All actual type-four incoming references have this negative
height. Formula (19) is an exact elementary observation
phase; it is not identified here with the geometric action
of the complete crossed source.

## 4. What remains for crossing transport

Equations (10), (18) pay a nontrivial signed endpoint
observation relative to the original cap. They do not give
a packet for \(\mathcal M_{-2}Z_N\), and therefore do not
justify replacing \(Z_N\) by that complete crossed source
in the denominator of (17).

For any fixed signed run \(n\), the exact observation remains
\[
 \Pi_0\mathcal M_n Z_N
     =\mathcal A_{n,N}(X)f_0(y),\qquad
 \mathcal A_{n,N}(r^b)
     =\frac{(-q)^{-b}}{\kappa N}
                     (M^*J\,\mathbf h^{(n+2)})_b .
 \tag{20}
\]
The general \(M^*J\) is unchanged. A proposed nonzero
geometric packet with phase \(\Phi_n\) on an actual
parameter neighborhood would still need the concrete
observation comparison
\[
 |\mathcal A_{n,N}(e^{-2\pi ia})f_0(y)|
       \le C N^A e^{N\{\Re\Phi_n(a,y)-\delta\}},
                         \qquad \delta>0,
 \tag{21}
\]
if its endpoint projection is to be discarded. The complete
crossed packet and its own complementary source estimates
are also required. Even for \(n=-2\), (21) relative to
\(\Phi_{-2}\) is not asserted: (10), (18) instead prove the
precise comparison with \(\Phi\).

Thus an actual short-run endpoint term is now paid, but
iteration over arbitrary short fillings and the ordinary
closing lower bound remain separate.
