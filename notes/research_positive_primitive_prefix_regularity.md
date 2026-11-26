# Proper Newton prefixes at a positive primitive filling

Private written proof, 15 November 2026.

At a positive solution of the original primitive filling equations,
every proper group of incident edges has a nonzero period component
in a fixed real direction. This excludes all algebraic divisors of
the intermediate Newton labels, independently of the signed powers
assigned to the group. A binary resolution that leaves one incident
factor for the final complementary pairing therefore has no
algebraically singular multiplication or single-crossing gate.

This does not place the labels in the strips required by the original
factorial asymptotics. It does not determine a coefficient in the
original quantum integration cycle.

## 1. Comparing one endpoint with its complete value

For an original positive edge use the canonical angles \(t,u\),
returns \(r_t,r_u\), and coordinates
\[
 a=\tan(t/2),\qquad b=\tan(u/2),\qquad q^2=1+a^2+b^2.
 \tag{1}
\]
The pinned positive-edge theorem gives the exact criterion
\[
                  \Re q>\sqrt{(\Re a)^2+(\Re b)^2},
 \tag{2}
\]
and the global comparison
\[
 \Re\{\delta r_t\,\overline{\delta t}
               +\delta r_u\,\overline{\delta u}\}>0
 \tag{3}
\]
for any two distinct positive configurations. Their joining segment
need not remain positive. Its canonical branches satisfy
\[
       |\Re t|,|\Re u|<\pi,\qquad
       |\Im r_t|,|\Im r_u|<\pi/2.
 \tag{4}
\]

**Lemma 1.** If \((t,u)\) is positive, so is \((0,u)\). If \(t\ne0\),
\[
                            \Re(r_t\overline t)>0.
 \tag{5}
\]

**Proof.** Positivity excludes
\(b\in i[1,\infty)\cup-i[1,\infty)\). Write \(b=x+iy\), and
choose \(q_0=\sqrt{1+b^2}\) with positive real part. For \(x\ne0\),
the radicand is not a nonpositive real number, and
\[
 (\Re q_0)^2-x^2
       =\frac{|1+b^2|+1-|b|^2}{2}>0.
 \tag{6}
\]
If \(|b|^2\le1\), positivity of the expression is immediate,
with equality requiring the excluded values \(b=\pm i\).
If \(|b|^2>1\), it follows from
\[
                 |1+b^2|^2-(|b|^2-1)^2=4x^2>0.
\]
For \(x=0\), the excluded cuts give \(|y|<1\), so
\(q_0=\sqrt{1-y^2}>0\). Hence \(\Re q_0>|\Re b|\) in all
cases. This is criterion (2) at \((0,u)\).

Its canonical first return is zero. Apply (3) to \((t,u)\)
and \((0,u)\): the second angle is unchanged, and the first
changes nontrivially. This gives (5). \(\square\)

## 2. A strip containing every proper prefix

Fix a selected vertex of the original circle tree, and count its
incident factors individually. Write its angle as \(t\), its returns
as \(r_e\), and its real signed power as \(n\). Assume all its
incident edges are positive and that its full marked period is
\[
                         \sum_e r_e-\frac{int}{2}=-\pi i.
 \tag{7}
\]
For physical surgery \(n=\eta-2p\), with the original carrier
\(\eta\). There is no new existence assertion here.

We have \(t\ne0\), since otherwise all its returns vanish and (7)
fails. Lemma 1 makes every number
\[
                            \ell_e=\Re(r_e\overline t)
 \tag{8}
\]
strictly positive. Pairing (7) with \(\overline t\) gives
\[
                       \sum_e\ell_e=-\pi\Im t.
 \tag{9}
\]
Thus \(H=-\Im t>0\) follows from the stated hypotheses.

For a nonempty proper edge subset \(A\) and any real allocation
\(n_A\), put
\[
                    R_A=\sum_{e\in A}r_e-\frac{i n_A t}{2}.
 \tag{10}
\]
An integer \(n_A\) is the actual signed number of crossing layers
assigned to that partial product.

