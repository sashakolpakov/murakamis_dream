# The complete outgoing polynomial on a larger unit-circle arc

Private research theorem, 9 November 2026. The terminating outgoing
recurrence determines a nonzero complex asymptotic on a fixed
neighborhood of every compact arc
\[
             Z=e^{-i\alpha},\qquad \pi/2<\alpha<\pi .
\]
In the coordinate \(Z=e^{-2\pi iy}\), this includes every compact
real interval \(1/4<y<1/2\). The result therefore reaches beyond
the previously used upper endpoint \(y=39/100\).

The proof first excludes the unit-circle arc from the spectral
interval of every frozen recurrence. It then constructs the
finite solution backwards from its exact terminal value. Uniform
contraction proves that no denominator vanishes during this
construction. This supplies the finite-source conclusion without
assuming that the earlier energy estimate extends to the new arc.
No numerical evaluation or change to a frozen input is used.

## 1. The original source and the assertion

Retain
\[
 D=N-1,\quad M=\lceil N/2\rceil,\quad
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 S_j=|P_j|=\prod_{\nu=1}^j2\sin(\pi\nu/N).
\]
The complete physical outgoing polynomial is
\[
 C_{b,N}(Z)
 =\sum_{j=0}^{D}
       \frac{r^{-bj}(r^{b+1};r)_j(rZ;r)_j}{P_j^2},
                  \qquad 0\le b\le D .
 \tag{1}
\]
Its exact stopping index is \(D-b\); in particular
\(C_{D,N}=1\). Neither its phases nor its physical numerator
zeros are replaced in this argument.

For \(1/2\le a\le1\), put
\[
 t=\frac{\pi a-\pi/2}{2},\qquad
 \sigma(a)=2\sin(\pi a)=2\cos(2t),\qquad k(a)=\sigma(a)^3,
\]
\[
 V(a,Z)=3e^{it}+2e^{-3it}+Ze^{5it}.
 \tag{2}
\]
Let \(I=[\alpha_0,\alpha_1]\) be any fixed closed interval with
\(\pi/2<\alpha_0<\alpha_1<\pi\), and let
\(\mathcal Z_I=\{e^{-i\alpha}:\alpha\in I\}\).

**Theorem.** On a fixed complex neighborhood of
\([1/2,1]\times\mathcal Z_I\), there is a holomorphic branch
\(m(a,Z)\), nonzero and bounded away from zero, satisfying
\[
 km^2-Vm+1=0,\qquad
 |k m^2|<1,\qquad
 m(1,Z)=\frac{e^{-i\pi/4}}{1-Z}.
 \tag{3}
\]
The strict inequality holds with one uniform margin after a
fixed shrink of the neighborhood.

