# Polynomial multiplicity of the actual high-color root jets

Private written proof, 17 November 2026.

Fix a zero-framed knot \(K\) and \(N\ge2\). Regard its ordinary reduced
integral-color invariant as a function \(\mathcal C_n(q)\), so that
\(\mathcal C_n(q)=C_n(q^2)\) in the notation of the direct sources.
Set
\[
 q_N=e^{\pi i/N},\qquad q(\delta)=q_N(1-\delta)^{1/(2N)},\qquad
 J_j(r)=[\delta^j]\mathcal C_{N(r+1)}(q(\delta)).                 \tag{1}
\]
The root and the half-Cartan sheet are those of the original integral
matrices. Here \(r\) ranges over the nonnegative integers.

**Theorem.** For every \(j\ge0\), there is a polynomial
\(P_j\in\mathbb C[r]\) of degree at most \(2j\) such that
\(J_j(r)=P_j(r)\) for every \(r\ge0\). In particular,
\[
 J_j(r)=\sum_{a=0}^{2j}J_j(a)
       \prod_{\substack{0\le b\le2j\\b\ne a}}
                    \frac{r-b}{a-b}.                          \tag{2}
\]
The empty product for \(j=0\) is one. Equivalently,
\(\Delta_r^{2j+1}J_j=0\). Thus these actual root jets are determined
by the jets at colors \(N,2N,\ldots,(2j+1)N\).

The bound need not be optimal. Its constants and polynomial coefficients
may depend without restriction on \(K,N,j\). The proof gives no uniform
level estimate, convergent reconstruction from all jets, or lower bound
for the original closed scalar.

## 1. The coefficient filtration includes the multiplicity

Use the original matrices and constant sign frame of [H, §§1–3]:
\[
 m=N(r+1)-1,\quad
 Eu_i=[m-i+1]_q u_{i-1},\quad Fu_i=[i+1]_q u_{i+1},\quad
 Hu_i=(m-2i)u_i,
\]
\[
 w_{a,s}=(-1)^{Na(a-1)/2+as}u_{aN+s},\qquad 0\le s<N.          \tag{3}
\]
Out-of-range vectors vanish. The classical multiplicity operators are
\[
 ev_a=(r-a+1)v_{a-1},\quad fv_a=(a+1)v_{a+1},\quad Av_a=av_a,
\]
with \(ev_0=0\). Work over \(\mathbb C[r]\) with the filtered algebra
\[
 [A,e]=-e,\quad[A,f]=f,\quad[e,f]=r-2A,\qquad
 \deg r=\deg A=\deg e=\deg f=1.                               \tag{4}
\]
Head matrices have degree zero. On several strands use total degree,
with the same central parameter \(r\). This strengthens the filtration
in [A]: its coefficients were allowed arbitrary dependence on \(r\).

Here is the needed refinement of its literal coefficient proof. Put
\(z=\log(q/q_N)=\log(1-\delta)/(2N)\). For any affine integral
expression \(L\) in \(r,A\),
\[
 [NL+s]_q=(-1)^L
 \frac{q_N^s e^{(NL+s)z}-q_N^{-s}e^{-(NL+s)z}}{q-q^{-1}}.       \tag{5}
\]
After its displayed sign, a nonzero-residue factor has order-
\(\ell\) coefficient of total \(r,A\)-degree at most \(\ell\).
For a zero-residue factor,
\[
 \frac{[NL]_q}{\delta}
 =\frac{(-1)^{L+1}L}{q_N-q_N^{-1}}
       \left(1+\sum_{\ell\ge1}\delta^\ell p_\ell(L)\right),
 \qquad \deg p_\ell\le\ell.                                 \tag{6}
\]
Both assertions follow by expanding the exponentials, factoring \(Lz\)
in the second formula, and dividing only by formal units. They hold
also when \(L=0\), with the factored zero retained.

