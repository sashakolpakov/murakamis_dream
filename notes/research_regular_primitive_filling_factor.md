# The regular peripheral factor for a primitive filling

Private written proof, 18 November 2026.

In a regular peripheral chart, the matrix filling equation has a
single regular coordinate. The eigenvalue equation has an extra
parabolic factor. Keeping the regular coordinate explains why the
zero centered charge is excluded by the full group relation, and
gives a quantitative exclusion for approximate closure.

The group law below is the familiar regular centralizer model.
No novelty is claimed for that group. The point here is the
literal primitive word, its unspecialized factor, and the precise
logarithmic condition on the actual complete chart.

## 1. Actual commuting peripheral maps

Use the marked complete peripheral chart of [F]. On one selected
cusp its projective affine holonomies are
\[
 \mu(w)=m w+B,\qquad \lambda(w)=l w+D,\qquad
 m=e^U,\quad l=e^V .
 \tag{1}
\]
The centered logarithms vanish at the complete point. The
functions \(B,D\) are holomorphic on a fixed chart, \(B\ne0\),
and
\[
 (m-1)D=(l-1)B,\qquad
 V=U\tau,\qquad \Im\tau>0 .
 \tag{2}
\]
Other cusp parameters may vary in this chart. These are actual
primitive peripheral words and translations, not just their traces.
Set \(d=D/B\). Then
\[
                         l=1+(m-1)d .
 \tag{3}
\]
For any integer \(k\), the function
\[
 u_k(z)=
 \begin{cases}
  \sum_{j=0}^{k-1}z^j,&k>0,\\
  0,&k=0,\\
  -\sum_{j=k}^{-1}z^j,&k<0
 \end{cases}
 \tag{4}
\]
is a Laurent polynomial and obeys
\((z-1)u_k(z)=z^k-1\), including at \(z=1\).
In particular \(u_k(1)=k\).

Fix integers \(a,b\), not both zero; for an actual primitive filling
also require \(\gcd(a,b)=1\). Composition of (1), including inverse
powers, gives
\[
 \mu^a\lambda^b(w)=m^al^b w+B\,t_{a,b},\qquad
 t_{a,b}=u_a(m)+m^a d\,u_b(l).
 \tag{5}
\]
For positive powers this is the finite geometric sum. For inverse
powers the translation of \(\mu^{-1}\) is \(-B/m\), which
proves the negative case in (4)--(5). Commutation makes the chosen
word order immaterial.

The whole peripheral identity is
\[
                  m^al^b-1=(m-1)t_{a,b}.
 \tag{6}
\]
One may verify it directly using (3)--(4), without dividing by
\(m-1\). Since \(B\ne0\), (5)--(6) prove
\[
 \boxed{\qquad \mu^a\lambda^b=1\text{ in }\mathrm{PSL}_2
                         \quad\Longleftrightarrow\quad t_{a,b}=0 .
 \qquad}
 \tag{7}
\]
The eigenvalue condition \(m^al^b=1\) alone is weaker.
At \(m=l=1\), it holds identically whereas
\(t_{a,b}=a+bd\).

## 2. The regular centralizer coordinate and saturation

Relative to \(B\), write a commuting affine map as
\[
             g_t(w)=(1+(m-1)t)w+Bt .
\]
The multiplier must be nonzero. Direct composition gives
\[
 g_tg_s=g_{t+s+(m-1)ts}.
 \tag{8}
\]
The meridian is \(g_1\), the longitude is \(g_d\), and the
primitive word is \(g_{t_{a,b}}\). At \(m=1\) this is the
additive translation group. Thus \(t_{a,b}\), not just its
multiplier, is the regular group coordinate of the filling word.

This distinction is scheme-theoretic as well. In the universal
regular peripheral coordinate ring
\[
 R=\mathbb C[m,m^{-1},d,(1+(m-1)d)^{-1}],
 \tag{9}
\]
\(m-1\) is prime, and \(t_{a,b}\) is not divisible by it:
its restriction is the nonzero polynomial \(a+bd\).
The ring is a localization of a polynomial ring and is a unique
factorization domain. Equation (6) therefore implies
\[
  (m^al^b-1):(m-1)^\infty=(t_{a,b}) .
 \tag{10}
\]
Indeed repeated division removes precisely the \(m-1\) factor;
none is a factor of \(t_{a,b}\). Here
\(I:f^\infty=\{r:f^kr\in I\text{ for some }k\ge0\}\).
Formula (10) is a statement in the regular peripheral ring.
It is not an instruction to saturate an already eliminated
A-polynomial in the eigenvalue torus and assume the translation
coordinate has thereby been recovered.

