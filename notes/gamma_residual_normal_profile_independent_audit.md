# An exact pointed unit comparison for the factorial source factor

Proof and independent audit, 27 October 2026. The normal quantum
factorial residual has the stated whole Gamma profile. More strongly,
its middle component is exactly a holomorphic unit times the actual
root Weyl splitting after the correct normal-coordinate change.
The unit preserves all finite resonance zeros, is normalized at the
complete point, and tends uniformly to one. This is an actual scalar
source-factor comparison, not a comparison of the full knot period.

Use the exact factorial frames of
[the integral-color source](integral_color_global_q_difference_source.md)
and the marked root splitting of
[the balanced Weyl cocycle](twisted_cotangent_source_and_weyl_gluing.md).

## 1. Exact normal product and its whole limit

Put
\[
 c=2\pi i,\quad H_0=c/N,\quad H=H_0+ca/N^2,\quad
 q=e^{H/2},\quad M=-q^N=e^{ca/(2N)},
\]
and set
\[
 b=a_N=\frac{a}{1+a/N},\qquad
 J(x)=\frac{2\sinh(x/2)}x,\quad J(0)=1 .
\]
Then \(Hb=ca/N\). For the actual residual diagonal factor
\[
 V_{N,j}(a)=\frac{{N-1\choose j}_{q,\rm sym}}{M^j},
\]
the exact identity is
\[
 V_{N,j}(a)
  =e^{-Hbj/2}
     \prod_{r=1}^j
       \frac{\sinh[H(r-b)/2]}{\sinh(Hr/2)}.       \tag{1}
\]
There is no extra sign: \(HN=c+Hb\) gives
\(\sinh[H(N-r)/2]=\sinh[H(r-b)/2]\).

For \(j/N=T_N\) in a compact subinterval of \((0,1)\),
uniformly on every compact complex \(a\)-set,
\[
 N^aV_{N,j}(a)
   =\Phi_a(T_N)+O((1+\log N)/N),\qquad
 \Phi_a(T)=\frac{G(T)^{-a}}{\Gamma(1-a)},          \tag{2}
\]
where
\[
 G(T)=\frac{e^{cT}-1}{c},\qquad
 \log G(T)=\log\!\left(\frac{\sin\pi T}{\pi}\right)
                                     +cT/2.     \tag{3}
\]
Positive real \(N\) specifies \(N^a=e^{a\log N}\).

Here is a proof uniform through integer resonances. Factor (1) into
\[
 e^{-Hbj/2}
 \prod_{r=1}^j(1-b/r)
 \prod_{r=1}^j\frac{J(H(r-b))}{J(Hr)}.           \tag{4}
\]
The Euler product implies
\[
 j^b\prod_{r=1}^j(1-b/r)
       =\Gamma(1-b)^{-1}+O(1/j)
\]
uniformly on compact \(b\)-sets. One may prove this directly
using \((1-b/r)e^{b/r}=1+O(r^{-2})\) and
\(H_j-\log j=\gamma+O(1/j)\). The product convergence is
uniform and absolute, including its zeros; no relative estimate
at a zero is used.

On a fixed zero-free neighborhood of \([0,cT_{\max}]\), choose
\(B=\log J\), \(B(0)=0\). Taylor expansion and a Riemann sum give
\[
 \sum_{r=1}^j[B(H(r-b))-B(Hr)]
       =-bB(Hj)+O(1/N).
\]
The remaining factors have limits
\(e^{-caT/2}\), \(T^{-a}\), and \(J(cT)^{-a}\).
Their product is (3). Finally
\(N^{a-b}=1+O((1+\log N)/N)\), which explains the stated error.
All errors in (2) are absolute. At positive integer \(a\) the
limit can vanish.

## 2. The actual Weyl factor has the opposite Gamma profile

