# The characteristic curve and initial mode of an original crossing source

Research note, 3 November 2026.

The finite-channel source recurrence has the same classical cap curve
as the original quantum conjugation. This can be checked by an explicit
polynomial identity, including the elementary factors. Its initial
condition also selects a nonzero mode on a fixed small interval of
colors for every fixed crossing power. For odd powers the selected
classical mode on that interval is the constant root minus one.
Neither statement continues a mode through the whole color circle.

## 1. The actual limiting transfer

Use the original source recurrence in
[the resonant run note](research_resonant_crossing_run_source.md).
For a positive power \(p\), put \(k=\lceil p/2\rceil\), and let
\(T_k\) be path adjacency on \(k\) coordinates. Write
\[
 A_k(z)=(z+z^{-1})I_k-T_k-zE_{11}-E_{kk},\qquad
 B_k(z)=(1-z)A_k(z)^{-1}.
 \tag{1}
\]
The polynomial formula in the
[two-run source note](research_two_run_source_transfer.md), equation (4),
defines \(B_k\) also at \(z=1\). In particular
\(B_k(1)=\mathbf1\mathbf1^T\), where \(\mathbf1\) has \(k\)
entries equal to one.

Set
\[
 \mathcal T_p(z)=
 \begin{cases}
 (1-z^{-1})B_k(z),&p=2k,\\
 B_k(z)\operatorname{diag}(-z^{-1},1-z^{-1},\ldots,1-z^{-1}),
                      &p=2k-1,
 \end{cases}
 \qquad
 \chi_p(z,y)=\det(yI_k-\mathcal T_p(z)).
 \tag{2}
\]
These are the \(q\to1\) limits of the actual source matrices,
with the color clock \(z=Q^j\) retained. The coefficients of
\(\chi_p\) are Laurent polynomials in \(z\), and it is monic
of degree \(k\) in \(y\).

Here \(z\) is the Newton color clock and \(y\) is the forward
coefficient ratio. They are not yet meridian and longitude
coordinates of a knot complement.

## 2. An explicit characteristic polynomial

Put
\[
 h=2-z-z^{-1},\qquad a=z+z^{-1}-h/y,
 \qquad
 v=\begin{cases}z,&p\text{ even},\\
                 z+(z-1)/y,&p\text{ odd}.
    \end{cases}
 \tag{3}
\]
Let \(U_j\) be Chebyshev polynomials of the second kind, with
\(U_{-1}=0\) and \(U_{-2}=-1\) when needed below.

**Proposition 1.** For \(p=2k\) or \(p=2k-1\),
\[
 \boxed{\quad
 \chi_p(z,y)=\frac{z^ky^k}{1-z}
 \left[U_k(a/2)-(v+1)U_{k-1}(a/2)+vU_{k-2}(a/2)\right].
 \quad} \tag{4}
\]
The apparent denominators on the right cancel as a Laurent
polynomial identity. For example,
\[
 \begin{split}
 \chi_1&=y+1,\\
 \chi_2&=y-z+1,\\
 \chi_3&=(y+1)\{y+(z-1)^2\},\\
 \chi_4&=y^2+(-z^3+2z^2-3z+2)y-(z-1)^3.
 \end{split} \tag{5}
\]

*Proof.* The determinant of a tridiagonal matrix with common
diagonal \(a\), off-diagonals minus one, and first and last
diagonal subtractions \(v,1\), is
\[
 U_k(a/2)-(v+1)U_{k-1}(a/2)+vU_{k-2}(a/2).
 \tag{6}
\]
This follows by expanding in the two diagonal modifications;
the unmodified path determinant is \(U_k(a/2)\). For \(k=1\)
the modifications affect the same entry and (6) is \(a-v-1\),
as required.

For even \(p\), \(\mathcal T_p=hA_k^{-1}\), so
\(\chi_p=y^k\det(A_k-hI/y)/\det A_k\).
For odd \(p\), the matrix in this numerator gains
\((1-z)E_{11}/y\). Its first boundary subtraction is therefore
exactly \(v\) in (3). Since
\(\det A_k=z^{-k}(1-z)\), formula (6) proves (4) where the
displayed inverses are regular. The left side of (4) is already
Laurent polynomial by (1)--(2), so the identity extends to all
nonzero \(z\), including \(z=1\), and to \(y=0\).
\(\square\)