For transfer \(k=aN+b\), \(0\le b<N\), and input heads \(s,t\), the
actual counts from [A, §3] are
\[
 c_E=a+\mathbf1_{s<b},\quad c_F=a+\mathbf1_{t+b\ge N},\quad
 \nu=c_E+c_F-a.                                               \tag{7}
\]
The zero numerator strings are exactly \(e^{c_E}\) and \(f^{c_F}\).
Their remaining order-\(\ell\) factors have joint degree at most
\(\ell\), by (5)–(6). The factorial denominator depends on \(k,N,q\),
not on \(r\); its valuation is already included in \(\nu\).
Consequently the order-\(j\) coefficient of the nilpotent crossing
term has joint degree at most
\[
 c_E+c_F+j-\nu=j+a\le2j,\qquad a\le j.                       \tag{8}
\]
Only \(k<(j+1)N\) occurs. The beta signs in [A, (3.3)–(3.4)] cancel
the input-block signs at every order. The remaining \(r\)-characters
will be removed explicitly in §2, rather than absorbed into arbitrary
coefficient functions. All coefficient constants left in (8) depend
only on \(N\), heads and the indicated transfer.

The varying Cartan is \(\exp(zH_1H_2/2)\); its order-\(\ell\)
coefficient has joint degree at most \(2\ell\), since each weight
is affine in \(r,A\). The pivot \(q^H\) has degree at most
\(\ell\) at that order, and the varying zero-framing twist
\(q^{-w m(m+2)/2}\) has degree at most \(2\ell\). Products add these
budgets. Inverse-crossing coefficients obey the finite-order inverse
recursion of [A, §4], so the same \(2j\) bound holds for either sign.
Root permutations, fixed block parities and head conjugations preserve
(4). No division by a function of \(r\) is used.

## 2. The same staggered gauge removes parity at every order

This calculation is in the original integral index basis, before (3).
Put \(m_0=N-1\). A positive checked crossing with transfer \(k\) takes
\((i,j)\) to \((\alpha,\beta)=(j+k,i-k)\). Increasing the highest
weight from \(m_0\) to \(m_0+Nr\) gives a sign \((-1)^{rk}\) from
its \(k\) factors of \(E\). Formula (5) shows that this sign accompanies
every Taylor coefficient, including each vanishing root factor.
The root Cartan contributes
\[
 s_N(r)(-1)^{r(i+j)},\qquad
 s_N(r)=q_N^{(m^2-m_0^2)/2}.                                  \tag{9}
\]
Indeed the change of the half-product of output weights is
\((m^2-m_0^2)/2-Nr(\alpha+\beta)\), and
\(\alpha+\beta=i+j\). The remaining Taylor coefficients of this
Cartan have the polynomial budget already proved.
After extracting \(s_N(r)\), the full entry therefore has the sign
\((-1)^{r(i+j+k)}\), at every order.

For a braid on \(b\) strands define the constant involution
\[
 G_r|j_1,\ldots,j_b\rangle
       =(-1)^{r\sum_{\ell=1}^b\ell j_\ell}
                           |j_1,\ldots,j_b\rangle.            \tag{10}
\]
At the crossing in positions \(\ell,\ell+1\), its output/input
exponent difference is \(r(i-j-k)\), equal to \(r(i+j+k)\) modulo
two. Thus one and the same \(G_r\) removes the entry signs from
every generator. Inversion gives the negative crossing with scalar
\(s_N(r)^{-1}\). The beta frame (3) commutes with \(G_r\).
After this removal the root head matrix is the \(r=0\) head matrix,
and its multiplicity factor is the block flip with the fixed parity
\((-1)^{(N-1)(A_1+A_2)}\). It no longer depends on \(r\).

