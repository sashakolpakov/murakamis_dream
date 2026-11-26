# Complete low physical blocks on the lower left interval

Private research deduction, 8 November 2026. Both original low
physical blocks increase to their original real cuts on the lower
left shared interval. Their complete positive sums can therefore
be attached to the already paid joint profiles. In particular the
literal product with both conditional factors restricted to their
low physical blocks has a strict bound at the required action rate,
including the full negative-depth seam and the zero rows.

This does not estimate either whole conditional factor. Upper
physical rows, last rows, aliases and noncentral first incoming
pieces remain separate. No numerical evaluation or frozen-source
edit is used.

## 1. Exact partial sums and rates

Use the actual ordinary-next references, original primitives and
allocations of
[the joint profile theorem](research_mixed_next_lower_left_joint_main_profiles.md),
including its Section 6. Thus
\[
\begin{gathered}
a=x+ih_a,\quad x\in P=[.22,.45],\qquad
y=q+ih_y,\quad 0\le q\le.22,\qquad
z=u+ih_z,\quad u\in P,\\
-.072<h_a<0,\qquad -.102<h_y<-.001,\qquad
|h_z|\le.108,\qquad \beta=0,1 .
\end{gathered}
\tag{1}
\]
When \(\beta=1\), \(h_z<0\). All typed-reference
correlations are retained. Write \(X=e^{-2\pi ia}\),
\(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\),
\(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
and \(p_j(W)=(rW;r)_j\).

The literal partial kernels are
\[
\begin{split}
L_{1,N}(X,Y)&=\sum_{j=0}^{\lfloor N/8\rfloor}
              \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
L_{\beta,N}(Y,Z)&=\sum_{j=0}^{\lfloor N\ell_\beta\rfloor}
              \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
\qquad
\ell_0=3/20,\quad\ell_1=1/8.
\end{split}
\tag{2}
\]
They retain every indicated original physical row. Both zero
rows equal exactly one, because \(P_0=p_0=1\).
For a contour decomposition, the matching lower half-grid cut
is \((\lfloor N\ell\rfloor+1/2)/N\); it differs from
\(\ell\) by at most \(1/(2N)\). Such a change costs only
a bounded factor at these fixed regular cuts.

For real row parameter \(v\), set
\[
\begin{split}
E_\gamma(v;b,c)
={}&\int_0^v\log|1-e^{-2\pi i(b+t)}|\,dt
  +\int_0^v\log|1-e^{-2\pi i(c+t)}|\,dt\\
 &-(2+\gamma)J(v)-2\pi v\Im b .
\end{split}
\tag{3}
\]
This is exactly \(\Re Q_\gamma(v;b,c)\), with the
original constants \(g(0)=0\) and the incoming chirp.
In particular \(E_\gamma(0;b,c)=0\).
The allocation terms are independent of \(v\).

The uniform sine-factorial estimate gives
\(\log|P_j|=NJ(j/N)+O(\log N)\), including \(j=0\).
The two numerator products in (2) have the corresponding
uniform Riemann bounds on (1): their low-row shifted real
parts stay away from one, and their original nonzero heights
or positive real separations keep these products regular.
Equivalently one can use the original zero-safe uniform
product upper bound. Thus, for every prescribed \(\tau>0\),
each modulus in (2) is at most
\[
C_\tau N^{B_\tau}
e^{N\{E_\gamma(j/N;b,c)+\tau\}},
\tag{4}
\]
uniformly at both parities. The exact zero-row value is
included without using a logarithm at zero.

## 2. The two low profiles increase to their cuts

Put \(S(v)=2\sin\pi v\), \(R=e^{2\pi h_y}\le1\), and
\(T=e^{-2\pi h_a}<8/5\). For \(0<v\le1/8\), the first
exact force is
\[
\exp E_1'(v;a,y)
=\frac{|T-e^{-2\pi i(x+v)}|
        |1-Re^{-2\pi i(q+v)}|}{S(v)^3}.
\tag{5}
\]
The first numerator exceeds \(5/4\). Indeed \(x+v\)
lies between \(.22\) and \(.575\), its minimum unit-radius
chord is at least \(2\sin(11\pi/50)>5/4\), and its
modulus is increasing in \(T\ge1\).
For a rational witness,
\[
\sin(11\pi/50)>
\frac{11}{16}-\frac{(11/16)^3}{6}
=\frac{15565}{24576}>\frac58.
\]
The second numerator is at least \(\sin(2\pi v)\).
Before \(q+v=1/4\), minimize over its radius and use
increasing sine; after that point its cosine is nonpositive
and its modulus is at least one. Therefore
\[
\exp E_1'(v;a,y)
>\frac54\,\frac{\cos\pi v}{S(v)^2}
>\frac54\,\frac{9/10}{3/5}=\frac{15}{8}>1 .
\tag{6}
\]
We used \(\cos(\pi/8)>9/10\) and
\(S(1/8)^2=2-\sqrt2<3/5\).

For the next factor, the exact folded incoming force is
\[
\exp E_\beta'(v;y,z)
=\frac{|R^{-1}-e^{-2\pi i(q+v)}|
        |1-e^{2\pi h_z}e^{-2\pi i(u+v)}|}
       {S(v)^{2+\beta}}.
\tag{7}
\]
For \(v\le\ell_\beta\), one has \(q+v<1/2\);
the first numerator is at least \(S(v)\). Its square
increases with the radius \(R^{-1}\ge1\), and the
unit-radius chord increases from \(v\) to \(q+v\).
The second numerator exceeds \(19/20\), uniformly over
its positive radius. If its shifted cosine is positive,
then \(u+v\in[.22,.25)\), and radial minimization gives
the bound \(\sin(11\pi/25)>19/20\). Otherwise its modulus
is at least one. The sine witness follows from
\(\sin(11\pi/25)=\cos(3\pi/50)>1-(1/5)^2/2>19/20\).

For own three,
\[
S(v)\le2\sin(3\pi/20)<3\pi/10<33/35,
\qquad
\exp E_0'(v;y,z)>\frac{19/20}{33/35}=\frac{133}{132}>1 .
\tag{8}
\]
For own four,
\[
\exp E_1'(v;y,z)>
\frac{19/20}{3/5}=\frac{19}{12}>1 .
\tag{9}
\]
Thus each entire low real profile is bounded by its value
at its original cut, including the value zero at \(v=0\).

Combining (4)--(9), and summing at most \(N\) moduli, proves
\[
\begin{split}
\sum_{j\le\lfloor N/8\rfloor}
\left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
&\le C_\tau N^{B_\tau}
 e^{N\{\Re Q_1(1/8;a,y)+\tau\}},\\
\sum_{j\le\lfloor N\ell_\beta\rfloor}
\left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}}\right|
&\le C_\tau N^{B_\tau}
 e^{N\{\Re Q_\beta(\ell_\beta;y,z)+\tau\}}.
