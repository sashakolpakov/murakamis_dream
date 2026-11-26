# A centered Fourier basis for the original Conway gluing

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

A single unitary change of Newton coordinates makes the original
bilinear gluing diagonal and makes both signed crossing coupons
coordinate vectors. Every multiplication then uses one symmetric
three-index tensor. The tensor is explicit, but its phases cannot
all be removed while keeping this diagonal gluing and the full
repeated-root algebra.

This is an exact compiler for the original finite source. It neither
truncates a packet to a Gaussian window nor proves a geometric lower
bound after short fillings.

## 1. The algebra and the two original closures

Fix \(N\ge2\), and put
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad
 \kappa=q^{d^2/2},\qquad
 S_r=\prod_{j=1}^r2\sin(\pi j/N),\quad S_0=1.
 \tag{1}
\]
Powers of \(q\) in this note mean \(q^a=e^{\pi ia/N}\), including
half-integer exponents. This fixes the phases at even levels.
The original algebra and its normalized Newton basis are
\[
 \mathcal H_N=\mathbb C[z]/P_N(z),\quad
 P_N(z)=2T_N(z/2)+2,\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 e_r=S_r^{-2}\prod_{j=0}^{r-1}(c_j-z).
 \tag{2}
\]
Here \(T_N(\cos t)=\cos Nt\). Work in the entire quotient, including
the first derivatives at its double roots.

The original Frobenius closing \(\phi\), the ordinary marked
closing \(m\), the genuine turn \(J\), and coefficient reflection
\(a^\sharp(z)=\overline{a(\bar z)}\) satisfy
\[
 \phi(e_re_s)=\delta_{r+s,d},\qquad
 \phi(e_r)=\delta_{r,d},\qquad m(e_r)=\delta_{r,0},
 \qquad Je_r=e_{d-r},\qquad e_r^\sharp=e_r.
 \tag{3}
\]
The positive Newton norm is
\(\|\sum_r\alpha_re_r\|^2=\sum_r|\alpha_r|^2\).
The actual signed crossing elements are
\[
 R^+=\kappa\sum_{r=0}^d(-q)^re_r,\qquad
 R^-=\kappa^{-1}\sum_{r=0}^d(-q)^{-r}e_r,\qquad
 R^+R^-=1.
 \tag{4}
\]
These identities, including the original cups, caps and Cartan
scalar, are the direct inputs from the Newton source theorem.

## 2. Diagonal bilinear gluing and exact signed modes

For \(0\le a\le d\), set
\[
 k_a=a-d/2,\qquad
 U_{ra}=N^{-1/2}
     \exp\!\left(\frac{2\pi i}{N}k_a(r-d/2)\right),
 \qquad
 f_a=\sum_{r=0}^dU_{ra}e_r.
 \tag{5}
\]
If \(\alpha\) and \(\beta\) are the Newton and Fourier coefficient
columns of the same element, then \(\alpha=U\beta\).

**Proposition 1.** The basis in (5) is Hermitian orthonormal in the
positive Newton norm. It also satisfies the bilinear identities
\[
 \boxed{\quad
 \phi(f_af_b)=\delta_{ab},\qquad
 Jf_a=f_{d-a},\qquad f_a^\sharp=f_{d-a}.
 \quad}
 \tag{6}
\]
The two signed crossings are exactly
\[
                       R^+=\sqrt N\,f_0,\qquad
                       R^-=\sqrt N\,f_d .
 \tag{7}
\]

**Proof.** The differences \(k_b-k_a=b-a\) are integers. The
finite geometric sum in \(\sum_r\overline{U_{ra}}U_{rb}\)
therefore gives \(U^*U=I\), at both parities. Moreover
\[
 U_{d-r,b}=\overline{U_{rb}},\qquad
 U_{r,d-a}=\overline{U_{ra}}.
 \tag{8}
\]
Combining the first equality with (3) proves
\(\phi(f_af_b)=\sum_rU_{ra}\overline{U_{rb}}=\delta_{ab}\).
The two reversal assertions follow from (8).

Since \(r\) is an integer,
\[
 (-q)^r=e^{-\pi idr/N},\qquad
 \sqrt N\,U_{r0}=\kappa(-q)^r,\qquad
 \sqrt N\,U_{rd}=\kappa^{-1}(-q)^{-r}.
 \tag{9}
\]
Thus (4) proves (7) with no remaining phase factor. \(\square\)

