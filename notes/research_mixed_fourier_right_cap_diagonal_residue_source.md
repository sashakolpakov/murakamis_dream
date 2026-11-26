# The original finite source carried by the diagonal residues

Research deduction, 7 November 2026. The poles of the shifted
retained chart carry exact original total-index rows. Their
four-current correction simplifies to one outgoing Fourier
factor times those rows, with no residual denominator. This
identifies the residue current and its original phase.

That Fourier factor also pays the positive retained-height
displacement relative to the corresponding real retained
profile. The latter profile has not been compared with the
calibrated plane here. No evaluation, source replay or new
stationary root is used.

## 1. Exact residues and the cancellation of their denominator

Keep the notation and original scalar of
[the shifted-current identity](research_mixed_fourier_right_cap_shifted_current_identity.md).
Thus \(L_N=\lceil N/8\rceil\), \(M_N=\lceil N/2\rceil-1\),
the retained cuts are
\[
 \sigma_-=(L_N-\tfrac12)/N,\qquad
 \sigma_+=(M_N+\tfrac12)/N,
 \qquad q=z+ih_q,\quad 9/20\le z<1,
 \quad -.102\le h_q\le-.001 .
 \tag{1}
\]
Use the same \(T_N(s,q)\), shifted \(\widetilde T_N(s,q)\),
global cardinal \(\widehat f_N(q;y)\), and actual incoming
parameter \(a\). In particular, no incoming finite halfweight
is divided out.

It is convenient to label the poles by their total index
\(\ell=N-k\), rather than their negative factorial index \(k\).
For \(1\le\ell<N\), put
\[
 s_\ell(q)=\ell/N-q,\qquad
 D_{\ell,N}(q)=T_N(s_\ell(q),q),\qquad
 Z_q=e^{-2\pi iNq}.
 \tag{2}
\]
The residue formula and the reciprocal period identity give
exactly
\[
 \begin{split}
 \operatorname*{Res}_{s=s_\ell(q)}\widetilde T_N(s,q)
  &=\frac{1-Z_q}{2\pi iN}\,D_{\ell,N}(q),\\
 2\pi iN\,\frac{e^{2\pi iNs_\ell(q)}}
                    {1-e^{2\pi iNs_\ell(q)}}
       \operatorname*{Res}_{s=s_\ell(q)}\widetilde T_N(s,q)
  &=Z_qD_{\ell,N}(q).
 \end{split}
 \tag{3}
\]
Indeed the numerator factorial has residue
\(P_\ell/(2\pi iN)\), while
\[
 E_N(q-1)=(1-Z_q)E_N(q),\qquad
                  e^{2\pi iNs_\ell(q)}=Z_q.
\]
All other factors have precisely their unshifted values.
Equation (3) is a multiplicative identity; zeros of any
other source factor cause no difficulty.

Consequently the exact additional term in the meromorphic
four-current formula is
\[
 \sum_{\substack{1\le\ell<N\\
           \sigma_-<\ell/N-z<\sigma_+}}
                         Z_qD_{\ell,N}(q).
 \tag{4}
\]
The factor \(1/(1-Z_q)\) in the separate upper-alias kernel
has canceled against the actual residue. It must not be
retained as an extra source multiplier.

## 2. These are original total-index layers

The exact expression in (2) is
\[
 \begin{split}
 D_{\ell,N}(q)={}&
 e^{2\pi iNa(\ell/N-q)}
 \Pi_N(\ell/N-q+a)P_\ell
 E_N(a)E_N(q)E_N(\ell/N-q)^3\widehat f_N(q;y).
 \end{split}
 \tag{5}
\]
At a physical outgoing \(q=l/N\), put \(j=\ell-l\).
Whenever \(0\le l\), \(L_N\le j\le M_N\), and \(\ell<N\),
the original recurrence identifies (5) with
\[
 D_{\ell,N}(l/N)
   =\frac{X^{-j}p_j(X)P_{j+l}}{P_j^3P_l}\,f_l(y).
 \tag{6}
\]
Thus the unchanged central physical source has the exact
alternative enumeration
\[
 V_N^{\rm cen}
   =\sum_{\ell=L_N}^{N-1}
       \sum_{l=\max(0,\ell-M_N)}^{\ell-L_N}
                              D_{\ell,N}(l/N).
 \tag{7}
\]
This is a finite change of indices in the original triangular
support. It does not introduce a physical row with total
index \(N\), nor impose physical support at an off-grid point.
At \(N=2\) the central retained range is empty; otherwise
the same formula applies to both parities.

