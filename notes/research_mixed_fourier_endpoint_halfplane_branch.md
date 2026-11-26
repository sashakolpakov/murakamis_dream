# A uniform branch domain for the Fourier endpoint equation

Research deduction, 7 November 2026. The outgoing endpoint equation
has a distinguished quadratic root. This note constructs that root
on an explicit half-plane, rather than only on a neighborhood of
the already known critical points. On its intersection with the
lower half-plane, the auxiliary matching coordinate also has a
single holomorphic logarithm with the original normalization.

These assertions concern the critical equations. They supply no
estimate for the remainder of a finite quantum sum and do not prove
that the auxiliary coordinate belongs to the narrower domain of
the complete conditional-source estimates.

## 1. The equation and the original parameter bounds

Use the notation of the
[correlated endpoint calculation](research_mixed_fourier_right_cap_correlated_endpoint.md).
The fixed Fourier parameter is
\[
 Y=e^{2\pi i x_0}=\rho e^{i\phi},\qquad
 c=Y^{-1}-1,
\]
where the original bounds give
\[
 \frac35<\rho<\frac58,
 \qquad .18299<\Re x_0<.18301,
 \qquad \phi=2\pi\Re x_0.
 \tag{1}
\]
No value of the original algebraic parameter is replaced by a
rounded center. The outgoing exponent \(Q=e^{-2\pi iq}\) and
the preceding exponent \(S=e^{-2\pi is}\) satisfy
\[
 Q^2-(1+Y^{-1}-S)Q+c=0.
 \tag{2}
\]
For \(Q\ne0\), equivalently,
\[
 S=S(Q):=2+c-Q-c/Q.
 \tag{3}
\]
The original actual family has \(|Q|<1\),
\(\Im S<0\), and
\(\Re S+\Im S/15<0\). These restrictions were proved from
the original type-four image, not from a choice of a new root.

We will use the elementary bounds
\[
 \frac25<\cos\phi<\frac{21}{50},
 \qquad \frac9{10}<\sin\phi<\frac{921}{1000}.
 \tag{4}
\]
The lower bounds are proved in Section 2 of the
[original boundary update](research_mixed_fourier_boundary_update.md).
For completeness, (1), \(25/8<\pi<22/7\), give
\(8/7<\phi<7/6\). Monotonicity on this interval and the
alternating Taylor bounds give
\[
 \cos\phi
 <1-\frac12(8/7)^2+\frac1{24}(8/7)^4<\frac{21}{50},
\]
\[
 \sin\phi
 <\frac76-\frac16(7/6)^3+\frac1{120}(7/6)^5
 <\frac{921}{1000}.
\]
All ensuing comparisons use only (1) and (4).

## 2. The image of the unit circle stays beyond a fixed line

Define the real linear functional
\[
 L(S)=\Re S+\frac1{15}\Im S
      =\Re(tS),\qquad t=1-i/15,
\]
and put \(Z=t/Y\). For \(|Q|=1\), (3) gives exactly
\[
 \min_{|Q|=1}L(S(Q))
       =1+\Re Z-|Z+2i/15|.
 \tag{5}
\]
Indeed \(2+c=1+Y^{-1}\), while
\[
 \max_{|Q|=1}\Re(tQ+tc\overline Q)
       =|t+\overline t\,\overline c|
       =|Z+2i/15|.
\]
This is the support function of the ellipse parametrized by
\(S(Q)\) on the unit circle; no root of (2) is evaluated.

Set \(u=\cos\phi\), \(v=\sin\phi\), and
\(A_0=1+\Re Z=1+(u-v/15)/\rho\). A direct subtraction yields
\[
 \rho^2\bigl(A_0^2-|Z+2i/15|^2\bigr)
 =\rho^2+2\rho(u-v/15)
       -(v+u/15-2\rho/15)^2.
 \tag{6}
\]
The last parenthesis is positive throughout (1), (4). Its
upper bound is
\(.921+.42/15-2(.6)/15=.869\). Consequently (6) is greater than
\[
 .36+1.2(.4-.921/15)-(.869)^2
                  =\frac{11159}{10^6}.
 \tag{7}
\]
Also \(0<A_0<17/10\). Since (7) is positive,
\(|Z+2i/15|<A_0\), and hence
\[
 \rho^2(A_0+|Z+2i/15|)<\frac{85}{64}.
\]
Dividing the difference of squares in (6) proves
\[
 \boxed{\displaystyle
       \min_{|Q|=1}L(S(Q))
       >\frac{11159\cdot64}{85\cdot10^6}
       >\frac1{125}.}
 \tag{8}
\]