## 3. Agreement with the original cap, including its square

Use the original trace symbols from the
[rational-word cap factorization](research_rational_word_cap_square_factorization.md):
\[
 \begin{split}
 A&=z+z^{-1}+(z+z^{-1}-2)y^{-1}=a,\\
 B&=z+z^{-1}+(z+z^{-1}-2)y,\\
 C&=4z-2z^2-(1-z)^2(y+y^{-1}).
 \end{split} \tag{7}
\]
The crossing acts by \((A,B,C)\mapsto(A,8-AB-C,B)\).
Let \(d_p\) be its transformed second coordinate minus two
after \(p\) positive crossings. This is the symbol of the
original cap \(M^p(L-c_0I)M^{-p}\).

**Theorem 2.** For every positive \(p\),
\[
 \boxed{\begin{aligned}
 d_{2k}(z,y)
   &=\frac{(z-1)^2(1+y)}{z^{2k+1}y^{2k}}\,
                                      \chi_{2k}(z,y)^2,\\
 d_{2k-1}(z,y)
   &=-\frac{(z-1)^2}{z^{2k}y^{2k-1}}\,
                                      \chi_{2k-1}(z,y)^2.
 \end{aligned}} \tag{8}
\]
Thus the source transfer has the original cap curve, with the
square and its elementary factors recorded explicitly.

*Proof.* Use the square-root cover of the cited cap theorem.
Denote its roots by \(s,t,u\), so
\(s^2=2-A\), \(t^2=2-B\), and \(u^2=2-C\).
Under successive crossings the second root obeys
\[
 t_0=t,\qquad t_1=st-u,\qquad
                         t_{j+1}=s t_j-t_{j-1}.
 \tag{9}
\]
Hence either parity subsequence obeys
\(t_{j+2}=-A t_j-t_{j-2}\).
The initial root ratios in the cap theorem give
\[
 \frac{t_1}{u}=-z^{-1},\qquad
 \frac{t_2}{t}=-\frac{y-z+1}{zy}.
 \tag{10}
\]

For each parity, expression (4) obeys the recurrence
\[
 \chi_{p+2}=Azy\,\chi_p-(zy)^2\chi_{p-2}.
 \tag{11}
\]
This is the Chebyshev recurrence in (4), since \(A,v\) do
not depend on \(k\). In the even sequence use \(\chi_0=1\).
For the first step of the odd sequence one may use
\(\chi_{-1}=(y+1)/y\), the value supplied by the same
formula with \(k=0\); subsequent terms are the polynomials
in (2). Equations (9)--(11) therefore prove
\[
 t_{2k}=\frac{(-1)^k\chi_{2k}}{z^ky^k}\,t,
 \qquad
 t_{2k-1}=\frac{(-1)^k\chi_{2k-1}}{z^ky^{k-1}(1+y)}\,u.
 \tag{12}
\]
These equations are initially in the root function field.
Now \(d_j=-t_j^2\), and
\[
 t^2=-\frac{(z-1)^2(1+y)}z,\qquad
 u^2=\frac{(z-1)^2(1+y)^2}y.
 \tag{13}
\]
Squaring (12) gives (8). All resulting identities are Laurent
polynomial identities, so no division at a zero of an initial
root has been assumed. \(\square\)

The odd characteristic polynomial always contains \(y+1\).
This follows from (5) and (11), or directly from (4).
It is part of the source characteristic polynomial and has
not been removed. The identity (8) alone does not determine
which modes the actual finite source contains.

Negative powers are obtained by the actual conjugation
\(\overline M=M^{-1}\): their limiting transfer is
\(\mathcal T_{|p|}(z^{-1})\), and their cap identity is
(8) with \(z\) replaced by \(z^{-1}\). No peripheral
interpretation of these two bulk variables is inferred.

## 4. A nonzero initial mode for every fixed power

Write \(\alpha_{p,j}=(M^p\mathbf e_0)_j\), with the original
scalar \(\kappa^p\) retained. For even \(p=2k>0\), let
\(\beta_k(z)\) be the analytic eigenvalue of \(B_k(z)\)
with \(\beta_k(1)=k\). It is simple near one, because
\(B_k(1)=\mathbf1\mathbf1^T\).