For a closed outgoing interval \(J\subset[9/20,1)\), define
\[
 J_{\ell,N}
   =J\cap(\ell/N-\sigma_+,\ell/N-\sigma_-).
 \tag{8}
\]
The integrated diagonal correction, including the original
outgoing zero-mode coefficient, is exactly
\[
 \boxed{\qquad
 \mathcal R_N(J)
   =N\sum_{\ell=1}^{N-1}
       \int_{J_{\ell,N}}
        e^{-2\pi iN(z+ih_q)}
                    D_{\ell,N}(z+ih_q)\,dz .
 \qquad}
 \tag{9}
\]
The side-crossing prescription in the shifted-current identity
justifies (9), including the finitely many changes of inventory.
No endpoint term has been discarded. Formula (9) is the first
outgoing Fourier harmonic of these total-index layers, not
their complete lower-alias kernel.

In particular it is not a new Wall value obtained by adding
a physical row or changing its degree. Any further contour
motion in an individual integral of (9) must retain that
fiber's endpoints in (8).

## 3. The original diagonal phase and its finite upper envelope

Write \(h=-h_q\in[.001,.102]\), \(s=u+ih\), and
\(\tau=\ell/N=u+z<1\). The limiting retained range is
\(1/8\le u\le1/2\). Let \(\eta\in\{0,1\}\) be the original
incoming allocation. The allocated regular phase is
\[
 F_\eta(s,a,q)=g(s+a)+g(s+q)-3g(s)
  -(1+\eta/2)g(a)-g(q)+2\pi ias+\ell_q(y).
 \tag{10}
\]
Every \(g\) here is on its original regular-strip branch;
in particular \(g(\tau)\) uses the real value with
\(0<\tau<1\). The output action \(\ell_q(y)\) keeps its
original lift. No period reset of that action is performed.

The complex phase of the diagonal Fourier factor is therefore
\[
 \begin{split}
 \mathscr D_\eta(\tau,q;a)
  ={}&g(\tau-q+a)+g(\tau)-3g(\tau-q)
       -(1+\eta/2)g(a)-g(q)\\
     &+2\pi ia(\tau-q)+\ell_q(y)-2\pi iq .
 \end{split}
 \tag{11}
\]
Its real rate is exactly
\[
 \boxed{\quad
 \mathcal P_\eta(u,z;a)
    =\Re F_\eta(u+ih,a,z-ih)-2\pi h .
 \quad}
 \tag{12}
\]
In particular the Fourier debit is \(2\pi h\), with no
additional index or cardinal normalization.

On a fixed compact actual parameter family and a fixed
\(J\Subset[9/20,1)\), for every prescribed \(\epsilon>0\),
the original finite upper estimates give
\[
 |d_N(X)|^{\eta/2}|Z_qD_{\ell,N}(q)|
       \le C_\epsilon N^{A_\epsilon}
                    e^{N(\mathcal P_\eta(u,z;a)+\epsilon)}
 \tag{13}
\]
uniformly on all fibers (8), with their actual half-grid
endpoints, for all sufficiently large \(N\) of either parity.
Here the constants and threshold may depend on \(\epsilon\),
but not on \(N\) or \(\ell\).
To see the boundary scope of this estimate, keep the factor
\(P_\ell\) in (5) physical and use the original uniform bound
\[
                 \log|P_\ell|=N J(\ell/N)+O(\log N),
                         \qquad 0\le\ell<N,
 \tag{14}
\]
as in
[the retained-rate source proof](research_mixed_fourier_right_cap_coherent_retained_rate.md).
All other factorial arguments in (5) stay in fixed regular
strips; \(q-y\) stays in the original cardinal strip.
The incoming weight uses its original arbitrarily small
rate-tolerance upper bound, including its possible zeros,
as in the cited retained-rate proof. These facts prove (13),
also when \(\ell=N-1\). No tolerance-free polynomial bound
for that weight is inferred. The unweighted row itself
has the polynomial upper bound just described.