**Theorem 2.** Every such prefix lies in the open convex strip
\[
             \mathcal S_t=\{R:0<\Re(R\overline t)<\pi H\}.
 \tag{11}
\]
Consequently, for every integer \(k\),
\[
           R_A\ne\pi i k,\qquad
           R_A\ne it/2+\pi i k,\qquad
           R_A\ne-it/2+\pi i k.
 \tag{12}
\]

**Proof.** The allocation term in (10) has zero real pairing
with \(t\). Therefore
\[
                  \Re(R_A\overline t)=\sum_{e\in A}\ell_e.
 \tag{13}
\]
The sum is positive and omits at least one positive term in (9).
This proves (11). Each value excluded in (12) has real pairing
\(-\pi kH\), outside the strict interval in (11). \(\square\)

This is independent of the powers' signs and magnitudes, the number
of incident factors, and the chosen binary tree. The proof uses the
actual canonical returns, not arbitrary logarithms of eigenvalues.

## 3. Newton labels and multiplication divisors

Keep \(a=\tan(t/2)\). The positive canonical domain gives
\(a\ne0\) and \(1+a^2\ne0\). Define
\[
 N(R)=a\cosh R+i\sinh R,\qquad
 D(R)=a\cosh R-i\sinh R,\qquad Y(R)=N(R)/D(R).
 \tag{14}
\]
The original prefix dictionary in the pinned spectral-adapter note is
\[
          e^{2\pi i x_A}=Y(R_A),\qquad
          \tan(\pi x_A)=\tanh(R_A)/a.
 \tag{15}
\]
The exponential formula remains meaningful when the tangent formula
has a pole. The label retains its continued logarithmic lift.

The zeros of \(N\) and \(D\) are respectively
\(R=it/2\pmod{\pi i}\) and \(R=-it/2\pmod{\pi i}\).
This follows by exponentiating \(a=\tan(t/2)\).
Also \(Y(R)=1\) exactly when \(\sinh R=0\). Theorem 2 gives
\[
                      Y(R_A)\in\mathbb C^*,\qquad
                      \sin(\pi x_A)\ne0.
 \tag{16}
\]
The strip \(\mathcal S_t\) is simply connected, so its nonvanishing
holomorphic function \(Y\) has a holomorphic logarithm. One prescribed
value fixes that logarithm; other choices shift \(x_A\) by an integer.

For \(c=-2\cos t\) and \(C(x)=2\cos(2\pi x)\), direct substitution
also gives
\[
 C(x_A)-c=
 \frac{4a^2}
 {(1+a^2)(a^2\cosh^2R_A+\sinh^2R_A)}\ne0.
 \tag{17}
\]
The denominator is \((1+a^2)N(R_A)D(R_A)\).
Thus there is no additional spectral-node collision.

Consider a product with disjoint nonempty subsets \(A,B\), whose
union is still proper. Allocated powers add, so its output return
is \(R_A+R_B\). Denote its labels by \(x,y,z\).
The seven arguments of the original multiplication factorials are
\[
                   x,\ y,\ z,\ x+y,\ z-x,\ z-y,\ x+y-z.
 \tag{18}
\]

**Corollary 3.** None of the seven sines of the arguments (18)
vanishes at the stated positive primitive point.

**Proof.** The individual prefix sines are nonzero by (16).
For two returns \(\alpha,\beta\), direct multiplication gives
\[
 N(\alpha)N(\beta)-D(\alpha)D(\beta)
                         =2ia\sinh(\alpha+\beta),
 \tag{19}
\]
\[
 \begin{split}
 &N(\alpha)N(\beta)D(\alpha+\beta)
       -D(\alpha)D(\beta)N(\alpha+\beta)\\
 &\hspace{12mm}=2i(1+a^2)\sinh\alpha\,\sinh\beta\,
                                         \sinh(\alpha+\beta).
 \end{split}
 \tag{20}
\]
All denominator factors are nonzero. Equation (19) excludes
\(e^{2\pi i(x+y)}=1\); (20) excludes
\(e^{2\pi i(x+y-z)}=1\).
Finally,
\[
        Y(R)=\frac{(a+i)e^{2R}+a-i}{(a-i)e^{2R}+a+i}
 \tag{21}
\]
is a Möbius function of \(e^{2R}\), with determinant \(4ia\ne0\).
Hence \(Y(\alpha+\beta)=Y(\alpha)\) would force \(e^{2\beta}=1\),
and \(Y(\alpha+\beta)=Y(\beta)\) would force \(e^{2\alpha}=1\).
Both are excluded by Theorem 2. These are the divisors for
\(z-x\) and \(z-y\). \(\square\)

