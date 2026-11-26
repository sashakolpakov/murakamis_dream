# Polynomial error control for the next crossing in a lower half-disk

This note bounds the exact polynomial interpolation of one original
crossing applied after a turn. It applies to an arbitrary input
column, with all colors retained. In particular a polynomial-size
remainder in the original three-crossing column stays polynomial
in a fixed complex neighborhood of the candidate geometric clock.
The proof is an elementary entropy inequality, not a numerical
stationary-phase certificate.

The external phase used to recover the crossing coefficient from
this polynomial is retained explicitly. A lower asymptotic for the
main term is a separate requirement.

## 1. The exact arbitrary-input polynomial

Let \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(F_k=(Q;Q)_k\), and \(\kappa=q^{D^2/2}\). Let \(M\) be the
original crossing matrix and \(J\) index reversal. For an arbitrary
column \(u=(u_0,\ldots,u_D)\), define
\[
 \mathcal G_u(X)=\frac1{N\kappa}
    \sum_{k=0}^D\frac{q^{k^2}u_{D-k}}{F_k}
          X^{D-k}\prod_{r=0}^{k-1}(X-Q^{-r}).
 \tag{1}
\]
This is an ordinary polynomial of degree at most \(D\). Its
physical values reproduce the actual transformed column exactly:
\[
       (MJu)_j=N\kappa^2(-q^{-1})^j\mathcal G_u(Q^{-j}).
 \tag{2}
\]
To verify this, at \(X=Q^{-j}\) every term with \(k>j\)
vanishes, while for \(k\le j\)
\[
 X^{D-k}\prod_{r<k}(X-Q^{-r})
            =Q^j\frac{F_j}{F_{j-k}}.
 \tag{3}
\]
The original matrix coefficients in these variables are
\[
 M_{jk}=\kappa(-1)^j q^{j+k^2}
                   \frac{F_j}{F_kF_{j-k}}\quad(k\le j).
\]
Substitution proves (2), with the displayed scalar. There is no
reduction to distinct spectral values or omission of Newton
coordinates in (1).

## 2. A uniform entropy inequality

Put
\[
 \mathcal J(s)=\int_0^s\log(2\sin\pi t)\,dt,
 \qquad
 T(s;X)=(1-s)\log|X|
       +\int_0^s\log|X-e^{-2\pi it}|\,dt-\mathcal J(s).
 \tag{4}
\]
The endpoint logarithms in \(\mathcal J\) are integrable.

**Theorem 1.** For every \(0<|X|\le13/20\) with
\(\operatorname{Im}X\le0\),
\[
                   T(s;X)\le0\qquad(0\le s\le1).
 \tag{5}
\]
Equality holds at \(s=1\). No root-of-unity or arithmetic
restriction on \(X\) is used.

*Proof.* Write \(X=\rho e^{i\varphi}\), with
\(-\pi\le\varphi\le0\), and
\(L_\rho(v)=\log|1-\rho e^{iv}|\).
For \(0<s<1\), differentiation with respect to \(\varphi\)
of the integral in (4) gives
\[
 \frac{L_\rho(\varphi+2\pi s)-L_\rho(\varphi)}{2\pi}.
 \tag{6}
\]
Its sign is the sign of \(\sin(\varphi+\pi s)\), since the
difference of the two squared moduli has sign
\(\sin(\varphi+\pi s)\sin\pi s\). Thus the sole interior
stationary angle \(\varphi=-\pi s\) is a minimum. The maximum
on this closed half-circle occurs at \(X=\rho\) or \(X=-\rho\).