The gauges telescope through the entire word, including any normal
insertions. They commute with the diagonal pivots; on closed indices
they cancel, and the highest cut index \(0\) is fixed. The remaining
common root scalar also cancels in the actual ordinary zero-framed
closure. To see this without changing the marked half-Cartan sheet,
write \(w\) for writhe. Each of the \(b-1\) ordinary closed pivots
changes by \((-1)^r\), while the ordinary twist changes by
\[
 q_N^{[m(m+2)-m_0(m_0+2)]/2}=s_N(r)(-1)^r.
\]
The total ratio is exactly
\[
 s_N(r)^w(-1)^{r(b-1)}[s_N(r)(-1)^r]^{-w}
                   =(-1)^{r(b-1-w)}=1.                       \tag{11}
\]
The last equality uses that a one-cycle braid permutation has
\(b-1-w\) even. This is a cancellation of constant factors of the
whole formal family, hence applies to every inserted normal term.
The nonconstant Cartan, pivot and twist factors remain in §1's joint
degree budget. No parity subsequence of \(r\) is being selected.

## 3. The original one-component cut preserves the degree bound

Use a braid whose closure is \(K\), cut on one strand, and take the
highest integral entry of its ordinary pivotal partial trace. The
generic long-knot matrix is the scalar \(\mathcal C_{N(r+1)}(q)\)
times the identity [H, §5]; thus this is the required invariant,
with no division by the color dimension.

Expand the order-\(j\) word, after §2, into fixed head matrices and
products of multiplicity operators of total joint degree at most
\(2j\). The root multiplicity permutation is a single cycle. The
ordered partial trace of that permutation with a tensor product
of inserted words multiplies the words along that cycle. One can
check this directly by writing its index deltas: every closed index
is identified with the next word's index, leaving one matrix product
from the incoming cut to the outgoing cut. There is no residual
closed multiplicity loop and hence no factor \(r+1\).

The fixed root parities can be commuted through the words using
\(PeP=-e\), \(PfP=-f\), \(PAP=A\) when \(P=(-1)^A\).
Each crossing supplies two such parity occurrences; their total
around the one component is even. Their remaining commutation signs
are constants independent of \(r\). All head contractions are finite
sums in spaces of dimension depending on \(N\) and the fixed braid,
also independent of \(r\). We are left with highest multiplicity
matrix coefficients of joint degree at most \(2j\).

For completeness, such a coefficient has \(r\)-degree at most its
joint degree, uniformly down to \(r=0\). In the highest-weight Verma
basis \(v_a\), \(a\ge0\), each step of a fixed word has a coefficient
constant or affine in \(r\); the visited indices are fixed integers
determined by the word. A word of degree \(d\) therefore has highest
coefficient polynomial in \(r\) of degree at most \(d\). For integral
\(r\ge0\), the tail spanned by \(v_a\), \(a\ge r+1\), is invariant:
the only possible returning edge has \(ev_{r+1}=0\). Its quotient is
the finite multiplicity module. The highest coefficient is unchanged
by this quotient. This also proves that the transfer cutoff in (8)
does not add spurious terms at small \(r\).

The finite sum of these coefficients proves the theorem. At \(j=0\)
it agrees with the actual all-color root identity in [H, (5.1)].
Formula (2) is ordinary interpolation of the proved polynomial; it
does not assume a color recurrence or identify different colors away
from the root.

## 4. Scope and complete proof sources

This is a finite-matrix coherence statement for the ordinary reduced
zero-framed knot invariant. It does not assert that arbitrary inserted
co-sources obey the same scalar formula, or replace an ordinary pivot
by a frozen ADO pivot off the root. It supplies neither a geometric
projection nor a growth-selection principle from root jets alone.

The only proof sources are the following complete texts. The new
ingredients above are the joint coefficient degree, the all-order
global parity cancellation, and its scalar highest-cut evaluation.
No computational audit cited by either source is used in this proof.

- A: [high_color_all_normal_frobenius_filtration.md](high_color_all_normal_frobenius_filtration.md),
  SHA256 `ec43cf5e29aa5acfe64662cd95a12f4afbdac07a50798f96b886d4d52baa0b5a`.
- H: [high_integral_color_frobenius_wall_source.md](high_integral_color_frobenius_wall_source.md),
  SHA256 `0a896424a143c133631f11d6a58c34c36aa1d90c3db60d3ade9b9b23da623578`.
