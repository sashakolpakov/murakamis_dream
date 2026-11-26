# The selected kernel of every original odd crossing run

Research note, 3 November 2026.

The backward period of an odd crossing run has a distinguished
eigenvalue, determined by the constant forward mode. Its spectrum
is simple throughout the closed auxiliary disk. The actual source
is its zero-eigenvalue line at the physical reset, with an explicit
normalization obtained from the double reset pole.

Together with the
[even-run theorem](research_even_run_simple_spectrum_and_marked_kernel.md),
this identifies the original marked source for every nonzero
crossing power. It does not bound transport along a proper part
of a period or a coherent pairing between different runs.

## 1. A second simple Robin family

Let \(T_m\) be adjacency on a path of \(m\) vertices. For
\(m\ge1\), set
\[
 J_m^0(s)=T_m+sE_{11},\qquad
 U_0(x)=1,\quad U_1(x)=x,\quad
 U_{n+1}(x)=xU_n(x)-U_{n-1}(x).
 \tag{1}
\]
Thus \(U_n\) is the monic rescaling of the second-kind
Chebyshev polynomial. Direct expansion gives
\[
 \det(xI-J_m^0(s))=U_m(x)-sU_{m-1}(x),\qquad
 U_m(2\cos\omega)=\frac{\sin((m+1)\omega)}{\sin\omega}.
 \tag{2}
\]

**Lemma 1.** The matrix \(J_m^0(s)\) has simple spectrum
for every \(|s|\le1\), and on some larger disk.

*Proof.* The proof retains algebraic multiplicities. For
\(\Im s>0\), an eigenpair satisfies
\(\Im x\,\|v\|^2=\Im s\,|v_1|^2>0\). The endpoint coordinate
cannot vanish by the tridiagonal recurrence.
Write \(x=z+z^{-1}\) with \(z=re^{-i\omega}\),
\(0<r<1\), \(0<\omega<\pi\). Formula (2) gives
\[
 s=\frac{1-z^{2m+2}}{z(1-z^{2m})}.
 \tag{3}
\]
The denominator is nonzero. The condition \(|s|\le1\) yields
\[
 -4r^{2m+2}\sin((2m+1)\omega)\sin\omega
       \ge(1-r^2)(1-r^{4m+2})>0.
 \tag{4}
\]
Hence each root belongs to one of the \(m\) disjoint sectors
\[
 \frac{(2j-1)\pi}{2m+1}<\omega<
                    \frac{2j\pi}{2m+1},\qquad 1\le j\le m.
 \tag{5}
\]
At \(s=0\), the roots have angles \(j\pi/(m+1)\),
strictly inside the respective sectors. A small positive
imaginary perturbation therefore puts one root in each.
Along any compact parameter path in
\(\{\Im s>0,\ |s|\le1\}\), boundedness of the eigenvalues,
the strict imaginary-part identity, and (4) prevent a root
from escaping through zero, the unit circle, or a sector side.
Every sector retains algebraic count one.
Conjugation handles the lower half disk; real \(s\) gives a
real symmetric irreducible Jacobi matrix.
Finally the discriminant is a polynomial nonzero on the
closed unit disk, so remains nonzero on a slightly larger disk.
\(\square\)

## 2. The classical odd backward matrix

For \(k\ge1\) and \(z\ne0\), define
\[
 H_k(z)=C_k(z)-E_{kk},\qquad
 C_k(z)=(z+z^{-1})I_k-T_k-zE_{11},\qquad
 A_k(z)=(I_k-zE_{11})H_k(z).
 \tag{6}
\]
The modifications in (6) overlap when \(k=1\); then
\(A_1(z)=z+z^{-1}-2\).
For every \(k\), the vector \({\bf1}\) is an eigenvector:
\[
              A_k(z){\bf1}=(z+z^{-1}-2){\bf1}.
 \tag{7}
\]
For \(k\ge2\), apply the difference map
\((Dv)_j=v_j-v_{j+1}\), \(1\le j<k\). Direct row subtraction
gives
\[
 DA_k(z)=\bigl[(z+z^{-1})I_{k-1}
                              -J_{k-1}^0(z)\bigr]D.
 \tag{8}
\]
Consequently the characteristic polynomial factors as
\[
 \det(tI-A_k(z))
  =[t-(z+z^{-1}-2)]
     \det\!\left([t-(z+z^{-1})]I_{k-1}
                                  +J_{k-1}^0(z)\right).
 \tag{9}
\]