For \(X=\rho\), differentiation in \(s\) shows \(T'>0\):
the difference of the squared numerator and denominator in its
exponential is
\[
 |1-\rho e^{2\pi is}|^2
       -\rho^2|1-e^{2\pi is}|^2
 =1-\rho^2-2\rho(1-\rho)\cos(2\pi s)
 \ge(1-\rho)^2>0.
 \tag{7}
\]
The full-period logarithmic mean of \(1-\rho e^{2\pi it}\)
is zero, as follows by integrating its convergent logarithmic
power series. Also \(\mathcal J(1)=0\). Hence \(T(1;\rho)=0\)
and this case follows.

For \(X=-\rho\), direct integration of the radial derivative
gives
\[
 \partial_\rho T(s;-\rho)
 =\frac{1-s+(2\pi)^{-1}\arg(1+\rho e^{2\pi is})}{\rho}>0
                  \quad(0\le s<1).
 \tag{8}
\]
The principal argument is used. For \(s\le1/2\) it is
nonnegative. For \(s>1/2\), putting \(\delta=2\pi(1-s)\)
gives \(-\delta<\arg(1+\rho e^{-i\delta})<0\), so the
numerator remains positive. This proves that it suffices to
consider \(\rho=13/20\).

At this radius, the sign of \(T'(s;-\rho)\) is the sign of
\[
              1-\rho+2\rho\cos(2\pi s).
 \tag{9}
\]
There is exactly one interior local maximum, at
\[
 s_0=\frac1{2\pi}\arccos(-7/26)<\frac13.
\]
The other stationary point is a minimum. The global maximum
therefore occurs at \(0,1\), or \(s_0\). The first endpoint
is \(\log\rho<0\), and the second is zero.

For the remaining point, the triangle inequality gives
\[
 T(s;-\rho)\le E(s):=(1-s)\log\rho+s\log(1+\rho)
                                      -\mathcal J(s).
 \tag{10}
\]
Here \(E'>0\), because \((1+\rho)/(2\rho)>1\).
Consequently
\[
 T(s_0;-13/20)\le E(1/3)
     =\tfrac13\log(5577/8000)-\mathcal J(1/3)<-\frac1{120}.
 \tag{11}
\]
The final strict inequality has the following elementary rational
verification. Integrating the logarithmic Fourier series, or
first its Abel regularization, gives
\[
 -\mathcal J(1/3)=\frac{\sqrt3}{4\pi}
       \sum_{m\ge0}\left(\frac1{(3m+1)^2}
                              -\frac1{(3m+2)^2}\right).
 \tag{12}
\]
The positive summand decreases in \(m\). After the first three
terms its tail is at most
\(\int_2^\infty[(3t+1)^{-2}-(3t+2)^{-2}]dt=1/168\).
Thus the sum is less than \(79/100\). Using
\(\sqrt3<26/15\) and \(\pi>157/50\) gives
\(-\mathcal J(1/3)<11/100\). The latter bound for \(\pi\)
also follows immediately from
\(\pi=16\arctan(1/5)-4\arctan(1/239)\) and the first two
alternating terms of \(\arctan(1/5)\).
Finally \(\log u\le-2(1-u)/(1+u)\) for \(0<u<1\), so
\[
 \tfrac13\log(5577/8000)+\tfrac{11}{100}
 \le-\frac{4846}{40731}+\frac{11}{100}
 =-\frac{36559}{4073100}<-\frac1{120}.
 \tag{13}
\]
This proves (11) and then (5). \(\square\)

## 3. Consequence for the full original input error

**Corollary 2.** Let \(K\) be a compact subset of
\[
       \{X:0<|X|\le13/20,\ \operatorname{Im}X\le0\}.
\]
There are constants \(C_K,A_K\), independent of \(N\) and
the input vector, such that
\[
      \sup_{X\in K}|\mathcal G_u(X)|
                       \le C_KN^{A_K}\max_j|u_j|.
 \tag{14}
\]
On compact subsets of the strict open lower half-disk, the same
statement holds for every fixed number of complex derivatives,
with constants allowed to depend on the derivative order.

*Proof.* Since \(|F_k|=S_k\), the logarithm of the absolute
value of the coefficient multiplying \(u_{D-k}/(N\kappa)\)
in (1) equals
\[
 (D-k)\log|X|+\sum_{r=0}^{k-1}\log|X-Q^{-r}|-\log S_k
                    =NT(k/N;X)+O_K(\log N).
 \tag{15}
\]
The finite-product sum has a uniform bounded Euler-sum error:
its integrand and first derivative are bounded because
\(|X-Q^{-r}|\ge7/20\). The replacement of \(D-k\) by
\(N-k\) costs the bounded term \(-\log|X|\). The uniform
sine-factorial estimate
\(\log S_k=N\mathcal J(k/N)+O(\log N)\) includes every
\(0\le k<N\); see
[the elementary weighted Green estimate](research_elementary_weighted_green_transport.md).
Theorem 1 now bounds every coefficient polynomially. Summing all
\(N\) terms proves (14). For the derivative assertion enlarge
the compact set slightly inside the same open domain and use
Cauchy's formula. \(\square\)

This domain contains the actual remaining geometric clock. In
[the marked remaining-saddle dictionary](research_three_crossing_geometric_remaining_saddle.md),
\(X_*=1/r(\tau_*)\), and its certified rectangle gives
\(-\Re r>63/100\) and \(\Im r>36/25\). Thus
\[
 |r|^2>\frac{4941}{2000}>\frac{400}{169},\qquad
 |X_*|<\frac{13}{20},\qquad \Im X_*<0.
\]
There is consequently a fixed complex neighborhood of that
clock to which the derivative version of (14) applies.

For example, the actual source decomposition proved in
[the next-step profile theorem](research_three_crossing_next_step_profile.md)
is \(\alpha=\kappa^3A_N h+\delta_N\), with
\(\max_j|\delta_{N,j}|=O(N)\). Linearity and (14) show that
\[
 \mathcal G_\alpha=\kappa^3A_N\mathcal G_h
                                      +\mathcal G_{\delta_N},
 \qquad \mathcal G_{\delta_N}=O_K(N^{A_K+1}),
 \tag{16}
\]
including fixed derivatives on strict interior compact sets.
This is a bound for the actual whole polynomial error.

The original crossing coefficient is recovered through (2).
For a noninteger color \(j=Nx\), the chosen analytic lift of
its explicit chirp must also be retained. In particular the
principal logarithms obey
\[
 \operatorname{Log}(-q)=-i\pi+i\pi/N,
 \qquad \operatorname{Log}(-q^{-1})=i\pi-i\pi/N.
\]
Their quotient at that noninteger color is
\(e^{-2\pi iNx+2\pi ix}=X^{N-1}\), where
\(X=e^{-2\pi ix}\). It is not merely \(X^{-1}\), though
these agree on physical colors. Bound (16) is therefore not a
permission to drop a factor \(X^N\) in a contour formula.
Nor does it by itself prove a nonzero asymptotic for the main
term \(\mathcal G_h\) or the remaining boundary pairing.