The distinction between bilinear and Hermitian pairing remains
essential. If \(A=\sum_aA_af_a\) and \(B=\sum_aB_af_a\), then
\[
                    \phi(AB)=\sum_aA_aB_a ,
 \tag{10}
\]
without conjugating either input. A physical turn on an attaching
edge still inserts the reversal \(a\mapsto d-a\).

The original closure rows are not discarded. Define
\[
 \omega_a=N^{-1/2}e^{\pi ik_ad/N}.
 \tag{11}
\]
Then
\[
 \phi(f_a)=\omega_a,\qquad m(f_a)=\overline{\omega_a},\qquad
                         1=\sum_{a=0}^d\omega_af_a .
 \tag{12}
\]
These formulas follow by taking the \(e_d\) and \(e_0\)
coefficients in (5), or by pairing the unit with \(f_a\).
Both closure rows retain dual norm one. For example
\(\phi(1)=\sum_a\omega_a^2=0\), whereas
\(m(1)=\sum_a|\omega_a|^2=1\). Thus the diagonal gluing has
not erased the original source's exact zero or its marked closure.

## 3. One symmetric multiplication tensor

Define the real symmetric Newton tensor
\[
                         \tau_{ijk}=\phi(e_ie_je_k).
 \tag{13}
\]
Its exact support and coefficients are
\[
 \tau_{ijk}=
 \begin{cases}
 \displaystyle
 \frac{S_{i+j}S_{i+k}S_{j+k}}
 {N S_iS_jS_kS_{i+j+k-d}},
 &i+j,\ i+k,\ j+k\le d,\quad i+j+k\ge d,\\[6pt]
 0,&\text{otherwise}.
 \end{cases}
 \tag{14}
\]
All factorial indices in the nonzero case lie between \(0\)
and \(d\); every displayed coefficient is strictly positive.

To derive (14), the actual positive multiplication theorem gives
\[
 e_ie_j=\sum_{\ell=\max(i,j)}^{i+j}
 \frac{S_{i+j}S_\ell}
 {S_iS_jS_{\ell-i}S_{\ell-j}S_{i+j-\ell}}e_\ell
 \quad(i+j<N),
 \tag{15}
\]
and gives zero when \(i+j\ge N\). By (3), only
\(\ell=d-k\) contributes to (13). Its permitted range is
equivalent to the four inequalities in (14). Finally use
\(S_rS_{d-r}=N\) in its three complementary factorials.
This proves the symmetric formula without evaluating only at
the distinct Casimir roots.

In the Fourier basis put
\[
 C_{abc}=\phi(f_af_bf_c)
       =\sum_{i,j,k=0}^dU_{ia}U_{jb}U_{kc}\tau_{ijk}.
 \tag{16}
\]
Thus \(C\) is an explicit centered three-dimensional finite Fourier
transform of (14). Equivalently the summand's phase is
\[
 \exp\!\left\{\frac{2\pi i}{N}
  [k_a(i-d/2)+k_b(j-d/2)+k_c(k-d/2)]\right\},
 \tag{17}
\]
with the common factor \(N^{-3/2}\). The tensor is symmetric in
all three legs, and (6) gives
\[
                    f_af_b=\sum_{c=0}^dC_{abc}f_c .
 \tag{18}
\]
It retains the conjugation rule
\(\overline{C_{abc}}=C_{d-a,d-b,d-c}\).
In particular multiplication by the two actual signed crossings
has matrices
\[
 (A_+)_{cb}=\sqrt N\,C_{0bc},\qquad
 (A_-)_{cb}=\sqrt N\,C_{dbc},\qquad A_-A_+=I.
 \tag{19}
\]
These matrices retain their repeated-root Jordan directions.
They have not become diagonal phase multipliers.

## 4. The actual Casimir becomes tridiagonal