**Proposition 2.** The \(k\) eigenvalues in (9) are distinct
for \(0<|z|\le1\). After subtracting
\((z+z^{-1})I\), they extend as distinct holomorphic
functions through \(z=0\) and to a disk of radius greater
than one.

*Proof.* Lemma 1 separates the quotient eigenvalues. A collision
with (7) requires an eigenvalue two of \(J_{k-1}^0(z)\).
But
\[
 \det(2I_{k-1}-J_{k-1}^0(z))=k-(k-1)z.
 \tag{10}
\]
For \(k\ge2\) its only zero is \(k/(k-1)>1\).
The shifted matrix \(A_k(z)-(z+z^{-1})I\) is polynomial;
its eigenvalues are \(-2\) and the negatives of the
eigenvalues of \(J_{k-1}^0(z)\).
These remain distinct on a slightly larger disk, by Lemma 1
and (10), and have holomorphic labels there.
For \(k=1\) the shifted matrix is the constant \(-2\).
\(\square\)

The constant mode does collide outside this disk: at
\(z=k/(k-1)\), (10) vanishes. In the classical matrix
the corresponding double eigenvalue has geometric multiplicity
one, since all super- and subdiagonal entries there are
nonzero. Thus one must not claim global simplicity in the
entire complex plane.

## 3. The exact original quantum period

Fix a signed odd power \(p=\sigma(2k-1)\), \(\sigma=\pm1\), and put
\[
 N\ge2,\quad D=N-1,\quad
 q_\sigma=e^{\sigma\pi i/N},\quad Q_\sigma=q_\sigma^2,\quad
 \epsilon=(-1)^N,\quad X=x^N,\quad
 \kappa=\exp\!\frac{\pi iD^2}{2N}.
 \tag{11}
\]
The single-run auxiliary clock \(x\) is independent of the sign.
On the common signed clock of a joined word, it is replaced by
the appropriate signed power of that clock.
Define
\[
 \begin{split}
 H_j(x)&=C_k(q_\sigma Q_\sigma^jx)-q_\sigma^{-1}E_{kk},\\
 A_j(x)&=(I-Q_\sigma^jxE_{11})H_j(x),\\
 \mathcal B_N(x)&=A_0(x)A_1(x)\cdots A_{N-1}(x).
 \end{split}
 \tag{12}
\]
The order in (12) is the backward order.
The full original forward transfer equals
\[
 \mathcal T_p(j;x)
       =w(Q_\sigma^jx)A_j(x)^{-1},\qquad
                         w(z)=(1-z)(1-z^{-1}),
 \tag{13}
\]
on its regular set, with the already proved polynomial
extension elsewhere.

**Theorem 3.** The backward characteristic identity is
\[
       \det(tI-\mathcal B_N(x))
                    =\det(tI-\epsilon A_k(x^N)).
 \tag{14}
\]
Moreover
\[
 \mathcal G_N(x)=\mathcal B_N(x)
                       -\epsilon(x^N+x^{-N})I
 \tag{15}
\]
is a polynomial matrix of degree at most \(N\).
Its spectrum is simple on a disk containing the closed unit
disk, and its distinguished eigenvalue is the constant
\(-2\epsilon\).

*Proof.* The original odd implicit color equation has diagonal
factor
\(\operatorname{diag}(1-z^{-1},w(z),\ldots,w(z))\).
Multiplying it on the left by \(I-zE_{11}\) gives (13),
including the first channel; no replacement by a scalar
factor before that multiplication is made.
The full forward product is
\(w(x^N)\mathcal B_N(x)^{-1}\).
The proved
[all-power resonant characteristic identity](research_resonant_source_monodromy_characteristic.md)
identifies it with the characteristic polynomial of
\(\epsilon w(X)A_k(X)^{-1}\).
Taking reciprocals on the regular set and using Laurent
continuation proves (14).

For the entrywise statement, write
\[
 \begin{split}
 K(z)&=I-q_\sigma zT_k-zE_{kk}
                         +q_\sigma^2z^2(I-E_{11}),\\
 \widetilde K(z)&=(I-zE_{11})K(z),\\
 F(x)&=\widetilde K(x)\widetilde K(Q_\sigma x)
                       \cdots\widetilde K(Q_\sigma^{N-1}x).
 \end{split}
 \tag{16}
\]
Although written as a product of degrees one and two,
\(\widetilde K\) has degree at most two, because
\(E_{11}(I-E_{11})=0\). It has value \(I\) at zero.
One has \(\mathcal B_N=\epsilon x^{-N}F\) and, near zero,
\[
 F(Q_\sigma x)=\widetilde K(x)^{-1}F(x)\widetilde K(x).
 \tag{17}
\]
The coefficient induction from the even-run proof gives
\(x^N\mid F-I\). Since \(\deg F\le2N\), (15) is polynomial
of degree at most \(N\).
Theorem 3's spectral assertion now follows from (14) and
Proposition 2, including at zero. \(\square\)

