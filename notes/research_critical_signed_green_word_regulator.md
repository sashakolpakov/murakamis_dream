# A formal five-shape identity on the critical signed Gauss word

> **Source-identification correction, 31 October 2026.** The exact algebra below uses the complete-color five-shape expression at every crossing, although the auxiliary raw meridian has trace zero and color \(\chi_{aux}=\pm i\), rather than \(-1\). The universal Gauss/Hurwitz MAP remains valid, but the actual mixed crossing symbol has color factors omitted here. Therefore the asserted identification with the ORIGINAL mixed source or its diagram regulator is withdrawn. The computed rational word closure, formal-symbol differential and calibrated formal-symbol identity remain valid algebraic results. The true mixed-color symbol, its monomial boundary term, and any actual relative-volume comparison are UNPROVED in this note. All occurrences of “actual” below referring to the twenty SYMBOLS must be read subject to this correction; the actual matrix maps are unaffected. This note is unpublished and quarantined from geometric or quantum conclusions.

Internally reviewed FORMAL algebraic identity, 31 October 2026. Not
approved for publication. The exact verifier and the complete local
domain/calibration argument have passed separate full reviews and
fresh replays by root and coherent_partner_currents at the scope
stated below. These are internal checks, not external peer review.

This is a FORMAL-symbol identity on the universal untwisted four-crossing
word on its free-spectral critical straddling branch. Both auxiliary
central lifts are included. It does not assert an off-critical identity,
a global relative fundamental-cycle identity, or a contribution of any
original finite-sum cycle. In fact the corresponding off-critical
local identity is false.

## 1. The critical domain and the retained source primitive

Use the calibrated action and physical conventions of
[the signed straddling relation](research_signed_straddling_green_relation.md).
Let \(x,y,b>0\), \(0<\delta<1/2\), and put

\[
s=\sin(\pi\delta),\quad k=\cos(\pi\delta),\quad A=x+y,\qquad
c=b+A/s^2,\qquad T=\sqrt{bA+xy+b^2s^2}.
\tag{1}
\]

Thus \(c>\max(x,y)\). The selected pre- and post-pole endpoints satisfy

\[
\mu=\frac1\pi\arctan\frac{bk}{T},\qquad
\nu=\frac1\pi\arctan\frac{ck}{T},\qquad
0<\mu<\tfrac12-\delta<\nu<\tfrac12.
\tag{2}
\]

The output root is the negative one, \(T_{-c}=-T\).
Equation (1) is exactly the free real-spectral stationarity equation
for the retained absolute interval action \(G\):

\[
G_\delta=0,\qquad E_b=H_c,\qquad R_0=-E_b/H_c=-1.
\tag{3}
\]

Here both unused spectral intervals and the omitted-half scalar modes
are retained, as in the cited note. The original signed Green primitive
is \(S_G=G-\pi i(1/2+\delta)\); the actual two scalar modes differ from
it by \(\pi i/2\) and \(\pi i/2+2\pi i\delta\). Their real parts agree
on this real chart. The primitive logarithm is \(U_0=\pm\pi i\), not
zero. This distinction is essential to the auxiliary matrix below.

Write the actual face derivatives as

\[
\partial_{\log b}G=\mu,\quad
\partial_{\log c}G=1-\nu,\quad
\partial_{\log x}G=\xi,\quad
\partial_{\log y}G=\eta,\qquad
\xi+\eta=\nu-\mu.
\]

Define the critical Legendre value

\[
h=G-\mu\log b-(1-\nu)\log c-\xi\log x-\eta\log y.
\tag{4}
\]

This is the fixed-load value of the calibrated continuum source
primitive. The present lemma does not prove a new coefficient
asymptotic or a selected saddle contribution.

Let \(\mathcal W_\pm\) denote the signed Bloch--Wigner sum of the
actual four positive crossings below, with the two central choices
of the auxiliary meridian. Then the local conclusion is

\[
\boxed{\mathcal W_+=\mathcal W_-=2\pi h.}
\tag{5}
\]

The source reference flag and physical head conventions are unchanged
throughout the proof.

## 2. Rational original heads and the actual word