The tensor in (16) also satisfies finite three-term equations.
For \(0\le a\le d\), put
\[
 A_a=Q^{-a-1}-1,\qquad B_a=2q^{-1}Q^{-a},\qquad
 D_a=Q^{-a}-1,\qquad Q=q^2.
 \tag{20}
\]
Then multiplication by the actual Casimir coordinate has the form
\[
                  zf_a=A_af_{a+1}+B_af_a+D_af_{a-1}.
 \tag{21}
\]
The \(f_{a+1}\) and \(f_{a-1}\) terms are absent at \(a=d\)
and \(a=0\), respectively: \(A_d=D_0=0\).
There is no cyclic endpoint arrow.

Here is a direct verification, including the endpoints. In Newton
coordinates
\[
 ze_r=c_re_r+b_{r+1}e_{r+1},\qquad
 b_r=Q^r+Q^{-r}-2,
 \tag{22}
\]
with the absent term at \(r=d\) and \(b_0=0\). Set
\(x=q^d=-q^{-1}\). In the output row \(r\), the coefficient of
\(zf_a\) is
\[
 U_{ra}\{c_r+b_rxQ^{-a}\}.
 \tag{23}
\]
Using \(c_r=qQ^r+q^{-1}Q^{-r}\) and
\(Q^{\pm r}U_{ra}=x^{\pm1}U_{r,a\pm1}\) gives (21).
One may temporarily extend \(f_{a+N}=(-1)^df_a\) in this
calculation, but the coefficients \(A_d,D_0\) kill both wrap terms
in the final identity.