Let \(\Pi_{0,N}(x)\) be the distinguished projector. It has
the particularly explicit marked expression
\[
 \boxed{\quad
 \Pi_{0,N}(x)=
  \frac{\operatorname{adj}(2I+\epsilon\mathcal G_N(x))}
       {k-(k-1)x^N}.
 \quad}                                                       \tag{18}
\]
For \(k=1\), the adjugate of the zero \(1\times1\) matrix
is one, so (18) gives the identity.
For \(k\ge2\), the denominator is exactly the product of
the other eigenvalues of \(2I+\epsilon\mathcal G_N\);
this proves (18).
All projectors, including (18), satisfy the inverse-free
transport law
\[
 \Pi_{j,N}(x)A_0(x)=A_0(x)\Pi_{j,N}(Q_\sigma x).
 \tag{19}
\]
It remains valid when \(A_0\) is singular.

## 4. The double reset and the original marked section

The original source has
\[
 (u_0)_a=q_\sigma^{k-a},\qquad
 H_j(1)u_j=
   \operatorname{diag}(1-Q_\sigma^{-j},w(Q_\sigma^j),
                    \ldots,w(Q_\sigma^j))u_{j-1}.
 \tag{20}
\]
Its entire Newton column is
\[
                   (M^pe_0)_j=\kappa^p e_k^Tu_j.
 \tag{21}
\]
Multiplication as in (13) gives
\[
 A_j(1)u_j=w(Q_\sigma^j)u_{j-1},\qquad
            A_1(1)\cdots A_D(1)u_D=N^2u_0.
 \tag{22}
\]
Every \(A_j(1)\), \(1\le j\le D\), is invertible. The reset
\(A_0(1)\) has rank \(k-1\), right kernel \(u_0\), and
left kernel \(e_1^T\). These facts also follow directly from
the last \(k-1\) tridiagonal rows.

**Theorem 4.** At every level, both signs and both parities,
\[
 \boxed{\quad
 \ker\mathcal B_N(1)=\mathbb C u_D,\qquad
 e_1^Tu_D=\epsilon q_\sigma^{-k},\qquad
 \Pi_{0,N}(1)=\epsilon q_\sigma^k u_De_1^T.
 \quad}                                                       \tag{23}
\]
In particular
\[
                 u_D=\epsilon q_\sigma^{-k}\Pi_{0,N}(1)e_1.
 \tag{24}
\]
There is no unchosen amplitude in this section of the kernel line.

*Proof.* The kernel statements follow from (22) and the reset
ranks. The eigenvalues of \(\mathcal B_N(1)\) are zero and
\(\epsilon\) times the eigenvalues of
\(2I_{k-1}-J_{k-1}^0(1)\). The latter are positive and have
product one by (10). Hence zero is simple and
\[
                   \operatorname{adj}\mathcal B_N(1)
                                =\epsilon^{k-1}\Pi_{0,N}(1).
 \tag{25}
\]

We calculate that adjugate with the double reset pole, rather
than trying to use a first determinant derivative, which vanishes.
Let \(v=u_0\). The exact polynomial inverse formula for the
resonant run gives
\[
 H_0(x)^{-1}
        =\frac{\mathcal B_k(q_\sigma x;q_\sigma)}{1-x},
       \qquad \mathcal B_k(q_\sigma;q_\sigma)=q_\sigma vv^T.
 \tag{26}
\]
Since
\((I-xE_{11})^{-1}=I+xE_{11}/(1-x)\), it follows that
\[
 A_0(x)^{-1}
       =\frac{q_\sigma^k v e_1^T}{(1-x)^2}
                                      +O((1-x)^{-1}).
 \tag{27}
\]
The regular remaining inverse product sends \(v\) to
\(u_D/N^2\), by (22).
On the other hand, multiplication of the literal determinants
in (12) gives
\[
 \det\mathcal B_N(x)=\epsilon^k X^{-k}(1-X)^2
          =\epsilon^k N^2(x-1)^2+O((x-1)^3).
 \tag{28}
\]
Multiplying (27) by the regular inverse product and by (28)
therefore gives
\[
        \operatorname{adj}\mathcal B_N(1)
                    =\epsilon^k q_\sigma^k u_De_1^T.
 \tag{29}
\]
Comparison with (25) proves the projector in (23).
Its value on its own nonzero kernel vector then gives
\(e_1^Tu_D=\epsilon q_\sigma^{-k}\), and (24) follows.
\(\square\)