## 3. A unique holomorphic root on a half-plane

**Proposition 1.** Let
\[
 \mathcal H=\{S\in\mathbb C:L(S)<1/125\}.
\]
For every \(S\in\mathcal H\), equation (2) has exactly one
root in the open unit disk. This root \(Q(S)\) is nonzero,
holomorphic, and injective on \(\mathcal H\). Its derivative
never vanishes. It agrees with the actual outgoing exponent at
every original reference.

*Proof.* First \(|c|>1\), since
\[
 |c|^2-1=\frac{1-2\rho\cos\phi}{\rho^2}>0.
\]
By (8), no root of (2) lies on the unit circle for any
\(S\in\mathcal H\). The number of roots inside that circle,
counted with multiplicity, is therefore constant on this
connected half-plane. At \(S=-10\),
\[
 |1+Y^{-1}-S|\ge11-|Y^{-1}|>28/3,
 \qquad 1+|c|<11/3.
\]
Rouché's theorem, comparing (2) with its linear term on the
unit circle, gives exactly one inside root.

The constant term \(c\) is nonzero, so this root is nonzero.
The other root is \(c/Q\), of modulus greater than one; in
particular the inside root is simple. The implicit function
theorem and uniqueness glue its local branches on all of
\(\mathcal H\). Formula (3) proves injectivity, and
\[
 Q'(S)=\frac{Q(S)^2}{c-Q(S)^2}\ne0.
 \tag{9}
\]
The actual root has modulus less than one and solves the same
equation, so it is this branch. \(\square\)

There is a useful uniform consequence. For every \(S\) with
\(L(S)\le0\), the disk \(|S'-S|<1/130\) is contained in
\(\mathcal H\), because \(|t|<26/25\). Since \(|Q|<1\),
Cauchy's inequalities give
\[
                 |Q^{(k)}(S)|\le k!\,130^k,
                 \qquad k\ge1.
 \tag{10}
\]
This bound is independent of the number and order of the preceding
blocks. It is a bound on the critical-coordinate response, not on
the finite quantum operator.

## 4. The auxiliary matching coordinate on the lower half-plane

Let
\[
 \mathcal H_-:=\{S\in\mathcal H:\Im S<0\},\qquad
 B(S)=\frac{1-YQ(S)}{Y+(1-2Y)Q(S)}.
 \tag{11}
\]
The numerator cannot vanish, since \(|YQ|<5/8\).
There is only one possible denominator zero in the \(Q\)-plane,
\[
 Q_p=-\frac{Y}{1-2Y}.
\]
Here \(1-2Y\ne0\), because \(\Im Y>0\). Substitution into
(3) gives its only possible \(S\)-coordinate:
\[
 S_p=3-\frac2Y+\frac1{Y^2}+\frac{Y}{1-2Y}.
 \tag{12}
\]
Its imaginary part is
\[
 \Im S_p
 =\frac{2\sin\phi\,(\rho-\cos\phi)}{\rho^2}
      +\frac{\rho\sin\phi}{|1-2Y|^2}>0,
 \tag{13}
\]
using \(\rho>3/5>21/50>\cos\phi\). It therefore lies outside
\(\mathcal H_-\). This proves that \(B\) is holomorphic and
nonzero on \(\mathcal H_-\).

This domain is convex, hence simply connected. It follows that
\(B\) has a holomorphic logarithm there. Choose its value at one
original reference to be the previously fixed matching logarithm,
and define
\[
                   b(S)=-\frac{\log B(S)}{2\pi i}.
 \tag{14}
\]
The normalization determines (14) uniquely. It agrees with the
original matching coordinate along continuation in the actual
connected incoming family. No pointwise re-selection of a
logarithm is made. Finally,
\[
 \frac{dB}{dQ}
   =-\frac{(1-Y)^2}{[Y+(1-2Y)Q]^2}\ne0,
\]
so both \(B'(S)\) and \(b'(S)\) are nonzero.

This removes a branch ambiguity on a fixed domain containing the
actual right-endpoint family. It does not give
\(b(S)\in K_3\), nor does it allocate the outgoing halfweight
in the finite-source estimate. Those are separate remaining
requirements of the right-boundary argument.