Since \(f_0=R^+/\sqrt N\) and \(R^+\) is invertible, (21) gives
unique polynomials \(p_a(z)\) of degree \(a\) such that
\[
              f_a=N^{-1/2}R^+p_a(z),\qquad p_0=1 .
 \tag{24}
\]
For \(a<d\), solve (21) for \(p_{a+1}\); its denominator
\(A_a\) is nonzero. The monic rescaling
\[
 \mathcal P_a=(-1)^a(Q^{-1};Q^{-1})_a p_a,\qquad
 (Q^{-1};Q^{-1})_a=\prod_{j=1}^a(1-Q^{-j}),
 \tag{25}
\]
satisfies, for \(0\le a<d\), with \(\mathcal P_{-1}=0\),
\[
 z\mathcal P_a=\mathcal P_{a+1}
       +2q^{-1}Q^{-a}\mathcal P_a
       +(1-Q^{-a})^2\mathcal P_{a-1}.
 \tag{26}
\]
This is the Al-Salam--Chihara recurrence with argument \(z/2\),
base \(Q^{-1}\), and both parameters \(q^{-1}\); compare
[Koornwinder (2004), equation (5)](https://staff.fnwi.uva.nl/t.h.koornwinder/art/informal/ASC.pdf).
The comparison only names a standard recurrence. Its specialization
here was derived above. Only \(0\le a\le d\) is rescaled in
(25); its factorial is nonzero on that range. No rescaling by the
vanishing factor \((Q^{-1};Q^{-1})_N\), positive measure, or
generic-parameter orthogonality theorem is used.

The original complex linear functional
\[
                         \psi(g)=\phi((R^+)^2g)/N
 \tag{27}
\]
obeys
\[
 \psi(p_ap_b)=\delta_{ab},\qquad
             C_{abc}=N^{-1/2}\psi(R^+p_ap_bp_c).
 \tag{28}
\]
These are bilinear identities; \(\psi\) is not asserted to be
a positive measure. They follow by substituting (24) in (6) and
(16). Finally, moving \(z\) among the three factors in
\(\phi(zf_af_bf_c)\) proves
\[
 \begin{aligned}
 A_aC_{a+1,b,c}+B_aC_{abc}+D_aC_{a-1,b,c}
 &=A_bC_{a,b+1,c}+B_bC_{abc}+D_bC_{a,b-1,c}\\
 &=A_cC_{a,b,c+1}+B_cC_{abc}+D_cC_{a,b,c-1}.
 \end{aligned}
 \tag{29}
\]
Every endpoint in these equations retains its zero coefficient.
Thus the universal multiplication tensor comes with explicit
finite difference equations, not only its Fourier sum.

## 5. The exact source compiler

Every specified finite Conway source can now be evaluated using:

* the single tensor \(C\) for each multiplication;
* reversal \(a\mapsto d-a\) for each genuine turn;
* the vectors \(\sqrt N\,\delta_0\) and
  \(\sqrt N\,\delta_d\) for signed crossing coupons;
* the unit and the two original closing rows in (12).

A power \(R^n\) is a product of \(|n|\) signed unit crossings,
or the unit for \(n=0\). Consequently
\(J(R^+)=\sqrt N f_d\) and \(J(R^-)=\sqrt N f_0\).
An arbitrary fixed short filling can be retained exactly by this
finite algebraic expansion. These auxiliary multiplication vertices
are not new crossing circles or new independent twist parameters.
There is no assertion that the expanded diagram is a new strict
filling template, or that turns may be moved through products.

The source identity follows by induction on the original expression,
using (6), (12), and (18) at its actual attachments. Open outputs
are retained as full \(N\)-component columns. No Casimir value or
first derivative has been removed, because \(U\) is invertible on
the entire algebra.

The same change is unitary for the positive Newton packet norm.
It preserves every vector norm, operator Hilbert--Schmidt norm,
and multiplication-tensor Hilbert--Schmidt norm. For the latter,
the ordinary output/input coordinate formula is \(U^*M(U\otimes U)\);
equations (3) and (8) identify it with (16). Thus a previously
recorded norm budget is unchanged if the same algebraic tree is
written in these coordinates. In particular a normalized signed
leaf is an exact endpoint mode, rather than an approximation
obtained by deleting its other Newton coordinates.

## 6. The phases cannot all be removed

There is a structural limit to simultaneous diagonal gluing and
real multiplication.

**Proposition 2.** For \(N\ge2\), in any basis \(g_a\) satisfying
\(\phi(g_ag_b)=\delta_{ab}\), the full triple tensor
\(\phi(g_ag_bg_c)\) cannot have all its entries in
\(e^{i\vartheta}\mathbb R\) for one common phase \(\vartheta\).
In particular it cannot be entirely real or nonnegative.

**Proof.** Write \(1=\sum_a\ell_ag_a\), so
\(\ell_a=\phi(g_a)\). Then
\[
                  \sum_a\ell_a^2=\phi(1)=0 .
 \tag{30}
\]
Suppose the triple tensor were \(e^{i\vartheta}R_{abc}\) with
all \(R_{abc}\) real. The unit equations become
\[
             \sum_av_aR_{abc}=\delta_{bc},\qquad
                         v_a=e^{i\vartheta}\ell_a .
 \tag{31}
\]
Their solution is unique: the difference of two solutions would
give an element whose multiplication operator is zero, and applying
it to \(1\) would show that element is zero. Real coefficients
therefore force \(v=\bar v\). It is nonzero because the unit is
nonzero. But then
\(\sum_a\ell_a^2=e^{-2i\vartheta}\sum_av_a^2\ne0\),
contrary to (30). \(\square\)

This statement concerns bases orthonormal for the original
**bilinear Frobenius form**. It does not concern every Hermitian
orthonormal basis. The original Newton basis already has real
nonnegative multiplication, but its Frobenius pairing is
anti-diagonal. The two facts are compatible. Here the signed
leaves and gluing simplify, while necessary phases remain in \(C\)
and in the two explicit closing rows.

## 7. Scope and complete sources

The construction is at the fixed original root and complete main
color. It transports the entire Casimir algebra, including its
Hermite directions. It does not claim a generic-\(q\) or moving
peripheral extension without the corresponding original families.
No positive geometric contour, nonzero global saddle coefficient,
or additional volume-identity class follows from this basis change.

Both complete proof texts were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Original Newton turn, closures and signed crossings](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [Full positive Newton multiplication](actual_positive_newton_multiplication.md) | 543b5be6035ecec349ce8e78ee47085345ceefe4fc51e5f2005b802d999805bb |

The complete [arbitrary-power compiler](research_arbitrary_power_source_compilation.md)
and [finite Fourier-band theorem](research_newton_interpolation_finite_fourier_band.md)
were also read for coverage, at pins
55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f
and 2e2d95184081ba6440b56268cb597624d97a5f1931e8c0df886fa754e6684304.
They already supply exact source compilation and finite Fourier
representations. No novelty is claimed for the Fourier transform or
for unitary changes of tensor coordinates. The useful combination
here is diagonal original bilinear gluing, both signed leaves as
exact modes, one symmetric multiplication tensor, and the
obstruction to removing all of that tensor's phases.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git
operation or earlier-final edit was performed.
