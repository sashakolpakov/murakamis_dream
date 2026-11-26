# The exact all-index prepared amplitude and its boundary truncation

Research proof, 7 November 2026.

The prepared insertion used in the
[low Newton coefficient theorem](research_three_crossing_low_newton_coefficients.md)
has an explicit finite sine-factorial expansion at every index.
The root-of-unity split is different on the two sides of \(2b=N\).
Above that threshold its middle Laurent harmonics vanish exactly.
The boundary forcing is also explicit: it removes precisely the
first \(b\) coordinates of the amplitude-weighted prepared vector.

These identities preserve the original preparation error. They
give an explicit amplitude upper profile on every fixed contour,
but no comparison of that profile with the next geometric action
is made here.

## 1. Original operators and the amplitude

Fix \(N\ge2\), and put
\[
 \begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad r=Q^{-1},\\
 S_j=\prod_{m=1}^j2\sin(\pi m/N),\quad S_0=1,\quad
 s_j=2\sin(\pi j/N),\\
 c_j=qQ^j+q^{-1}Q^{-j},\qquad
 p_b(x)=\prod_{j=0}^{b-1}(c_j-x),\qquad
 e_b(x)=p_b(x)/S_b^2,\qquad 0\le b<N .
 \end{gathered}                                                   \tag{1}
\]
All the factorials in (1) are original positive sine factorials.
Let \(C\) be the original multiplication matrix
\[
 C_{mm}=c_m,\qquad C_{m,m-1}=-s_m^2,
\]
and retain \(M,J,\kappa\) from the
[prepared-source theorem](research_three_crossing_prepared_boundary_sum.md).
Its exact preparation is
\[
 M^3\mathbf e_0=\kappa^3A_Nh+\delta_N,\qquad
 h_m=q^{m(m+2)}S_m^2,\qquad
 \|\delta_N\|_2=O(N^{3/2}).                                    \tag{2}
\]
The scalar \(A_N\) in (2) is the specified exact finite scalar,
not its leading approximation.

Define an operator on ordinary polynomials in \(z\) by
\[
 \mathscr Ca(z)
       =(z+z^{-1})a(z)-z^{-1}a(rz),\qquad
 a_b(z)=p_b(\mathscr C)1,\qquad
 \mathcal A_b(z)=a_b(z)/S_b^2.                                 \tag{3}
\]
The apparent negative power is removable. More explicitly,
\[
 \mathscr C z^k=z^{k+1}+(1-r^k)z^{k-1},                        \tag{4}
\]
with the second term zero at \(k=0\).
This is an exact polynomial identity, before any specialization
of \(z\) to a physical clock.

## 2. A finite q-Vandermonde identity

Write \({m\brack k}_r\) for the Gaussian binomial polynomial,
zero outside \(0\le k\le m\). When \(m<N\) it can be evaluated as
\[
 {m\brack k}_r=\frac{(r;r)_m}{(r;r)_k(r;r)_{m-k}},
\]
whose denominators are nonzero. For \(m\ge N\) the polynomial
definition, not a quotient with a zero factorial, is used.

**Lemma 1.** At every original level and every \(0\le b<N\),
\[
 \boxed{\quad
 p_b(\zeta+\zeta^{-1})
   =q^{b^2}\sum_{n=-b}^b
       (-1)^nq^{-n^2}{2b\brack b-n}_r\,\zeta^n .
 \quad}                                                        \tag{5}
\]

*Proof.* Set \(a=q^{-1}\), so \(a^2=r\) and
\(c_j=ar^j+a^{-1}r^{-j}\). Factor each term in (1):
\[
 p_b(\zeta+\zeta^{-1})
   =a^{-b}r^{-b(b-1)/2}
                    (a\zeta;r)_b(a\zeta^{-1};r)_b.             \tag{6}
\]
The finite q-binomial theorem follows by induction from
\[
 {m+1\brack k}_r={m\brack k}_r
                         +r^{m+1-k}{m\brack k-1}_r .
\]
Apply it to both factors in (6). For \(0\le n\le b\),
the coefficient of \(\zeta^n\) in their product is
\[
 (-a)^n r^{n(n-1)/2}
       \sum_{k=0}^{b-n}r^{k(k+n)}
                      {b\brack k+n}_r{b\brack k}_r .           \tag{7}
\]
The exponent in the inner sum uses \(a^2=r\).
Splitting the product
\(\prod_{j=0}^{2b-1}(1+r^jt)\) into its two length-\(b\)
parts and comparing the coefficient of \(t^{b-n}\) gives
\[
 {2b\brack b-n}_r
    =\sum_{j}r^{(b-j)(b-n-j)}
                    {b\brack j}_r{b\brack b-n-j}_r .
\]
Substitute \(j=b-n-k\) and use the binomial symmetry
\({b\brack b-n-k}_r={b\brack n+k}_r\). This is the
sum in (7).

