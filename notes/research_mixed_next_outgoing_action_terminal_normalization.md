# Terminal normalization of the original outgoing action

Private phase proof, 9 November 2026. The original selected outgoing
action continues to the terminating input and tends to zero there.
Consequently the action obtained by integrating the stable recurrence
root from that endpoint has exactly the original real normalization.
No finite summation contour is continued across a factorial wall in
this argument. No mathematical numerical evaluation is used.

## 1. The original root continues to the endpoint

Keep the outgoing rectangle and the original phase of the
[selected-sheet theorem](research_mixed_next_outer_selected_outgoing_sheet.md):
\[
 z_*=u+ih,\quad 3/10\le u\le39/100,\quad
 -3/100\le h\le1/50,\qquad Z=e^{-2\pi iz_*},
\]
\[
 Q(s;a,z_*)=g(a+s)+g(z_*+s)-2g(s)-g(a)-g(z_*)+2\pi ias,
 \qquad
 g(v)=\frac{\operatorname{Li}_2(e^{-2\pi iv})-\pi^2/6}{2\pi i}.
                                                               \tag{1}
\]
The primitive in (1) is the one fixed in
[the original cotangent source](research_mixed_global_cotangent_roots.md).
It is initially taken on the strip \(0<\Re v<1\).

We now allow the real input to range over \(1/2\le a<1\).
Write
\[
 P=\cot(\pi a)\le0,\qquad Q_0=\cot(\pi z_*)=q_0+i\beta.
\]
The original bounds \(q_0>|\beta|\), \(|\beta|<1/2\) are
unchanged. The quadratic for \(S=\cot(\pi s)\) is
\[
 F(S)=S^2+(P+Q_0)S-1+i(Q_0-P)=0.                              \tag{2}
\]
The half-plane argument in the selected-sheet proof applies to
every \(P\le0\). Explicitly,
\[
 \Re F(iv)=-1-v^2-\beta(1+v)\le-7/16\qquad(v\in\mathbb R).
                                                               \tag{3}
\]
At \(\beta=0\), the discriminant has a square root whose positive
real part exceeds \(|P+q_0|\); hence exactly one root lies in each
open half-plane. A compact homotopy in \(\beta\) preserves this
count by (3). The roots cannot coalesce because there is one in
each half-plane. Thus the right root is simple for every finite
\(P\le0\).

The right root also has negative imaginary part. It does at
\(\beta=0\). A crossing through a positive real root \(S=r\)
would give
\[
 P=q_0+\beta r,\qquad (1+\beta)r^2+2q_0r=1+\beta.
\]
The second equation implies \(0<r<1\), and the first would then
give \(P>0\), a contradiction. Therefore
\[
 T=\frac{S+i}{S-i},\qquad s=\frac{\Log T}{2\pi i},
 \qquad \Im T>0,\quad |T|<1,\quad
 0<\Re s<1/2,\quad \Im s>0.                                  \tag{4}
\]
Here \(0<\arg T<\pi\) fixes the logarithm. This root agrees
with the original selected root on \([1/2,5/6]\).

Its limiting value is explicit. Put \(P=-R\) and
\(\varepsilon=1/R\). Multiplying (2) by \(\varepsilon\)
gives
\[
 \varepsilon S^2+(-1+\varepsilon Q_0)S
       -\varepsilon+i\varepsilon Q_0+i=0.
\]
At \(\varepsilon=0\) the finite root is \(S=i\), with
nonzero derivative \(-1\) with respect to \(S\). The implicit
function theorem and coefficient comparison give, uniformly over
the compact outgoing rectangle,
\[
 S_{\rm small}=i+
       \frac{-2-2\beta+2iq_0}{R}+O(R^{-2}).                     \tag{5}
\]
Its real part is negative for large \(R\). By the sum of the
two roots, the right root is therefore
\[
 S=R-Q_0-i+O(R^{-1}).                                         \tag{6}
\]
Consequently \(T\to1\) and \(s\to0\), uniformly as
\(a\uparrow1\).

The sharper inequality \(\Re s<1-a\) was proved only on the
original middle interval. It is not needed here. This section
continues an algebraic critical point, not an admissible finite
integration contour.

## 2. Continuing the primitive with its additive constant intact

There is a convenient explicit continuation to the upper half-plane:
\[
 g_+(v)=i\pi(v-v^2)
       -\frac{\operatorname{Li}_2(e^{2\pi iv})-\pi^2/6}{2\pi i},
                           \qquad \Im v>0.                    \tag{7}
\]
The dilogarithm here is defined by its convergent unit-disc series.
Its derivative is
\[
 g_+'(v)=i\pi-2\pi iv+\log(1-e^{2\pi iv}).                      \tag{8}
\]
Exponentiating (8) gives \(1-e^{-2\pi iv}\). On the upper part
of the original strip its logarithm agrees with the one in (1).
For example the boundary value for \(0<v<1\) is
\(\log(2\sin\pi v)+i(\pi/2-\pi v)\). The derivatives agree
there, and both primitives tend to zero at \(v=0\). Therefore
\(g_+=g\) on that overlap.