Every intermediate coefficient can also be recovered exactly:
\[
 u_j=\frac{S_j^2}{N^2}
       A_{j+1}(1)\cdots A_D(1)
            \,\epsilon q_\sigma^{-k}\Pi_{0,N}(1)e_1,\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N).
 \tag{30}
\]
The empty product at \(j=D\) is \(I\), and \(S_D=N\).
Equations (21) and (30) retain the original crossing phase,
all Newton coefficients, the entire free-boundary polynomial,
and its repeated-root normal derivatives.

## 5. A unique primitive polynomial horizontal section

The distinguished odd mode also has an exact cyclic descent.
Write \(c=-q_\sigma\), so \(c^N=-\epsilon\), and let
\(T(x)=\mathcal T_p(0;x)\) be the original polynomial
forward transfer. Its constant term is \(cI\), and
\[
 \deg T\le2k-2,\qquad
             \det T(x)=(-q_\sigma)^k(1-x)^{2k-2}.
 \tag{31}
\]
These are the original transfer identities from the
[marked Laurent source theorem](research_two_run_marked_laurent_numerator.md).
For \(k=1\), \(T(x)=c\).

**Theorem 5.** There is a unique polynomial vector \(f_N(x)\)
whose components have no nonconstant common factor, satisfying
\[
 \boxed{\quad
 T(x)f_N(x)=c\,f_N(Q_\sigma x),\qquad
                         f_N(Q_\sigma)=u_0.
 \quad}                                                       \tag{32}
\]
It lies in the distinguished eigenline, is nonzero at every
finite \(x\), and may be chosen with degree at most
\((3k-2)N-2k+1\).
Every original channel and every original coefficient are its
literal samples:
\[
 \boxed{\quad
 u_j=c^j f_N(Q_\sigma^{j+1}),\qquad
 (M^pe_0)_j=\kappa^p c^j e_k^T f_N(Q_\sigma^{j+1}).
 \quad}                                                       \tag{33}
\]
In particular \(f_N(1)=\epsilon q_\sigma u_D\).

*Proof.* Let \(E_x=\operatorname{ran}\Pi_{0,N}(x)\) over
the rational function field. The inverse-free transport (19)
and (13) give \(T(x)E_x=E_{Q_\sigma x}\) generically.
The full forward period acts on this line by
\[
 \frac{w(x^N)}{-\epsilon w(x^N)}
                 =-\epsilon=c^N.
 \tag{34}
\]
On rational sections of this line define
\[
 (\mathcal L g)(x)
       =c^{-1}T(Q_\sigma^{-1}x)g(Q_\sigma^{-1}x).
 \tag{35}
\]
The exact ordered product and (34) give \(\mathcal L^N=I\)
on that rank-one module.

There is an explicit normalized averaging construction.
Set
\[
 \ell(x)=\frac1N\sum_{r=0}^{N-1}(x/Q_\sigma)^r,\qquad
 g(x)=\ell(x)\Pi_{0,N}(x)u_0,\qquad
 f^{\rm av}(x)=\sum_{r=0}^{N-1}\mathcal L^r g(x).
 \tag{36}
\]
It obeys (32)'s horizontal equation. The projector is
regular on the physical orbit. Its range at \(Q_\sigma\)
is \(\mathbb C u_0\), since the backward period there ends
on its right with \(A_0(1)\), whose kernel is \(u_0\).
Thus \(g(Q_\sigma)=u_0\), while \(g\) vanishes at every
other physical orbit point. In evaluating (36) at
\(Q_\sigma\), only the term \(r=0\) contributes. Hence
\(f^{\rm av}(Q_\sigma)=u_0\), without a further scalar choice.

The transfer on the selected line is nonzero around that
entire orbit. Indeed the factors at colors \(1,\ldots,D\)
are invertible. At the reset the polynomial transfer has
the exact value
\[
       T(1)=-q_\sigma^k u_0e_1^T,\qquad
                      T(1)u_D=-\epsilon u_0,
 \tag{37}
\]
using (23). The horizontal equation and its normalized
initial value therefore give (33) for \(f^{\rm av}\).
The last assertion uses \(c^{N-1}=\epsilon q_\sigma^{-1}\).