**Theorem 3.** For each fixed nonzero power \(p\), there are
\(\delta_p>0\), positive constants, and a starting level such
that every coefficient with \(0\le j\le\delta_p N\) is nonzero.
Uniformly on that interval, if \(|p|=2k\),
\[
 \log|\alpha_{p,j}|=
 \log S_j+
 N\int_0^{j/N}\log|\beta_k(e^{2\pi ix})|\,dx+O_p(1),
 \qquad S_j=\prod_{r=1}^j2\sin(r\pi/N).
 \tag{14}
\]
If \(|p|\) is odd, instead
\[
                         c_p\le|\alpha_{p,j}|\le C_p
 \tag{15}
\]
for some \(0<c_p<C_p\) independent of \(N,j\) in that
interval.

*Proof.* It suffices to consider positive powers, since negative
ones have conjugate coefficients. For an even power, divide the
state at color \(j\) by
\(\prod_{r=1}^j(1-Q^{-r})\). Its exact step matrix is the
polynomial \(\mathcal B_k(qQ^j;q)\) in the two-run note. This
converges, with its first derivatives on a fixed small complex
neighborhood, to \(B_k(e^{2\pi ix})\), with error \(O_p(N^{-1})\).
For an odd power, use the original step (19) of the resonant run
note without any scalar division. Its limit at \(x=0\) is
\(-\mathbf1\mathbf e_1^T\), with simple eigenvalue minus one
and all other eigenvalues zero. The factor \(y+1\) just proved
shows that its simple eigenvalue remains exactly minus one on
a sufficiently small neighborhood.

In either case the limiting matrix has a simple nonzero eigenvalue
\(\lambda(x)\), with a complementary block which is zero at
\(x=0\). Choose an analytic eigenvector and a complementary frame
there, with initial eigenvector \(\mathbf1\). After shrinking
the interval and fixing a compatible norm, the complementary
block has norm at most \(|\lambda(x)|/2\), and the last coordinate
of the eigenvector stays nonzero. The exact initial vector
\((q^{k-1},\ldots,1)^T\) differs from \(\mathbf1\) by
\(O_p(N^{-1})\).

In these moving coordinates, consecutive exact steps have block
diagonal leading part \(\operatorname{diag}(\lambda(x_j),C(x_j))\)
and error \(O_p(N^{-1})\), including the change of frame between
\(x_{j-1}\) and \(x_j\). If the transverse coordinate divided by
the first coordinate has size at most \(K/N\), its next value
has size at most \(K/(2N)+C/N\). Choose \(K\) larger than
\(2C\) and the initial bound, then increase the starting level
to absorb the harmless denominator errors. Induction keeps this
ratio \(O_p(N^{-1})\); in particular the first coordinate never
vanishes. Its successive multipliers are
\(\lambda(x_j)+O_p(N^{-1})\). The final coordinate of the
original state is therefore bounded above and below by fixed
positive multiples of \(\prod_{r=1}^j|\lambda(r/N)|\).

For even powers restore the scalar product, whose modulus is
exactly \(S_j\). A Riemann-sum estimate for the smooth function
\(\log|\lambda|=\log|\beta_k|\) has error \(O_p(1)\), giving
(14). For odd powers \(\lambda=-1\), so the same comparison
gives (15). The carrier has modulus one throughout. \(\square\)

The interval in Theorem 3 is fixed before taking the level limit.
It is not the whole color interval. In particular the odd source
starts on the constant classical branch; other components can
matter later. The theorem neither rules out switching between
modes outside this interval nor replaces the signed accumulator
of a two-run source by a norm. Those are still necessary steps
toward the short-partial-filling theorem.

The [symbolic check](../experiments/check_crossing_source_characteristic.py)
builds the source matrices and iterates the original trace transport
independently. Its [saved output](../repro/results/research-crossing-source-characteristic.json)
verifies the characteristic squares, elementary factors, determinant
identities and limiting reset matrices for powers one through eight
using exact rational arithmetic. The all-power identities and the
local analytic estimates are proved above.