All these identities are polynomial identities in \(r\);
they remain valid at its primitive \(N\)-th root.
The prefactor in (6) is \(q^{b^2}\), and
\((-a)^nr^{n(n-1)/2}=(-1)^nq^{-n^2}\).
The product is invariant under \(\zeta\mapsto\zeta^{-1}\),
so the negative coefficients agree with the positive ones.
This proves (5). \(\square\)

## 3. The exact root-of-unity split

The lower-index positive Laurent formula already appears in
[the degree-three zero-wire estimates, Section 3, equation (20)](research_degree_three_zero_wire_tails.md).
That note also records the original positive Newton multiplication
law and its full-quotient zero-product rule in equations (11)--(13),
from [the finite Newton calculus](../papers/newton-calculus/finite.tex).
The proof here retains the phases in our \(p_b\) convention and
extends the harmonic split to every \(b<N\), for its prepared-source
and boundary-cutoff application below.

Let \(\mathsf T_n(x)=2T_n(x/2)\) for \(n\ge1\), where
\(T_n\) is the ordinary Chebyshev polynomial. Thus
\(\mathsf T_n(\zeta+\zeta^{-1})=\zeta^n+\zeta^{-n}\).

**Proposition 2.** If \(2b<N\), then
\[
 \boxed{\quad
 p_b(x)=S_{2b}\left\{
       \frac1{S_b^2}
       +\sum_{n=1}^b
          \frac{(-1)^n\mathsf T_n(x)}
                         {S_{b-n}S_{b+n}}\right\}.
 \quad}                                                        \tag{8}
\]
If \(N\le2b<2N\), then
\[
 \boxed{\quad
 p_b(x)=(-1)^b S_{2b-N}
       \sum_{n=N-b}^b
          \frac{\mathsf T_n(x)}
                         {S_{b-n}S_{b+n-N}} .
 \quad}                                                        \tag{9}
\]
Every displayed factorial has an index in \(\{0,\ldots,N-1\}\).
In (9), the Laurent harmonics \(|n|<N-b\), including the
constant harmonic, vanish.

*Proof.* For \(0\le k\le m<N\), the exact elementary factor
\[
 1-r^j=i q^{-j}s_j
\]
gives
\[
 {m\brack k}_r
       =q^{-k(m-k)}
                    \frac{S_m}{S_kS_{m-k}}.                    \tag{10}
\]
For \(m=2b<N\), \(k=b-n\), its phase cancels the entire
\(q^{b^2-n^2}\) factor in (5). Group the two equal Laurent
coefficients to obtain (8).

For the other range put \(m=2b-N\), so \(0\le m<N\).
The exact finite product identity is
\[
 (z;r)_{N+m}=(1-z^N)(z;r)_m .
 \tag{11}
\]
Comparing its coefficients by the finite q-binomial theorem
shows
\[
 {N+m\brack k}_r=
 \begin{cases}
 {m\brack k}_r,&0\le k\le m,\\
 0,&m<k<N,\\
 {m\brack k-N}_r,&N\le k\le N+m .
 \end{cases}                                                   \tag{12}
\]
There is no missing sign in the last line. Its coefficient
comparison uses
\[
 r^{N(N-1)/2}=(-1)^{N-1},\qquad r^{N\ell}=1,
\]
which cancels the sign of the second term of (11).
Thus (12) holds at even as well as odd levels.