\end{split}
\tag{10}
\]
Every subset of either low block inherits its positive bound.
No extra coefficient-extraction factor \(N\) belongs in (2)
or (10).

## 3. The complete Fourier weight through the deep lower seam

For every \(\tau>0\), uniformly on
\[
0\le q\le.22,\qquad -.102\le h\le-.001,
\]
the original complete polynomial obeys
\[
\boxed{\quad
|d_N(e^{-2\pi i(q+ih)})|
\le C_\tau N^{B_\tau}
      e^{N\{-\Re g(q+ih)+\tau\}} .
\quad}
\tag{11}
\]
This is an upper bound, not a relative factorial packet at
the seam.

To prove it, retain the absolutely normalized lower-half identity
from [Fourier-weight continuation, equation (22)](research_mixed_fourier_weight_continuation.md):
\[
g(y)=\frac{\operatorname{Li}_2(e^{-2\pi iy})-\pi^2/6}{2\pi i}.
\tag{12}
\]
It gives \(\nu(y)=-\Re g(y)>0\) for
\(0<\Re y<1/2,\Im y<0\), and
\(\nu(ih)=0\) on the displayed negative imaginary segment.
The full absolute Fourier bound in that theorem therefore
gives (11) on every compact subinterval \(q\ge\epsilon>0\).