All face weights may be divided by \(y\). This changes neither the
physical ratios nor any head or shape below; it is not a change of
Gauss reference. Hence set \(y=1\). A common nonzero head scale \(g\)
rescales every \(E\) by \(g^{-1}\) and \(F\) by \(g\); every crossing
shape uses only \(K\)'s and products \(EF\). Thus set \(g_{\rm in}=1\)
without changing a shape.

For rational calculation use independent real parameters \(b,T,v\):

\[
s=\frac{2v}{1+v^2},\quad k=\frac{1-v^2}{1+v^2},\quad
x=\frac{T^2-b-b^2s^2}{b+1},\quad c=b+\frac{x+1}{s^2}.
\tag{6}
\]

The physical domain is \(b>0,\ 0<v<1,\ T>0,\ x>0\). It is
diffeomorphic to the connected domain \(b,x>0,\ 0<v<1\), using
\(T=\sqrt{x(b+1)+b+b^2s^2}\). In particular it is not legitimate
to keep arbitrary \(b,T\) fixed all the way to \(v=1\).

The actual head map is

\[
K=-X^{-1},\quad F=S(1-X),\quad E=(X^{-1}-1)/S,\qquad
G(K,E,F)=
\begin{pmatrix}K&E\\FK&FE+K^{-1}\end{pmatrix},\quad
L^-=\begin{pmatrix}1&0\\-KF&K\end{pmatrix}.
\tag{7}
\]