Let \(Q_0=e^{H_0}\), and let \(\beta_N\) be the exact root
splitting, with its prescribed even phase:
\[
 L_N=\begin{cases}(N-1)/2&N\text{ odd},\\N/2-1&N\text{ even},
 \end{cases}
\]
\[
 \beta_N(M)=
   \prod_{r=1}^{L_N}\frac{1-M^2Q_0^r}{1-Q_0^r}
   \times
   \begin{cases}1&N\text{ odd},\\
                 (1+iM)/(1+i)&N\text{ even}.
   \end{cases}                                      \tag{5}
\]
For \(M=e^{ca/(2N)}\),
\[
 N^{-a}\beta_N(M)
       \longrightarrow
       \frac{G(1/2)^a}{\Gamma(1+a)}
       =\Phi_{-a}(1/2)                              \tag{6}
\]
uniformly on compact \(a\)-sets, with absolute error \(O(1/N)\).
Indeed each quotient in (5) is
\[
 e^{H_0a/2}\frac{r+a}{r}
                  \frac{J(H_0(r+a))}{J(H_0r)}.
\]
The same Euler-product and smooth-product calculation proves (6).
The even prefactor tends to one uniformly. Its marked phase
introduces no extra constant. In particular
\[
 G(1/2)=i/\pi,\qquad\log G(1/2)=-\log\pi+\pi i/2 .
\]

## 3. Exact finite comparison, including every normal zero

The proper opposite meridian coordinate is
\[
 \widetilde M_N(a)=e^{-H_0b/2},\qquad b=a_N,
\]
not \(e^{-H_0a/2}\). At \(j=L_N\), there is the exact identity
\[
 V_{N,L_N}(a)=u_N(a)\,\beta_N(\widetilde M_N(a)), \tag{7}
\]
with
\[
 u_N(a)=e^{-(H-H_0)bL_N/2}
   \prod_{r=1}^{L_N}
   \frac{J(H(r-b))J(H_0r)}
        {J(Hr)J(H_0(r-b))}
   \times
   \begin{cases}1&N\text{ odd},\\
     (1+i)/(1+i\widetilde M_N)&N\text{ even}.
   \end{cases}                                      \tag{8}
\]
Equation (7) follows by factoring the two sine products; their
entire factors \((r-b)/r\) cancel before evaluating zeros.
Thus it holds at the resonance points by holomorphic continuation.

All factors in (8) are units on \(|b|<N/2\). To check this
without assuming separation from integer \(b\), the only zeros
of \(J\) are \(ck\), \(k\ne0\). Using
\(H=H_0/(1-b/N)\), each possible zero of the four displayed
arguments has \(|b|\ge N/2\) for \(r\le L_N\).
The even prefactor likewise first vanishes at
\(|b|=N/2\). Thus every fixed compact normal set is contained
in this unit domain for all sufficiently large \(N\).
In particular
\[
 u_N(0)=1,\qquad u_N(a)=1+O(1/N)                 \tag{9}
\]
uniformly on compact sets.