## 3. Centered charges and the divided exponential

Define the entire function
\[
        \psi(z)=\frac{e^z-1}{z},\qquad \psi(0)=1.
 \tag{11}
\]
It has the everywhere convergent series
\(\sum_{j\ge0}z^j/(j+1)!\). Shrink the complete chart so
\(\psi(U)\) is a unit. Put
\[
             s=aU+bV=U(a+b\tau).
\]
Equations (2), (5), and (6) give the exact holomorphic formula
\[
 \boxed{\qquad
 t_{a,b}=(a+b\tau)\frac{\psi(s)}{\psi(U)} .
 \qquad}
 \tag{12}
\]
For \(U\ne0\), divide (6) by \(e^U-1\) and use \(s/U=a+b\tau\).
Both sides are holomorphic at \(U=0\), so equality extends there.
In particular this extension retains the whole factor; it never
specializes a quotient of two zeros separately.

For real \(a,b\), the factor \(a+b\tau\) does not vanish on this
chart. Consequently (7) is equivalent to
\[
                 s=2\pi i q,\qquad q\in\mathbb Z\setminus\{0\}.
 \tag{13}
\]
To check the zero set, \(\psi(s)=0\) means \(e^s=1\) and
\(s\ne0\). Writing \(s=x+iy\) first gives \(x=0\), then
\(y\in2\pi\mathbb Z\). At such a nonzero zero,
\(\psi'(s)=1/s\ne0\). At \(s=0\) its value is one.
These facts also give the local multiplicity of the regular
word equation in the \(s\)-coordinate.

All integers in (13) are projective charges. Retaining a chosen
\(\mathrm{SL}_2\) slope sign may further restrict their parity;
it does not permit zero. Outside the centered chart one must use
the whole word formula (5), not keep (12) while forgetting a zero
of its denominator or changing a logarithmic lift independently.

## 4. Quantitative exclusion of the zero-charge region

On a smaller fixed compact chart suppose
\[
 |B|\ge B_0>0,\qquad
 \Im\tau\ge m_0>0,\qquad |\tau|\le T,\qquad
                           |\psi(U)|\le C_\psi .
\]
For \(\ell=(a^2+b^2)^{1/2}\), elementary real linear algebra gives
\[
 |a+b\tau|\ge c_0\ell,\qquad
                         c_0=m_0/\sqrt{1+T^2}.
 \tag{14}
\]
Indeed the real matrix with columns \(1,\tau\) has determinant at
least \(m_0\) and largest singular value at most
\(\sqrt{1+T^2}\). Its smallest singular value is at least their
quotient.

Choose a fixed \(\eta>0\) sufficiently small that
\(|\psi(s)|\ge1/2\) for \(|s|\le\eta\). Such a choice follows
directly from (11), since
\(|\psi(s)-1|\le |s|e^{|s|}/2\). The translation \(T_{a,b}=Bt_{a,b}\)
of the full slope word then satisfies
\[
       |s|\le\eta
       \quad\Longrightarrow\quad
       |T_{a,b}|\ge\frac{B_0c_0}{2C_\psi}\,\ell .
 \tag{15}
\]
Thus approximate matrix closure with translation error smaller
than this bound cannot occur in the zero-charge region. This is
a bound in the fixed normalized affine chart; it is not invariant
under arbitrary unbounded conjugations. In particular it does
not control a source configuration escaping that chart.

## 5. Source relevance and complete direct

The regular peripheral coordinate removes the parabolic factor
in the eigenvalue equation while keeping the original primitive
word. For an actual representation of a filled group, (13)
supplies nonzero centered integer charges without first choosing
a Fourier alias label.

This is a statement about the matrix filling relation. To apply
it to a quantum critical point one must still prove its actual
peripheral-word map and that full matrix relation, with its
boundary and normal terms. Exponentiated critical equations or
the existence of a nonzero Fourier label do not supply those
facts. No geometric coefficient or volume-conjecture limit is
claimed here.

The sole complete proof direct is
notes/finite_geometric_certificate_uniform_filling_existence.md,
SHA256 f3f78212e1f42f501593412a71c21590f24f8838f4add8abeb2f12534ad2b39b.
It supplies the actual holomorphic affine peripheral chart,
commutation, and \(V=U\tau\) with positive cusp shape. Its entire
unchanged text was read in this research sequence, every used
implication checked, and the matching pin renewed. All word,
group, saturation, zero-set and quantitative calculations are
proved above. Only written mathematics and text/hash operations
were used; frozen manuscripts and public files are unchanged.