It remains to obtain a primitive polynomial section, rather
than a rational one. Put \(d(X)=k-(k-1)X\).
Formula (18) shows that
\[
                    F(x)=d(x^N)f^{\rm av}(x)
 \tag{38}
\]
is polynomial. The denominator is invariant under
\(x\mapsto Q_\sigma x\), so \(F\) has the same horizontal
equation and \(F(Q_\sigma)=u_0\).
Its degree is at most
\((k-1)N+(N-1)+(2k-2)(N-1)=(3k-2)N-2k+1\):
these are respectively the adjugate, the cardinal polynomial,
and the maximum number of transfer factors in (36).

Let \(g_0(x)\) be the monic common divisor of the components
of \(F\). Away from zero and the physical orbit, (31) and
the horizontal equation transport a common zero, with its
multiplicity, around its whole \(Q_\sigma\)-orbit. There
are no common zeros on the physical orbit, by (33) and
the nonzero source states.
If the common order at zero is \(r\), comparison of lowest
coefficients in the horizontal equation, using \(T(0)=cI\),
gives \(Q_\sigma^r=1\). Thus \(N\mid r\).
The root factorization of \(g_0\) consequently has the form
\[
                       g_0(x)=h(x^N),\qquad h(1)\ne0.
 \tag{39}
\]
The vector
\(f_N(x)=h(1)F(x)/h(x^N)\) is polynomial, primitive,
horizontal and normalized as in (32). Over \(\mathbb C\),
primitive components have no common finite zero. Division
does not increase the degree, and the scalar is one on
the physical orbit, so (33) remains unchanged.

For uniqueness, iteration of the horizontal equation
puts any such section in the distinguished rational
eigenline. Two nonzero horizontal sections differ by a
rational scalar \(a(x)\) satisfying
\(a(Q_\sigma x)=a(x)\). The invariant field is
\(\mathbb C(x^N)\), as follows by expanding over the basis
\(1,x,\ldots,x^{N-1}\) over that field.
A nonconstant rational ratio between two primitive
polynomial vectors would have either a finite pole,
forcing a common zero of the first vector, or a finite
zero, forcing a common zero of the second. Both are
impossible. The ratio is constant, and normalization
at \(Q_\sigma\) makes it one. \(\square\)

The descent uses the finite cyclic semilinear action, not
a positivity replacement. The invariant scalar freedom
before primitiveness is the multiplicative group
\(\mathbb C(x^N)^*\); the cap normalization and primitive
polynomial requirement fix it exactly. This does not
provide a bound for the coefficients or values of \(f_N\).

The cyclic descent mechanism is classical Hilbert 90; see
Andrew V. Sutherland,
[Number Theory I, Lecture 24, Theorem 24.2 and Corollary 24.3](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_full_lec.pdf#page=254).
No novelty is claimed for that mechanism. The argument above
supplies its actual source module, the ordered quantum action,
the cap-normalized nonzero average, and the primitive polynomial
representative explicitly.

## 6. What the selected line does not yet estimate

The odd selected eigenvalue is separated throughout the closed
auxiliary disk, just as the selected even line is separated in
the even-run theorem. There is no eigenvalue collision in that
domain. For \(k\ge2\), the possible collision with the constant
mode begins outside it at \(x^N=k/(k-1)\).

The marked projector and its transported section can nevertheless
have large norms. Different nonzero backward eigenvalues can
exchange their modulus order without colliding. Formula (30)
is an exact source representation, not a bound on its partial
products or on a later nonreflected closing pairing.
Accordingly no new volume-conjecture or finite-exception
coverage assertion follows from this selected-line theorem.

## 7. Finite normalization diagnostic

The [independent checker](../experiments/check_odd_run_simple_spectrum_and_marked_kernel.py)
tests the classical sector labels, the coefficientwise polynomial
shift and cyclic identities, and the actual marked projector.
It constructs the original \(N\times N\) crossing matrix and
compares the entire signed odd source column with the channel
equations. The
[120-digit record](../repro/results/research-odd-run-simple-spectrum-and-marked-kernel.json)
passes 40 classical parameter cases and 96 signed quantum cases,
including 20 with \(k>N\), 384 projector clocks, and 528 original
source colors. It also checks the unshortened Reynolds sum on
72 complete clock orbits, its exact horizontal equation, and
162 physical channel samples against the original source.
The maximum relative identity residual is
\(2.23145362902\cdot10^{-116}\).
The all-parameter simplicity and exact descent are proved above,
not inferred from these finite checks.