On a smaller domain where \(\tau\) stays away from one,
the ordinary nonzero row symbol has power \(N^{-5/2}\),
as in the original joint chart. That nonvanishing symbol
is not asserted uniformly at the endpoint \(\tau=1\).
The polynomial upper bound (13) is sufficient for the
entire residue inventory. The outside \(N\) and the at most
\(N-1\) layers in (9) are further polynomial factors only.

## 4. The residue debit pays the retained height increase

The following derivative estimate was also obtained independently
in the shifted-current analysis. It requires only the stated
actual real ranges; it does not assume a new stationary equation.

**Lemma.** For \(1/8\le u\le1/2\), \(z\ge9/20\),
\(u+z<1\), \(0\le v\le h\le.102\), and the original
\(\Re a=x\in[11/50,9/20]\),
\[
 \Im F_{\eta,s}(u+iv,a,z-ih)>-\frac{387\pi}{200}.
 \tag{15}
\]

For the proof put
\[
 A(t,b)=\arg(1-e^{2\pi b-2\pi it})
\]
on the original strip lift. If \(u\le1/4\), the radial
argument inequalities imply
\[
 A(u+x,v+\Im a)+2\pi x\ge11\pi/25.
 \tag{16}
\]
Indeed when \(u+x\le1/2\) the argument is nonnegative,
and otherwise the sum is at least \(\pi(1-2u)\ge\pi/2\).
The argument with real part \(u+z<1\) and height \(v-h\le0\)
is greater than \(-\pi/2\).
Finally
\[
 A(u,v)<5\pi/8 \qquad(u\ge1/8,\ 0\le v\le.102).
 \tag{17}
\]
For (17), its radius is less than two, and its real angle
is at least \(\pi/4\). On this range the argument decreases
with the angle and increases with the radius. At radius two
and angle \(\pi/4\), it equals
\(\pi-\arctan(2+\sqrt2)<5\pi/8\), since
\(\tan(3\pi/8)=1+\sqrt2<2+\sqrt2\).
The same conclusion is immediate if \(u=1/2\).
Combining (16)--(17) with the coefficient \(-3\) of \(g'(s)\)
gives
\[
 11\pi/25-\pi/2-15\pi/8=-387\pi/200.
 \tag{18}
\]

For \(u\ge1/4\), the corresponding lower bound, divided by
\(\pi\), is
\[
 \min(11/25,1-2u)-1/2-3(1-2u)\ge-39/25,
 \tag{19}
\]
which is stronger than (15). This proves the lemma.
At the finite lower half-grid endpoint an \(O(1/N)\)
displacement changes these bounds by \(O(1/N)\), uniformly;
the own and first-incident arguments stay in fixed regular
strips. The separate bound for \(g'(s+q)\) is uniform up
to its real endpoint: it remains greater than \(-\pi/2\)
in imaginary part and requires no derivative or Lipschitz
estimate as \(\ell/N\) approaches one.

Integrating (15) at fixed \(q=z-ih\) now gives
\[
 \boxed{\quad
 \mathcal P_\eta(u,z;a)
   <\Re F_\eta(u,a,z-ih)-\frac{13\pi}{200}h .
 \quad}
 \tag{20}
\]
The finite half-grid version allows a uniform \(O(1/N)\)
addition, hence only a bounded multiplicative factor in
(13). Thus the outgoing Fourier debit genuinely pays
raising the retained variable from zero to its pole height.
It does not compare the real retained profile on the right
of (20) with the original critical-height plane.

For possible further motion at fixed total index, the exact
derivative identity is
\[
 \partial_q\mathscr D_\eta
       =F_{\eta,q}-F_{\eta,s}-2\pi i.
 \tag{21}
\]
For \(q=z-iH\) this gives
\[
 \frac{d}{dH}\Re\mathscr D_\eta(\tau,z-iH;a)
       =-\Im(F_{\eta,s}-F_{\eta,q})-2\pi .
 \tag{22}
\]
No sign for (22) is claimed. A bound on the original real
profile in (20), or a justified fiber deformation using
(22) with all endpoint currents retained, is still needed
to pay the diagonal correction. The shifted main and
unpenalized top current have their separate obligations.