Define, with derivatives in \(a\),
\[
 \begin{split}
 V_1&=\frac{i\pi}{4}
           \{3e^{it}-6e^{-3it}+Ze^{5it}\},\\
 m_1&=\frac{m^2\{(km)'-V_1\}}{1-km^2},\\
 h(a,Z)&=e^{i(\pi/4-\pi a/2)}m(a,Z),\qquad
 \eta(a,Z)=\frac{i\pi}{4}+\frac{m_1(a,Z)}{m(a,Z)},\\
 \mathcal B(a,Z)&=
 \exp\left\{\frac{\log h(a,Z)+\log h(1,Z)}2
                          -\int_a^1\eta(x,Z)\,dx\right\}.
 \end{split}
 \tag{4}
\]
Choose the logarithm continuously on a simply connected
neighborhood. Then, for all sufficiently large levels of both
parities, uniformly for \(M-1\le b\le D\) and
\(Z\) in a smaller fixed complex neighborhood of \(\mathcal Z_I\),
\[
 \boxed{\quad
 C_{b,N}(Z)=\frac{S_b}{N}
       \exp\left\{-N\int_{b/N}^1\log h(a,Z)\,da\right\}
       \mathcal B(b/N,Z)\{1+O_{\rm hol}(N^{-1})\}.
 \quad}
 \tag{5}
\]
The coefficient is nonzero, and the relative error and every
fixed \(Z\)-derivative of that error are \(O(N^{-1})\) on
smaller neighborhoods. In particular every polynomial in this
range is zero-free there for sufficiently large \(N\).
The sine product \(S_b\) remains exact through the last row.

On every overlap with the
[previous outgoing amplitude theorem](research_mixed_next_outgoing_complex_amplitude.md),
the functions in (3)--(5) are precisely its functions. Thus
this is an extension of the original normalized finite source.

## 2. Where the frozen spectral interval meets the unit circle

Fix \(0\le t<\pi/4\), and abbreviate
\[
 c=\cos(2t)>0,\qquad
 A=3e^{it}+2e^{-3it},\qquad
 d=2\sigma^{3/2}=4\sqrt2\,c^{3/2},\qquad
 I_t=\Im A=\sin t(1-4c).
 \tag{6}
\]
We will show that
\[
             A+Ze^{5it}\notin[-d,d]
                    \qquad (Z\in\mathcal Z_I).
 \tag{7}
\]
This is the exact condition that the two roots
\(\zeta=\sigma^{3/2}m\) of
\(\zeta^2-(V/\sigma^{3/2})\zeta+1=0\)
avoid the unit circle.

First \(|I_t|\le1/\sqrt2\). Indeed
\[
 I_t^2=\frac{1-c}{2}(1-4c)^2.
\]
For \(0\le c\le1/4\) the bound follows at once from
\((1-4c)^2\le1\). For \(1/4\le c\le1\) the derivative
of the last expression is
\((4c-1)(9-12c)/2\), so its maximum is attained at
\(c=3/4\), with value \(1/2\).

If \(|Z|=1\) and \(V=A+Ze^{5it}\) is real, then its two
possible values are
\[
                  \Re A\pm\sqrt{1-I_t^2}.
 \tag{8}
\]
The plus choice lies strictly above \(d\). To prove this,
compute
\[
 |A|^2=1+24c^2,\qquad
 \Re A=\sqrt{(1+c)/2}\,(1+4c),
\]
\[
 |A-d|^2
 =1+8c^{3/2}
       \{\sqrt c(3+4c)-\sqrt{1+c}(1+4c)\}<1 .
 \tag{9}
\]
Both terms compared in braces are positive, and the square
of the second exceeds the square of the first by exactly one.
Equation (9) implies
\(|\Re A-d|<\sqrt{1-I_t^2}\), proving the assertion for
the plus choice. Also \(|A+d|^2>1\), since \(c>0\),
\(|A|^2>1\), and \(\Re A>0\).
It follows that the minus choice in (8) lies strictly between
\(-d\) and \(d\).

Consequently a unit point giving \(V\in[-d,d]\) must satisfy
\[
 Ze^{5it}=-\sqrt{1-I_t^2}-iI_t=-e^{i\varphi(t)},
       \qquad \varphi(t)=\arcsin I_t\in[-\pi/4,\pi/4].
 \tag{10}
\]
Writing this point as \(Z=e^{-i\alpha(t)}\), one continuous
argument is
\[
                  \alpha(t)=5t-\pi-\varphi(t).
 \tag{11}
\]
It satisfies
\[
                         -\pi\le\alpha(t)\le\pi/2 .
 \tag{12}
\]
The upper bound uses \(t\le\pi/4\) and
\(\varphi\ge-\pi/4\). For the lower bound, if \(I_t\le0\)
then \(\varphi\le0\le5t\). If \(I_t>0\), then \(c<1/4\),
so \(t>\pi/6\), whereas \(\varphi\le\pi/4<5t\).
Thus in both cases \(\varphi\le5t\), proving (12).
No number in (12), even modulo \(2\pi\), belongs to the
open interval \((\pi/2,\pi)\). This proves (7).

At the endpoint \(a=1\), \(k=0\) and
\[
                  V(1,Z)=e^{i\pi/4}(1-Z)\ne0 .
 \tag{13}
\]
This is a scalar terminal equation, not a limiting
division by \(\sigma^{3/2}\).

## 3. Selecting a uniformly contracting branch

For \(a<1\), (7) implies that the two reciprocal roots
\(\zeta\) have exactly one root inside the unit disk.
Choose this root. Its corresponding \(m\) is nonzero, and
\[
                         |k m^2|=|\zeta|^2<1.
 \tag{14}
\]
As \(a\) tends to one, it converges to \(1/V(1,Z)\):
the quadratic has one bounded root with that limit and
one unbounded root, and only the bounded root satisfies
(14) near the endpoint.

The resulting branch is continuous on the compact parameter
set and is simple everywhere. At \(a<1\),
\[
                 2km-V=\frac{km^2-1}{m}\ne0;
 \tag{15}
\]
at \(a=1\) it is \(-V(1,Z)\ne0\).
The implicit function theorem gives compatible local
holomorphic extensions, including the endpoint. Uniqueness
of the inside root makes them agree. Taking a sufficiently
thin simply connected neighborhood of the interval times
the arc gives one common extension. Compactness gives
\[
 0<c_m\le |m|\le C_m,\qquad |km^2|\le\rho<1
 \tag{16}
\]
there, after shrinking it if necessary. All fixed derivatives
needed in (4) are bounded. This proves (3), including its
terminal convention.

## 4. Constructing the finite solution from its terminal row

Put \(\epsilon=1/N\). The exact normalized trailing matrices
of the
[original determinant calculation](research_mixed_next_outgoing_trailing_determinants.md)
have diagonal
\[
 V_N(a,Z)=3e^{i(t+\pi\epsilon/4)}
       +2\cos(\pi\epsilon)e^{-i(3t+3\pi\epsilon/4)}
       +Ze^{i(5t+\pi\epsilon/4)}
 \tag{17}
\]
and adjacent-entry product \(k(a+\epsilon)\). The finite
Riccati equation to be constructed is
\[
 m_{b,N}
  =\{V_N(b/N,Z)-k((b+1)/N)m_{b+1,N}\}^{-1},\qquad
 m_{D,N}=V_N(D/N,Z)^{-1}.
 \tag{18}
\]
We do not assume in advance that its intermediate denominators
are nonzero on the new arc.

Let \(\widetilde m_N(a)=m(a)+\epsilon m_1(a)\), using (4).
Since \(V_N=V+\epsilon V_1+O(\epsilon^2)\), direct Taylor
expansion and the equation for \(m_1\) give
\[
 \widetilde m_N(a)-
 \{V_N(a,Z)-k(a+\epsilon)\widetilde m_N(a+\epsilon)\}^{-1}
                         =O(\epsilon^2).
 \tag{19}
\]
All bounds are uniform on the fixed complex neighborhood.
The map on the right has derivative tending to \(km^2\)
at its comparison point. By (16), there is a fixed radius
and a constant \(\rho_1<1\) on which the map is defined
and is Lipschitz with constant \(\rho_1\), uniformly over
the whole real \(a\)-interval and the smaller complex
output neighborhood.

At \(b=D\), the next coefficient is exactly \(k(1)=0\).
Thus (19) proves that the terminal value in (18) is
defined and differs from \(\widetilde m_N(D/N)\) by
\(O(N^{-2})\). Backward induction now constructs every
remaining denominator in (18), and gives
\[
              m_{b,N}=m(b/N)+N^{-1}m_1(b/N)+O(N^{-2}).
 \tag{20}
\]
Indeed, if the next error is at most \(C\epsilon^2/(1-\rho_1)\),
then (19) and contraction give the same bound at the current
row. For sufficiently large \(N\) this stays inside the fixed
disc. Nonzero Schur complements in this construction also
prove that every normalized trailing matrix is invertible.

The exact determinant identities therefore apply to these
constructed diagonals. With the original signs and row phase,
they yield
\[
 \frac{C_{b,N}}{C_{b-1,N}}
  =s_b h(b/N,Z)
      \{1+N^{-1}\eta(b/N,Z)+O(N^{-2})\},
       \qquad s_b=2\sin(\pi b/N),\quad M\le b\le D .
 \tag{21}
\]
The identity and its normalization are equations (23)--(24)
of the earlier amplitude proof; their algebra is independent
of its energy domain. No extra factor is inserted at either
parity.

Multiply the inverse ratios from \(b+1\) to \(D\) and use
\(C_{D,N}=1\) and \(\prod_{j=b+1}^{D}s_j=N/S_b\).
The near-one errors in (21) accumulate to a relative
\(O(N^{-1})\). Euler--Maclaurin for the smooth logarithm
of \(h\) and the smooth function \(\eta\) gives exactly
(5) and (4). It also covers the empty product at \(b=D\).
The one grid step below \(1/2\) at \(b=M-1\) uses the
already obtained analytic extension of \(m,h,\eta\);
the finite recurrence itself has only been used on its
original physical range.

The construction and errors are holomorphic in \(Z\).
Cauchy's formula on smaller fixed neighborhoods proves
the derivative assertion. This completes the proof of
the finite-source theorem.

## 5. Original phase and the next composition

On an overlap with the old containing region, its stable
branch and (3) coincide by the uniqueness in (14). Hence
their \(h,\eta,\mathcal B\) and exact source normalization
coincide. A compact arc can be enlarged within
\((\pi/2,\pi)\) to meet that old region. Continuing its
logarithm from the overlap fixes the same original action,
rather than introducing a new additive period.

For physical \(a=b/N\), changing \(\log h\) by \(2\pi i\ell\)
does not change (5): its exponential factor changes by
\(e^{-2\pi i\ell(N-b)}=1\), and \(\mathcal B\) is unchanged.
Matching on the overlap is nevertheless necessary when one
uses the continued action as a function of a free boundary
coordinate.

At \(a=1/2\), the usual interior sine-product asymptotic
puts (5) in the form of a nonzero \(N^{-1/2}\) amplitude
times the original exponential action. Its odd half-input
shift must still be retained; (5) does so before expansion.

This extension supplies a complete finite asymptotic near
each real shared coordinate \(1/4<y<1/2\). It does not
evaluate a subsequent integral over the whole shared
circle, establish a nonzero four-block coefficient after
that integration, or control competing parts of that circle.
Those requirements remain separate from the recurrence
transport proved here.

## Source versions

- Original terminating recurrence, trailing polynomial identities,
  and exact ratio signs:
  8564c705a0c8cd96cb7211c10166a522dde511bda27a94ac18a7cdafccf0b47f.
- Exact normalized finite Riccati equation, correction, original
  amplitude and scalar restoration:
  1620ac15a7fb61021729aeb3831b85dc6c716f140787f9984ecc29bd3be61840.
- Calibration against the original factorial action on the overlap:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