Set \(p=(T-ibk)/(T+ibk)\), \(p'=(T-ick)/(T+ick)\).
The input pairs \((X,S)\) are \((-x/b,-p)\) and \((-b,1)\).
If their matrices are \(G_1,G_2,L_1^-,L_2^-\), the ORIGINAL based
ordered product is

\[
P=(L_1^-)^{-1}G_2L_1^-G_1,\qquad
\operatorname{tr}P=\sigma=-2+4s^2.
\]

The critical auxiliary matrix and its other central lift are

\[
M_\pm=\pm\frac{2P-\sigma I}{4sk},\qquad
\det M_\pm=1,\quad \operatorname{tr}M_\pm=0,\quad M_\pm^2=-I.
\tag{8}
\]

This is the physical lift \(-iC^{-1}\) and its negative for the
already selected projective collar \(C\). The third head is the
Gauss decomposition of
\((L_2^-L_1^-)M_\pm(L_2^-L_1^-)^{-1}\).

For two successive heads \((K,E,F)=(a,e,f)\) and \((d,g,j)\), put
\(w=1-ej\). One actual positive crossing replaces them by

\[
\begin{split}
&(dw,\ [wg+e(wd-d^{-1})]/a,\ aj/w),\\
&(a/w,\ e/(dw),\ d[wf+j(w/a-a)]).
\end{split}
\tag{9}
\]

Its five shapes, with their signs, are

\[
 +B,\quad +w^{-1},\quad +A^{-1},\quad
 -B/w,\quad -(wA)^{-1},
\qquad A=-a^{-1},\quad B=-d^{-1}.
\tag{10}
\]

The minus signs in (10) denote negative coefficients of \(D\), not
negation of the shape. Apply (9)--(10) in the original order
\([2,1,1,2]\), where the positions are one-based. This defines the
twenty terms of \(\mathcal W_\pm\), with their actual crossing signs.

For completeness put

\[
\begin{split}
N_{yb}&=(x-1)+b(x+2k^2-1)+2ikT,\\
N_{yc}&=(x-1)-c(x+2k^2-1)-2ikT,\qquad
g'=\frac{N_{yb}(1-c)}{N_{yc}(1+b)} .
\end{split}
\]

The returned main pairs are exactly \((x/c,-g'p')\) and \((c,g')\);
the auxiliary head is unchanged. The verifier proves all nine
returned Gauss-coordinate identities for each lift as rational
identities over \(\mathbb Q(i)(b,T,v)\). This word closure is checked
separately from the regulator differential.

## 3. Differential identity, including rational constant norms

From (4), stationarity and \(G_\delta=0\) give
\(dh=-\log b\,d\mu+\log c\,d\nu-\log x\,d\xi\), since \(y=1\).
Define

\[
\begin{split}
N_{xb}&=x(1-x)+b(1+x(2k^2-1))+2ixkT,\\
N_{xc}&=x(1-x)-c(1+x(2k^2-1))-2ixkT.
\end{split}
\]

The physical force formulas give
\(d\arg p=-2\pi\,d\mu\), \(d\arg p'=-2\pi\,d\nu\), and
\(d\arg(N_{xb}/N_{xc})=2\pi\,d\xi\). The omitted denominators in
the last ratio are real units, so only their argument DIFFERENTIAL
vanishes. Consequently

\[
2\pi\,dh=
\log b\,d\arg p-\log c\,d\arg p'
-\log x\,d\arg(N_{xb}/N_{xc}).
\tag{11}
\]

Apply to every signed term of (10) the exact convention

\[
dD(z)=\log|z|\,d\arg(1-z)-\log|1-z|\,d\arg z.
\tag{12}
\]

The following finite factor computation proves that the sum of
(12) is precisely (11), for EACH auxiliary lift.

Factor every numerator and denominator of \(z\) and \(1-z\) over
\(\mathbb Q(i)\), make each polynomial factor monic, and place its
leading coefficient in the Gaussian rational constant. Identify a
factor with its complex conjugate in the log-norm vector. Identify
their argument differentials with opposite signs. A real polynomial
factor has zero argument differential on a regular real component.
For a Gaussian rational constant \(a\), factor the positive rational
\(a\bar a\); the coefficient of each \(\log p\) is half the exponent
of the rational prime \(p\). This retains, for example, ALL
\(\log|2|\,d\arg f\) terms. The unit \(i\) has norm one and constant
argument, so its contribution is zero for these two separate reasons.

Expand (12) as a tensor of these log-norm and argument vectors, and
subtract the three tensors on the right of (11). Every rational
tensor coefficient is exactly zero. There are 81 expanded positions
for each lift. No numerical evaluation, tolerance, use of a
closed-orbit theorem, or omission of nonunit constants enters this
certificate. Equations (6)--(10) and this factor algorithm specify
every input to the accompanying exact verifier.

## 4. Actual chart divisors and the absolute constant

The reduced rational shapes themselves extend throughout the
positive critical domain as maps to \(\mathbb P^1(\mathbb C)\).
Here is a finite factor check that avoids an assumption about
arbitrary coalescing flags. Their polynomial factors consist of
\(b,b+1,v,v\pm1,v\pm i\), four real factors, and one nonreal
factor. After the physical substitution for \(T^2\), the four
real factors, up to the explicitly nonzero factors recorded in
the verifier, are

\[
x+1-2s^2,\quad x,\quad x+1-2xs^2,\quad x+1+bs^2.
\tag{13}
\]

The nonreal factor has imaginary part
\((b+1)T(v^4-1)/2\ne0\). Only the first and third factors of (13)
can vanish. They cannot both vanish: their equations imply
\(x=1,s^2=1\), outside the domain. As the numerator and denominator
of each shape were cancelled over \(\mathbb Q(i)\), no shape has
a simultaneous zero numerator and denominator here. A Gauss-chart
divisor can therefore produce only a definite zero or pole of the
shape. The continuous extension \(D(0)=D(1)=D(\infty)=0\) extends
the sum through these divisors. The verifier independently checks
the factor registry and the five physical reductions.

For the constant, keep \(b,x>0\) fixed, with \(x\ne1\), and let
\(v\uparrow1\), using
\[
T(v)=\sqrt{x(b+1)+b+b^2s(v)^2}.
\tag{14}
\]
Then \(c\to c_1=b+x+1\), \(\mu,\nu=O(k)\), and the interval in
the definition of \(G\) shrinks to zero. Explicitly, with
\(T_1=\sqrt{x(b+1)+b+b^2}\),
\(\mu/k\to b/(\pi T_1)\) and
\(\nu/k\to c_1/(\pi T_1)\). These two positive limits lie
strictly on either side of \(1/\pi\). Put
\(r_k(\tau)=\sin(\pi k\tau)/k\). On this fixed compact
\(\tau\)-interval the actual cleared root and denominator are

\[
\begin{split}
\Lambda(k\tau)&=2k^2r_k
 \left[(x+1)r_k+\sqrt{(x-1)^2r_k^2+4x}\right],\\
\alpha(k\tau)&=4k^2(1-r_k^2).
\end{split}
\]

The numerator of their ratio, after cancelling \(k^2\), is
uniformly bounded above and below by positive constants.
Moreover \(r_k'(\tau)=\pi\cos(\pi k\tau)\) stays bounded
away from zero, so \(1-r_k^2\) has one uniformly simple zero.
The integral of \(\left|\log(\Lambda/|\alpha|)\right|\) in
\(\tau\) is therefore uniformly bounded, and the original
integral is \(O(k)\). Finally the positive-root homogeneous
formula gives \(0\le x\partial_x\log\Lambda\le1\), so
\(0\le\xi,\eta\le\nu-\mu\).
Thus (4) gives \(h\to0\). This uses the retained interval
primitive, not a normalization of a geometric volume.

Independently, the exact twenty rational shapes in (10) have,
for each lift, four zeros, four poles, and twelve finite REAL
limits as \(v\uparrow1\). The verifier records the valuation and
leading coefficient of every term. Substituting the finite
\(T(1)\) from (14) preserves those valuations for \(x\ne1\);
all their displayed leading denominators are then nonzero.
Each Bloch--Wigner value tends to zero, hence
\(\mathcal W_\pm\to0\).

More explicitly, writing \(c_1=b+x+1\), the five SHAPE limits in
their original crossing order are the same for both lifts:

| Crossing position | First | Second | Third | Fourth | Fifth |
|---|---:|---:|---:|---:|---:|
| 2 | \(0\) | \(-b\) | \(-1/b\) | \(0\) | \(1\) |
| 1 | \(0\) | \(-x/b\) | \(-b/x\) | \(0\) | \(1\) |
| 1 | \(1\) | \(x/c_1\) | \(\infty\) | \(x/c_1\) | \(\infty\) |
| 2 | \(1\) | \(c_1\) | \(\infty\) | \(c_1\) | \(\infty\) |

Each row retains the regulator coefficients \(+,+,+,-,-\).

Equations (11)--(12) make \(\mathcal W_\pm-2\pi h\) locally
constant away from the listed chart divisors. Both quantities
extend continuously across each such divisor, and the physical
domain is connected. The fixed-positive-\(b,x\) paths (14) fix
the constant to zero. Continuity in \(x\) includes \(x=1\).
This proves (5), without resetting the source reference flag.

## 5. What this identity does and does not settle

The local primitive includes all source logarithms in (4); its
Legendre subtraction is essential. The actual scalar modes have
purely imaginary differences on this real critical chart. The
auxiliary lift and its primitive logarithm are retained in (8),
so the result does not silently replace \(U_0=\pm\pi i\) by zero.

This calculation does not discard a global peripheral boundary
term. To turn the sum of local identities into representation
volume, one must still identify the ORIGINAL sewn relative
fundamental chain, including cups, caps, the unrestricted mark
and any retained half twist. The conditional group construction
is stated separately in
[the signed group-sewing note](research_regular_signed_spectral_group_sewing.md).
It does not itself imply the needed chain identity.

The present proof also does not extend to a free noncritical
spectral parameter, arbitrary complex clocks, or an arbitrary
absolute shared maximum. The sign-cocycle and regularity
hypotheses remain independent issues. No global period bound or
volume-conjecture conclusion is claimed.

## Verification artifact

The [standalone exact verifier](../experiments/research_audit_critical_signed_green_word_regulator.py)
has an optional \(\texttt{--output}\) argument and a portable
same-directory default. It generates the
word and its shapes from (7)--(10), proves the rational word
closure and differential tensor, verifies the physical factor
registry, and records all endpoint valuations. Its JSON output
contains the actual forty signed rational shapes, not only a
zero residual; the [recorded result](../experiments/research_critical_signed_green_word_regulator_results.json)
is retained as an unpublished research artifact. No
floating-point computation is used.

Internal review: root and coherent_partner_currents read the complete
proof and verifier, including constant norms, both physical lifts,
the chart-divisor argument and fixed-positive-\(b,x\) calibration.
Their separate redirected exact replays reproduced 18 returned head coordinates,
2 zero differential tensors, 172 physical shape-factor incidences,
10 physical factor reductions and 40 endpoint valuations. The
review excludes retained half twists, protected-line limits and
global relative-chain claims, which are not proved here.