The series in (7) is continuous up to the unit circle, so (7)
also proves
\[
                        g_+(0)=g_+(1)=0.                       \tag{9}
\]
In particular continuing \(g(a+s)\) above the point \(1\)
does not insert a new additive constant.

Define the continued phase by
\[
 \widetilde Q(s;a,z_*)=
 g_+(a+s)+g(z_*+s)-2g_+(s)-g(a)-g(z_*)+2\pi ias.               \tag{10}
\]
For the root in (4), the two upper-half-plane arguments in
(10) are legitimate. Also
\(0<\Re(z_*+s)<89/100\), so that term stays in the original
regular strip, even when its imaginary part changes sign.
The remaining terms retain the original strip or boundary values.

The exponentiated critical equation is unchanged by (8).
Hence \(\partial_s\widetilde Q\) belongs to \(2\pi i\mathbb Z\)
along this continuous root. It is zero on the original middle
interval, and therefore remains zero for all \(1/2\le a<1\).
Set
\[
 \widetilde{\mathcal S}(a,z_*)
                 =\widetilde Q(s(a,z_*);a,z_*).
\]
This is the original \(\mathcal S\) on \([1/2,5/6]\). By
(4)--(6), the continuity in (9), and continuity of the original
strip primitive at \(z_*\) and at \(1\), every difference in
(10) tends to zero. Thus
\[
 \boxed{\quad
 \lim_{a\uparrow1}\widetilde{\mathcal S}(a,z_*)=0.
 \quad}                                                        \tag{11}
\]
The limit is uniform in the outgoing rectangle. This proves the
normalization directly from the original primitive.

## 3. The stable recurrence root gives the same real action

For \(1/2\le a\le1\), put
\[
 t=(\pi a-\pi/2)/2,\quad \sigma=2\sin(\pi a),\quad
 \tau=\sigma^{3/2},\quad w=-e^{5it},\quad
 V=3e^{it}+2e^{-3it}+Ze^{5it}.
\]
The principal full-tail energy estimate provides a continuous
row rotation \(1+i\beta_0(t)\) with
\[
 \Re V-\beta_0(t)\Im V-2\tau>51/350.                            \tag{12}
\]
Define \(m(a,Z)\) as the first diagonal of the bounded inverse
of the half-line operator with diagonal \(V\) and off-diagonals
\(\tau e^{it}\), \(\tau e^{-it}\). The accretivity argument
in the [finite-ratio theorem](research_mixed_next_finite_outgoing_ratio_transport.md)
applies with the rotation in (12). For \(a<1\),
\[
 \tau^2m^2-Vm+1=0,\qquad |\tau m|<1.                           \tag{13}
\]
At \(a=1\), the operator is the scalar \(V(1,Z)I\), so
\(m(1,Z)=1/V(1,Z)\ne0\). Thus \(m\) is continuous, bounded,
and bounded away from zero on the closed parameter set.

For \(a<1\), let \(Y=e^{-2\pi ia}\) and
\[
                       L(a,Z)=-Y(Y-1)w m(a,Z).                  \tag{14}
\]
The exact principal algebra in the finite-ratio theorem shows
that this is the unsigned outgoing root inside
\(|L|=\sigma^{-1/2}\). The full-tail inequality (12) excludes
any root on that circle. The continued critical root (4)
gives another expression for an unsigned root,
\[
                         L_{\rm crit}=\frac{T-Y}{1-Y}.          \tag{15}
\]
It agrees with (14) on the middle interval. The two roots cannot
coalesce or cross the circle for \(a<1\): their modulus product
is \(1/\sigma\), and a double root would lie on the excluded
circle. Neither root is zero or infinite at any such parameter.
Continuity therefore gives \(L_{\rm crit}=L\) throughout
\([1/2,1)\).

Since the continued phase is critical in \(s\), differentiating
in \(a\) and exponentiating gives (15). Taking moduli yields
\[
 \partial_a\Re\widetilde{\mathcal S}(a,z_*)=
                  \log|L(a,Z)|=\log\sigma+\log|m(a,Z)|.         \tag{16}
\]
Only \(\log\sigma\) is singular at the terminal endpoint;
it has an integrable logarithmic singularity. Integrating (16)
and using the proved terminal value (11) gives
\[
 \boxed{\quad
 \Re\widetilde{\mathcal S}(a,z_*)
 =-\int_a^1\log|L(v,Z)|\,dv
 =J(a)-\int_a^1\log|m(v,Z)|\,dv,
 \quad}                                                        \tag{17}
\]
where
\(J(a)=\int_0^a\log(2\sin\pi v)\,dv\) and \(J(1)=0\).
In particular, on the original middle interval this is an
identity for the original action, with no undetermined real
additive constant.

Equation (17) identifies the action obtained by the finite
trailing-resolvent product with the original conditional action.
It does not estimate the coherent sum of these outgoing
polynomials against the inner periods. It also does not claim
that the original finite contour follows the continued critical
point beyond the middle interval.

## Source versions

- Selected outgoing zero lift and signed pairing:
  850d97273259d39b0fc0ecf89bedaddceb97b13555c38a95d1f3e9fa7643067d.
- Full-tail energy:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Actual finite ratio and half-line root conventions:
  2bf8a2f401b3472da0d250c97403fa776396e3dd524bd149a9209b6f8eacdeaf.