For the bound in (9), take \(B=\log J\) on a fixed zero-free
neighborhood of \([0,c/2]\) and put \(\Delta H=H-H_0=O(N^{-2})\).
The logarithm of each four-factor quotient is
\[
 \Delta H\left[(r-b)B'(H_0(r-b))-rB'(H_0r)\right]
       +O(\Delta H^2r^2).
\]
The bracket is \(O(1)\), not \(O(r)\), by differentiating
\(xB'(H_0x)\) over the bounded displacement \(b\).
Summing \(O(N)\) terms gives \(O(1/N)\); the quadratic remainders,
phase and even prefactor have that same bound. There is no
uncontrolled logarithmic loss here.

The coordinate correction is essential for a unit statement.
The quantum factor has zeros at
\(a=kN/(N-k)\), whereas the uncorrected
\(\beta_N(e^{-H_0a/2})\) has zeros at \(a=k\).
Their limits agree, but their ratio is not a unit at those
finite-\(N\) divisors. Using \(b=a_N\) aligns them exactly.

It also matches the marked power character exactly. On the
integral-color curve \(M_{\rm col}=e^{Hb/2}\), the inverse-flux
period of
[the peripheral-character calculation](gauss_wall_flux_and_actual_peripheral_character.md)
is
\[
 \chi_H(M_{\rm col})=e^{-2c\log M_{\rm col}/H}=e^{-cb}.
\]
The root meridian used in (7) satisfies
\[
 \widetilde M_N^{\,2N}=e^{-cb}=\chi_H(M_{\rm col}).
\]
Thus its inverse-power character is the opposite oriented one.
This is an identity of the specified whole functions; it does
not assume an off-root horizontal equation for a knot state.

## 4. Normalized difference line and its actual Weyl norm

The whole limiting function satisfies
\[
 \Phi_{a+1}(T)=-\frac{a}{G(T)}\Phi_a(T).          \tag{10}
\]
Its paired norm is
\[
 \Phi_a(T)\Phi_{-a}(T)
       =\frac1{\Gamma(1-a)\Gamma(1+a)}
       =\frac{\sin\pi a}{\pi a}
       =\frac{2\sinh(z/2)}z,\qquad z=ca.        \tag{11}
\]
The normalization can be checked without importing a reflection
formula: apply (6) with \(a,-a\) to the already proved finite
identity \(\beta_N(M)\beta_N(M^{-1})=c_N(M)^{-1}\).
Its right side is exactly
\(\sinh(z/2)/(N\sinh(z/(2N)))\), which tends to (11).
The \(T\)-dependent factors cancel, so the result holds for
every interior \(T\).

The norm line has shift
\[
 (a+1)H(a+1)=-aH(a),\qquad H(a)=\sin(\pi a)/(\pi a).
\]
Cocycle orientation must remain explicit:
\[
 c_N(e^{z/(2N)})\to\Gamma(1-a)\Gamma(1+a),\qquad
 c_N^{-1}\to H(a).
\]

Equations (7)--(11) provide a pointed local functional comparison
of actual scalar source factors, with their zeros and marks
retained. They do not identify the full moving-\(q\) color state
with a fixed-root meridian state, construct a star/current map
for its whole word, or prove a geometric regular-profile norm.

## 5. Independent check of the full-head extension

The stronger [full-head theorem](full_head_gamma_source_transport.md)
has also been checked directly. With \(n=N-1\), \(L=\lfloor n/2\rfloor\),
and partial \(\beta_j(M)=(M^2Q_0;Q_0)_j/(Q_0;Q_0)_j\), its complement is
\[
 \beta_j(M)\beta_{n-j}(M^{-1})
       =M^{2j-n}\frac{S_N(M^2)}{NM^n}.          \tag{12}
\]
Indeed reversing the \(n-j\) suffix indices sends each ratio
to \(M^{-2}(1-M^2Q_0^r)/(1-Q_0^r)\). Multiplying that suffix
by the prefix gives \(M^{-2(n-j)}S_N(M^2)/N\), proving (12).
Thus the upper source section is defined by the canceled
complementary product; no inverse is evaluated at a zero.

For \(j\le L\), the exact unit is (8) with product length \(j\)
and no even-level scalar prefactor. Its \(O(1/N)\) estimate is
uniform over all prefix lengths by the same double difference.
For \(j>L\), symmetric q-binomial reflection gives
\[
 V_{N,j}=M_{\rm col}^{n-2j}V_{N,n-j};
\]
the remaining upper comparison character has logarithm
\((H-H_0)b(n-2j)/2=O(1/N)\), uniformly in \(j\).
This proves the claimed whole-head diagonal unit estimate.

The retained chirp comparison has the exact exponent
\[
 \log (U_{\rm col}/U_0)_j
       =ca\left(\frac{j}{2N}-\frac{j(j+1)}{4N^2}\right).
\]
It and its inverse are uniformly bounded in every common
diagonal metric on a fixed compact normal set. The same
conclusion holds for the whole source comparison \(T_N\).

The coupon identities in the full-head theorem are exact
coordinate statements. Both frames act on the same original
balanced column \((1,\ldots,1)^t\) and dual row
\((1,\ldots,1)/N\); their respective coordinate maps are
\(U_{\rm col}\operatorname{diag}V\) and
\(U_0\operatorname{diag}B\). Their quotient is \(T_N\), hence
the columns, rows and rank-one coupons transform by \(T_N\),
\(T_N^{-1}\), and conjugation. Position moments and endpoint
projectors commute with this diagonal comparison. At a
resonance this statement uses the paired fractional lattices,
whose abstract tensor pairing remains one; their singular
coordinate arrays cannot be specialized separately.

The root chart is a meromorphic gauge of the same actual
root head. All root operators must therefore conjugate with
the coupon. No equality with the moving-q crossing follows:
[the independent spectral proof](crossing_normal_spectra_obstruction.md)
rules out even arbitrary scalar-adjusted same-fiber similarity.