At \(q=0\), apply
[lower radial seam, Lemma 1](research_mixed_next_lower_radial_seam.md)
to a fixed positive inward radial segment containing
\(\{e^{2\pi h}:-.102\le h\le-.001\}\).
For the same prescribed tolerance it gives a fixed complex
tube with \(|d_N|\le C_\tau N^B e^{N\tau}\).
This source uses the exact forced recurrence
\[
d_N(r^{-1}Y)=(1-Y)d_N(Y)+\frac{Y}{N^2}\sum_{k=0}^{N-1}Y^k;
\tag{13}
\]
its full forcing is retained. Compactness gives one fixed
\(\epsilon>0\) so that all \(0\le q\le\epsilon\) lie
in that tube. Since \(\nu\ge0\) there, this is (11).
The overlap with the first compact estimate proves the
whole assertion, with an arbitrarily small common tolerance.
Continuity and smaller fixed parameter neighborhoods give
the corresponding upper bounds for fixed derivatives.
Their width may depend on \(\tau\); no relative approximation
or prescribed neighborhood width at \(q=0\) is asserted.

The original outgoing allocation, when \(\beta=1\), is
likewise bounded by
\[
|d_N(Z)|^{1/2}\le
C_\tau N^{B_\tau}e^{N\{-\Re g(z)/2+\tau\}}
\tag{14}
\]
on its original ordinary negative-height plateau.
For \(\beta=0\) this factor is absent.

## 4. A literal finite low-block product

The joint profile theorem, Section 6, proves on (1)
\[
B_U(x)+\Re\{Q_1(1/8;a,y)+Q_\beta(\ell_\beta;y,z)
                         -g(y)-\tfrac\beta2g(z)\}
<\Lambda_{123}(z)-10^{-10}.
\tag{15}
\]
Its two old real-cut calibrations and original marginal
cancellation are retained. The complete first cap satisfies
the all-real-color upper plane \(B_U(x)\), with every
private source row and current already included.
Choose the total tolerances in that cap bound and
(10)--(14) sufficiently small inside (15).

**Theorem.** On the full closed domain (1), including \(q=0\),
both parities and every real ordinary color satisfy
\[
\boxed{\quad
|U_{0,N}(w,X)L_{1,N}(X,Y)d_N(Y)L_{\beta,N}(Y,Z)|
\,|d_N(Z)|^{\beta/2}
\le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}} .
\quad}
\tag{16}
\]
The same statement holds if either low block is replaced
by any subset of its rows, with the positive sums (10)
used before taking the modulus. This is an actual partial
finite-source estimate, not only an inequality of phases.

Fixed real-color derivatives have polynomial cost by the
complete cap source. On smaller fixed complete-color and
actual-output neighborhoods, the corresponding normalized
fixed mixed derivatives have an exponential loss \(10^{-12}\).
Use the original holomorphic integer-weight squares for the
modulus allocation, and remove the outgoing halfweight only
near its actual nonzero factorial packet. No division through
an independent output zero is used. The physical cutoffs
in (2), the heights and all integration paths stay fixed at
each base reference before these derivatives are taken.

If the first incoming coordinate is integrated over
\(P+ih_a\), its literal measure is \(+N\,da=+N\,dx\).
The fixed length and this single factor \(N\) change only
the polynomial prefactor in (16). There is no additional
factor from either physical row sum.

For completeness, the same allocation can pair one low
block with the other's original retained zero-mode main
integral on any fixed closed regular substrip
\(\epsilon\le q\le.22\), \(\epsilon>0\).
The exact factorial row interpolant there has phase
\(Q_\gamma\) and polynomial amplitude, and the central
measure is its original \(+N\,ds\). The joint main/real-cut
profile theorem and (10)--(14) give the same strict loss.
This statement includes that whole specified main segment;
it does not include its vertical joins or weighted remainders.
No uniform extension of this main interpolation through
\(q=0\) is inferred merely from (11).

## 5. Remaining source pieces

Theorem (16) pays the low-by-low part of the central first
incoming source on the entire lower left interval. Formula
(10) also supplies a positive low-block bound whenever a
separately established counterpart is attached.

It does not bound the entire kernels \(C_1,C_\beta\), the
post-half physical blocks, their last rows, or their complete
contour currents. It does not replace the initial, taper or
right-hand parts of the first incoming integration by its
central interval. The original second Fourier coefficient
and the signed paired-left residue/current balance remain
present. No whole next-transfer or new knot-family conclusion
is asserted.