For positive \(n\), a nonzero coefficient in (5) now requires
\(k=b-n\le m\), equivalently \(n\ge N-b\).
Apply (10) with this \(m,k\). The remaining phase is
\[
 q^{b^2-n^2-k(m-k)}=q^{Nk}=(-1)^k .
\]
Together with \((-1)^n\), it equals \((-1)^b\).
Its two factorial indices are \(b-n\) and \(b+n-N\).
Reflection supplies the negative harmonics, proving (9).
\(\square\)

At the threshold \(2b=N\), formula (9) has exactly one
summand and says \(p_b=(-1)^b\mathsf T_b\).
This includes \(N=2,b=1\): \(p_1(x)=-x\).
For \(b=0\), formula (8) reads \(p_0=1\).
No special parity or endpoint convention has been introduced.

## 4. Inverting the Hermite basis

The polynomials and inverse connection coefficients in this
section are standard continuous \(q\)-Hermite identities.
See Johann Cigler,
[Continuous q-Hermite polynomials: An elementary approach](https://homepage.univie.ac.at/johann.cigler/preprints/contqhermite.pdf),
Section 6.1, equations (6.1) and (6.7), printed pages 25--26,
with his variable replaced by \(x/2\) and his parameter by \(r\);
see also [DLMF Section 18.28(vi)](https://dlmf.nist.gov/18.28#vi).
The finite proof below fixes the scaling and checks the permitted
root-of-unity denominators. The application here is their combination
with the original Newton source, its exact harmonic split, and
the retained boundary truncation in Sections 5--6.

Define monic polynomials, for the same finite parameter \(r\), by
\[
 H_0=1,\quad H_1=x,\qquad
 H_{n+1}=xH_n-(1-r^n)H_{n-1}.                                 \tag{13}
\]
Equation (4) proves by induction that
\[
                         H_n(\mathscr C)1=z^n .               \tag{14}
\]
The following finite inverse is useful because its denominators
do not reach the root-of-unity index.

**Lemma 3.** For \(1\le n<N\), put
\[
 d_{n,k}=(-1)^k r^{k(k-1)/2}
       \frac{1-r^n}{1-r^{n-k}}{n-k\brack k}_r,
               \qquad 0\le k\le\lfloor n/2\rfloor .
 \tag{15}
\]
Then
\[
 \mathsf T_n(x)=\sum_{k=0}^{\lfloor n/2\rfloor}
                         d_{n,k}H_{n-2k}(x),\qquad
 \mathcal T_n(z):=\mathsf T_n(\mathscr C)1
             =\sum_{k=0}^{\lfloor n/2\rfloor}d_{n,k}z^{n-2k}.
 \tag{16}
\]

*Proof.* Both sides start with
\[
 \mathsf T_1=H_1,\qquad
 \mathsf T_2=H_2-(1+r)H_0 .
\]
Declare \(d_{n,k}=0\) when \(k\) is outside its range.
Substitution of (15), followed by the q-binomial recurrence,
gives for \(n\ge2\)
\[
 d_{n+1,k}=d_{n,k}
       +(1-r^{\,n-2k+2})d_{n,k-1}-d_{n-1,k-1}.                \tag{17}
\]
This is exactly the coefficient recurrence obtained by using
\(xH_m=H_{m+1}+(1-r^m)H_{m-1}\) in
\(\mathsf T_{n+1}=x\mathsf T_n-\mathsf T_{n-1}\).
The separate displayed \(n=2\) base value retains
\(\mathsf T_0=2\) in that Chebyshev recurrence.
Thus induction proves the first identity in (16).
Applying (14) proves the second.

The formula can first be checked with indeterminate \(r\).
In its actual specialization \(n-k\) lies between \(1\)
and \(N-1\), and every factorial denominator in
\({n-k\brack k}_r\) has index less than \(N\). Therefore
no singular specialization is used. \(\square\)

Combining (8)--(9) with (16) gives the complete amplitude:
\[
 a_b(z)=
 \begin{cases}
 S_{2b}\left\{S_b^{-2}+
       \displaystyle\sum_{n=1}^b
       \frac{(-1)^n\mathcal T_n(z)}
                           {S_{b-n}S_{b+n}}\right\},
                                      &2b<N,\\[3mm]
 (-1)^b S_{2b-N}
       \displaystyle\sum_{n=N-b}^b
       \frac{\mathcal T_n(z)}
                           {S_{b-n}S_{b+n-N}},
                                      &2b\ge N .
 \end{cases}                                                   \tag{18}
\]
In particular the alternating inner Hermite coefficients remain
present even when the Laurent coefficients in (9) share one sign.
No positivity of the actual amplitude follows from (9).

## 5. The boundary forcing is an exact truncation

Put \(z_m=qQ^m\) and
\((\mathsf T a)_m=a(z_m)h_m\).
Direct substitution into the original bidiagonal \(C\) gives
\[
 C\mathsf T a=\mathsf T\mathscr Ca
                         +q^{-1}a(q^{-1})\mathbf e_0 .          \tag{19}
\]
Iterating (19) through the \(b\) factors of \(p_b(C)\)
shows
\[
 p_b(C)h=\mathsf T a_b+r_b,\qquad
                         \operatorname{supp}r_b\subset[0,b-1].
 \tag{20}
\]
There is a second exact fact. The leading \(b\times b\)
block of \(C\) is lower triangular with characteristic
polynomial \((-1)^bp_b\). Its first \(b\) rows are closed
under multiplication by \(C\). Cayley--Hamilton therefore
makes the first \(b\) rows of \(p_b(C)\) zero. This includes
repeated diagonal values and does not replace their Jordan
blocks by distinct-node values.

Consequently (20) determines its forcing completely:
\[
 (r_b)_m=
 \begin{cases}
       -a_b(z_m)h_m,&m<b,\\
       0,&m\ge b .
 \end{cases}
\]
Equivalently, with \(P_{\ge b}\) the original coordinate
projection,
\[
 \boxed{\qquad
 e_b(C)h=P_{\ge b}\mathsf T\mathcal A_b .
 \qquad}                                                       \tag{21}
\]
This identity holds for every \(b<N\), not only in a low
index range. It is the full boundary current, not a reason
to omit it.

For the original coefficient
\(\ell_b(w)=(v(w)^TA_3^2)_b\), the exact insertion
identity in the low-coefficient theorem and (2) give
\[
 \ell_b(w)=
 \kappa^3A_N v(w)^TJM^3J
                   P_{\ge b}\mathsf T\mathcal A_b
          +v(w)^TJM^3J e_b(C)\delta_N .                         \tag{22}
\]
In the first term, the original prepared three-index sum
is now exactly
\[
 \begin{split}
 A_NN^3\kappa^2
 \sum_{\substack{i,j,k\ge0\\ i+j<N,\ k\le j,\ k\le D-b}}
 &\mathrm i^{\,i+j}(-1)^j
 q^{((i-j)^2-i+j)/2+k(j+k)}
 \frac{S_{i+j}}{S_i^2S_jS_k^3S_{j-k}}\\[-1mm]
 &\hspace{16mm}\times e_i(w)\,
                    \mathcal A_b(q^{-1}Q^{-k}) .
 \end{split}                                                   \tag{23}
\]
The additional cutoff \(k\le D-b\) is exactly (21) after
the original reversal. All other support restrictions,
Newton factors, and scalar powers are unchanged.
If a contour decomposition is applied for a macroscopic
\(b\), its new cutoff current must therefore be retained.

The last term of (22) is still the original preparation
error acted on by the full original matrices. For example
\[
 \|e_b(C)\|_2\le8^b/S_b^2
 \tag{24}
\]
gives an immediate bound by that factor times the old
remaining-operator preparation estimate. No assertion that
this error is exponentially small at every macroscopic
\(b\) is made. For \(b\le\delta N\), the low-coefficient
theorem proves the required vanishing debit and treats all
coherent outer removals separately.

## 6. Explicit finite upper bounds on a fixed contour

For \(R>0\) define the positive finite polynomial
\[
 \mathcal U_n(R)=
   \sum_{k=0}^{\lfloor n/2\rfloor}
      \frac{s_nS_{n-k-1}}{S_kS_{n-2k}}\,R^{n-2k},
                      \qquad 1\le n<N.                        \tag{25}
\]
Indeed (10) and (15) give exactly
\[
 |d_{n,k}|=
  \frac{s_n}{s_{n-k}}
       \frac{S_{n-k}}{S_kS_{n-2k}}
  =\frac{s_nS_{n-k-1}}{S_kS_{n-2k}} .
 \tag{26}
\]
All factors in (25) have permitted finite indices.
In particular \(n-k-1\ge0\).
For \(|z|\le R\), (18) yields the explicit bound
\[
 |\mathcal A_b(z)|\le\mathcal B_{N,b}(R),                        \tag{27}
\]
where
\[
 \mathcal B_{N,b}(R)=
 \begin{cases}
 \displaystyle\frac{S_{2b}}{S_b^2}
 \left\{\frac1{S_b^2}+
       \sum_{n=1}^b
          \frac{\mathcal U_n(R)}{S_{b-n}S_{b+n}}\right\},
                                      &2b<N,\\[4mm]
 \displaystyle\frac{S_{2b-N}}{S_b^2}
       \sum_{n=N-b}^b
          \frac{\mathcal U_n(R)}{S_{b-n}S_{b+n-N}},
                                      &2b\ge N .
 \end{cases}                                                   \tag{28}
\]
This includes \(b=0\), for which \(\mathcal B_{N,0}=1\).
The rate bound below is a consequence of this finite formula;
it is not a replacement for its exact zeros or cutoff.

Let \(J(t)=\int_0^t\log(2\sin\pi u)\,du\), continuously
extended to \(0\le t\le1\), and write \(x=b/N\),
\(\rho=\log R\). For \(0\le x<1/2\), put
\[
 \begin{split}
 \mathscr E_-(x,\rho)=
 \max_{\substack{0\le u\le x\\0\le v\le u/2}}
 \big\{&
 J(2x)-2J(x)-J(x-u)-J(x+u)\\
 &+J(u-v)-J(v)-J(u-2v)+(u-2v)\rho
 \big\}.
 \end{split}                                                   \tag{29}
\]
For \(1/2\le x<1\), put
\[
 \begin{split}
 \mathscr E_+(x,\rho)=
 \max_{\substack{1-x\le u\le x\\0\le v\le u/2}}
 \big\{&
 J(2x-1)-2J(x)-J(x-u)-J(x+u-1)\\
 &+J(u-v)-J(v)-J(u-2v)+(u-2v)\rho
 \big\}.
 \end{split}                                                   \tag{30}
\]
Every argument of \(J\) in these compact maxima lies in
\([0,1]\). They are explicit real functions of the original
index fraction and the contour radius.

**Corollary 4.** Uniformly over all \(0\le b<N\) and \(R\)
in a fixed compact subinterval of \((0,\infty)\),
\[
 \mathcal B_{N,b}(R)\le
 CN^A
 \begin{cases}
 e^{N\mathscr E_-(b/N,\log R)},&2b<N,\\
 e^{N\mathscr E_+(b/N,\log R)},&2b\ge N .
 \end{cases}                                                   \tag{31}
\]

*Proof.* Use the original uniform sine-factorial estimate
\(\log S_m=NJ(m/N)+O(\log N)\) for \(0\le m<N\).
In (26), the ratio \(s_n/s_{n-k}\) is at most \(N/2\):
the numerator is at most two and the denominator is at
least \(2\sin(\pi/N)\ge4/N\). Thus it has only polynomial
cost. The remaining factorials in one term of (28), with
\(u=n/N,v=k/N\), give precisely the expression in (29)
or (30). The first, constant term in the lower formula
is included by \(u=v=0\). At most \(O(N^2)\) terms occur.
These observations prove (31), with every endpoint covered
by the same uniform estimate. \(\square\)

For the old prepared contours, the amplitude argument in
(23) has modulus \(e^{2\pi\Im z}\). Thus (28), or (31)
with that actual radius, supplies a finite bound for the
multiplier on each original horizontal or vertical piece.
The lower and upper formulas at \(x=1/2\) must not be
interchanged: the exact root-of-unity cancellation there
changes the harmonic support.

All formulas are finite polynomial or original matrix
identities and consequently retain both level parities,
all ordinary boundary derivatives, and the original
preparation scalar. The signed amplitude, the preparation
error in (22), and the extra cutoff current in (23) still
need a coherent comparison before this all-index formula
can be used to control the remaining physical middle
range. No new numerical evaluation or threshold claim
is part of this note.