## 4. Signed crossings and a regular algebraic resolution

A single crossing of sign \(\sigma=\pm1\) changes a proper-prefix
return by
\[
                         R\longmapsto R-i\sigma t/2.
 \tag{22}
\]
Both returns remain in \(\mathcal S_t\), so their input and output
label sines are nonzero. The sine of their difference is also
nonzero: equality of their clocks would, by (21), force
\(e^{-i\sigma t}=1\), contrary to \(\Im t<0\).

For an integer physical crossing power, any selected vertex of degree
at least two has a direct algebraically regular resolution. Leave one incident factor for
the final complementary Frobenius pairing. Multiply the other
factors by any binary tree, apply the required signed crossing
layers, and perform that pairing. Every gate prefix has a nonempty
proper edge set, so all the preceding exclusions apply. The
degree-two zero-power expression has no gate to check.
Distributing crossing layers among other proper subproducts
gives the same divisor exclusions.

These are exact operations in the full original Newton algebra.
Multiplication is associative and commutative; crossing powers
are literal multiplications by \(R^n\); signed powers fuse exactly.
The final pairing remains
\(\phi_N(e_i e_j)=\mathbf1_{i+j=N-1}\), including all repeated-node
normal data. No factors or normals are discarded.

The rational fiber Hessians displayed in the spectral-adapter note
are consequently finite and nonzero at these labels. Every sine
in their formulas is among those just checked, their exponential
factors are units, and \((2-c)/4=1/(1+a^2)\ne0\). This is an
algebraic statement about those formulas, not a factorial
asymptotic outside its proved domain.

## 5. Remaining analytic and endpoint questions

The complete edge set, with its full power, has return \(-\pi i\)
on the boundary of (11). It is handled by the complementary
pairing, not as a strict multiplication gate. A degree-one vertex
has no nonempty proper subset, so this theorem supplies no
degree-one endpoint chart.

The theorem removes genuine algebraic prefix resonance as an
additional obstruction at an existing positive primitive point.
It does not prove that every hyperbolic partial filling has such
a positive point.

There is a separate analytic question. When \(\Re t\ne0\),
the strip (11) is oblique and its boundary generally has a
non-real image under (14). A holomorphic logarithm on (11)
does not by itself place the real parts of all arguments (18),
or the crossing arguments, between zero and one. The continued
primitive and its integer Fourier characters must still be
matched to a domain where the original factorial interpolation
has the required asymptotics. No label is reset here.

Even a valid factorial comparison and local Morse equivalence
do not determine the geometric block's coefficient in the original
finite cycle. Endpoints, other Fourier modes and the full coherent
contraction remain. No new volume limit or knot family is asserted.

## Direct sources

* notes/research_positive_edge_global_monotonicity.md, SHA256
  da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500:
  canonical branches, inverse-tangent cut exclusion, positivity,
  global comparison, and full marked primitive periods.
* notes/research_newton_spectral_legendre_adapters.md, SHA256
  34c0e2e1114488c6ac82a5dffbdbd8a4a8d85e7fbba252de91833dc8d697e303:
  original prefix dictionary and crossing increment, multiplication
  and crossing generating families, and their fiber Hessians.
* notes/research_corner_newton_source_transport.md, SHA256
  24a7f6f721d0a925405424d9a8aba1ac9db8ce7e90ddb937b2a317e10f98b345:
  full Newton algebra, signed layers and transpose convention,
  exact crossing transport, and original integer cycles.
* notes/actual_positive_newton_multiplication.md, SHA256
  543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb:
  original multiplication factorials, complementary pairing and
  associativity in the full repeated-root algebra.

Only written reasoning, source-text reads and file hashes were used.
No mathematical code, numerical evaluation, tests or compilation
were run. Frozen and public files were not changed.
